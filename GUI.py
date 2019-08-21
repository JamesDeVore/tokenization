
import sys
from token_scripts import tokens
from tkinter import *
from search import SearchForMonsters
from TokenPath import TokenPath
from MonsterSelection import MonsterSelection
from MonsterDisplay import MonsterDisplay
from TokenMacros import TokenMacros
sys.path.append('/token_scripts')
from token_scripts import tokens
#need to make the parts into different classes 


description = '''
This is a python based tool that creates monster tokens at the press of a button. 
'''
window = Tk()

window.title("Token Maker")
window.resizable(width=True, height=True)
# window.geometry('700x500')
title = Label(window, text="Monster Maker", font=('Courier', 24))
title.grid(row=0, column=0, sticky='N')

subtitle = Label(window, text=description ,wraplength=200)
subtitle.grid(row=1, column=0)

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
  print("hi")

SubmitButton = Button(window, text="Create Token!",height=5,width=15,font=('Courier',12),command=createToken)
SubmitButton.grid(row=3,column=2, sticky='N')

monsterBox = MonsterSelection(window)
monsterDisplay = MonsterDisplay(window)
tokenPath = TokenPath(window)
macros = TokenMacros(window)
monsterBox.listbox.bind('<<ListboxSelect>>',selectMonster)



window.mainloop()
