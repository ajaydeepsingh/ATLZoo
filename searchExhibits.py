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
        titleLabel.grid(row=0, column=1)

        # Labels
        numAnimalsLabel= Label(searchExhibitWindow,text = "Number of Animals")
        numAnimalsLabel.grid(row=2,column=2)
        nameLabel= Label(searchExhibitWindow,text = "Name")
        nameLabel.grid(row=2,column=0)

        # Entry
        self.exhibitNameSV = StringVar()
        exhibitNameEntry = Entry(searchExhibitWindow, textvariable=self.exhibitNameSV, width=20)
        exhibitNameEntry.grid(row=2, column=1)

        waterFeatureLabel= Label(searchExhibitWindow,text = "Water Feature")
        waterFeatureLabel.grid(row=3,column=2)
        sizeLabel= Label(searchExhibitWindow,text = "Size")
        sizeLabel.grid(row=3,column=0)

        # Button
        findExhibitsButton = Button(searchExhibitWindow, text="Find Exhibits", command=self.searchExhibitWindowFindExhibitsButtonClicked)
        findExhibitsButton.grid(row=6,column=3)

        backButton = Button(searchExhibitWindow, text="Back", command=self.searchExhibitWindowBackButtonClicked)
        backButton.grid(row=6,column=1)

        selectExhibitTree = ttk.Treeview(searchExhibitWindow, columns=("Name", "Size", "NumAnimals", "Water"))
        # self.selectExhibitTree['show'] = "headings"
        selectExhibitTree.heading('#0', text = "Name")
        selectExhibitTree.heading('#1', text = "Size")
        selectExhibitTree.heading('#2', text = "NumAnimals")
        selectExhibitTree.heading('#3', text = "Water")
        selectExhibitTree.column('#0', width = 150, anchor = "center")
        selectExhibitTree.column('#1', width = 150, anchor = "center")
        selectExhibitTree.column('#2', width = 150, anchor = "center")
        selectExhibitTree.column('#3', width = 150, anchor = "center")
        selectExhibitTree.grid(row=5, columnspan=4, sticky = 'nsew')
        

    def searchExhibitWindowFindExhibitsButtonClicked(self):

        self.min = self.minSV.get()
        self.max = self.maxSV.get()
        self.name = self.nameSV.get()

        if self.min == self.max:
            # messagebox.showwarning("Error", "Your departure station and destination are the same.")
            return False

        self.searchExhibitWindow.destroy()
        self.createExhibitDetailWindow()
        self.buildExhibitWindow(self.selectDepartureWindow)

    def  searchExhibitWindowBackButtonClicked(self):
        self.searchExhibitWindow.destroy()
        self.chooseFunctionalityWindow.deiconify()



d=ATLzooSearchExhibits()
