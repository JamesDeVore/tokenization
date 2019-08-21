import sys
import requests
sys.path.append('/token_scripts')
from token_scripts import tokens

r = requests.get('http://vignette3.wikia.nocookie.net/forgottenrealms'
                 '/images/3/36/Monster_Manual_5e_-_Ogre_-_p237.jpg')


other = requests.get(
    'https://vxe45sf1th.execute-api.us-east-1.amazonaws.com/1/main?name=ogre')
body = other.json();

image = tokens.Asset('ogre', 'jpg', r.content)
t = tokens.Token(image=image, name='Ogre', size='Large',
                 properties={
                     'Strength': 21, 'Dexterity': 8, 'Constitution': 15,
                     'Intelligence': 6, 'Wisdom': 10, 'Charisma': 7,
                     'BAB': 3, 'MaxHP': 30,
                     'Armor': '{4+5}',
                 }
                 )
#t.make_file('ogre.rptok')

#t.make_file('ogre.zpi')
