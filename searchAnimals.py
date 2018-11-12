from tkinter import *
from PIL import ImageTk, Image
import pymysql
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime, timedelta
import decimal

#=========Search Exhibit Window============
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
        titleLabel= Label(searchAnimalWindow,text = "Search Animals")
        titleLabel.grid(row=1,column=2,sticky=W+E)

        # Labels
        exhibitLabel = Label(searchAnimalWindow,text = "Exhibit")
        exhibitLabel.grid(row=2,column=1)
        ageLabel = Label(searchAnimalWindow,text = "Age")
        ageLabel.grid(row=3,column=1)
        typeLabel = Label(searchAnimalWindow,text = "Type")
        typeLabel.grid(row=4,column=1)
        speciesLabel = Label(searchAnimalWindow,text = "Species")
        speciesLabel.grid(row=5, column=1)

        # Button
        findAnimalsButton = Button(searchAnimalWindow, text="Find Animals", command=self.searchAnimalWindowFindAnimalsButtonClicked)
        findAnimalsButton.grid(row=5,column=3)

        backButton = Button(searchAnimalWindow, text="Back", command=self.searchAnimalWindowBackButtonClicked)
        backButton.grid(row=5,column=1)


    def searchAnimalWindowFindAnimalsButtonClicked(self):


        self.searchAnimalWindow.destroy()
        self.createAnimalDetailWindow()
        self.buildAnimalWindow(self.selectDepartureWindow)

    def  searchAnimalWindowBackButtonClicked(self):
        self.searchAnimalWindow.destroy()
        self.chooseFunctionalityWindow.deiconify()


a=ATLzooSearchAnimals()