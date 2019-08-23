from tkinter import *
from search import SearchForMonsters


class MonsterSelection():
  def __init__(self, master):

    self.title = Label(master, text="Monster Search", font=('Courier', 18))
    self.title.grid(row=1, column=0)
    self.results = []
    monsterFrame = Frame(master, bd=5, width=200)
    monsterFrame.grid(row=2, rowspan=3, column=0, sticky='NW')

    self.SearchTitle = Label(monsterFrame, text="What Monster do you want?")
    self.SearchTitle.grid(row=0)
    self.SearchBar = Entry(monsterFrame)
    self.SearchBar.grid(row=1, ipady=5, ipadx=5)
    self.submitBtn = Button(monsterFrame, text="Search", command=self.search)
    self.submitBtn.grid(row=1, column=1)
    self.listbox = Listbox(monsterFrame,height=15,width=30)
    self.listbox.grid(row=3)

  def search(self):
    if(self.SearchBar.get() == ""):
      pass
    else:
      self.listbox.delete(0, END)
      self.results = SearchForMonsters(self.SearchBar.get())
      for item in self.results:
        self.listbox.insert(END, item['Name'])
