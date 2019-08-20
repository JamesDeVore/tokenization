import requests

def SearchForMonsters(name):
  if(isinstance(name,str)):
    results = requests.get(
      "https://vxe45sf1th.execute-api.us-east-1.amazonaws.com/1/main?name=%s" %(name))
    if(results.status_code != 200):
      return "Something went wrong"
    else:
      json = results.json()['body']
      return json
  else:
    return None
      
SearchForMonsters('eel')
