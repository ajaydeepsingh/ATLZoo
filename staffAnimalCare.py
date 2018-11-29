from tkinter import *
from PIL import ImageTk, Image
import pymysql
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime, timedelta
import decimal

#=========Search Animals Window============
class ATLzooStaffAnimalCare:

    def __init__(self):
        # Invoke createLoginWindow; Invoke buildLoginWindow, Set loginWindow as mainloop
        #Connect to the database
        # self.db = self.connect()
        # self.cursor = self.db.cursor()
        # Login Window
        self.createSearchAnimalWindow()
        self.buildSearchAnimalWindow(self.searchAnimalWindow)
        self.searchAnimalWindow.mainloop()
        sys.exit()

    def createSearchAnimalWindow(self):
        # Create blank Search Animal Window
        self.searchAnimalWindow=Toplevel()
        self.searchAnimalWindow.title("Zoo Atlanta")
        self.searchAnimalWindow.geometry("600x600")

    def buildSearchAnimalWindow(self,searchAnimalWindow):

 
        titleLabel= Label(searchAnimalWindow,text = "Animal Detail", font = "Verdana 16 bold ")
        titleLabel.grid(row=1,column=1,sticky=W+E,pady=10)

        nameLabel = Label(searchAnimalWindow,text = "Name:")
        nameLabel.grid(row=2, column=0,pady=10)

        speciesLabel = Label(searchAnimalWindow, text="Species:")
        speciesLabel.grid(row=2, column=1,pady=10)
        
        ageLabel = Label(searchAnimalWindow,text = "Age:")
        ageLabel.grid(row=2,column=2,pady=10)

        exhibitLabel = Label(searchAnimalWindow,text = "Exhibit:")
        exhibitLabel.grid(row=3,column=0,pady=10)

        typeLabel = Label(searchAnimalWindow,text = "Type:")
        typeLabel.grid(row=3,column=1,pady=10)



        self.animalCareNotes = StringVar()
        animalCareEntry = Entry(searchAnimalWindow, textvariable=self.animalCareNotes, width=20)
        animalCareEntry.grid(row=4, column=0,pady=10, padx=10)

        logCareButton = Button(searchAnimalWindow, text="Log Notes", command=self.logAnimalNotesButtonClicked)
        logCareButton.grid(row=4,column=1,pady=10)
        
        selectAnimalTree = ttk.Treeview(searchAnimalWindow, columns=("Staff Member", "Note", "Time"))
        selectAnimalTree.heading('#0', text = "Staff Member")
        selectAnimalTree.heading('#1', text = "Note")
        selectAnimalTree.heading('#2', text = "Time")
        selectAnimalTree.column('#0', width = 150, anchor = "center")
        selectAnimalTree.column('#1', width = 150, anchor = "center")
        selectAnimalTree.column('#2', width = 150, anchor = "center")
        selectAnimalTree.place(x=20, y=200,width=450)

        

        backButton = Button(searchAnimalWindow, text="Back", command=self.searchAnimalWindowBackButtonClicked)
        backButton.place(x=240,y=440)


    def logAnimalNotesButtonClicked(self):

        self.searchAnimalWindow.destroy()
        self.createAnimalDetailWindow()

    def  searchAnimalWindowBackButtonClicked(self):
        self.searchAnimalWindow.destroy()
        import staffAnimals

a=ATLzooStaffAnimalCare()