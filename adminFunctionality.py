from tkinter import *
from PIL import ImageTk, Image
import pymysql
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime, timedelta
import decimal


class ATLzooAdminFunctionality:
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
            self.chooseFunctionalityWindow.geometry("800x600")
            self.chooseFunctionalityWindow.resizable(0,0)

    def buildChooseFunctionalityWindow(self,chooseFunctionalityWindow):
        # Add component to chooseFunctionalityWindow

        #Choose Functionality Label
        chooseFunctionalityLabel = Label(chooseFunctionalityWindow, text="Choose Functionality",font = "Verdana 16 bold ")
        # chooseFunctionalityLabel.grid(row=1, column=1, sticky=W+E)
        chooseFunctionalityLabel.place(x=400, y = 25, anchor="center")

        # View Visitors Label
        viewVisitorsLabel = Label(chooseFunctionalityWindow, text="View Visitors", font = "Verdana 13")
        # viewVisitorsLabel.grid(row=2, column=1)
        viewVisitorsLabel.bind("<ButtonPress-1>", self.chooseFunctionalityWindowViewVisitorsLabelClicked)
        viewVisitorsLabel.place(x=400, y = 100, anchor="center")

        # View Shows 
        viewShowsLabel = Label(chooseFunctionalityWindow, text="View Shows", font = "Verdana 13")
        # viewShowsLabel.grid(row=3, column=1)
        viewShowsLabel.bind("<ButtonPress-1>", self.chooseFunctionalityWindowViewShowsLabelClicked)
        viewShowsLabel.place(x=400, y = 200, anchor="center")

        # View Animals Label
        viewAnimalsLabel = Label(chooseFunctionalityWindow, text="View Animals", font = "Verdana 13")
        # viewAnimalsLabel.grid(row=4,column=1)
        viewAnimalsLabel.bind("<ButtonPress-1>", self.chooseFunctionalityWindowViewAnimalsLabelClicked)
        viewAnimalsLabel.place(x=400, y = 300, anchor="center")

        # View Staff
        viewStaffLabel = Label(chooseFunctionalityWindow, text="View Staff", font = "Verdana 13")
        # viewStaffLabel.grid(row=5,column=1)
        viewStaffLabel.bind("<ButtonPress-1>", self.chooseFunctionalityWindowViewStaffLabelClicked)
        viewStaffLabel.place(x=400, y = 400, anchor="center")


        # View Show History Label
        viewShowAdd = Label(chooseFunctionalityWindow, text="Add Show", font = "Verdana 13")
        # viewReviewLabel.grid(row=6,column=1)
        viewShowAdd.bind("<ButtonPress-1>", self.chooseFunctionalityWindowViewShowAddLabelClicked)
        viewShowAdd.place(x=400, y = 500, anchor="center")

        # Log Out Buttons

        logOutButton = Button(chooseFunctionalityWindow, text="Log out", command=self.chooseFunctionalityWindowLogOutButtonClicked)
        logOutButton.grid(row=8, column=2,sticky=E)
        logOutButton.place(x = 720, y = 570)

    def chooseFunctionalityWindowViewVisitorsLabelClicked(self,event):
        # Hide Choose Functionality Window.
        self.createViewVisitorsWindow()
        self.buildViewVisitorsWindow(self.viewVisitorsWindow)
        self.chooseFunctionalityWindow.withdraw()

    def chooseFunctionalityWindowViewShowsLabelClicked(self,event):
        # Hide Choose Functionality Window
        self.createViewShowsWindow()
        self.buildViewShowsWindow(self.viewShowWindow)
        self.chooseFunctionalityWindow.withdraw()

    def chooseFunctionalityWindowViewAnimalsLabelClicked(self,event):
        self.createViewAnimalsWindow()
        self.buildViewAnimalsWindow(self.viewAnimalsWindow)
        self.chooseFunctionalityWindow.withdraw()

    def chooseFunctionalityWindowViewStaffLabelClicked(self,event):
        self.createViewStaffWindow()
        self.buildViewStaffWindow(self.viewStaffWindow)
        self.chooseFunctionalityWindow.withdraw()

    def chooseFunctionalityWindowViewShowAddLabelClicked(self,event):
        self.createViewShowAddWindow()
        self.buildViewShowAddWindow(self.viewShowAddWindow)
        self.chooseFunctionalityWindow.withdraw()

    def chooseFunctionalityWindowLogOutButtonClicked(self):
        # Click Log Out Buttion on Choose Functionality Window:
        # Destroy Choose Functionality Window
        # Display Login Window
        self.chooseFunctionalityWindow.destroy()
        self.loginWindow.deiconify()


a=ATLzooAdminFunctionality()