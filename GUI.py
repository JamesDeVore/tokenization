

from tkinter import *
from search import SearchForMonsters
#need to make the parts into different classes 
testJson = [
  {"name":"hi"},
  {"name":"hello"}
]



#monster selection class
class MonsterSelection():
  def __init__(self, master):
    self.results = []
    monsterFrame = Frame(window, bd=5, width=200, height=400)
    monsterFrame.grid(row=2, rowspan=3, column=0, sticky='W')

    self.SearchTitle = Label(monsterFrame, text="What Monster do you want?")
    self.SearchTitle.grid(row=0)
    self.SearchBar = Entry(monsterFrame)
    self.SearchBar.grid(row=1, ipady=5, ipadx=5)
    self.submitBtn = Button(monsterFrame, text="Search", command=self.search)
    self.submitBtn.grid(row=1, column=1)
    self.listbox = Listbox(monsterFrame)
    self.listbox.grid(row=3)

  def search(self):
    self.listbox.delete(0,END)
    self.results = SearchForMonsters(self.SearchBar.get())
    for item in self.results:
      self.listbox.insert(END, item['Name'])


description = '''
This is a python based tool that creates monster tokens at the press of a button. 
'''
window = Tk()

window.title("Token Maker")
window.resizable(width=True, height=True)
window.geometry('700x500')
title = Label(window, text="Monster Maker", font=('Courier', 24))
title.grid(row=0, column=0, sticky='N', columnspan=3)

subtitle = Label(window, text=description)
subtitle.grid(row=1, column=0)
monsterBox = MonsterSelection(window)

window.mainloop()
