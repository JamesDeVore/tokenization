from tkinter import *
from tkinter import filedialog
from tkinter import messagebox


class TokenPath():

  def __init__(self,master):
    self.PathFrame = Frame(
        master, highlightbackground='black')
    self.PathFrame.grid(row=3,column=0 ,columnspan=3,sticky='W')
    self.title = Label(self.PathFrame, text="Token Details", font=('Courier', 18))
    self.title.grid(row=0, column=0)
    self.NameLabel = Label(self.PathFrame,text="Token File Name")
    self.NameLabel.grid(row=0,column=1)
    self.TokenName = Entry(self.PathFrame,)
    self.TokenName.grid(row=0,column=2)
    self.PathLabel = Label(self.PathFrame, text="Output Location")
    self.PathLabel.grid(row=1, column=1)
    self.PathEntry = Entry(self.PathFrame, )
    self.PathEntry.grid(row=1, column=2)
    self.PathButton = Button(self.PathFrame,text="Choose Output Location",command=self.openPath)
    self.PathButton.grid(row=1,column=3,rowspan=1)

    self.MonsterImg = Label(self.PathFrame, text="Image URL")
    self.MonsterImg.grid(row=2, column=1, )
    self.MonsterImgEntry = Entry(self.PathFrame)
    self.MonsterImgEntry.grid(row=2, column=2)

    self.MonsterImgPath = Label(self.PathFrame, text="Local image Path")
    self.MonsterImgPath.grid(row=3, column=1, )
    self.MonsterImgPathEntry = Entry(self.PathFrame)
    self.MonsterImgPathEntry.grid(row=3, column=2)

    self.PathButton = Button(self.PathFrame, text="Choose file", command=self.openFile)
    self.PathButton.grid(row=3, column=3)

  def openPath(self):
    filePath = filedialog.askdirectory()
    print(filePath)
    self.PathEntry.delete(0,END)
    self.PathEntry.insert(0,filePath)
  def openFile(self):
    chosenFile = filedialog.askopenfile()
    self.pathToFile = chosenFile.name #extra?
    self.MonsterImgPathEntry.delete(0,END)
    self.MonsterImgPathEntry.insert(0,chosenFile.name)
  def returnTokenInformation(self):
    name = self.TokenName.get()
    output = self.PathEntry.get()
    imgURL = self.MonsterImgEntry.get()
    imgPath = self.MonsterImgPathEntry.get()
    errorString = ""
    if(name == ""):
      errorString += "Invalid file name \n"
    if(output == ""):
      errorString += "Invalid file path \n"
    if(imgURL == "" and imgPath == ""):
      errorString += "No image specified \n"
    if(errorString != ""):
      raise Exception(errorString)
    else:
      return  {
          'fileName' : self.TokenName.get(),
          'outputPath' : self.PathEntry.get(),
          'imgUrl' : self.MonsterImgEntry.get(),
          'imgPath' : self.MonsterImgPathEntry.get()
      }
    
    
  


    
