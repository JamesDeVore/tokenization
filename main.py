
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sys
sys.path.insert(1,'/token_scripts')
sys.path.insert(1,'/pythonScripts')
from token_scripts import tokens

from search import SearchForMonsters
from TokenPath import TokenPath
from MonsterSelection import MonsterSelection
from MonsterDisplay import MonsterDisplay
from TokenMacros import TokenMacros
from TokenMaker import makeToken
import requests

from token_scripts import tokens
#need to make the parts into different classes 


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
    else :
      thisMonster = None
  monsterDisplay.updateMonster(thisMonster)
  macros.updateMacros(thisMonster)

def createToken():
  #Need to gather all data in one dict for easy access
  try:
    stats = monsterDisplay.returnStats()
    tokenMacros = macros.returnMacros()
    tokenInfo = tokenPath.returnTokenInformation()
    makeToken(window, stats, tokenMacros, tokenInfo)
  except Exception as e:
    messagebox.showerror("Error", e.args)

window = Tk()

window.title("Token Maker")
window.resizable(width=True, height=True)
# window.geometry('700x500')
title = Label(window, text="Monster Maker", font=('Courier', 24))
title.grid(row=0, column=0, sticky='N')

SubmitButton = Button(window, text="Create Token!",height=5,width=15,font=('Courier',12),command=createToken)
SubmitButton.grid(row=3,column=2, sticky='N')
monsterBox = MonsterSelection(window)
monsterDisplay = MonsterDisplay(window)
tokenPath = TokenPath(window)
macros = TokenMacros(window)
monsterBox.listbox.bind('<<ListboxSelect>>',selectMonster)



window.mainloop()
