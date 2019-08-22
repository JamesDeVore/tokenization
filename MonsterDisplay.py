from tkinter import *
from search import SearchForMonsters

class MonsterDisplay():
  def __init__(self, master):
    self.title = Label(master, text="Monster Details", font=('Courier',18))
    self.title.grid(row=1, column=1)

    self.MonsterDisplay = Frame(
        master, highlightbackground='black', highlightthickness=2)
    self.MonsterDisplay.grid(row=2, column=1)
    self.MonsterName = Label(self.MonsterDisplay, text="Name of Monster")
    self.MonsterName.grid(row=0, column=0,)
    self.MonsterEntry = Entry(self.MonsterDisplay)
    self.MonsterEntry.grid(row=0, column=1)

    self.MonsterDesc = Text(self.MonsterDisplay, height=10, width=60)
    self.MonsterDesc.grid(row=1, column=0,columnspan=4)
    # self.DescScroll = Scrollbar(self.MonsterDisplay,orient='vertical',command=self.MonsterDesc.yview)
    # self.DescScroll.grid(row=1,column=2, sticky='E')
    # self.MonsterDesc['yscrollcommand'] = self.DescScroll.set

    self.MonsterStats = Frame(
        self.MonsterDisplay, highlightbackground='black', highlightthickness=2)
    self.MonsterStats.grid(row=2, column=0,sticky='S',columnspan=4)

    self.StrLabel = Label(self.MonsterStats, text="Strength")
    self.StrLabel.grid(row=0, column=0)
    self.StrEntry = Entry(self.MonsterStats,width=10)
    self.StrEntry.grid(row=0, column=1)

    self.DexLabel = Label(self.MonsterStats, text="Dexterity")
    self.DexLabel.grid(row=0, column=2)
    self.DexEntry = Entry(self.MonsterStats,width=10)
    self.DexEntry.grid(row=0, column=3)

    self.ConLabel = Label(self.MonsterStats, text="Constitution")
    self.ConLabel.grid(row=0, column=4)
    self.ConEntry = Entry(self.MonsterStats,width=10)
    self.ConEntry.grid(row=0, column=5)

    self.IntLabel = Label(self.MonsterStats, text="Intelligence")
    self.IntLabel.grid(row=1, column=0)
    self.IntEntry = Entry(self.MonsterStats,width=10)
    self.IntEntry.grid(row=1, column=1)

    self.WisLabel = Label(self.MonsterStats, text="Wisdom")
    self.WisLabel.grid(row=1, column=2)
    self.WisEntry = Entry(self.MonsterStats,width=10)
    self.WisEntry.grid(row=1, column=3)

    self.ChaLabel = Label(self.MonsterStats, text="Charisma")
    self.ChaLabel.grid(row=1, column=4)
    self.ChaEntry = Entry(self.MonsterStats,width=10)
    self.ChaEntry.grid(row=1, column=5)

    self.BaBLabel = Label(self.MonsterStats, text="BaB")
    self.BaBLabel.grid(row=2, column=0)
    self.BaBEntry = Entry(self.MonsterStats,width=10)
    self.BaBEntry.grid(row=2, column=1)

    self.HPLabel = Label(self.MonsterStats, text="HP")
    self.HPLabel.grid(row=2, column=2)
    self.HPEntry = Entry(self.MonsterStats,width=10)
    self.HPEntry.grid(row=2, column=3)

    self.HDLabel = Label(self.MonsterStats, text="HD")
    self.HDLabel.grid(row=2, column=4)
    self.HDEntry = Entry(self.MonsterStats,width=10)
    self.HDEntry.grid(row=2, column=5)

    self.ACLabel = Label(self.MonsterStats, text="AC")
    self.ACLabel.grid(row=3, column=0)
    self.ACEntry = Entry(self.MonsterStats,width=10)
    self.ACEntry.grid(row=3, column=1)

    self.ArmorBonusLabel = Label(self.MonsterStats, text="Armor Bonus")
    self.ArmorBonusLabel.grid(row=3, column=2)
    self.ArmorBonusEntry = Entry(self.MonsterStats,width=10)
    self.ArmorBonusEntry.grid(row=3, column=3)

    self.NaturalArmorBonusLabel = Label(self.MonsterStats, text="Natural Armor Bonus")
    self.NaturalArmorBonusLabel.grid(row=3, column=4)
    self.NaturalArmorBonusEntry = Entry(self.MonsterStats,width=10)
    self.NaturalArmorBonusEntry.grid(row=3, column=5)

    self.SizeLabel = Label(self.MonsterStats, text="Size")
    self.SizeLabel.grid(row=4, column=0)
    self.SizeEntry = Entry(self.MonsterStats,width=10)
    self.SizeEntry.grid(row=4, column=1)

    self.FortLabel = Label(self.MonsterStats, text="Fortitude")
    self.FortLabel.grid(row=4, column=2)
    self.FortEntry = Entry(self.MonsterStats,width=10)
    self.FortEntry.grid(row=4, column=3)

    self.WillLabel = Label(self.MonsterStats, text="Will")
    self.WillLabel.grid(row=4, column=4)
    self.WillEntry = Entry(self.MonsterStats,width=10)
    self.WillEntry.grid(row=4, column=5)

    self.RefLabel = Label(self.MonsterStats, text="Reflex")
    self.RefLabel.grid(row=5, column=0)
    self.RefEntry = Entry(self.MonsterStats,width=10)
    self.RefEntry.grid(row=5, column=1)

    self.CMDLabel = Label(self.MonsterStats, text="CMD")
    self.CMDLabel.grid(row=5, column=2)
    self.CMDEntry = Entry(self.MonsterStats,width=10)
    self.CMDEntry.grid(row=5, column=3)

    self.CMBLabel = Label(self.MonsterStats, text="CMB")
    self.CMBLabel.grid(row=5, column=4)
    self.CMBEntry = Entry(self.MonsterStats,width=10)
    self.CMBEntry.grid(row=5, column=5)


  def updateMonster(self, monsterObj):
    print('updating')
    #will update all the various stats for the monster
    self.MonsterEntry.delete(0, END)
    self.MonsterEntry.insert(END, monsterObj['Name'])
    self.MonsterDesc.delete(1.0,END)
    self.MonsterDesc.insert(1.0,monsterObj['Description'])
    self.StrEntry.delete(0, END)
    self.StrEntry.insert(0, monsterObj['Str'])
    self.DexEntry.delete(0, END)
    self.DexEntry.insert(0, monsterObj['Dex'])
    self.ConEntry.delete(0, END)
    self.ConEntry.insert(0, monsterObj['Con'])
    self.IntEntry.delete(0, END)
    self.IntEntry.insert(0, monsterObj['Int'])
    self.WisEntry.delete(0, END)
    self.WisEntry.insert(0, monsterObj['Wis'])
    self.ChaEntry.delete(0, END)
    self.ChaEntry.insert(0, monsterObj['Cha'])
    self.BaBEntry.delete(0, END)
    self.BaBEntry.insert(0, monsterObj['BaseAtk'])
    self.ArmorBonusEntry.delete(0, END)
    self.ArmorBonusEntry.insert(0, monsterObj['Armor'][0])
    self.HPEntry.delete(0, END)
    self.HPEntry.insert(0, monsterObj['HP'])
    self.HDEntry.delete(0, END)
    self.HDEntry.insert(0, monsterObj['HD'])
    self.ACEntry.delete(0, END)
    self.ACEntry.insert(0, monsterObj['AC'][0])
    self.NaturalArmorBonusEntry.delete(0, END)
    self.NaturalArmorBonusEntry.insert(0, monsterObj['Natural'][0])
    self.SizeEntry.delete(0, END)
    self.SizeEntry.insert(0, monsterObj['Size'])
    self.FortEntry.delete(0, END)
    self.FortEntry.insert(0, monsterObj['Fort'])
    self.WillEntry.delete(0, END)
    self.WillEntry.insert(0, monsterObj['Will'])
    self.RefEntry.delete(0, END)
    self.RefEntry.insert(0, monsterObj['Ref'])
    self.CMDEntry.delete(0, END)
    self.CMDEntry.insert(0, monsterObj['CMD'])
    self.CMBEntry.delete(0, END)
    self.CMBEntry.insert(0, monsterObj['CMB'])
  def returnStats(self):
    allStats = {}
    allStats['Name'] = self.MonsterEntry.get()
    allStats['Str'] = self.StrEntry.get()
    allStats['Dex'] = self.DexEntry.get()
    allStats['Con'] = self.ConEntry.get()
    allStats['Int'] = self.IntEntry.get()
    allStats['Wis'] = self.WisEntry.get()
    allStats['Cha'] = self.ChaEntry.get()
    allStats['BaB'] = self.BaBEntry.get()
    allStats['Armor'] = self.ArmorBonusEntry.get()
    allStats['Natural'] = self.NaturalArmorBonusEntry.get()
    allStats['HP'] = self.HPEntry.get()
    allStats['HD'] = self.HDEntry.get()
    allStats['Size'] = self.SizeEntry.get()
    allStats['AC'] = self.ACEntry.get()
    allStats['Fort'] = self.FortEntry.get()
    allStats['Will'] = self.WillEntry.get()
    allStats['Ref'] = self.RefEntry.get()
    allStats['CMD'] = self.CMDEntry.get()
    allStats['CMB'] = self.CMBEntry.get()
    allStats['Desc'] = self.MonsterDesc.get(1.0,END)
    return allStats
