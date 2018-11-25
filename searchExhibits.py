from tkinter import *
from PIL import ImageTk, Image
import pymysql
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime, timedelta
import decimal

#=========Search Exhibit Window============
class ATLzooSearchExhibits:

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

    def buildSearchExhibitWindow(self,searchExhibitWindow):

        # Title Label
        titleLabel= Label(searchExhibitWindow,text = "Search Exhibits")
        titleLabel.grid(row=1, column=2, sticky=W+E)

        # Labels
        numAnimalsLabel= Label(searchExhibitWindow,text = "Number of Animals")
        numAnimalsLabel.grid(row=2,column=1)
        waterFeatureLabel= Label(searchExhibitWindow,text = "Water Feature")
        waterFeatureLabel.grid(row=3,column=1)
        sizeLabel= Label(searchExhibitWindow,text = "Size")
        sizeDateLabel.grid(row=4,column=1)

        # Button
        findExhibitsButton = Button(searchExhibitWindow, text="Find Exhibits", command=self.searchExhibitWindowFindExhibitsButtonClicked)
        findExhibitsButton.grid(row=5,column=3)

        backButton = Button(searchExhibitWindow, text="Back", command=self.searchExhibitWindowBackButtonClicked)
        backButton.grid(row=5,column=1)



    def searchExhibitWindowFindExhibitsButtonClicked(self):

        self.departsFrom = self.departsFromSV.get()
        self.arrivesAt = self.arrivesAtSV.get()
        self.departureDate = self.departureDateSV.get()

        if self.departsFrom == self.arrivesAt:
            messagebox.showwarning("Error", "Your departure station and destination are the same.")
            return False
        if datetime.strptime(self.departureDate, '%Y-%m-%d').date() < datetime.today().date():
            messagebox.showwarning("Error", "Departure date cannot be earlier than today")
            return False

        try:
            datetime.strptime(self.departureDate, '%Y-%m-%d')
        except ValueError:
            messagebox.showwarning("Error", "Departure date is not valid. (yyyy-mm-dd)")
            return False

        self.searchExhibitWindow.destroy()
        self.createExhibitDetailWindow()
        self.buildExhibitWindow(self.selectDepartureWindow)

    def  searchExhibitWindowBackButtonClicked(self):
        self.searchExhibitWindow.destroy()
        self.chooseFunctionalityWindow.deiconify()


a=ATLzooSearchExhibits()