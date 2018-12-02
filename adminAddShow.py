from tkinter import *
from PIL import ImageTk, Image
import pymysql
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime, timedelta
import decimal

class ATLzooAdminAddShow:
    def __init__(self):
        self.createAdminAddShowWindow()
        self.buildAdminAddShowWindow(self.adminAddShowWindow)
        self.adminAddShowWindow.mainloop()
        sys.exit()

    def createAdminAddShowWindow(self):
        # Create blank Search Animal Window
        self.adminAddShowWindow=Toplevel()
        self.adminAddShowWindow.title("Zoo Atlanta")
        self.adminAddShowWindow.geometry("800x600")

    def buildAdminAddShowWindow(self, adminAddShowWindow):

        titleLabel= Label(adminAddShowWindow,text = "Add Show", font = "Verdana 16 bold ")
        titleLabel.grid(row=1,column=2, sticky=W+E, padx=200,pady=20)


        nameLabel = Label(adminAddShowWindow,text = "Show Name")
        nameLabel.grid(row=2, column=1,pady=15)

        showName = StringVar()
        showName = Entry(adminAddShowWindow, textvariable=self.animalNameSV, width=20)
        showName.grid(row=2, column=2,pady=15)


        exhibitLabel = Label(adminAddShowWindow,text = "Exhibit")
        exhibitLabel.grid(row=3,column=1,pady=15)
        exhibitDefault = StringVar()
        exhibitDefault.set("")
        exhibitMenu = OptionMenu(adminAddShowWindow, exhibitDefault, "this","will","have","options","later")
        exhibitMenu.grid(row=3, column=2,pady=15)

        staffLabel = Label(adminAddShowWindow,text = "Staff")
        staffLabel.grid(row=4, column=1,pady=15)
        
        # Name Entry
        staffDefault = StringVar()
        staffDefault.set("")
        staffMenu = OptionMenu(adminAddShowWindow, staffDefault, "this","will","have","options","later")
        staffMenu.grid(row=4, column=2,pady=15)

        dateLabel = Label(adminAddShowWindow,text = "Date")
        dateLabel.grid(row=5,column=1,pady=15)
        self.dateNameSV = StringVar()
        dateEntry = Entry(adminAddShowWindow, textvariable=self.dateNameSV, width=20)
        dateEntry.grid(row=5, column=2,pady=15)

        timeLabel = Label(adminAddShowWindow,text = "Time")
        timeLabel.grid(row=6,column=1, pady=15)
        self.timeNameSV = StringVar()
        timeEntry = Entry(adminAddShowWindow, textvariable=self.timeNameSV, width=20)
        timeEntry.grid(row=6, column=2, pady=15)



        addShowButton = Button(adminAddShowWindow, text="Add Show", command=self.adminAddShowWindowAddButtonClicked)
        addShowButton.grid(row=4, column =3, pady=15)


        backButton = Button(adminAddShowWindow, text="Back", command=self.adminViewShowWindowBackButtonClicked)
        backButton.place(x=360, y=400)

    def adminAddShowWindowAddButtonClicked(self):
        self.adminViewShowWindow.destroy()

    def adminViewShowWindowRemoveButtonClicked(self):
        self.adminViewShowWindow.destroy()

    def adminViewShowWindowBackButtonClicked(self):
        self.adminViewShowWindow.destroy()
        import adminFunctionality

a = ATLzooAdminAddShow()

