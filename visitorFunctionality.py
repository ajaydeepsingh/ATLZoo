from tkinter import *
from PIL import ImageTk, Image
import pymysql
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime, timedelta
import decimal


class ATLzooVisitorFunctionality:
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

    def createVisitorChooseFunctionalityWindow(self):
            # Create blank chooseVisitorFunctionalityWindow
            self.chooseVisitorFunctionalityWindow = Toplevel()
            self.chooseVisitorFunctionalityWindow.title("Zoo Atlanta")
            self.chooseVisitorFunctionalityWindow.geometry("800x600")
            self.chooseVisitorFunctionalityWindow.resizable(0,0)

    def buildVisitorChooseFunctionalityWindow(self,chooseVisitorFunctionalityWindow):
        # Add component to chooseVisitorFunctionalityWindow

        #Choose Functionality Label
        chooseFunctionalityLabel = Label(chooseVisitorFunctionalityWindow, text="Choose Functionality",font = "Verdana 16 bold ")
        # chooseFunctionalityLabel.grid(row=1, column=1, sticky=W+E)
        chooseFunctionalityLabel.place(x=400, y = 25, anchor="center")

        # Search Exhibits Label
        searchExhibitLabel = Label(chooseVisitorFunctionalityWindow, text="Search Exhibits", font = "Verdana 13")
        # searchExhibitLabel.grid(row=2, column=1)
        searchExhibitLabel.bind("<ButtonPress-1>", self.chooseFunctionalityWindowSearchExhibitLabelClicked)
        searchExhibitLabel.place(x=400, y = 100, anchor="center")

        # Search Shows 
        searchShowsLabel = Label(chooseVisitorFunctionalityWindow, text="Search Shows", font = "Verdana 13")
        # searchShowsLabel.grid(row=3, column=1)
        searchShowsLabel.bind("<ButtonPress-1>", self.chooseFunctionalityWindowSearchShowsLabelClicked)
        searchShowsLabel.place(x=400, y = 200, anchor="center")


        # Search for Animals Label
        searchAnimalsLabel = Label(chooseVisitorFunctionalityWindow, text="Search for Animals", font = "Verdana 13")
        # searchAnimalsLabel.grid(row=4,column=1)
        searchAnimalsLabel.bind("<ButtonPress-1>", self.chooseFunctionalityWindowSearchAnimalsLabelClicked)
        searchAnimalsLabel.place(x=400, y = 300, anchor="center")

        # View Exhibit History
        viewExhibitHistoryLabel = Label(chooseVisitorFunctionalityWindow, text="View Exhibit History", font = "Verdana 13")
        # viewExhibitHistoryLabel.grid(row=5,column=1)
        viewExhibitHistoryLabel.bind("<ButtonPress-1>", self.chooseFunctionalityWindowViewExhibitHistoryLabelClicked)
        viewExhibitHistoryLabel.place(x=400, y = 400, anchor="center")


        # View Show History Label
        viewShowHistory = Label(chooseVisitorFunctionalityWindow, text="View Show History", font = "Verdana 13")
        # viewReviewLabel.grid(row=6,column=1)
        viewShowHistory.bind("<ButtonPress-1>", self.chooseFunctionalityWindowViewShowHistoryLabelClicked)
        viewShowHistory.place(x=400, y = 500, anchor="center")

        # Log Out Buttons

        logOutButton = Button(chooseVisitorFunctionalityWindow, text="Log out", command=self.chooseFunctionalityWindowLogOutButtonClicked)
        logOutButton.grid(row=8, column=2,sticky=E)
        logOutButton.place(x = 720, y = 570)

    def chooseFunctionalityWindowSearchExhibitLabelClicked(self,event):
        # Hide Choose Functionality Window.
        self.createSearchExhibitWindow()
        self.buildSearchExhibitWindow(self.viewSearchExhibitWindow)
        self.chooseVisitorFunctionalityWindow.withdraw()

    def chooseFunctionalityWindowSearchShowsLabelClicked(self,event):
        # Hide Choose Functionality Window
        self.createSearchShowWindow()
        self.buildSearchShowWindow(self.searchShowWindow)
        self.chooseVisitorFunctionalityWindow.withdraw()

    def chooseFunctionalityWindowSearchAnimalsLabelClicked(self,event):
        self.createSearchAnimalsWindow()
        self.buildSearchAnimalsWindow(self.searchAnimalsWindow)
        self.chooseVisitorFunctionalityWindow.withdraw()

    def chooseFunctionalityWindowViewExhibitHistoryLabelClicked(self,event):
        self.createViewExhibitHistoryWindow()
        self.buildViewExhibitHistoryWindow(self.viewExhibitHistoryWindow)
        self.chooseVisitorFunctionalityWindow.withdraw()

    def chooseFunctionalityWindowViewShowHistoryLabelClicked(self,event):
        self.createViewShowHistoryWindow()
        self.buildViewShowHistoryWindow(self.viewShowHistoryWindow)
        self.chooseVisitorFunctionalityWindow.withdraw()

    def chooseFunctionalityWindowLogOutButtonClicked(self):
        # Click Log Out Buttion on Choose Functionality Window:
        # Destroy Choose Functionality Window
        # Display Login Window
        self.chooseVisitorFunctionalityWindow.destroy()
        self.loginWindow.deiconify()


a=ATLzooVisitorFunctionality()