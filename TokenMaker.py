from token_scripts import tokens
import requests
import sys
import mimetypes
import io

sys.path.append('/token_scripts')


def makeToken(master,stats, macros, tokenInfo):
  #first, get the image from the URL. will either be a local file or URL
  if(tokenInfo['imgUrl'] != ""):
    #assuming they want an image URL
    try:
      imgFile = requests.get(tokenInfo['imgUrl']).content
    except Exception as e:
      raise e
  elif(tokenInfo['imgPath'] != ""):
    correctedPath = tokenInfo['imgPath'].replace("/","\\")
    imgFile = io.open(correctedPath, mode='rb').read()

  image = tokens.Asset('ASSETNAME','jpg',imgFile)
  propertyMap = {
      'Strength': stats['Str'],
      'Dexterity': stats['Dex'],
      'Constitution': stats['Con'],
      'Intelligence': stats['Int'],
      'Wisdom': stats['Wis'],
      'Charisma': stats['Cha'],
      'BAB': stats['BaB'],
      'MaxHP': stats['HP'],
      'Armor': ("{%s+%s}"%(stats['Armor'],stats['Natural'])),
      'Reflex':stats['Ref'],
      'Fortitude':stats['Fort'],
      'Will':stats['Will'],
      'AC':stats['AC']
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

  final_token = tokens.Token(image=image,name=stats['Name'], size=temp,properties=propertyMap,macros=macros)
  tokenFileName = tokenInfo['fileName'] if tokenInfo['fileName'] != "" else "token"

  final_token.make_file(tokenInfo['outputPath'] + "/" + tokenFileName + '.rptok')
