from tkinter import *
from PIL import ImageTk, Image
import pymysql
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime, timedelta
import decimal

class ATLzooStaffShowHistory:
    def __init__(self):
        self.createStaffShowHistoryWindow()
        self.buildStaffShowHistoryWindow(self.staffShowHistoryWindow)
        self.staffShowHistoryWindow.mainloop()
        sys.exit()

    def createStaffShowHistoryWindow(self):
        # Create blank Search Animal Window
        self.staffShowHistoryWindow=Toplevel()
        self.staffShowHistoryWindow.title("Zoo Atlanta")
        self.staffShowHistoryWindow.geometry("800x600")

    def buildStaffShowHistoryWindow(self, staffShowHistoryWindow):
        '''
        frame = Frame(staffShowHistoryWindow)
        frame.pack()
        treeFrame = Frame(staffShowHistoryWindow)
        treeFrame.pack()
        buttonFrame = Frame(staffShowHistoryWindow)
        buttonFrame.pack(side=BOTTOM)
        '''

        titleLabel= Label(staffShowHistoryWindow,text = "Staff - Show History", font = "Verdana 16 bold ")
        titleLabel.grid(row=1,column=2, sticky=W+E, padx=200)


        staffShowTree = ttk.Treeview(staffShowHistoryWindow, columns=("Name", "Exhibit", "Date"))
        staffShowTree.column("#0", width=200, anchor="center")
        staffShowTree.column("#1", width= 200, anchor="center")
        staffShowTree.column("#2", width=200, anchor="center")
        staffShowTree.heading("#0", text="Name")
        staffShowTree.heading("#1", text="Time")
        staffShowTree.heading("#2", text="Exhibit")
        staffShowTree.place(x=20,y=60,width=600)


        backButton = Button(staffShowHistoryWindow, text="Back", command=self.staffShowHistoryWindowBackButtonClicked)
        backButton.place(x=290, y=300)


    def staffShowHistoryWindowBackButtonClicked(self):
        self.staffShowHistoryWindow.destroy()
        import staffFunctionality

a = ATLzooStaffShowHistory()

