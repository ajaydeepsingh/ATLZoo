from tkinter import *
from PIL import ImageTk, Image
import pymysql
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime, timedelta
import decimal

#=========Search Animals Window============
class ATLzooStaffSearchAnimals:

    def __init__(self):
        # Invoke createLoginWindow; Invoke buildLoginWindow, Set loginWindow as mainloop
        #Connect to the database
        self.db = self.connect()
        self.cursor = self.db.cursor()
        # Login Window
        self.createSearchAnimalWindow()
        self.buildSearchAnimalWindow(self.searchAnimalWindow)
        self.searchAnimalWindow.mainloop()
        sys.exit()

    def createSearchAnimalWindow(self):
        # Create blank Search Animal Window
        self.searchAnimalWindow=Toplevel()
        self.searchAnimalWindow.title("Zoo Atlanta")

    def buildSearchAnimalWindow(self,searchAnimalWindow):

        # Title Label
        titleLabel= Label(searchAnimalWindow,text = "Search Animals", font = "Verdana 16 bold ")
        titleLabel.grid(row=1,column=2,sticky=W+E)

        
        nameLabel = Label(searchAnimalWindow,text = "Name")
        nameLabel.grid(row=2, column=0)


        self.animalNameSV = StringVar()
        animalNameEntry = Entry(searchAnimalWindow, textvariable=self.animalNameSV, width=20)
        animalNameEntry.grid(row=2, column=1)

        speciesLabel = Label(searchAnimalWindow,text = "Species")
        speciesLabel.grid(row=3,column=0)
        self.speciesNameSV = StringVar()
        speciesNameEntry = Entry(searchAnimalWindow, textvariable=self.speciesNameSV, width=20)
        speciesNameEntry.grid(row=3, column=1)

        exhibitLabel = Label(searchAnimalWindow,text = "Exhibit")
        exhibitLabel.grid(row=4,column=0)
        self.exhibitDefault = StringVar()
        self.exhibitDefault.set("")
        exhibitMenu = OptionMenu(searchAnimalWindow, self.exhibitDefault, "Pacific","Jungle","Sahara","Mountainous","Birds")
        exhibitMenu.grid(row=4, column=1)

        minLabel=Label(searchAnimalWindow,text="Min")
        minLabel.grid(row=2,column=3, sticky=W)

        maxLabel=Label(searchAnimalWindow,text="Max")
        maxLabel.grid(row=2,column=4, sticky=W)

        ageLabel = Label(searchAnimalWindow,text = "Age")
        ageLabel.grid(row=3,column=2)

        self.minSpinBox = Spinbox(searchAnimalWindow, from_=0, to=10000, width=5)
        self.minSpinBox.grid(row=3, column=3,pady=10,sticky=W)

        self.maxSpinBox = Spinbox(searchAnimalWindow, from_=0, to=10000, width=5)
        self.maxSpinBox.grid(row=3, column=4,pady=10,sticky=W)
        
        typeLabel = Label(searchAnimalWindow,text = "Type")
        typeLabel.grid(row=4, column=2)
        # Name Entry
        self.typeDefault = StringVar()
        self.typeDefault.set("")
        typeMenu = OptionMenu(searchAnimalWindow, self.typeDefault, "mammal", "bird", "amphibian", "reptile", "fish", "invertebrate")
        typeMenu.grid(row=4, column=3, sticky=W)
       
        self.selectAnimalTree = ttk.Treeview(searchAnimalWindow, columns=("1", "2", "3", "4","5"))
        self.selectAnimalTree['show'] = "headings"
        self.selectAnimalTree.column("1", width = 150, anchor = "center")
        self.selectAnimalTree.column("2", width = 150, anchor = "center")
        self.selectAnimalTree.column("3", width = 150, anchor = "center")
        self.selectAnimalTree.column("4", width = 150, anchor = "center")
        self.selectAnimalTree.column("5", width = 150, anchor = "center")

        self.selectAnimalTree.heading("1", text = "Name")
        self.selectAnimalTree.heading("2", text = "Species")
        self.selectAnimalTree.heading("3", text = "Exhibit")
        self.selectAnimalTree.heading("4", text = "Age")
        self.selectAnimalTree.heading("5", text = "Type")

        self.selectAnimalTree.grid(row=5, columnspan=4, sticky = 'nsew')



        findAnimalsButton = Button(searchAnimalWindow, text="Find Animals", command=self.searchAnimalWindowFindAnimalsButtonClicked)
        findAnimalsButton.grid(row=6,column=3)

        backButton = Button(searchAnimalWindow, text="Back", command=self.searchAnimalWindowBackButtonClicked)
        backButton.grid(row=6,column=1)


    def searchAnimalWindowFindAnimalsButtonClicked(self):

        for i in self.selectAnimalTree.get_children():
            self.selectAnimalTree.delete(i)  

        # Table is a list of table names"
        attributes = ["Name", "Species", "Type", "Age", "E_Name",]

        # Entry is a list of the filter inputs
        entry = []
        entry.append(str(self.animalNameSV.get()))
        entry.append(str(self.speciesNameSV.get()))
        entry.append(self.typeDefault.get())
        entry.append(self.exhibitDefault.get())


        sql = "SELECT * FROM Animal WHERE "

        for i in range(len(entry)):
            if i == 3:
                sql = sql + attributes[i] + " BETWEEN " + self.minSpinBox.get() + " AND " + self.maxSpinBox.get() + " "
            elif entry[i] != "":
                sql = sql + attributes[i] + " = " + "'" + entry[i] + "'"
            else:
                sql = sql + attributes[i] + " LIKE '%'"
        #This is to check if the next box is filled as well so we add an AND statement to make sure all conditions are met. 
            if i < len(entry)-1:
                sql = sql + " AND "
        #end of statement
        sql = sql + ";"

        # print(sql)
        self.cursor.execute(sql)

        self.animalResults = self.cursor.fetchall()
        # print(self.animalResults)

        self.animalName = []
        self.species = []
        self.type = []
        self.ename = []
        self.age = []

        for i in self.animalResults:
            self.age.append(i[0])
            self.type.append(i[1])
            self.animalName.append(i[2])
            self.species.append(i[3])
            self.ename.append(i[4])
        
        for i in range(len(self.animalResults)):
            self.selectAnimalTree.insert('', i , values=(self.animalName[i], self.species[i], self.ename[i], self.age[i], self.type[i]))

        # self.createSearchAnimalWindow()
        # self.buildSearchAnimalWindow(searchAnimalWindow)
        # self.searchAnimalWindow.destroy()
        # self.createAnimalDetailWindow()

    def  searchAnimalWindowBackButtonClicked(self):
        self.searchAnimalWindow.withdraw()
        import staffFunctionality


    def connect(self):
        try:
            db = pymysql.connect(host = 'academic-mysql.cc.gatech.edu',
                                 db = 'cs4400_group33', user = 'cs4400_group33', passwd = '9dpzV4ce')
            return db
        except:
            messagebox.showwarning('Error!','Cannot connect. Please check your internet connection.')
            return False


a=ATLzooStaffSearchAnimals()