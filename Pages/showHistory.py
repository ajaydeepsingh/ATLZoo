from tkinter import *
from PIL import ImageTk, Image
import pymysql
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime, timedelta
import decimal

class ATLzooShowHistory:
    def __init__(self):
        self.createShowHistoryWindow()
        self.buildShowHistoryWindow(self.showHistoryWindow)
        self.showHistoryWindow.mainloop()
        sys.exit()

    def createShowHistoryWindow(self):

        self.showHistoryWindow=Toplevel()
        self.showHistoryWindow.title("Zoo Atlanta")
        self.showHistoryWindow.geometry("800x600")


    def buildShowHistoryWindow(self, showHistoryWindow):
        titleLabel= Label(showHistoryWindow,text = "Show History", font = "Verdana 16 bold ")
        titleLabel.grid(row=1,column=2,sticky=W+E)

        # Labels
        showLabel = Label(showHistoryWindow,text = "Name")
        showLabel.grid(row=2,column=0,pady=10)
        self.showNameString = StringVar()
        showNameEntry = Entry(showHistoryWindow, textvariable=self.showNameString, width=20)
        showNameEntry.grid(row=2,column=1,pady=10)

        exhibitLabel = Label(showHistoryWindow,text = "Exhibit")
        exhibitLabel.grid(row=2,column=2,pady=10)
        exhibitDefault = StringVar()
        exhibitDefault.set("options")
        exhibitMenu = OptionMenu(showHistoryWindow, exhibitDefault, "this","will","have","options","later")
        exhibitMenu.grid(row=2, column=3,pady=10)

        dateLabel = Label(showHistoryWindow,text = "Date")
        dateLabel.grid(row=3, column=0,pady=10)

        #showDateEntry = CalendarDialog.main()
        showDateEntry= Entry(showHistoryWindow)
        showDateEntry.grid(row=3, column=1,pady=10)

        # Button
        findShowsButton = Button(showHistoryWindow, text="Search", command=self.showHistoryWindowFindShowsButtonClicked)
        findShowsButton.grid(row=3,column=2,pady=10)

        
        selectShowTree = ttk.Treeview(showHistoryWindow, columns=("Name", "Exhibit", "Date"))
        selectShowTree.heading('#0', text = "Name")
        selectShowTree.heading('#1', text = "Exhibit")
        selectShowTree.heading('#2', text = "Date")
        selectShowTree.column('#0', width = 200, anchor = "center")
        selectShowTree.column('#1', width = 200, anchor = "center")
        selectShowTree.column('#2', width = 200, anchor = "center")
        selectShowTree.place(x=20, y=130,width=600)

        backButton = Button(showHistoryWindow, text="Back", command=self.showHistoryWindowBackButtonClicked)
        backButton.place(x=310,y=370)

    def showHistoryWindowFindShowsButtonClicked(self):
        self.showHistoryWindow.destroy()
        self.createShowsDetailWindow()

    def showHistoryWindowBackButtonClicked(self):
        self.showHistoryWindow.withdraw()
        import visitorFunctionality

a = ATLzooShowHistory()

