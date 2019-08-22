from __future__ import unicode_literals

import base64
import hashlib
import io
import os
import uuid
import zipfile

import jinja2
from PIL import Image
from six import iteritems


################################################################################
### Asset class: manage images/etc stored with the token

asset_template = '''
<net.rptools.maptool.model.Asset>
  <id>
    <id>{{ asset.md5 }}</id>
  </id>
  <name>{{ asset.name }}</name>
  <extension>{{ asset.ext }}</extension>
  <image/>
</net.rptools.maptool.model.Asset>
'''.strip()

class Asset(object):
    def __init__(self, name, ext, contents, md5=None):
        self.contents = contents
        self.name = name
        self.ext = ext
        if md5 is None:
            md5 = hashlib.md5(contents).hexdigest()
        self.md5 = md5

    def asset_xml(self):
        return jinja2.Template(asset_template).render(asset=self)

    def __repr__(self):
        return '<Asset {}.{}>'.format(self.name, self.ext)


################################################################################
### Macro class: container for metada about macros. Basically just a dict.

macro_defaults = {
    'command': '',
    'label': '',
    'group': '',
    'sortby': '',
    'color': 'default',
    'font_color': 'black',
    'font_size': '1.00em',
    'tooltip': '',
    'hotkey': 'None',
}

class Macro(object):
    def __init__(self, **kwargs):
        for k, v in iteritems(macro_defaults):
            setattr(self, k, v)
        for k, v in iteritems(kwargs):
            setattr(self, k, v)


################################################################################
### Token class

size_map = {
    'Fine': 'fwABAc1lFSoBAAAAKgABAQ==',
    'Diminutive': 'fwABAc1lFSoCAAAAKgABAQ==',
    'Tiny': 'fwABAc5lFSoDAAAAKgABAA==',
    'Small': 'fwABAc5lFSoEAAAAKgABAA==',
    'Medium': 'fwABAc9lFSoFAAAAKgABAQ==',
    'Large': 'fwABAdBlFSoGAAAAKgABAA==',
    'Huge': 'fwABAdBlFSoHAAAAKgABAA==',
    'Gargantuan': 'fwABAdFlFSoIAAAAKgABAQ==',
    'Colossal': 'fwABAeFlFSoJAAAAKgABAQ==',
}

token_defaults = {
    'is_visible': 'true',
    'name': 'Default Token',
    'label': '',
    'gm_name': '',
    'notes': '',
    'gm_notes': '',
    'owners': [],
    'PC': True,
    'layer': 'TOKEN',
    'halo_color': -256,
    'sight_type': 'Normal',
}

_toggles = ("Other Other2 Other3 Other4 Enlarged Dead Incapacitated "
            "BullStrength Prone Hidden Disabled").split()
base_states = {k: ('boolean', 'false') for k in _toggles}
base_states['Health'] = ('big-decimal', '1')

# No need to explicitly store properties that will just be set to the default.
# Here's some you might want to set, though:
    # 'HP', 'MaxHP', 'Nonlethal', 'TempHP',
    # 'BAB', 'Level',
    # 'Armor', 'ACAlways', 'DexDodge',
    # 'Description', 'HasInit', 'Elevation',
    # 'ACP', 'CMB', 'CMD',
    # 'Strength', 'Dexterity', 'Constitution',
    # 'Intelligence', 'Wisdom', 'Charisma',
    # 'Fortitude', 'Reflex', 'Will',
    # 'Perception', 'SenseMotive', 'Initiative',
    # 'AbilityPool', 'AbilityPoolMax', 'Pool1Name',
    # 'Pool2', 'Pool2Max', 'Pool2Name',
base_properties = {
    'HasInit': 1,
    'Fortitude': '{ConMod}',
    'Reflex': '{DexMod}',
    'Will': '{WisMod}',
    'HP': '{MaxHP}',
}

atk_macro = '''
[h:Name="%s"]
[h:type="damage"]
[h:dice=%s]
[h:ndice=%s]
[h:attack_bonus=%s]
[h:crit_low=20]
[h:damage_mod=StrMod + %s]
[h:crit_mult=2]
[h:damage_dice=roll(ndice,dice)]
[h:crit_dice=roll(ndice,dice)]
[h:attack_stat=StrMod]
[h:roll=1d20]
[h:crit_damage=reroll(crit_mult-1, dice+damage_mod, 1+damage_mod)]
[Name]: [roll+attack_stat+BAB-SizeMod+attack_bonus] to hit, 

[damage_dice+damage_mod] ["%s damage"]
[if(roll>=crit_low), CODE:{


Crit chance! [1d20+attack_stat+BAB-SizeMod+attack_bonus] to confirm
[crit_damage] extra damage
};{ 
}]
'''

base_macros = [
    Macro(label='Fortitude', group='saves', command='Fort: [d20+Fortitude]'),
    Macro(label='Reflex',  group='saves', command='Reflex: [d20+Reflex]'),
    Macro(label='Will', group='saves', command='Will: [d20+Will]'),
    Macro(label='str', group='skills', sortby='_1', command='Str: [d20+StrMod] (ACP: [ACP])'),
    Macro(label='dex', group='skills', sortby='_2', command='Dex: [d20+DexMod] (ACP: [ACP])'),
    Macro(label='con', group='skills', sortby='_3', command='Con: [d20+ConMod]'),
    Macro(label='int', group='skills', sortby='_4', command='Int: [d20+IntMod]'),
    Macro(label='wis', group='skills', sortby='_5', command='Wis: [d20+WisMod]'),
    Macro(label='cha', group='skills', sortby='_6', command='Cha: [d20+ChaMod]'),
    Macro(label='Perception', group='skills', command='Perception: [d20+Perception]'),
    Macro(label='Sense Motive', group='skills', command='Sense Motive: [d20+SenseMotive]'),
    Macro(label='Mod HP', color='pink', sortby='0', command='''
[h: input(
"mode|Damage,Heal,Temp HP,Nonlethal|Choose|RADIO|ORIENT=H",
"Amt|0|Amount|TEXT"
)]
[h, switch(mode),code:
case 0: {
  [HP = HP - Amt + min(TempHP, Amt)]
  [TempHP = max(0, TempHP - Amt)]
};
case 1: { [HP = min(HP + Amt, MaxHP)] };
case 2: { [TempHP = TempHP + Amt] };
case 3: { [Nonlethal = Nonlethal + Amt] }]
[s:CurrentHitPoints]
'''.strip()),
]



properties_xml = '''<map>
  <entry>
    <string>version</string>
    <string>1.4.0.0
</string>
  </entry>
</map>'''

with open('templates/content.xml') as f:
    content_template = jinja2.Template(f.read())
# add a macro argument to the token
class Token(object):
    def __init__(self, image, portrait_image=None, size='Medium',
                 states=None, properties=None, macros=None,
                 default_states=True, default_properties=True,
                 default_macros=True, **kwargs):
        assert isinstance(image, Asset)
        self.image = image
        if portrait_image is not None:
            assert isinstance(image, Asset)
        self.portrait_image = portrait_image

        self.id = base64.encodestring(uuid.uuid4().bytes).strip()

        self.size_id = size_map[size]

        for k, v in iteritems(token_defaults):
            setattr(self, k, v)
        for k, v in iteritems(kwargs):
            setattr(self, k, v)

        self.states = {}
        if default_states:
            for name, (typ, val) in iteritems(base_states):
                self.states[name] = (typ, val)
        if states:
            for name, (typ, val) in iteritems(states):
                self.states[name] = (typ, val)

        self.properties = {}
        if default_properties:
            for name, val in iteritems(base_properties):
                self.properties[name] = val
        if properties:
            for name, val in iteritems(properties):
                self.properties[name] = val

        self.macros = []
        ## here is where I can add additional macros before the template finishes
        #use the base_macros as an example
        if default_macros:
            self.macros.extend(base_macros)
        if macros:
            for macroTuple in macros:
                macroString = (atk_macro % macroTuple)
                thisMacro = Macro(label=macroTuple[0], group='Attacks',sortby='_1', command=macroString),
                self.macros.extend(thisMacro)

    def _add_asset(self, f, asset):
        f.writestr('assets/{}'.format(asset.md5), asset.asset_xml())
        f.writestr('assets/{}.{}'.format(asset.md5, asset.ext), asset.contents)

    def make_thumbnail(self):
        with io.BytesIO(self.image.contents) as f_in:
            image = Image.open(f_in)
            image.thumbnail((50, 50))
            with io.BytesIO() as f_out:
                image.save(f_out, 'png')
                return f_out.getvalue()

    def content_xml(self):
        return content_template.render(t=self)

    def make_file(self, file, mode='w', compressed=True):
        c = zipfile.ZIP_DEFLATED if compressed else zipfile.ZIP_STORED
        with zipfile.ZipFile(file, mode=mode, compression=c) as f:
            f.writestr('content.xml', self.content_xml())
            f.writestr('properties.xml', properties_xml)
            f.writestr('thumbnail', self.make_thumbnail())
            self._add_asset(f, self.image)
            if self.portrait_image is not None:
                self._add_asset(f, self.portrait_image)
