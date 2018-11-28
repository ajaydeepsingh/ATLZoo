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

    def createStaffChooseFunctionalityWindow(self):
            # Create blank chooseFunctionalityWindow
            self.chooseStaffFunctionalityWindow = Toplevel()
            self.chooseStaffFunctionalityWindow.title("Zoo Atlanta")
            self.chooseStaffFunctionalityWindow.geometry("800x600")
            self.chooseStaffFunctionalityWindow.resizable(0,0)

    def buildStaffChooseFunctionalityWindow(self,chooseStaffFunctionalityWindow):
        # Add component to chooseFunctionalityWindow

        #Choose Functionality Label
        chooseFunctionalityLabel = Label(chooseStaffFunctionalityWindow, text="Staff Functions",font = "Verdana 16 bold ")
        # chooseFunctionalityLabel.grid(row=1, column=1, sticky=W+E)
        chooseFunctionalityLabel.place(x=400, y = 25, anchor="center")

        # Search Exhibits Label
        searchAnimalsLabel = Label(chooseStaffFunctionalityWindow, text="Search Animals", font = "Verdana 13")
        # searchAnimalsLabel.grid(row=2, column=1)
        searchAnimalsLabel.bind("<ButtonPress-1>", self.chooseStaffFunctionalityWindowSearchAnimalsLabelClicked)
        searchAnimalsLabel.place(x=400, y = 100, anchor="center")

        # View Show History Label
        viewAssignedShows = Label(chooseStaffFunctionalityWindow, text="View Your Assigned Shows", font = "Verdana 13")
        # viewReviewLabel.grid(row=6,column=1)
        viewAssignedShows.bind("<ButtonPress-1>", self.chooseStaffFunctionalityWindowViewAssignedShowsLabelClicked)
        viewAssignedShows.place(x=400, y = 150, anchor="center")

        # Log Out Buttons

        logOutButton = Button(chooseStaffFunctionalityWindow, text="Log out", command=self.chooseStaffFunctionalityWindowLogOutButtonClicked)
        logOutButton.grid(row=8, column=2,sticky=E)
        logOutButton.place(x = 720, y = 570)



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

    def chooseStaffFunctionalityWindowSearchAnimalsLabelClicked(self,event):
        # Hide Choose Functionality Window.
        self.createSearchAnimalsWindow()
        self.buildSearchAnimalsWindow(self.viewSearchAnimalsWindow)
        self.chooseStaffFunctionalityWindow.withdraw()



    def chooseStaffFunctionalityWindowViewAssignedShowsLabelClicked(self,event):
        self.createViewAssignedShowsWindow()
        self.buildViewAssignedShowsWindow(self.viewAssignedShowsWindow)
        self.chooseStaffFunctionalityWindow.withdraw()

    def chooseStaffFunctionalityWindowLogOutButtonClicked(self):
        # Click Log Out Buttion on Choose Functionality Window:
        # Destroy Choose Functionality Window
        # Display Login Window
        self.chooseStaffFunctionalityWindow.destroy()
        self.loginWindow.deiconify()

    # def chooseFunctionalityWindowSearchShowsLabelClicked(self,event):
    #     # Hide Choose Functionality Window
    #     self.createSearchShowWindow()
    #     self.buildSearchShowWindow(self.searchShowWindow)
    #     self.chooseFunctionalityWindow.withdraw()

    # def chooseFunctionalityWindowSearchAnimalsLabelClicked(self,event):
    #     self.createSearchAnimalsWindow()
    #     self.buildSearchAnimalsWindow(self.searchAnimalsWindow)
    #     self.chooseFunctionalityWindow.withdraw()

    # def chooseFunctionalityWindowViewExhibitHistoryLabelClicked(self,event):
    #     self.createViewExhibitHistoryWindow()
    #     self.buildViewExhibitHistoryWindow(self.viewExhibitHistoryWindow)
    #     self.chooseFunctionalityWindow.withdraw()

a=ATLzooStaffFunctionality()