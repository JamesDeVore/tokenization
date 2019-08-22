from tkinter import *
from tkinter import ttk


macrodesc = '''
Tokens come pre-loaded with the following macros: Fortitude save, Will Save, Reflex save, All ability checks, and modify HP. '''
class TokenMacros():
  def __init__ (self,master):
    self.MacroFrame = Frame(master, highlightbackground='black', highlightthickness=2, bd=5)
    self.MacroFrame.grid(row=2, column=2,columnspan=2, sticky='NE')
    self.MacroTitle = Label(master, text="Macro Details", font=('Courier', 18))
    self.MacroTitle.grid(column=2,row=1,sticky='')
    self.MacroDesc = Label(self.MacroFrame,text=macrodesc,wraplength=220,width=30)
    self.MacroDesc.grid(column=0, row=1, columnspan=4)
    self.ATKLabel = Label(self.MacroFrame,text="Attack Macro Details")
    self.ATKLabel.grid(column=0,row=2, columnspan=4)

    self.Seperator = ttk.Separator(self.MacroFrame)
    self.Seperator.grid(row=3, sticky = 'EW', columnspan=4)

    self.AtkMacroLabel = Label(self.MacroFrame, text="Name", )
    self.AtkMacroLabel.grid(column=0,row=4)
    self.AtkMacroName = Entry(self.MacroFrame,)
    self.AtkMacroName.grid(row=4,column=1, sticky='W')


    self.AtkMacroTypeLabel = Label(self.MacroFrame, text="Type", )
    self.AtkMacroTypeLabel.grid(column=2, row=4)
    self.AtkMacroTypeName = Entry(self.MacroFrame, width=10)
    self.AtkMacroTypeName.grid(row=4, column=3, sticky='W')

    self.AtkNumLabel = Label(self.MacroFrame,text="Number of dice")
    self.AtkNumLabel.grid(row=5,column=0)
    self.AtkNumEntry = Entry(self.MacroFrame, width=5)
    self.AtkNumEntry.grid(row=5,column=1)

    self.DieNumLabel = Label(self.MacroFrame, text="Dice Step")
    self.DieNumLabel.grid(row=5, column=2, sticky='W')
    self.DieNumEntry = Entry(self.MacroFrame,width=5)
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

  def updateMacros(self,monsterObj):
    try:
      firstMacro = monsterObj['MeleeAtks'][0]
      self.AtkMacroName.delete(0,END)
      self.AtkMacroName.insert(0,firstMacro[0])
      self.AtkNumEntry.delete(0,END)
      self.AtkNumEntry.insert(0,firstMacro[3])
      self.DieNumEntry.delete(0,END)
      self.DieNumEntry.insert(0,firstMacro[4])
      self.AtkBonusEntry.delete(0,END)
      self.AtkBonusEntry.insert(0,firstMacro[1])
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
        macro1 = (name,num,dice,atkBon,dmgBon,dmgType)
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
        macro2 = (name,dice,num,atkBon,dmgBon,dmgType)
        allMacros.append(macro2)
    except Exception as e:
      pass
    return allMacros

