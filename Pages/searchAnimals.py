from tkinter import *
from PIL import ImageTk, Image
import pymysql
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime, timedelta
import decimal

#=========Search Animals Window============
class ATLzooSearchAnimals:

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

    def buildSearchAnimalWindow(self,searchAnimalWindow):

        # Title Label
        titleLabel= Label(searchAnimalWindow,text = "Search Animals", font = "Verdana 16 bold ")
        titleLabel.grid(row=1,column=2,sticky=W+E)

        nameLabel = Label(searchAnimalWindow,text = "Name")
        nameLabel.grid(row=2, column=0)


        self.animalNameSV = StringVar()
        animalNameEntry = Entry(searchAnimalWindow, textvariable=self.animalNameSV, width=20)
        animalNameEntry.grid(row=2, column=1)

        speciesLabel = Label(searchAnimalWindow,text = "Species")
        speciesLabel.grid(row=3,column=0)
        self.speciesNameSV = StringVar()
        speciesNameEntry = Entry(searchAnimalWindow, textvariable=self.speciesNameSV, width=20)
        speciesNameEntry.grid(row=3, column=1)



        exhibitLabel = Label(searchAnimalWindow,text = "Exhibit")
        exhibitLabel.grid(row=4,column=0)
        exhibitDefault = StringVar()
        exhibitDefault.set("options")
        exhibitMenu = OptionMenu(searchAnimalWindow, exhibitDefault, "this","will","have","options","later")
        exhibitMenu.grid(row=4, column=1)

        minLabel=Label(searchAnimalWindow,text="Min")
        minLabel.grid(row=2,column=3, sticky=W)

        maxLabel=Label(searchAnimalWindow,text="Max")
        maxLabel.grid(row=2,column=4, sticky=W)

        ageLabel = Label(searchAnimalWindow,text = "Age")
        ageLabel.grid(row=3,column=2)

        minSpinBox = Spinbox(searchAnimalWindow, from_=0, to=10000)
        minSpinBox.grid(row=3, column=3,pady=10,sticky=W)

        maxSpinBox = Spinbox(searchAnimalWindow, from_=0, to=10000)
        maxSpinBox.grid(row=3, column=4,pady=10,sticky=W)


        typeLabel = Label(searchAnimalWindow,text = "Type")
        typeLabel.grid(row=4, column=2)
        # Name Entry
        typeDefault = StringVar()
        typeDefault.set("mammal")
        typeMenu = OptionMenu(searchAnimalWindow, typeDefault, "mammal", "bird", "amphibian", "reptile", "fish", "invertebrate")
        typeMenu.grid(row=4, column=3, sticky=W)

        
        # self.selectExhibitTree['show'] = "headings"
        selectAnimalTree = ttk.Treeview(searchAnimalWindow, columns=("Name", "Size", "Exhibit", "Age"))
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
        findAnimalsButton = Button(searchAnimalWindow, text="Find Animals", command=self.searchAnimalWindowFindAnimalsButtonClicked)
        findAnimalsButton.grid(row=6,column=3)

        backButton = Button(searchAnimalWindow, text="Back", command=self.searchAnimalWindowBackButtonClicked)
        backButton.grid(row=6,column=1)


    def searchAnimalWindowFindAnimalsButtonClicked(self):


        self.searchAnimalWindow.destroy()
        self.createAnimalDetailWindow()

    def  searchAnimalWindowBackButtonClicked(self):
        self.searchAnimalWindow.destroy()
        self.chooseFunctionalityWindow.deiconify()


a=ATLzooSearchAnimals()