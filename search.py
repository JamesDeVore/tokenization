import requests
import re
def SearchForMonsters(name):
  if(isinstance(name,str)):
    results = requests.get(
      "https://vxe45sf1th.execute-api.us-east-1.amazonaws.com/1/main?name=%s" %(name))
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
        allAbilities = result['AbilityScores'].replace(",","")
        matches = re.findall(abilitiesRegEx,allAbilities)
        result['Str'] = matches[0]
        result['Dex'] = matches[1]
        result['Con'] = matches[2]
        result['Int'] = matches[3]
        result['Wis'] = matches[4]
        result['Cha'] = matches[5]
        allMods = result['AC_Mods'].strip("()").split(",")
        result['Armor'] = [re.search(ArmorReg,a)[0] for a in allMods if 'armor' in a]
        if(result['Armor'] == []):
          result['Armor'] = [0]
        result['Natural'] = [re.search(ArmorReg,n)[0] for n in allMods if 'natural' in n]
        if(result['Natural'] == []):
          result['Natural'] = [0]
        result['AC'] = result['AC'].split(",")
        saves = result['Saves'].split(",")
        result['Fort'] = [re.search(ArmorReg,n)[0] for n in saves if 'Fort' in n]
        result['Will'] = [re.search(ArmorReg,n)[0] for n in saves if 'Will' in n]
        result['Ref'] = [re.search(ArmorReg,n)[0] for n in saves if 'Ref' in n]
        meleeAtks = result['Melee'].split(',')
        result['MeleeAtks'] = []
        for atk in meleeAtks:
          name = re.search(weaponNameReg,atk)[0]
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
          result['MeleeAtks'].append((name,atk,dmg,X,Y))
          atk
        meleeAtks
      return json
  else:
    return None
      
# SearchForMonsters('Dragon')
