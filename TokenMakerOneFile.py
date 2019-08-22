from __future__ import unicode_literals

import requests
import mimetypes
import io
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import base64
import hashlib
import io
import os
import uuid
import zipfile

import jinja2
from PIL import Image
from six import iteritems

#need to make the parts into different classes
from tkinter import *




macrodesc = '''
Tokens come pre-loaded with the following macros: Fortitude save, Will Save, Reflex save, All ability checks, and modify HP. '''

class TokenMacros():
  def __init__(self, master):
    self.MacroFrame = Frame(
        master, highlightbackground='black', highlightthickness=2, bd=5)
    self.MacroFrame.grid(row=2, column=2, columnspan=2, sticky='NE')
    self.MacroTitle = Label(master, text="Macro Details", font=('Courier', 18))
    self.MacroTitle.grid(column=2, row=1, sticky='')
    self.MacroDesc = Label(
        self.MacroFrame, text=macrodesc, wraplength=220, width=30)
    self.MacroDesc.grid(column=0, row=1, columnspan=4)
    self.ATKLabel = Label(self.MacroFrame, text="Attack Macro Details")
    self.ATKLabel.grid(column=0, row=2, columnspan=4)

    self.Seperator = ttk.Separator(self.MacroFrame)
    self.Seperator.grid(row=3, sticky='EW', columnspan=4)

    self.AtkMacroLabel = Label(self.MacroFrame, text="Name", )
    self.AtkMacroLabel.grid(column=0, row=4)
    self.AtkMacroName = Entry(self.MacroFrame,)
    self.AtkMacroName.grid(row=4, column=1, sticky='W')

    self.AtkMacroTypeLabel = Label(self.MacroFrame, text="Type", )
    self.AtkMacroTypeLabel.grid(column=2, row=4)
    self.AtkMacroTypeName = Entry(self.MacroFrame, width=10)
    self.AtkMacroTypeName.grid(row=4, column=3, sticky='W')

    self.AtkNumLabel = Label(self.MacroFrame, text="Number of dice")
    self.AtkNumLabel.grid(row=5, column=0)
    self.AtkNumEntry = Entry(self.MacroFrame, width=5)
    self.AtkNumEntry.grid(row=5, column=1)

    self.DieNumLabel = Label(self.MacroFrame, text="Dice Step")
    self.DieNumLabel.grid(row=5, column=2, sticky='W')
    self.DieNumEntry = Entry(self.MacroFrame, width=5)
    self.DieNumEntry.grid(row=5, column=3, sticky='W')

    self.AtkBonusLabel = Label(self.MacroFrame, text="ATK Bonus")
    self.AtkBonusLabel.grid(row=6, column=0)
    self.AtkBonusEntry = Entry(self.MacroFrame, width=5)
    self.AtkBonusEntry.grid(row=6, column=1)

    self.DmgBonusLabel = Label(self.MacroFrame, text="Damage Bonus")
    self.DmgBonusLabel.grid(row=6, column=2, sticky='W')
    self.DmgBonusEntry = Entry(self.MacroFrame, width=5)
    self.DmgBonusEntry.grid(row=6, column=3, sticky='W')

    self.Seperator2 = ttk.Separator(self.MacroFrame)
    self.Seperator2.grid(row=7, sticky='EW', columnspan=4)

    self.AtkMacroLabel2 = Label(self.MacroFrame, text="Name", )
    self.AtkMacroLabel2.grid(column=0, row=8)
    self.AtkMacroName2 = Entry(self.MacroFrame,)
    self.AtkMacroName2.grid(row=8, column=1, sticky='W')

    self.AtkMacroTypeLabel2 = Label(self.MacroFrame, text="Type", )
    self.AtkMacroTypeLabel2.grid(column=2, row=8)
    self.AtkMacroTypeName2 = Entry(self.MacroFrame, width=10)
    self.AtkMacroTypeName2.grid(row=8, column=3, sticky='W')

    self.AtkNumLabel2 = Label(self.MacroFrame, text="Number of dice")
    self.AtkNumLabel2.grid(row=9, column=0)
    self.AtkNumEntry2 = Entry(self.MacroFrame, width=5)
    self.AtkNumEntry2.grid(row=9, column=1)

    self.DieNumLabel2 = Label(self.MacroFrame, text="Dice Step")
    self.DieNumLabel2.grid(row=9, column=2, sticky='W')
    self.DieNumEntry2 = Entry(self.MacroFrame, width=5)
    self.DieNumEntry2.grid(row=9, column=3, sticky='W')

    self.AtkBonusLabel2 = Label(self.MacroFrame, text="ATK Bonus")
    self.AtkBonusLabel2.grid(row=10, column=0)
    self.AtkBonusEntry2 = Entry(self.MacroFrame, width=5)
    self.AtkBonusEntry2.grid(row=10, column=1)

    self.DmgBonusLabel2 = Label(self.MacroFrame, text="Damage Bonus")
    self.DmgBonusLabel2.grid(row=10, column=2, sticky='W')
    self.DmgBonusEntry2 = Entry(self.MacroFrame, width=5)
    self.DmgBonusEntry2.grid(row=10, column=3, sticky='W')

  def updateMacros(self, monsterObj):
    try:
      firstMacro = monsterObj['MeleeAtks'][0]
      self.AtkMacroName.delete(0, END)
      self.AtkMacroName.insert(0, firstMacro[0])
      self.AtkNumEntry.delete(0, END)
      self.AtkNumEntry.insert(0, firstMacro[3])
      self.DieNumEntry.delete(0, END)
      self.DieNumEntry.insert(0, firstMacro[4])
      self.AtkBonusEntry.delete(0, END)
      self.AtkBonusEntry.insert(0, firstMacro[1])
      self.DmgBonusEntry.delete(0, END)
      self.DmgBonusEntry.insert(0, firstMacro[2])
      print(firstMacro)
    except IndexError as e:
      pass
    try:
      secondMacro = monsterObj['MeleeAtks'][1]
      self.AtkMacroName2.delete(0, END)
      self.AtkMacroName2.insert(0, secondMacro[0])
      self.AtkNumEntry2.delete(0, END)
      self.AtkNumEntry2.insert(0, secondMacro[3])
      self.DieNumEntry2.delete(0, END)
      self.DieNumEntry2.insert(0, secondMacro[4])
      self.AtkBonusEntry2.delete(0, END)
      self.AtkBonusEntry2.insert(0, secondMacro[1])
      self.DmgBonusEntry2.delete(0, END)
      self.DmgBonusEntry2.insert(0, secondMacro[2])
      print(secondMacro)
    except IndexError as e:
      pass

  def returnMacros(self):
    #gather all macro information and return it
    allMacros = []
    try:
      name = self.AtkMacroName.get()
      if(name != ''):
        num = self.AtkNumEntry.get()
        dice = self.DieNumEntry.get()
        atkBon = self.AtkBonusEntry.get()
        dmgBon = self.DmgBonusEntry.get()
        dmgType = self.AtkMacroTypeName.get()
        macro1 = (name, num, dice, atkBon, dmgBon, dmgType)
        allMacros.append(macro1)
    except Exception as e:
      pass
    try:
      name = self.AtkMacroName2.get()
      if(name != ''):
        num = self.AtkNumEntry2.get()
        dice = self.DieNumEntry2.get()
        atkBon = self.AtkBonusEntry2.get()
        dmgBon = self.DmgBonusEntry2.get()
        dmgType = self.AtkMacroTypeName2.get()
        macro2 = (name, dice, num, atkBon, dmgBon, dmgType)
        allMacros.append(macro2)
    except Exception as e:
      pass
    return allMacros



class MonsterDisplay():
  def __init__(self, master):
    self.title = Label(master, text="Monster Details", font=('Courier', 18))
    self.title.grid(row=1, column=1)

    self.MonsterDisplay = Frame(
        master, highlightbackground='black', highlightthickness=2)
    self.MonsterDisplay.grid(row=2, column=1)
    self.MonsterName = Label(self.MonsterDisplay, text="Name of Monster")
    self.MonsterName.grid(row=0, column=0,)
    self.MonsterEntry = Entry(self.MonsterDisplay)
    self.MonsterEntry.grid(row=0, column=1)

    self.MonsterDesc = Text(self.MonsterDisplay, height=10, width=60)
    self.MonsterDesc.grid(row=1, column=0, columnspan=4)
    # self.DescScroll = Scrollbar(self.MonsterDisplay,orient='vertical',command=self.MonsterDesc.yview)
    # self.DescScroll.grid(row=1,column=2, sticky='E')
    # self.MonsterDesc['yscrollcommand'] = self.DescScroll.set

    self.MonsterStats = Frame(
        self.MonsterDisplay, highlightbackground='black', highlightthickness=2)
    self.MonsterStats.grid(row=2, column=0, sticky='S', columnspan=4)

    self.StrLabel = Label(self.MonsterStats, text="Strength")
    self.StrLabel.grid(row=0, column=0)
    self.StrEntry = Entry(self.MonsterStats, width=10)
    self.StrEntry.grid(row=0, column=1)

    self.DexLabel = Label(self.MonsterStats, text="Dexterity")
    self.DexLabel.grid(row=0, column=2)
    self.DexEntry = Entry(self.MonsterStats, width=10)
    self.DexEntry.grid(row=0, column=3)

    self.ConLabel = Label(self.MonsterStats, text="Constitution")
    self.ConLabel.grid(row=0, column=4)
    self.ConEntry = Entry(self.MonsterStats, width=10)
    self.ConEntry.grid(row=0, column=5)

    self.IntLabel = Label(self.MonsterStats, text="Intelligence")
    self.IntLabel.grid(row=1, column=0)
    self.IntEntry = Entry(self.MonsterStats, width=10)
    self.IntEntry.grid(row=1, column=1)

    self.WisLabel = Label(self.MonsterStats, text="Wisdom")
    self.WisLabel.grid(row=1, column=2)
    self.WisEntry = Entry(self.MonsterStats, width=10)
    self.WisEntry.grid(row=1, column=3)

    self.ChaLabel = Label(self.MonsterStats, text="Charisma")
    self.ChaLabel.grid(row=1, column=4)
    self.ChaEntry = Entry(self.MonsterStats, width=10)
    self.ChaEntry.grid(row=1, column=5)

    self.BaBLabel = Label(self.MonsterStats, text="BaB")
    self.BaBLabel.grid(row=2, column=0)
    self.BaBEntry = Entry(self.MonsterStats, width=10)
    self.BaBEntry.grid(row=2, column=1)

    self.HPLabel = Label(self.MonsterStats, text="HP")
    self.HPLabel.grid(row=2, column=2)
    self.HPEntry = Entry(self.MonsterStats, width=10)
    self.HPEntry.grid(row=2, column=3)

    self.HDLabel = Label(self.MonsterStats, text="HD")
    self.HDLabel.grid(row=2, column=4)
    self.HDEntry = Entry(self.MonsterStats, width=10)
    self.HDEntry.grid(row=2, column=5)

    self.ACLabel = Label(self.MonsterStats, text="AC")
    self.ACLabel.grid(row=3, column=0)
    self.ACEntry = Entry(self.MonsterStats, width=10)
    self.ACEntry.grid(row=3, column=1)

    self.ArmorBonusLabel = Label(self.MonsterStats, text="Armor Bonus")
    self.ArmorBonusLabel.grid(row=3, column=2)
    self.ArmorBonusEntry = Entry(self.MonsterStats, width=10)
    self.ArmorBonusEntry.grid(row=3, column=3)

    self.NaturalArmorBonusLabel = Label(
        self.MonsterStats, text="Natural Armor Bonus")
    self.NaturalArmorBonusLabel.grid(row=3, column=4)
    self.NaturalArmorBonusEntry = Entry(self.MonsterStats, width=10)
    self.NaturalArmorBonusEntry.grid(row=3, column=5)

    self.SizeLabel = Label(self.MonsterStats, text="Size")
    self.SizeLabel.grid(row=4, column=0)
    self.SizeEntry = Entry(self.MonsterStats, width=10)
    self.SizeEntry.grid(row=4, column=1)

    self.FortLabel = Label(self.MonsterStats, text="Fortitude")
    self.FortLabel.grid(row=4, column=2)
    self.FortEntry = Entry(self.MonsterStats, width=10)
    self.FortEntry.grid(row=4, column=3)

    self.WillLabel = Label(self.MonsterStats, text="Will")
    self.WillLabel.grid(row=4, column=4)
    self.WillEntry = Entry(self.MonsterStats, width=10)
    self.WillEntry.grid(row=4, column=5)

    self.RefLabel = Label(self.MonsterStats, text="Reflex")
    self.RefLabel.grid(row=5, column=0)
    self.RefEntry = Entry(self.MonsterStats, width=10)
    self.RefEntry.grid(row=5, column=1)

    self.CMDLabel = Label(self.MonsterStats, text="CMD")
    self.CMDLabel.grid(row=5, column=2)
    self.CMDEntry = Entry(self.MonsterStats, width=10)
    self.CMDEntry.grid(row=5, column=3)

    self.CMBLabel = Label(self.MonsterStats, text="CMB")
    self.CMBLabel.grid(row=5, column=4)
    self.CMBEntry = Entry(self.MonsterStats, width=10)
    self.CMBEntry.grid(row=5, column=5)

  def updateMonster(self, monsterObj):
    print('updating')
    #will update all the various stats for the monster
    self.MonsterEntry.delete(0, END)
    self.MonsterEntry.insert(END, monsterObj['Name'])
    self.MonsterDesc.delete(1.0, END)
    self.MonsterDesc.insert(1.0, monsterObj['Description'])
    self.StrEntry.delete(0, END)
    self.StrEntry.insert(0, monsterObj['Str'])
    self.DexEntry.delete(0, END)
    self.DexEntry.insert(0, monsterObj['Dex'])
    self.ConEntry.delete(0, END)
    self.ConEntry.insert(0, monsterObj['Con'])
    self.IntEntry.delete(0, END)
    self.IntEntry.insert(0, monsterObj['Int'])
    self.WisEntry.delete(0, END)
    self.WisEntry.insert(0, monsterObj['Wis'])
    self.ChaEntry.delete(0, END)
    self.ChaEntry.insert(0, monsterObj['Cha'])
    self.BaBEntry.delete(0, END)
    self.BaBEntry.insert(0, monsterObj['BaseAtk'])
    self.ArmorBonusEntry.delete(0, END)
    self.ArmorBonusEntry.insert(0, monsterObj['Armor'][0])
    self.HPEntry.delete(0, END)
    self.HPEntry.insert(0, monsterObj['HP'])
    self.HDEntry.delete(0, END)
    self.HDEntry.insert(0, monsterObj['HD'])
    self.ACEntry.delete(0, END)
    self.ACEntry.insert(0, monsterObj['AC'][0])
    self.NaturalArmorBonusEntry.delete(0, END)
    self.NaturalArmorBonusEntry.insert(0, monsterObj['Natural'][0])
    self.SizeEntry.delete(0, END)
    self.SizeEntry.insert(0, monsterObj['Size'])
    self.FortEntry.delete(0, END)
    self.FortEntry.insert(0, monsterObj['Fort'])
    self.WillEntry.delete(0, END)
    self.WillEntry.insert(0, monsterObj['Will'])
    self.RefEntry.delete(0, END)
    self.RefEntry.insert(0, monsterObj['Ref'])
    self.CMDEntry.delete(0, END)
    self.CMDEntry.insert(0, monsterObj['CMD'])
    self.CMBEntry.delete(0, END)
    self.CMBEntry.insert(0, monsterObj['CMB'])

  def returnStats(self):
    allStats = {}
    allStats['Name'] = self.MonsterEntry.get()
    allStats['Str'] = self.StrEntry.get()
    allStats['Dex'] = self.DexEntry.get()
    allStats['Con'] = self.ConEntry.get()
    allStats['Int'] = self.IntEntry.get()
    allStats['Wis'] = self.WisEntry.get()
    allStats['Cha'] = self.ChaEntry.get()
    allStats['BaB'] = self.BaBEntry.get()
    allStats['Armor'] = self.ArmorBonusEntry.get()
    allStats['Natural'] = self.NaturalArmorBonusEntry.get()
    allStats['HP'] = self.HPEntry.get()
    allStats['HD'] = self.HDEntry.get()
    allStats['Size'] = self.SizeEntry.get()
    allStats['AC'] = self.ACEntry.get()
    allStats['Fort'] = self.FortEntry.get()
    allStats['Will'] = self.WillEntry.get()
    allStats['Ref'] = self.RefEntry.get()
    allStats['CMD'] = self.CMDEntry.get()
    allStats['CMB'] = self.CMBEntry.get()
    allStats['Desc'] = self.MonsterDesc.get(1.0, END)
    return allStats




class MonsterSelection():
  def __init__(self, master):
    self.results = []
    monsterFrame = Frame(master, bd=5, width=200,
                         highlightbackground='black', highlightthickness=2)
    monsterFrame.grid(row=2, rowspan=3, column=0, sticky='NW')

    self.SearchTitle = Label(monsterFrame, text="What Monster do you want?")
    self.SearchTitle.grid(row=0)
    self.SearchBar = Entry(monsterFrame)
    self.SearchBar.grid(row=1, ipady=5, ipadx=5)
    self.submitBtn = Button(monsterFrame, text="Search", command=self.search)
    self.submitBtn.grid(row=1, column=1)
    self.listbox = Listbox(monsterFrame, height=15, width=30)
    self.listbox.grid(row=3)

  def search(self):
    if(self.SearchBar.get() == ""):
      pass
    else:
      self.listbox.delete(0, END)
      self.results = SearchForMonsters(self.SearchBar.get())
      for item in self.results:
        self.listbox.insert(END, item['Name'])


class TokenPath():
  
  def __init__(self,master):
    self.PathFrame = Frame(
        master, highlightbackground='black', highlightthickness=2,bd=5)
    self.PathFrame.grid(row=3,column=0 ,columnspan=3,sticky='W')
    self.title = Label(self.PathFrame, text="Token Details", font=('Courier', 18))
    self.title.grid(row=0, column=0)
    self.NameLabel = Label(self.PathFrame,text="Token File Name")
    self.NameLabel.grid(row=0,column=1)
    self.TokenName = Entry(self.PathFrame,)
    self.TokenName.grid(row=0,column=2)
    self.PathLabel = Label(self.PathFrame, text="Output Location")
    self.PathLabel.grid(row=1, column=1)
    self.PathEntry = Entry(self.PathFrame, )
    self.PathEntry.grid(row=1, column=2)
    self.PathButton = Button(self.PathFrame,text="Choose Output Location",command=self.openPath)
    self.PathButton.grid(row=1,column=3,rowspan=1)

    self.MonsterImg = Label(self.PathFrame, text="Image URL")
    self.MonsterImg.grid(row=2, column=1, )
    self.MonsterImgEntry = Entry(self.PathFrame)
    self.MonsterImgEntry.grid(row=2, column=2)

    self.MonsterImgPath = Label(self.PathFrame, text="Local image Path")
    self.MonsterImgPath.grid(row=3, column=1, )
    self.MonsterImgPathEntry = Entry(self.PathFrame)
    self.MonsterImgPathEntry.grid(row=3, column=2)

    self.PathButton = Button(self.PathFrame, text="Choose file", command=self.openFile)
    self.PathButton.grid(row=3, column=3)

  def openPath(self):
    filePath = filedialog.askdirectory()
    print(filePath)
    self.PathEntry.delete(0,END)
    self.PathEntry.insert(0,filePath)
  def openFile(self):
    chosenFile = filedialog.askopenfile()
    self.pathToFile = chosenFile.name #extra?
    self.MonsterImgPathEntry.delete(0,END)
    self.MonsterImgPathEntry.insert(0,chosenFile.name)
  def returnTokenInformation(self):
    return {
        'fileName' : self.TokenName.get(),
        'outputPath' : self.PathEntry.get(),
        'imgUrl' : self.MonsterImgEntry.get(),
        'imgPath' : self.MonsterImgPathEntry.get()
    }
    

def SearchForMonsters(name):
  if(isinstance(name, str)):
    results = requests.get(
        "https://vxe45sf1th.execute-api.us-east-1.amazonaws.com/1/main?name=%s" % (name))
    if(results.status_code != 200):
      return "Something went wrong"
    else:
      json = results.json()['body']
      #will regex and fix all the various parts of each result
      newjson = []
      ArmorReg = re.compile('(\d+)')
      weaponNameReg = re.compile("(\w+\s\w+|\w+)")
      wepBonusReg = re.compile("([\+\-]\d+)")
      abilitiesRegEx = re.compile('(\d+|[-])')
      diceReg = re.compile("(\d+d\d+)")
      for result in json:
        allAbilities = result['AbilityScores'].replace(",", "")
        matches = re.findall(abilitiesRegEx, allAbilities)
        result['Str'] = matches[0]
        result['Dex'] = matches[1]
        result['Con'] = matches[2]
        result['Int'] = matches[3]
        result['Wis'] = matches[4]
        result['Cha'] = matches[5]
        allMods = result['AC_Mods'].strip("()").split(",")
        result['Armor'] = [re.search(ArmorReg, a)[0]
                           for a in allMods if 'armor' in a]
        if(result['Armor'] == []):
          result['Armor'] = [0]
        result['Natural'] = [re.search(ArmorReg, n)[0]
                             for n in allMods if 'natural' in n]
        if(result['Natural'] == []):
          result['Natural'] = [0]
        result['AC'] = result['AC'].split(",")
        saves = result['Saves'].split(",")
        result['Fort'] = [re.search(ArmorReg, n)[0]
                          for n in saves if 'Fort' in n]
        result['Will'] = [re.search(ArmorReg, n)[0]
                          for n in saves if 'Will' in n]
        result['Ref'] = [re.search(ArmorReg, n)[0]
                         for n in saves if 'Ref' in n]
        meleeAtks = result['Melee'].split(',')
        result['MeleeAtks'] = []
        for atk in meleeAtks:
          name = re.search(weaponNameReg, atk)[0]
          bonuses = re.findall(wepBonusReg, atk)
          XdY = re.search(diceReg, atk)[0].split('d')
          try:
            atk = bonuses[0]
          except IndexError as e:
            atk = 0
          try:
            dmg = bonuses[1]
          except IndexError as e:
            dmg = 0
          try:
            X = XdY[0]
          except IndexError as e:
            X = 0
          try:
            Y = XdY[1]
          except IndexError as e:
            Y = 0
          result['MeleeAtks'].append((name, atk, dmg, X, Y))
          atk
        meleeAtks
      return json
  else:
    return None


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
    Macro(label='str', group='skills', sortby='_1',
          command='Str: [d20+StrMod] (ACP: [ACP])'),
    Macro(label='dex', group='skills', sortby='_2',
          command='Dex: [d20+DexMod] (ACP: [ACP])'),
    Macro(label='con', group='skills', sortby='_3',
          command='Con: [d20+ConMod]'),
    Macro(label='int', group='skills', sortby='_4',
          command='Int: [d20+IntMod]'),
    Macro(label='wis', group='skills', sortby='_5',
          command='Wis: [d20+WisMod]'),
    Macro(label='cha', group='skills', sortby='_6',
          command='Cha: [d20+ChaMod]'),
    Macro(label='Perception', group='skills',
          command='Perception: [d20+Perception]'),
    Macro(label='Sense Motive', group='skills',
          command='Sense Motive: [d20+SenseMotive]'),
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
                thisMacro = Macro(
                    label=macroTuple[0], group='Attacks', sortby='_1', command=macroString),
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


def makeToken(master, stats, macros, tokenInfo):
  #first, get the image from the URL. will either be a local file or URL
  if(tokenInfo['imgUrl'] != ""):
    #assuming they want an image URL
    try:
      imgFile = requests.get(tokenInfo['imgUrl']).content
    except Exception as e:
      print("Img url did not return image correctly", e)
  elif(tokenInfo['imgPath'] != ""):
    correctedPath = tokenInfo['imgPath'].replace("/", "\\")
    imgFile = io.open(correctedPath, mode='rb').read()

  image = Asset('ASSETNAME', 'jpg', imgFile)
  propertyMap = {
      'Strength': stats['Str'],
      'Dexterity': stats['Dex'],
      'Constitution': stats['Con'],
      'Intelligence': stats['Int'],
      'Wisdom': stats['Wis'],
      'Charisma': stats['Cha'],
      'BAB': stats['BaB'],
      'MaxHP': stats['HP'],
      'Armor': ("{%s+%s}" % (stats['Armor'], stats['Natural'])),
      'Reflex': stats['Ref'],
      'Fortitude': stats['Fort'],
      'Will': stats['Will'],
      'AC': stats['AC']
  }
  #need to make sure size doesn't fuck things up
  temp = stats['Size']
  if temp.upper() == 'TINY':
    temp = 'Tiny'
  elif temp.upper() == 'SMALL':
    temp = 'Small'
  elif temp.upper() == 'MEDIUM':
    temp = 'Medium'
  elif temp.upper() == 'LARGE':
    temp = 'Large'
  elif temp.upper() == 'HUGE':
    temp = 'Huge'
  elif temp.upper() == 'COLOSSAL':
    temp = 'Colossal'
  else:
    temp = 'Medium'

  final_token = Token(
      image=image, name=stats['Name'], size=temp, properties=propertyMap, macros=macros)
  tokenFileName = tokenInfo['fileName'] if tokenInfo['fileName'] != "" else "token"

  final_token.make_file(
      tokenInfo['outputPath'] + "/" + tokenFileName + '.rptok')



description = '''
This is a python based tool that creates monster tokens at the press of a button. 
'''


def selectMonster(evt):
  selection = monsterBox.listbox.get(monsterBox.listbox.curselection())
  thisMonster = {}
  for mons in monsterBox.results:
    if mons['Name'] == selection:
      thisMonster = mons
      break
    else:
      thisMonster = None
  monsterDisplay.updateMonster(thisMonster)
  macros.updateMacros(thisMonster)


def createToken():
  #Need to gather all data in one dict for easy access
  stats = monsterDisplay.returnStats()
  tokenMacros = macros.returnMacros()
  tokenInfo = tokenPath.returnTokenInformation()
  makeToken(window, stats, tokenMacros, tokenInfo)


window = Tk()

window.title("Token Maker")
window.resizable(width=True, height=True)
# window.geometry('700x500')
title = Label(window, text="Monster Maker", font=('Courier', 24))
title.grid(row=0, column=0, sticky='N')
subtitle = Label(window, text=description, wraplength=200)
subtitle.grid(row=1, column=0)
SubmitButton = Button(window, text="Create Token!", height=5,
                      width=15, font=('Courier', 12), command=createToken)
SubmitButton.grid(row=3, column=2, sticky='N')
monsterBox = MonsterSelection(window)
monsterDisplay = MonsterDisplay(window)
tokenPath = TokenPath(window)
macros = TokenMacros(window)
monsterBox.listbox.bind('<<ListboxSelect>>', selectMonster)


window.mainloop()
