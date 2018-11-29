from tkinter import *
from PIL import ImageTk, Image
import pymysql
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime, timedelta
import decimal

class ATLzooExhibitHistory:
    def __init__(self):
        self.createExhibitHistoryWindow()
        self.buildExhibitHistoryWindow(self.exhibitHistoryWindow)
        self.exhibitHistoryWindow.mainloop()
        sys.exit()

    def createExhibitHistoryWindow(self):

        self.exhibitHistoryWindow=Toplevel()
        self.exhibitHistoryWindow.title("Zoo Atlanta")
        self.exhibitHistoryWindow.geometry("800x600")

    def buildExhibitHistoryWindow(self, exhibitHistoryWindow):
        titleLabel= Label(exhibitHistoryWindow,text = "Exhibit History", font = "Verdana 16 bold ")
        titleLabel.grid(row=1,column=2,sticky=W+E)

        minLabel = Label(exhibitHistoryWindow, text="Min")
        minLabel.grid(row=2, column=3,pady=10)

        maxLabel = Label(exhibitHistoryWindow, text="Max")
        maxLabel.grid(row=2, column=4,pady=10)

        exhibitLabel = Label(exhibitHistoryWindow,text = "Name")
        exhibitLabel.grid(row=3,column=0,pady=10)
        self.exhibitNameString = StringVar()
        exhibitNameEntry = Entry(exhibitHistoryWindow, textvariable=self.exhibitNameString, width=20)
        exhibitNameEntry.grid(row=3,column=1,pady=10)

        numVisitsLabel = Label(exhibitHistoryWindow,text = "Number of Visits")
        numVisitsLabel.grid(row=3,column=2,pady=10)


        minDefault = StringVar()
        minDefault.set("0")
        minMenu = OptionMenu(exhibitHistoryWindow, minDefault, "0","1","2","3","4","5")
        minMenu.grid(row=3, column=3,pady=10)

        maxDefault = StringVar()
        maxDefault.set("2")
        maxMenu = OptionMenu(exhibitHistoryWindow, maxDefault, "0", "1","2","3","4","5")
        maxMenu.grid(row=3, column=4,pady=10)


        dateLabel = Label(exhibitHistoryWindow,text = "Date")
        dateLabel.grid(row=4, column=0,pady=10)

        #showDateEntry = CalendarDialog.main()
        exhibitDateEntry= Entry(exhibitHistoryWindow)
        exhibitDateEntry.grid(row=4, column=1,pady=10)

        # Button
        findShowsButton = Button(exhibitHistoryWindow, text="Search", command=self.exhibitHistoryWindowFindShowsButtonClicked)
        findShowsButton.grid(row=4,column=2,pady=10)

        
        # self.selectExhibitTree['show'] = "headings"
        selectExhibitTree = ttk.Treeview(exhibitHistoryWindow, columns=("Name", "Time", "Number of Visits"))
        selectExhibitTree.heading('#0', text = "Name")
        selectExhibitTree.heading('#1', text = "Time")
        selectExhibitTree.heading('#2', text = "Number of Visits")
        selectExhibitTree.column('#0', width = 200, anchor = "center")
        selectExhibitTree.column('#1', width = 200, anchor = "center")
        selectExhibitTree.column('#2', width = 200, anchor = "center")
        selectExhibitTree.place(x=20, y=200,width=600)

        

        backButton = Button(exhibitHistoryWindow, text="Back", command=self.exhibitHistoryWindowBackButtonClicked)
        backButton.place(x=310, y=440)

    def exhibitHistoryWindowFindShowsButtonClicked(self):
        self.exhibitHistoryWindow.destroy()
        import exhibitDetail

    def exhibitHistoryWindowBackButtonClicked(self):
        self.exhibitHistoryWindow.withdraw()
        import visitorFunctionality

a = ATLzooExhibitHistory()

