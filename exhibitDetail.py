from tkinter import *
from PIL import ImageTk, Image
import pymysql
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime, timedelta
import decimal




class exhibitDetail():

    def __init__(self):
        # Invoke createLoginWindow; Invoke buildLoginWindow, Set loginWindow as mainloop
        #Connect to the database
        # self.db = self.connect()
        # self.cursor = self.db.cursor()
        # Login Window
        self.createExhibitDetailWindow()
        self.buildExhibitDetailWindow(self.exhibitDetailWindow)
        self.exhibitDetailWindow.mainloop()
        sys.exit()

    def createExhibitDetailWindow(self):
            # Create blank chooseFunctionalityWindow
            self.exhibitDetailWindow = Toplevel()
            self.exhibitDetailWindow.title("Zoo Atlanta")
            self.exhibitDetailWindow.geometry("800x600")
            self.exhibitDetailWindow.resizable(0,0)

    def buildExhibitDetailWindow(self, exhibitDetailWindow):
        # Add component to chooseFunctionalityWindow

        # Title Label
        exhibitDetailLabel = Label(exhibitDetailWindow, text="Exhibit Details",font = "Verdana 16 bold ")
        # chooseFunctionalityLabel.grid(row=1, column=1, sticky=W+E)
        exhibitDetailLabel.place(x=400, y = 25, anchor="center")


        ## Name , Num Animals, Water Feature, List of Animals in the exhibit
        nameLabel= Label(exhibitDetailWindow, text = "Name:")
        nameLabel.place(x=400, y=150, anchor="center")
        numAnimalsLabel= Label(exhibitDetailWindow, text = "Number of Animals")
        numAnimalsLabel.place(x=400, y=175, anchor="center")
        sizeLabel= Label(exhibitDetailWindow, text = "Size:")
        sizeLabel.place(x=400, y=200, anchor="center")
        waterFeatureLabel= Label(exhibitDetailWindow, text = "Water Feature")
        waterFeatureLabel.place(x=400, y=225, anchor="center")


        # Log Out Buttons

        logVisitButton = Button(exhibitDetailWindow, text="Log Visit", command=self.exhibitDetailWindowLogVisitButtonClicked)
        # logVisitButton.grid(row=8, column=2,sticky=E)
        logVisitButton.grid(row=4)
        logVisitButton.place(x = 400, y=300, anchor="center")



        # Table of Animals

        detailExhibitTree = ttk.Treeview(exhibitDetailWindow, columns=("Name"))
        detailExhibitTree.heading('#0', text = "Name")
        detailExhibitTree.heading('#1', text = "Species")
        detailExhibitTree.column('#0', width = 150, anchor = "center")
        detailExhibitTree.column('#1', width = 150, anchor = "center")
        # detailExhibitTree.grid(row=5, columnspan=4, sticky = 'nsew')
        detailExhibitTree.place(x=400, y=450, anchor="center")


        # # Log Out Buttons

        # logOutButton = Button(chooseFunctionalityWindow, text="Log out", command=self.chooseFunctionalityWindowLogOutButtonClicked)
        # # logOutButton.grid(row=8, column=2,sticky=E)
        # logOutButton.place(x = 720, y = 570)

    # Log Visit Button

    def exhibitDetailWindowLogVisitButtonClicked(self):
            # Click Log Out Buttion on Choose Functionality Window:
            # Destroy Choose Functionality Window
            # Display Login Window
            self.exhibitDetailWindow.destroy()
            self.loginWindow.deiconify()

a = exhibitDetail()