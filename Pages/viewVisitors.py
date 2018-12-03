from tkinter import *
from PIL import ImageTk, Image
import pymysql
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime, timedelta
import decimal

class viewVisitors():

    def __init__(self):
        # Invoke createLoginWindow; Invoke buildLoginWindow, Set loginWindow as mainloop
        #Connect to the database
        # self.db = self.connect()
        # self.cursor = self.db.cursor()
        # Login Window
        self.createViewVisitorsWindow()
        self.buildViewVisitorsWindow(self.viewVisitorsWindow)
        self.viewVisitorsWindow.mainloop()
        sys.exit()

    def createViewVisitorsWindow(self):
        self.viewVisitorsWindow = Toplevel()
        self.viewVisitorsWindow.title("Zoo Atlanta")
        self.viewVisitorsWindow.geometry("800x600")
        self.viewVisitorsWindow.resizable(0,0)

    def buildViewVisitorsWindow(self, viewVisitorsWindow):

        # Title Label
        titleLabel = Label(viewVisitorsWindow, text = "View Vistors", font = "Verdana 16 bold ")
        titleLabel.place(x=350, y=25)

        # Table of all the visitors
        visitorsTree = ttk.Treeview(viewVisitorsWindow, columns=("Name"))
        visitorsTree.heading('#0', text = "Name")
        visitorsTree.heading('#1', text = "Email")
        visitorsTree.column('#0', width = 300, anchor = "center")
        visitorsTree.column('#1', width = 300, anchor = "center")
        visitorsTree.place(x=400, y=200, anchor="center")

        # Back Button
        backButton = Button(viewVisitorsWindow, text="Back", command=self.viewVisitorsBackButtonClicked)
        backButton.place(x=10,y=570)



    def viewVisitorsBackButtonClicked(self):
        self.viewVisitorsWindow.destroy()
        self.chooseAdminFunctionalityWindow.deiconify()

a = viewVisitors()