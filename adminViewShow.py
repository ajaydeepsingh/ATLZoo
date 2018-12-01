from tkinter import *
from PIL import ImageTk, Image
import pymysql
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime, timedelta
import decimal

class ATLzooAdminViewShow:
    def __init__(self):
        self.createAdminViewShowWindow()
        self.buildAdminViewShowWindow(self.adminViewShowWindow)
        self.adminViewShowWindow.mainloop()
        sys.exit()

    def createAdminViewShowWindow(self):
        # Create blank Search Animal Window
        self.adminViewShowWindow=Toplevel()
        self.adminViewShowWindow.title("Zoo Atlanta")
        self.adminViewShowWindow.geometry("800x600")

    def buildAdminViewShowWindow(self, adminViewShowWindow):
        '''
        frame = Frame(staffShowHistoryWindow)
        frame.pack()
        treeFrame = Frame(staffShowHistoryWindow)
        treeFrame.pack()
        buttonFrame = Frame(staffShowHistoryWindow)
        buttonFrame.pack(side=BOTTOM)
        '''

        titleLabel= Label(adminViewShowWindow,text = "Shows", font = "Verdana 16 bold ")
        titleLabel.grid(row=1,column=2, sticky=W+E, padx=200)


        nameLabel = Label(adminViewShowWindow,text = "Name")
        nameLabel.grid(row=2, column=0,pady=10)


        self.animalNameSV = StringVar()
        animalNameEntry = Entry(adminViewShowWindow, textvariable=self.animalNameSV, width=20)
        animalNameEntry.grid(row=2, column=1, pady=10)

    


        exhibitLabel = Label(adminViewShowWindow,text = "Exhibit")
        exhibitLabel.grid(row=3,column=0,pady=10)
        exhibitDefault = StringVar()
        exhibitDefault.set("options")
        exhibitMenu = OptionMenu(adminViewShowWindow, exhibitDefault, "this","will","have","options","later")
        exhibitMenu.grid(row=3, column=1,pady=10)

        dateLabel=Label(adminViewShowWindow,text="Date")
        dateLabel.grid(row=2,column=2,pady=10)

        self.dateSV = StringVar()
        dateEntry = Entry(adminViewShowWindow, textvariable=self.animalNameSV, width=20)
        dateEntry.grid(row=2, column=3,pady=10)

        searchButton = Button(adminViewShowWindow, text="Search", command=self.adminViewShowWindowSearchButtonClicked)
        searchButton.grid(row=3, column =2,pady=10)


        viewShowTree = ttk.Treeview(adminViewShowWindow, columns=("Name", "Exhibit", "Date"))
        viewShowTree.heading('#0', text = "Name")
        viewShowTree.heading('#1', text = "Exhibit")
        viewShowTree.heading('#2', text = "Date")
        viewShowTree.column('#0', width = 200, anchor = "center")
        viewShowTree.column('#1', width = 200, anchor = "center")
        viewShowTree.column('#2', width = 200, anchor = "center")
        viewShowTree.place(x=20, y=130,width=600)

        removeShowButton = Button(adminViewShowWindow, text="Remove Show", command=self.adminViewShowWindowRemoveButtonClicked)
        removeShowButton.place(x=220, y=400)

        backButton = Button(adminViewShowWindow, text="Back", command=self.adminViewShowWindowBackButtonClicked)
        backButton.place(x=360, y=400)

    def adminViewShowWindowSearchButtonClicked(self):
        self.adminViewShowWindow.destroy()

    def adminViewShowWindowRemoveButtonClicked(self):
        self.adminViewShowWindow.destroy()

    def adminViewShowWindowBackButtonClicked(self):
        self.adminViewShowWindow.destroy()
        import adminFunctionality

a = ATLzooAdminViewShow()

