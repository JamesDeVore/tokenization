from tkinter import *
from tkinter import ttk


macrodesc = '''
Tokens come pre-loaded with the following macros:\n\u2022Fortitude save\n\u2022Will Save\n\u2022Reflex save\n\u2022All ability checks\n\u2022Modify HP '''
class TokenMacros():
  def __init__ (self,master):

    self.MacroFrame = Frame(master, padx=10, pady=10)
    self.MacroFrame.grid(row=2, column=2, columnspan=2, sticky='NE')
    self.MacroTitle = Label(master, text="Macro Details", font=('Courier', 18))
    self.MacroTitle.grid(column=2, row=1, columnspan=2, sticky='')
    self.MacroDesc = Label(self.MacroFrame,text=macrodesc,wraplength=280,width=40)
    self.MacroDesc.grid(column=0, row=1, columnspan=4)
    self.ATKLabel = Label(self.MacroFrame,text="Attack Macro Details")
    self.ATKLabel.grid(column=0,row=2, columnspan=4)
    self.Seperator = ttk.Separator(self.MacroFrame)
    self.Seperator.grid(row=3, sticky='EW', columnspan=4)
    self.allData = []
    
    for i in range(1,4):
      #only want 3 because of space reasons
      AtkMacroLabel = Label(self.MacroFrame, text="Name", )
      AtkMacroLabel.grid(column=0,row=4 + (i * 4))
      AtkMacroName = Entry(self.MacroFrame,)
      AtkMacroName.grid(row=4 + (i * 4),column=1, sticky='W')

      AtkMacroTypeLabel = Label(self.MacroFrame, text="Type", )
      AtkMacroTypeLabel.grid(column=2, row=4 + (i * 4))
      AtkMacroTypeName = Entry(self.MacroFrame, width=10)
      AtkMacroTypeName.grid(row=4 + (i * 4), column=3, sticky='W')

      AtkNumLabel = Label(self.MacroFrame,text="Number of dice")
      AtkNumLabel.grid(row=5 + (i * 4),column=0)
      AtkNumEntry = Entry(self.MacroFrame, width=5)
      AtkNumEntry.grid(row=5 + (i * 4),column=1)

      DieNumLabel = Label(self.MacroFrame, text="Dice Step")
      DieNumLabel.grid(row=5 + (i * 4), column=2, sticky='W')
      DieNumEntry = Entry(self.MacroFrame,width=5)
      DieNumEntry.grid(row=5 + (i * 4), column=3, sticky='W')

      AtkBonusLabel = Label(self.MacroFrame, text="ATK Bonus")
      AtkBonusLabel.grid(row=6 + (i * 4), column=0)
      AtkBonusEntry = Entry(self.MacroFrame, width=5)
      AtkBonusEntry.grid(row=6 + (i * 4), column=1)

      DmgBonusLabel = Label(self.MacroFrame, text="Damage Bonus")
      DmgBonusLabel.grid(row=6 + (i * 4), column=2, sticky='W')
      DmgBonusEntry = Entry(self.MacroFrame, width=5)
      DmgBonusEntry.grid(row=6 + (i * 4), column=3, sticky='W')
      
      self.allData.append((AtkMacroName,AtkMacroTypeName,AtkNumEntry,DieNumEntry,AtkBonusEntry,DmgBonusEntry))


      self.Seperator2 = ttk.Separator(self.MacroFrame)
      self.Seperator2.grid(row=7 + (i * 4), sticky='EW', columnspan=4)
    print(self.allData)


  def updateMacros(self,monsterObj):
    #first clear all fields
    for macro in self.allData:
      for field in macro:
        field.delete(0,END)
        field.insert(0,"")
    incomingAtks = enumerate(monsterObj['MeleeAtks'])
    for enum,(name,atkBon,dmgBon,numDice,diceStep) in incomingAtks:
      macroTuple = self.allData[enum]
      # AtkMacroName,AtkMacroTypeName,AtkNumEntry,DieNumEntry,AtkBonusEntry,DmgBonusEntry = macroTuple order
      macroTuple[0].delete(0,END)
      macroTuple[0].insert(0,name) #name

      macroTuple[1].delete(0, END) #type doesn't get served in
      macroTuple[1].insert(0, "")

      macroTuple[2].delete(0,END)
      macroTuple[2].insert(0,numDice) #number of dice

      macroTuple[3].delete(0,END)
      macroTuple[3].insert(0,diceStep) #diestep

      macroTuple[4].delete(0,END)
      macroTuple[4].insert(0,atkBon) #to hit bonus

      macroTuple[5].delete(0, END)
      macroTuple[5].insert(0, dmgBon)
    
  def returnMacros(self):
    #gather all macro information and return it
    try:
      allMacros = []
      #may want to do some verification
      for AtkMacroName, AtkMacroTypeName, AtkNumEntry, DieNumEntry, AtkBonusEntry, DmgBonusEntry in self.allData:
        name = AtkMacroName.get()
        dmgType = AtkMacroTypeName.get()
        dieNum = AtkNumEntry.get()
        dieStep = DieNumEntry.get()
        atkBon = AtkBonusEntry.get()
        dmgBon = DmgBonusEntry.get()
        assert(name != "")
        allMacros.append((name, dieNum, dieStep, atkBon, dmgBon,dmgType))
        return allMacros
    except Exception as e:
      e = Exception("Macros require a name")
      raise e
    
    

