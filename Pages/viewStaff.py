from tkinter import *
from PIL import ImageTk, Image
import pymysql
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime, timedelta
import decimal

class viewStaff():

    def __init__(self):
        # Invoke createLoginWindow; Invoke buildLoginWindow, Set loginWindow as mainloop
        #Connect to the database
        # self.db = self.connect()
        # self.cursor = self.db.cursor()
        # Login Window
        self.createViewStaffWindow()
        self.buildViewStaffWindow(self.viewStaffWindow)
        self.viewStaffWindow.mainloop()
        sys.exit()

    def createViewStaffWindow(self):
        self.viewStaffWindow = Toplevel()
        self.viewStaffWindow.title("Zoo Atlanta")
        self.viewStaffWindow.geometry("800x600")
        self.viewStaffWindow.resizable(0,0)

    def buildViewStaffWindow(self, viewStaffWindow):

        # Title Label
        titleLabel = Label(viewStaffWindow, text = "View Staff", font = "Verdana 16 bold ")
        titleLabel.place(x=350, y=25)

        # Table of all the staff members
        staffTree = ttk.Treeview(viewStaffWindow, columns=("Name"))
        staffTree.heading('#0', text = "Name")
        staffTree.heading('#1', text = "Email")
        staffTree.column('#0', width = 300, anchor = "center")
        staffTree.column('#1', width = 300, anchor = "center")
        staffTree.place(x=400, y=200, anchor="center")

        # Back Button
        backButton = Button(viewStaffWindow, text="Back", command=self.viewStaffBackButtonClicked)
        backButton.place(x=10,y=570)



    def viewStaffBackButtonClicked(self):
        self.viewStaffWindow.destroy()
        self.chooseFunctionalityWindow.deiconify()

a = viewStaff()