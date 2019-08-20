

from tkinter import *
from search import SearchForMonsters
testJson = [
  {"name":"hi"},
  {"name":"hello"}
]

description = '''
This is a python based tool that creates monster tokens at the press of a button. 
'''
window = Tk()

window.title("Token Maker")
window.resizable(width=True,height=True)
window.geometry('700x500')
title = Label(window,text="Monster Maker",font=('Courier',24))
title.grid(row=0, column=0,sticky='N', columnspan=3)

subtitle = Label(window, text=description)
subtitle.grid(row=1, column=0)

monsterFrame = Frame(window, bd=5 ,width=200, height=400)
monsterFrame.grid(row=2,rowspan=3,column=0, sticky='W')


monsterSearchTitle = Label(monsterFrame,text="What Monster do you want?")
monsterSearchTitle.grid(row=0)

searchBar = Entry(monsterFrame,)
searchBar.grid(row=1, ipady=5, ipadx=5)
results = []
def search():
  listbox.delete(0,END)
  results = SearchForMonsters(searchBar.get())
  for item in results:
    listbox.insert(END, item['Name'])

submitBtn = Button(monsterFrame, text="Search",command=search)
submitBtn.grid(row=1,column=1)



listbox = Listbox(monsterFrame)
listbox.grid(row=3)






window.mainloop()
