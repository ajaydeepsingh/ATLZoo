from tkinter import *
from PIL import ImageTk, Image
import pymysql
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime, timedelta
import decimal

class ATLzooSearchShows:
    def __init__(self):
        self.createSearchShowsWindow()
        self.buildSearchShowsWindow(self.searchShowsWindow)
        self.searchShowsWindow.mainloop()
        sys.exit()

    def createSearchShowsWindow(self):

        self.searchShowsWindow=Toplevel()
        self.searchShowsWindow.title("Zoo Atlanta")
        self.searchShowsWindow.geometry("800x600")

    def buildSearchShowsWindow(self, searchShowsWindow):
        titleLabel= Label(searchShowsWindow,text = "Search Shows", font = "Verdana 16 bold ")
        titleLabel.grid(row=1,column=2,sticky=W+E,pady=10)

        # Labels
        showLabel = Label(searchShowsWindow,text = "Name")
        showLabel.grid(row=2,column=0,pady=10)

        self.showNameString = StringVar()
        showNameEntry = Entry(searchShowsWindow, textvariable=self.showNameString, width=20)
        showNameEntry.grid(row=2, column=1,pady=10)

        exhibitLabel = Label(searchShowsWindow,text = "Exhibit")
        exhibitLabel.grid(row=3,column=0,pady=10)
        exhibitDefault = StringVar()
        exhibitDefault.set("options")
        exhibitMenu = OptionMenu(searchShowsWindow, exhibitDefault, "this","will","have","options","later")
        exhibitMenu.grid(row=3, column=1,pady=10)

        dateLabel = Label(searchShowsWindow,text = "Date")
        dateLabel.grid(row=2, column=2,pady=10)



        #showDateEntry = CalendarDialog.main()
        showDateEntry= Entry(searchShowsWindow)
        showDateEntry.grid(row=2, column=3,pady=10)

        # Button
        findShowsButton = Button(searchShowsWindow, text="Search", command=self.searchShowsWindowFindShowsButtonClicked)
        findShowsButton.grid(row=3,column=2,pady=10)

        
        # self.selectExhibitTree['show'] = "headings"
        selectShowTree = ttk.Treeview(searchShowsWindow, columns=("Name", "Exhibit", "Date"))
        selectShowTree.heading('#0', text = "Name")
        selectShowTree.heading('#1', text = "Exhibit")
        selectShowTree.heading('#2', text = "Date")
        selectShowTree.column('#0', width = 175, anchor = "center")
        selectShowTree.column('#1', width = 175, anchor = "center")
        selectShowTree.column('#2', width = 175, anchor = "center")
        selectShowTree.place(x=280, y=280, anchor="center", width=525)

        logVisitButton = Button(searchShowsWindow, text="Log Visit", command = self.logVisitButtonClicked)  
        logVisitButton.place(x=220, y=415)  

        backButton = Button(searchShowsWindow, text="Back", command=self.searchShowsWindowBackButtonClicked)
        backButton.place(x=320, y=415)

    def searchShowsWindowFindShowsButtonClicked(self):
        self.searchShowsWindow.destroy()
        self.createShowsDetailWindow()

    def logVisitButtonClicked(self):
        self.searchShowsWindow.withdraw()
        import searchShows

    def searchShowsWindowBackButtonClicked(self):
        self.searchShowsWindow.withdraw()
        import visitorFunctionality


a = ATLzooSearchShows()

