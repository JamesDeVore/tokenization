from tkinter import *
from tkinter import filedialog


class TokenPath():

  def __init__(self,master):
    self.PathFrame = Frame(
        master, highlightbackground='black', highlightthickness=2,bd=5)
    self.PathFrame.grid(row=3,column=0 ,columnspan=3,sticky='W')
    self.title = Label(self.PathFrame, text="Token Details", font=('Courier', 18))
    self.title.grid(row=0, column=0)
    self.NameLabel = Label(self.PathFrame,text="Token File Name")
    self.NameLabel.grid(row=0,column=1)
    self.TokenName = Entry(self.PathFrame,width=25)
    self.TokenName.grid(row=0,column=2)
    self.PathLabel = Label(self.PathFrame, text="Token File Location")
    self.PathLabel.grid(row=1, column=1)
    self.PathEntry = Entry(self.PathFrame, width=25)
    self.PathEntry.grid(row=1, column=2,columnspan=3)
    self.PathButton = Button(self.PathFrame,text="Choose Location",command=self.openPath,height=3,width=12)
    self.PathButton.grid(row=0,column=5,rowspan=2)

  def openPath(self):
    filePath = filedialog.askdirectory()
    print(filePath)
    self.PathEntry.delete(0,END)
    self.PathEntry.insert(0,filePath)
    
  


    
