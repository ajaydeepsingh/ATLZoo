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
        self.createAdminChooseFunctionalityWindow()
        self.buildAdminChooseFunctionalityWindow(self.chooseAdminFunctionalityWindow)
        self.chooseAdminFunctionalityWindow.mainloop()
        sys.exit()

    def createAdminChooseFunctionalityWindow(self):
            # Create blank chooseFunctionalityWindow
            self.chooseAdminFunctionalityWindow = Toplevel()
            self.chooseAdminFunctionalityWindow.title("Zoo Atlanta")
            self.chooseAdminFunctionalityWindow.geometry("800x600")
            self.chooseAdminFunctionalityWindow.resizable(0,0)

    def buildAdminChooseFunctionalityWindow(self,chooseAdminFunctionalityWindow):
        # Add component to chooseFunctionalityWindow

        #Choose Functionality Label
        chooseFunctionalityLabel = Label(chooseAdminFunctionalityWindow, text="Choose Functionality",font = "Verdana 16 bold ")
        # chooseFunctionalityLabel.grid(row=1, column=1, sticky=W+E)
        chooseFunctionalityLabel.place(x=400, y = 25, anchor="center")

        # View Visitors Label
        viewVisitorsLabel = Label(chooseAdminFunctionalityWindow, text="View Visitors", font = "Verdana 13")
        # viewVisitorsLabel.grid(row=2, column=1)
        viewVisitorsLabel.bind("<ButtonPress-1>", self.chooseAdminFunctionalityWindowViewVisitorsLabelClicked)
        viewVisitorsLabel.place(x=400, y = 100, anchor="center")

        # View Shows 
        viewShowsLabel = Label(chooseAdminFunctionalityWindow, text="View Shows", font = "Verdana 13")
        # viewShowsLabel.grid(row=3, column=1)
        viewShowsLabel.bind("<ButtonPress-1>", self.chooseAdminFunctionalityWindowViewShowsLabelClicked)
        viewShowsLabel.place(x=400, y = 200, anchor="center")

        # View Animals Label
        viewAnimalsLabel = Label(chooseAdminFunctionalityWindow, text="View Animals", font = "Verdana 13")
        # viewAnimalsLabel.grid(row=4,column=1)
        viewAnimalsLabel.bind("<ButtonPress-1>", self.chooseAdminFunctionalityWindowViewAnimalsLabelClicked)
        viewAnimalsLabel.place(x=400, y = 300, anchor="center")

        # View Staff
        viewStaffLabel = Label(chooseAdminFunctionalityWindow, text="View Staff", font = "Verdana 13")
        # viewStaffLabel.grid(row=5,column=1)
        viewStaffLabel.bind("<ButtonPress-1>", self.chooseAdminFunctionalityWindowViewStaffLabelClicked)
        viewStaffLabel.place(x=400, y = 400, anchor="center")


        # View Show History Label
        viewShowAdd = Label(chooseAdminFunctionalityWindow, text="Add Show", font = "Verdana 13")
        # viewReviewLabel.grid(row=6,column=1)
        viewShowAdd.bind("<ButtonPress-1>", self.chooseAdminFunctionalityWindowViewShowAddLabelClicked)
        viewShowAdd.place(x=400, y = 500, anchor="center")

        # Log Out Buttons

        logOutButton = Button(chooseAdminFunctionalityWindow, text="Log out", command=self.chooseAdminFunctionalityWindowLogOutButtonClicked)
        logOutButton.grid(row=8, column=2,sticky=E)
        logOutButton.place(x = 720, y = 570)

    def chooseAdminFunctionalityWindowViewVisitorsLabelClicked(self,event):
        # Hide Choose Functionality Window.
        self.createViewVisitorsWindow()
        self.buildViewVisitorsWindow(self.viewVisitorsWindow)
        self.chooseAdminFunctionalityWindow.withdraw()

    def chooseAdminFunctionalityWindowViewShowsLabelClicked(self,event):
        # Hide Choose Functionality Window
        self.createViewShowsWindow()
        self.buildViewShowsWindow(self.viewShowWindow)
        self.chooseAdminFunctionalityWindow.withdraw()

    def chooseAdminFunctionalityWindowViewAnimalsLabelClicked(self,event):
        self.createViewAnimalsWindow()
        self.buildViewAnimalsWindow(self.viewAnimalsWindow)
        self.chooseAdminFunctionalityWindow.withdraw()

    def chooseAdminFunctionalityWindowViewStaffLabelClicked(self,event):
        self.createViewStaffWindow()
        self.buildViewStaffWindow(self.viewStaffWindow)
        self.chooseAdminFunctionalityWindow.withdraw()

    def chooseAdminFunctionalityWindowViewShowAddLabelClicked(self,event):
        self.createViewShowAddWindow()
        self.buildViewShowAddWindow(self.viewShowAddWindow)
        self.chooseAdminFunctionalityWindow.withdraw()

    def chooseAdminFunctionalityWindowLogOutButtonClicked(self):
        # Click Log Out Buttion on Choose Functionality Window:
        # Destroy Choose Functionality Window
        # Display Login Window
        self.chooseAdminFunctionalityWindow.destroy()
        self.loginWindow.deiconify()


a=ATLzooAdminFunctionality()