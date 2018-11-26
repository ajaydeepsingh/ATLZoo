from tkinter import *
from PIL import ImageTk, Image
import pymysql
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime, timedelta
import decimal

class animalDetail():

    def __init__(self):
        # Invoke createLoginWindow; Invoke buildLoginWindow, Set loginWindow as mainloop
        #Connect to the database
        # self.db = self.connect()
        # self.cursor = self.db.cursor()
        # Login Window
        self.createAnimalDetailWindow()
        self.buildAnimalDetailWindow(self.animalDetailWindow)
        self.animalDetailWindow.mainloop()
        sys.exit()

    def createAnimalDetailWindow(self):
            # Create blank chooseFunctionalityWindow
            self.animalDetailWindow = Toplevel()
            self.animalDetailWindow.title("Zoo Atlanta")
            self.animalDetailWindow.geometry("400x400")
            self.animalDetailWindow.resizable(0,0)

    def buildAnimalDetailWindow(self, animalDetailWindow):
         # Title Label
        titleLabel= Label(animalDetailWindow,text = "Animal Details", font = "Verdana 16 bold ")
        titleLabel.place(x=130,y=25)
        # titleLabel.grid(row=1, column=2)

        # Labels
        nameLabel = Label(animalDetailWindow,text = "Name:")
        nameLabel.place(x=130,y=60)
        speciesLabel = Label(animalDetailWindow,text = "Species:")
        speciesLabel.place(x=130,y=90)
        exhibitLabel = Label(animalDetailWindow,text = "Exhibit:")
        exhibitLabel.place(x=130,y=120)
        ageLabel = Label(animalDetailWindow,text = "Age:")
        ageLabel.place(x=130,y=150)
        typeLabel = Label(animalDetailWindow,text = "Type:")
        typeLabel.place(x=130,y=180)

        # Back Button
        backButton = Button(animalDetailWindow, text="Back", command=self.animalDetailWindowBackButtonClicked)
        backButton.place(x=10,y=370)



    def animalDetailWindowBackButtonClicked(self):
        self.animalDetailWindow.destroy()
        self.exhibitDetailWindow.deiconify()

a = animalDetail()