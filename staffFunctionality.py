from tkinter import *
from PIL import ImageTk, Image
import pymysql
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime, timedelta
import decimal



class ATLzooStaffFunctionality:
    def __init__(self):
        # Invoke createLoginWindow; Invoke buildLoginWindow, Set loginWindow as mainloop
        #Connect to the database
        # self.db = self.connect()
        # self.cursor = self.db.cursor()
        # Login Window
        self.createChooseFunctionalityWindow()
        self.buildChooseFunctionalityWindow(self.chooseFunctionalityWindow)
        self.chooseFunctionalityWindow.mainloop()
        sys.exit()

    def createChooseFunctionalityWindow(self):
            # Create blank chooseFunctionalityWindow
            self.chooseFunctionalityWindow = Toplevel()
            self.chooseFunctionalityWindow.title("Zoo Atlanta")

    def buildChooseFunctionalityWindow(self,chooseFunctionalityWindow):


        titleLabel= Label(chooseFunctionalityWindow,text = "Staff Functions", font = "Verdana 16 bold")
        titleLabel.grid(row=1,column=2,sticky=W+E)

        # Labels
        animalsButton = Button(chooseFunctionalityWindow,text = "Search Animals", command=self.chooseFunctionalityWindowSearchAnimalsLabelClicked)
        animalsButton.grid(row=3,column=1,sticky=W+E, padx=10, pady=20)


        # View Show History Label
        showButton = Button(chooseFunctionalityWindow, text="View Shows", command=self.chooseFunctionalityWindowViewAssignedShowsLabelClicked)
        showButton.grid(row=3, column=2,sticky=W+E, padx=10, pady=20)



        logOutButton = Button(chooseFunctionalityWindow, text="Log out", command=self.chooseFunctionalityWindowLogOutButtonClicked)
        logOutButton.grid(row=3, column=3,sticky=W+E, padx=10, pady=20)


        # # Search Shows 
        # searchShowsLabel = Label(chooseFunctionalityWindow, text="Search Shows", font = "Verdana 13")
        # # searchShowsLabel.grid(row=3, column=1)
        # searchShowsLabel.bind("<ButtonPress-1>", self.chooseFunctionalityWindowSearchShowsLabelClicked)
        # searchShowsLabel.place(x=400, y = 200, anchor="center")


        # # Search for Animals Label
        # searchAnimalsLabel = Label(chooseFunctionalityWindow, text="Search for Animals", font = "Verdana 13")
        # # searchAnimalsLabel.grid(row=4,column=1)
        # searchAnimalsLabel.bind("<ButtonPress-1>", self.chooseFunctionalityWindowSearchAnimalsLabelClicked)
        # searchAnimalsLabel.place(x=400, y = 300, anchor="center")

        # # View Exhibit History
        # viewExhibitHistoryLabel = Label(chooseFunctionalityWindow, text="View Exhibit History", font = "Verdana 13")
        # # viewExhibitHistoryLabel.grid(row=5,column=1)
        # viewExhibitHistoryLabel.bind("<ButtonPress-1>", self.chooseFunctionalityWindowViewExhibitHistoryLabelClicked)
        # viewExhibitHistoryLabel.place(x=400, y = 400, anchor="center")

    def chooseFunctionalityWindowSearchAnimalsLabelClicked(self):
        
        self.chooseFunctionalityWindow.withdraw()
        import staffAnimals

    def chooseFunctionalityWindowViewAssignedShowsLabelClicked(self):
        self.chooseFunctionalityWindow.withdraw()
        import staffShows

    def chooseFunctionalityWindowLogOutButtonClicked(self):
        # Click Log Out Buttion on Choose Functionality Window:
        # Destroy Choose Functionality Window
        # Display Login Window
        self.chooseFunctionalityWindow.withdraw()
        import atlzoo

a=ATLzooStaffFunctionality()