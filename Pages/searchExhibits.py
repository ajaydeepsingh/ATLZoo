import tkinter
from tkinter import *
from PIL import ImageTk, Image
import pymysql
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime, timedelta
import decimal

#=========Search Exhibit Window============
class ATLzooSearchExhibits():

    def __init__(self):
        # Invoke createLoginWindow; Invoke buildLoginWindow, Set loginWindow as mainloop
        #Connect to the database
        # self.db = self.connect()
        # self.cursor = self.db.cursor()
        # Login Window
        self.createSearchExhibitWindow()
        self.buildSearchExhibitWindow(self.searchExhibitWindow)
        self.searchExhibitWindow.mainloop()
        sys.exit()

    def createSearchExhibitWindow(self):
        # Create blank Search Exhibit Window
        self.searchExhibitWindow=Toplevel()
        self.searchExhibitWindow.title("Zoo Atlanta")

    def buildSearchExhibitWindow(self, searchExhibitWindow):

        # Title Label
        titleLabel= Label(searchExhibitWindow,text = "Search Exhibits", font = "Verdana 16 bold ")
        titleLabel.grid(row=1,column=2,sticky=W+E)

        nameLabel = Label(searchExhibitWindow,text = "Name:")
        nameLabel.grid(row=2, column=0)

        self.exhibitNameSV = StringVar()
        animalNameEntry = Entry(searchExhibitWindow, textvariable=self.exhibitNameSV, width=20)
        animalNameEntry.grid(row=2, column=1)

        minLabel=Label(searchExhibitWindow,text="Min:")
        minLabel.grid(row=2,column=4, sticky=W)

        maxLabel=Label(searchExhibitWindow,text="Max:")
        maxLabel.grid(row=2,column=5, sticky=W)

        numAnimalsLabel = Label(searchExhibitWindow,text = "Number of Animals:")
        numAnimalsLabel.grid(row=3,column=3)

        minSpinBox = Spinbox(searchExhibitWindow, from_=0, to=10000)
        minSpinBox.grid(row=3, column=4,pady=10,sticky=W)

        maxSpinBox = Spinbox(searchExhibitWindow, from_=0, to=10000)
        maxSpinBox.grid(row=3, column=5,pady=10,sticky=W)


        waterLabel = Label(searchExhibitWindow,text = "Water Feature:")
        waterLabel.grid(row=4, column=3)
        # Name Entry
        typeDefault = StringVar()
        typeDefault.set("No")
        typeMenu = OptionMenu(searchExhibitWindow, typeDefault, "Yes", "No")
        typeMenu.grid(row=4, column=4, sticky=W)


        min2Label=Label(searchExhibitWindow,text="Min:")
        min2Label.grid(row=3,column=1)

        max2Label=Label(searchExhibitWindow,text="Max:")
        max2Label.grid(row=3,column=2)

        sizeLabel = Label(searchExhibitWindow,text = "Size:")
        sizeLabel.grid(row=4,column=0)


        min2SpinBox = Spinbox(searchExhibitWindow, from_=0, to=10000)
        min2SpinBox.grid(row=4, column=1,pady=5,sticky=W)

        max2SpinBox = Spinbox(searchExhibitWindow, from_=0, to=10000)
        max2SpinBox.grid(row=4, column=2,pady=5,sticky=W)

        # Button
        findExhibitsButton = Button(searchExhibitWindow, text="Find Exhibits", command=self.searchExhibitWindowFindExhibitsButtonClicked)
        findExhibitsButton.grid(row=7,column=3)

        backButton = Button(searchExhibitWindow, text="Back", command=self.searchExhibitWindowBackButtonClicked)
        backButton.grid(row=7,column=1)

        selectExhibitTree = ttk.Treeview(searchExhibitWindow, columns=("Name", "Size", "NumAnimals"))
        # self.selectExhibitTree['show'] = "headings"
        selectExhibitTree.heading('#0', text = "Name")
        selectExhibitTree.heading('#1', text = "Size")
        selectExhibitTree.heading('#2', text = "NumAnimals")
        selectExhibitTree.heading('#3', text = "Water")
        selectExhibitTree.column('#0', width = 150, anchor = "center")
        selectExhibitTree.column('#1', width = 150, anchor = "center")
        selectExhibitTree.column('#2', width = 150, anchor = "center")
        selectExhibitTree.column('#3', width = 150, anchor = "center")
        selectExhibitTree.grid(row=6, columnspan=4, sticky = 'nsew')
        

    def searchExhibitWindowFindExhibitsButtonClicked(self):

        self.min = self.minSV.get()
        self.max = self.maxSV.get()
        self.name = self.nameSV.get()

        if self.min == self.max:
            # messagebox.showwarning("Error", "Your departure station and destination are the same.")
            return False

        self.searchExhibitWindow.destroy()
        self.createExhibitDetailWindow()
        self.buildExhibitDetailWindow(self.exhibitDetailWindow)

    def  searchExhibitWindowBackButtonClicked(self):
        self.searchExhibitWindow.destroy()
        self.chooseVisitorFunctionalityWindow.deiconify()



d=ATLzooSearchExhibits()
