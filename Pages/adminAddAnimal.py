from tkinter import *
from PIL import ImageTk, Image
import pymysql
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime, timedelta
import decimal

class ATLzooAdminAddAnimal:
    def __init__(self):
        self.createAdminAddAnimalWindow()
        self.buildAdminAddAnimalWindow(self.adminAddAnimalWindow)
        self.adminAddAnimalWindow.mainloop()
        sys.exit()

    def createAdminAddAnimalWindow(self):
        # Create blank Search Animal Window
        self.adminAddAnimalWindow=Toplevel()
        self.adminAddAnimalWindow.title("Zoo Atlanta")
        self.adminAddAnimalWindow.geometry("800x600")

    def buildAdminAddAnimalWindow(self, adminAddAnimalWindow):
        '''
        frame = Frame(staffShowHistoryWindow)
        frame.pack()
        treeFrame = Frame(staffShowHistoryWindow)
        treeFrame.pack()
        buttonFrame = Frame(staffShowHistoryWindow)
        buttonFrame.pack(side=BOTTOM)
        '''

        titleLabel= Label(adminAddAnimalWindow,text = "Add Animal", font = "Verdana 16 bold ")
        titleLabel.grid(row=1,column=2, sticky=W+E, padx=200,pady=20)


        nameLabel = Label(adminAddAnimalWindow,text = "Name")
        nameLabel.grid(row=2, column=1,pady=15)


        self.animalNameSV = StringVar()
        animalNameEntry = Entry(adminAddAnimalWindow, textvariable=self.animalNameSV, width=20)
        animalNameEntry.grid(row=2, column=2,pady=15)

    


        exhibitLabel = Label(adminAddAnimalWindow,text = "Exhibit")
        exhibitLabel.grid(row=3,column=1,pady=15)
        exhibitDefault = StringVar()
        exhibitDefault.set("options")
        exhibitMenu = OptionMenu(adminAddAnimalWindow, exhibitDefault, "this","will","have","options","later")
        exhibitMenu.grid(row=3, column=2,pady=15)

        typeLabel = Label(adminAddAnimalWindow,text = "Type")
        typeLabel.grid(row=4, column=1,pady=15)
        # Name Entry
        typeDefault = StringVar()
        typeDefault.set("mammal")
        typeMenu = OptionMenu(adminAddAnimalWindow, typeDefault, "mammal", "bird", "amphibian", "reptile", "fish", "invertebrate")
        typeMenu.grid(row=4, column=2,pady=15)

        speciesLabel = Label(adminAddAnimalWindow,text = "Species")
        speciesLabel.grid(row=5,column=1,pady=15)
        self.speciesNameSV = StringVar()
        speciesNameEntry = Entry(adminAddAnimalWindow, textvariable=self.speciesNameSV, width=20)
        speciesNameEntry.grid(row=5, column=2,pady=15)

        ageLabel=Label(adminAddAnimalWindow,text="Date")
        ageLabel.grid(row=6,column=1,pady=15)
        ageSpinBox = Spinbox(adminAddAnimalWindow, from_=0, to=100)
        ageSpinBox.grid(row=6, column=2,pady=15)



        addAnimalButton = Button(adminAddAnimalWindow, text="Add Animal", command=self.adminAddAnimalWindowAddButtonClicked)
        addAnimalButton.grid(row=4, column =3, pady=15)


        backButton = Button(adminAddAnimalWindow, text="Back", command=self.adminAddAnimalWindowBackButtonClicked)
        backButton.place(x=360, y=400)

    def adminAddAnimalWindowAddButtonClicked(self):
        self.adminAddAnimalWindow.destroy()

    def adminViewShowWindowRemoveButtonClicked(self):
        self.adminAddAnimalWindow.destroy()

    def adminAddAnimalWindowBackButtonClicked(self):
        self.adminAddAnimalWindow.destroy()
        import adminFunctionality

a = ATLzooAdminAddAnimal()

