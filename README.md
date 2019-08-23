# Token Maker

A GUI based in tkinter that helps in the creation of MapTool tokens. Built on the token making script by: 
https://github.com/dougalsutherland/tokenization

## How to use:
### pip install -r requirements.txt
### with python shell, run main.py
#### Or (if it works) run main.exe

There is a monster search feature that will automatically *try* to fill in most of the details for the token if you wish to create a monster from the bestiary (based on the paizo monster database). Otherwise, feel free to add/edit the various properties of the token. as of 8/22/19 you will NEED an image (preferably .jpg) wither via url link, or a local file. Maptool tokens require some kind of image and I haven't put in any error handling yet. Feel free to reach out with any issues or if you want to contribute and make this even better!

### Related API:
Monster api : https://vxe45sf1th.execute-api.us-east-1.amazonaws.com/1/main?name=ogre - search by name
Spells api: : https://vxe45sf1th.execute-api.us-east-1.amazonaws.com/1/spells?name=invisibility - search by name as well

