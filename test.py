import sys
import requests
sys.path.append('/token_scripts')
from token_scripts import tokens
import io


fileString = "C:/Users/jdevo/Desktop/Al.jpg".replace("/","\\")
myFile = io.open(fileString,mode='rb').read()

# # r = requests.get('http://vignette3.wikia.nocookie.net/forgottenrealms'
#                  '/images/3/36/Monster_Manual_5e_-_Ogre_-_p237.jpg')

# body = other.json();
# md5
image = tokens.Asset('ogre', 'jpg', myFile,)
t = tokens.Token(image=image, name='Ogre', size='Large',
                 properties={
                     'Strength': 21, 'Dexterity': 8, 'Constitution': 15,
                     'Intelligence': 6, 'Wisdom': 10, 'Charisma': 7,
                     'BAB': 3, 'MaxHP': 30,
                     'Armor': '{4+5}',
                 }, macros = []
                 )
                 
#need to figure out how to make it work without an image or a bad image
t.make_file('ogre1.rptok')

#t.make_file('ogre.zpi')
