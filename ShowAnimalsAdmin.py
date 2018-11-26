from tkinter import *
from PIL import ImageTk, Image
import pymysql
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime, timedelta
import decimal


class ATLzooAnimalsAdmin:

    def __init__(self):
        # Invoke createLoginWindow; Invoke buildLoginWindow, Set loginWindow as mainloop
        #Connect to the database
        # self.db = self.connect()
        # self.cursor = self.db.cursor()
        # Login Window
        self.createShowAnimalWindowAdmin()
        self.buildShowAnimalWindowAdmin(self.showAnimalWindowAdmin)
        self.showAnimalWindowAdmin.mainloop()
        sys.exit()

    def createShowAnimalWindowAdmin(self):
        # Create blank Search Animal Window
        self.showAnimalWindowAdmin=Toplevel()
        self.showAnimalWindowAdmin.title("Zoo Atlanta")

    def buildShowAnimalWindowAdmin(self,showAnimalWindowAdmin):

        # Title Label
        titleLabel= Label(showAnimalWindowAdmin,text = "Search Animals", font = "Verdana 16 bold ")
        titleLabel.grid(row=1,column=2,sticky=W+E)

        # Labels
        exhibitLabel = Label(showAnimalWindowAdmin,text = "Exhibit")
        exhibitLabel.grid(row=2,column=1)
        ageLabel = Label(showAnimalWindowAdmin,text = "Age")
        ageLabel.grid(row=3,column=1)
        typeLabel = Label(showAnimalWindowAdmin,text = "Type")
        typeLabel.grid(row=4,column=1)

        nameLabel = Label(showAnimalWindowAdmin,text = "Name")
        nameLabel.grid(row=2, column=2)
        # Name Entry
        self.animalNameSV = StringVar()
        animalNameEntry = Entry(showAnimalWindowAdmin, textvariable=self.animalNameSV, width=20)
        animalNameEntry.grid(row=2, column=3)

        speciesLabel = Label(showAnimalWindowAdmin,text = "Species")
        speciesLabel.grid(row=3, column=2)
        # Name Entry
        self.animalSpeciesSV = StringVar()
        animalSpeciesEntry = Entry(showAnimalWindowAdmin, textvariable=self.animalSpeciesSV, width=20)
        animalSpeciesEntry.grid(row=2, column=3)

        selectAnimalTree = ttk.Treeview(showAnimalWindowAdmin, columns=("Name", "Size", "Exhibit", "Age"))
        selectAnimalTree.heading('#0', text = "Name")
        selectAnimalTree.heading('#1', text = "Species")
        selectAnimalTree.heading('#2', text = "Exhibit")
        selectAnimalTree.heading('#3', text = "Age")
        selectAnimalTree.heading('#4', text = "Type")
        selectAnimalTree.column('#0', width = 150, anchor = "center")
        selectAnimalTree.column('#1', width = 150, anchor = "center")
        selectAnimalTree.column('#2', width = 150, anchor = "center")
        selectAnimalTree.column('#3', width = 150, anchor = "center")
        selectAnimalTree.column('#4', width = 150, anchor = "center")
        selectAnimalTree.grid(row=5, columnspan=4, sticky = 'nsew')

        # Button
        findAnimalsButton = Button(showAnimalWindowAdmin, text="Find Animals", command=self.showAnimalWindowAdminFindAnimalsButtonClicked)
        findAnimalsButton.grid(row=6,column=2)

        removeAnimalsButton = Button(showAnimalWindowAdmin, text="Remove Animal", command=self.showAnimalWindowAdminRemoveAnimalWindowButtonClicked)
        removeAnimalsButton.grid(row=6,column=3)

        backButton = Button(showAnimalWindowAdmin, text="Back", command=self.showAnimalWindowAdminBackButtonClicked)
        backButton.grid(row=6,column=1)


    def showAnimalWindowAdminFindAnimalsButtonClicked(self):
        self.searchAnimalWindowAdmin.destroy()
        self.createAnimalDetailWindow()

    def showAnimalWindowAdminRemoveAnimalWindowButtonClicked(self):
        self.searchAnimalWindowAdmin.destroy()
        self.chooseFunctionalityWindow.deiconify()

    def showAnimalWindowAdminBackButtonClicked(self):
        self.searchAnimalWindowAdmin.destroy()
        self.chooseFunctionalityWindow.deiconify()

a=ATLzooAnimalsAdmin()