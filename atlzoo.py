from tkinter import *
from PIL import ImageTk, Image
import pymysql
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime, timedelta
import hashlib
import decimal


class ATLzoo:
    def __init__(self):
        # Invoke createLoginWindow; Invoke buildLoginWindow, Set loginWindow as mainloop
        #Connect to the database

        self.db = self.connect()
        self.cursor = self.db.cursor()
        self.currentUser = ""
        self.exhibitOfInterest = ""
        self.animalOfInterest = ""
        self.animalSpeciesOfInterest = ""
        # Login Window
        self.createLoginWindow()
        self.buildLoginWindow(self.loginWindow)
        self.loginWindow.mainloop()
        sys.exit()


##  =======Login Window=======
    def createLoginWindow(self):
        # Create blank Login Window
        self.loginWindow = Tk()
        self.loginWindow.title("Atlanta Zoo")

        self.loginWindow.withdraw()
        self.loginWindow.update_idletasks()  # Update "requested size" from geometry manager
        x = (self.loginWindow.winfo_screenwidth() - self.loginWindow.winfo_reqwidth()) / 2
        y = (self.loginWindow.winfo_screenheight() - self.loginWindow.winfo_reqheight()) / 2
        self.loginWindow.geometry("+%d+%d" % (x, y))
        self.loginWindow.config(background='#fec409')
        self.loginWindow.deiconify()


    def buildLoginWindow(self, loginWindow):
        # Add component for Login Window
        # Login Label
        loginLabel = Label(loginWindow, text="Login",font = "Verdana 13 bold", background='#fec409')
        loginLabel.grid(row=1, column=3, sticky=W+E)

        # Username Label
        usernameLabel = Label(loginWindow, text="Username", background='#fec409')
        usernameLabel.grid(row=2, column=2, sticky=W)

        # Password Label
        passwordLabel = Label(loginWindow, text="Password", background='#fec409')
        passwordLabel.grid(row=4, column=2, sticky=W)

        # # Image
        image = Image.open("zoo-logo.jpg")
        image = image.resize((60, 60), Image.ANTIALIAS)
        zooImage = ImageTk.PhotoImage(image)
        imageLabel = Label(loginWindow, image=zooImage, background='#fec409', highlightbackground='#fec409')
        imageLabel.image = zooImage
        imageLabel.grid(row=2, column=4, rowspan=3, sticky=E)

        # Username Entry
        self.loginUsername = StringVar()
        usernameEntry = Entry(loginWindow, textvariable=self.loginUsername, width=20, highlightbackground='#fec409')
        usernameEntry.grid(row=2, column=3, sticky=W + E)


        # Password Entry
        self.loginPassword = StringVar()
        passwordEntry = Entry(loginWindow, textvariable=self.loginPassword, show = '*', width=20, highlightbackground='#fec409')
        passwordEntry.grid(row=4, column=3, sticky=W + E)

        # Login Buttons
        # loginButton = Button(loginWindow, text="Login", command=self.loginWindowLoginButtonClicked)
        loginButton = Button(loginWindow, text="Login", command=self.loginWindowLoginButtonClicked, background='#fec409', highlightbackground='#fec409')
        loginButton.grid(row=6, column=3)

        # Register Button

        # registerButton = Button(loginWindow, text="Register", command=self.loginWindowRegisterButtonClicked)
        registerButton = Button(loginWindow, text="Register", command=self.loginWindowRegisterButtonClicked, background='#fec409', highlightbackground='#fec409')
        registerButton.grid(row=6, column=4, sticky=E)


    def loginWindowLoginButtonClicked(self):
        # Click the button on Login Window:
        # Obtain the username and password from keypress;
        # Invoke;
        # Invoke;
        # Withdraw Login Window;
        self.username = self.loginUsername.get()
        self.password = self.loginPassword.get()

        def encrypt_string(hash_string):
            sha_signature = hashlib.sha256(hash_string.encode()).hexdigest()
            return sha_signature
        
        hashedPass = encrypt_string(self.password)
        print(hashedPass)

        if not self.username:
            messagebox.showwarning("Username input is empty", "Please enter username.")
            return False
        if not self.password:
            messagebox.showwarning("Password input is empty", "Please enter password")
            return False
        
        isUsername = self.cursor.execute("SELECT * FROM User WHERE Username = %s", self.username)
        if not isUsername:
           messagebox.showwarning("Username is not an user\'s username",
                                  "The username you entered is not an user\'s username.")
           return False


        usernameAndPasswordMatch = self.cursor.execute("SELECT * FROM User WHERE (Username = %s AND Password = %s)", (self.username, hashedPass))
        if not usernameAndPasswordMatch:
           messagebox.showwarning("Username and password don\'t match", "Sorry, the username and password you entered"
                                                                        + " do not match.")
           return False

        isStaffName = self.cursor.execute("SELECT * FROM User WHERE Username = %s AND Type = %s", (self.username, 'staff'))
        isAdminName = self.cursor.execute("SELECT * FROM User WHERE Username = %s AND Type = %s", (self.username, 'admin'))
        # isVisitorName = self.cursor.execute("SELECT * FROM User WHERE Username = %s a AND Type = %s", (self.username, 'visitor'))
        if isStaffName:
            self.loginWindow.withdraw()
            self.currentUser = self.username
            self.createStaffChooseFunctionalityWindow()
            self.buildStaffChooseFunctionalityWindow(self.chooseStaffFunctionalityWindow)
        elif isAdminName:
            self.loginWindow.withdraw()
            self.currentUser = self.username
            self.createAdminChooseFunctionalityWindow()
            self.buildAdminChooseFunctionalityWindow(self.chooseAdminFunctionalityWindow)
        else:
            self.loginWindow.withdraw()
            self.currentUser = self.username
            self.createVisitorChooseFunctionalityWindow()
            self.buildVisitorChooseFunctionalityWindow(self.chooseVisitorFunctionalityWindow)
        return True

    def loginWindowRegisterButtonClicked(self):
        # Click button on Login Window:
        # Invoke createNewUserRegistrationWindow; Invoke buildNewUserRegistrationWindow;
        # Hide Login Window; Set newUserRegistrationWindow on the top
        self.createNewUserRegistrationWindow()
        self.buildNewUserRegistrationWindow(self.newUserRegistrationWindow)
        self.loginWindow.withdraw()

#======New User Registration Window==============

    def createNewUserRegistrationWindow(self):
        # Create blank newUserRegistrationWindow
        self.newUserRegistrationWindow = Toplevel()
        self.newUserRegistrationWindow.title("Atlanta Zoo")


    def buildNewUserRegistrationWindow(self,newUserRegistrationWindow):
        # Add components for newUserRegistrationWindow

        # New User Rigestration Label
        newUserRegistrationLabel = Label(newUserRegistrationWindow, text="New User Registration",font = "Verdana 13 bold ")
        newUserRegistrationLabel.grid(row=1, column=3, sticky=W)


        # Username Label
        usernameLabel = Label(newUserRegistrationWindow, text="Username")
        usernameLabel.grid(row=2, column=2, sticky=W)


        # Email Address Label
        emailAddressLabel = Label(newUserRegistrationWindow, text="Email Address")
        emailAddressLabel.grid(row=3, column=2, sticky=W)

        # Password Label
        passwordLabel = Label(newUserRegistrationWindow, text="Password")
        passwordLabel.grid(row=4, column=2, sticky=W)

        # Confirm Password Label
        confirmPasswordLabel = Label(newUserRegistrationWindow, text="Confirm Password")
        confirmPasswordLabel.grid(row=5, column=2, sticky=W)


        # Username Entry
        self.registrationUsername = StringVar()
        usernameEntry = Entry(newUserRegistrationWindow, textvariable=self.registrationUsername, width=20)
        usernameEntry.grid(row=2, column=3, sticky=W + E)


        # Email Address Entry
        self.registrationEmailAddress = StringVar()
        emailAddressEntry = Entry(newUserRegistrationWindow, textvariable=self.registrationEmailAddress,width=20)
        emailAddressEntry.grid(row=3, column=3, sticky=W + E)

        # Password Entry
        self.registrationPassword = StringVar()
        passwordEntry = Entry(newUserRegistrationWindow, textvariable=self.registrationPassword,show = '*',width=20)
        passwordEntry.grid(row=4, column=3, sticky=W + E)

        # Confirm Password Entry
        self.registrationConfirmPassword = StringVar()
        confirmPasswordEntry = Entry(newUserRegistrationWindow, textvariable=self.registrationConfirmPassword,show = '*',width=20)
        confirmPasswordEntry.grid(row=5, column=3, sticky=W + E)


        # Create Visitor Button
        createButton = Button(newUserRegistrationWindow, text="Create Visitor", command=self.newUserRegistrationWindowCreateVisitorButtonClicked)
        createButton.grid(row=6, column=3)

        # Create Staff Button
        createButton = Button(newUserRegistrationWindow, text="Create Staff", command=self.newUserRegistrationWindowCreateStaffButtonClicked)
        createButton.grid(row=6, column=2)

    def newUserRegistrationWindowCreateVisitorButtonClicked(self):
        # Click the Create Button on New User Registration Window:
        # Invoke createChooseFunctionalityWindow; Invoke buildChooseFunctionalityWindow;
        # Destroy New User Registration Window
        self.username = self.registrationUsername.get()
        self.emailAddress = self.registrationEmailAddress.get()
        self.password = self.registrationPassword.get()

        def encrypt_string(hash_string):
            sha_signature = hashlib.sha256(hash_string.encode()).hexdigest()
            return sha_signature
        
        hashedPass = encrypt_string(self.password)
        # print(hashedPass)


        self.confirmPassword = self.registrationConfirmPassword.get()

        hashedPass2 = encrypt_string(self.confirmPassword)
        # print(hashedPass2)
        
        if not self.username:
            messagebox.showwarning("Error", "Username input is empty. Please enter username.")
            return False
        if not self.emailAddress:
            messagebox.showwarning("Error", "E-mail input is empty. Please enter E-mail.")
            return False
        if not self.password:
            messagebox.showwarning("Error", "Password input is empty. Please enter password")
            return False
        if not self.confirmPassword:
            messagebox.showwarning("Error", "Confirm password input is empty. Please enter confirm password")
            return False

        isUsername = self.cursor.execute("SELECT * FROM User WHERE Username = %s", self.username)
        if isUsername:
           messagebox.showwarning("Error",
                                  "This username has been used. Please input another username.")
           return False
        isEmail = self.cursor.execute("SELECT * FROM User WHERE Email = %s", self.emailAddress)
        if isEmail:
           messagebox.showwarning("Error",
                                  "This E-mail address has been used. Please input another E-mail address.")
           return False
        if not (hashedPass == hashedPass2):
           messagebox.showwarning("Error",
                                  "Passwords do not match. Please reconfirm the password.")
           return False
        messagebox.showinfo("Success!","Registered successfully!")
        self.cursor.execute("INSERT INTO User VALUES (%s, %s, %s, %s)", (self.username, hashedPass, self.emailAddress, "visitor"))
        # self.cursor.execute("INSERT INTO User VALUES (%s, %s)", (self.username, self.password))
        self.currentUser = self.username
        self.createVisitorChooseFunctionalityWindow()
        self.buildVisitorChooseFunctionalityWindow(self.chooseVisitorFunctionalityWindow)
        self.newUserRegistrationWindow.destroy()



    def newUserRegistrationWindowCreateStaffButtonClicked(self):
        # Click the Create Button on New User Registration Window:
        # Invoke createChooseFunctionalityWindow; Invoke buildChooseFunctionalityWindow;
        # Destroy New User Registration Window
        self.username = self.registrationUsername.get()
        self.emailAddress = self.registrationEmailAddress.get()
        self.password = self.registrationPassword.get()
        self.confirmPassword = self.registrationConfirmPassword.get()


        def encrypt_string(hash_string):
            sha_signature = hashlib.sha256(hash_string.encode()).hexdigest()
            return sha_signature
        
        hashedPass = encrypt_string(self.password)
        # print(hashedPass)

        self.confirmPassword = self.registrationConfirmPassword.get()

        hashedPass2 = encrypt_string(self.confirmPassword)
        # print(hashedPass2)
        
        if not self.username:
            messagebox.showwarning("Error", "Username input is empty. Please enter username.")
            return False
        if not self.emailAddress:
            messagebox.showwarning("Error", "E-mail input is empty. Please enter E-mail.")
            return False
        if not self.password:
            messagebox.showwarning("Error", "Password input is empty. Please enter password")
            return False
        if not self.confirmPassword:
            messagebox.showwarning("Error", "Confirm password input is empty. Please enter confirm password")
            return False

        isUsername = self.cursor.execute("SELECT * FROM User WHERE Username = %s", self.username)
        if isUsername:
           messagebox.showwarning("Error",
                                  "This username has been used. Please input another username.")
           return False
        isEmail = self.cursor.execute("SELECT * FROM User WHERE Email = %s", self.emailAddress)
        if isEmail:
           messagebox.showwarning("Error",
                                  "This E-mail address has been used. Please input another E-mail address.")
           return False
        if not (hashedPass == hashedPass2):
           messagebox.showwarning("Error",
                                  "Passwords do not match. Please reconfirm the password.")
           return False
        messagebox.showinfo("Success!","Registered successfully!")
        self.cursor.execute("INSERT INTO User VALUES (%s, %s, %s, %s)", (self.username, hashedPass, self.emailAddress, "staff"))
        # self.cursor.execute("INSERT INTO User VALUES (%s, %s)", (self.username, self.password))
        self.loginWindow.withdraw()
        self.currentUser = self.username
        self.createStaffChooseFunctionalityWindow()
        self.buildStaffChooseFunctionalityWindow(self.chooseStaffFunctionalityWindow)
        self.newUserRegistrationWindow.destroy()


    # def newUserRegistrationWindowBackButtonClicked(self):
    #     self.newUserRegistrationWindow.destroy()
    #     self.createLoginWindow()
    #     self.buildLoginWindow(self.loginWindow)



#--------------------ADMIN FUNCTIONALITY WINDOW---------------------------


    def createAdminChooseFunctionalityWindow(self):
            # Create blank chooseFunctionalityWindow
            self.chooseAdminFunctionalityWindow = Toplevel()
            self.chooseAdminFunctionalityWindow.title("Zoo Atlanta")
            self.chooseAdminFunctionalityWindow.geometry("800x600")
            self.chooseAdminFunctionalityWindow.resizable(0,0)

    def buildAdminChooseFunctionalityWindow(self,chooseAdminFunctionalityWindow):
        # Add component to chooseFunctionalityWindow

        #Choose Functionality Label
        chooseFunctionalityLabel = Label(chooseAdminFunctionalityWindow, text="Choose Functionality",font = "Verdana 16 bold ")
        # chooseFunctionalityLabel.grid(row=1, column=1, sticky=W+E)
        chooseFunctionalityLabel.place(x=400, y = 25, anchor="center")

        # View Visitors Label
        viewVisitorsLabel = Label(chooseAdminFunctionalityWindow, text="View Visitors", font = "Verdana 13")
        # viewVisitorsLabel.grid(row=2, column=1)
        viewVisitorsLabel.bind("<ButtonPress-1>", self.chooseAdminFunctionalityWindowViewVisitorsLabelClicked)
        viewVisitorsLabel.place(x=400, y = 100, anchor="center")

        # View Shows 
        viewShowsLabel = Label(chooseAdminFunctionalityWindow, text="View Shows", font = "Verdana 13")
        # viewShowsLabel.grid(row=3, column=1)
        viewShowsLabel.bind("<ButtonPress-1>", self.chooseAdminFunctionalityWindowViewShowsLabelClicked)
        viewShowsLabel.place(x=400, y = 175, anchor="center")

        # View Animals Label
        viewAnimalsLabel = Label(chooseAdminFunctionalityWindow, text="View Animals", font = "Verdana 13")
        # viewAnimalsLabel.grid(row=4,column=1)
        viewAnimalsLabel.bind("<ButtonPress-1>", self.chooseAdminFunctionalityWindowViewAnimalsLabelClicked)
        viewAnimalsLabel.place(x=400, y = 250, anchor="center")

        # View Staff
        viewStaffLabel = Label(chooseAdminFunctionalityWindow, text="View Staff", font = "Verdana 13")
        # viewStaffLabel.grid(row=5,column=1)
        viewStaffLabel.bind("<ButtonPress-1>", self.chooseAdminFunctionalityWindowViewStaffLabelClicked)
        viewStaffLabel.place(x=400, y = 325, anchor="center")

        # View Add Show
        viewShowAdd = Label(chooseAdminFunctionalityWindow, text="Add Show", font = "Verdana 13")
        # viewReviewLabel.grid(row=6,column=1)
        viewShowAdd.bind("<ButtonPress-1>", self.chooseAdminFunctionalityWindowViewShowAddLabelClicked)
        viewShowAdd.place(x=400, y = 400, anchor="center")

        # View Add Animal
        viewAnimalAdd = Label(chooseAdminFunctionalityWindow, text="Add Animal", font = "Verdana 13")
        viewAnimalAdd.bind("<ButtonPress-1>", self.chooseAdminFunctionalityWindowAddAnimalLabelClicked)
        viewAnimalAdd.place(x=400, y = 475, anchor="center")

        # Log Out Buttons

        logOutButton = Button(chooseAdminFunctionalityWindow, text="Log out", command=self.chooseAdminFunctionalityWindowLogOutButtonClicked)
        logOutButton.grid(row=8, column=2,sticky=E)
        logOutButton.place(x = 720, y = 570)

    def chooseAdminFunctionalityWindowViewVisitorsLabelClicked(self,event):
        # Hide Choose Functionality Window.
        self.createViewVisitorsWindow()
        self.buildViewVisitorsWindow(self.viewVisitorsWindow)
        self.chooseAdminFunctionalityWindow.withdraw()

    def chooseAdminFunctionalityWindowViewShowsLabelClicked(self,event):
        # Hide Choose Functionality Window

        self.createAdminViewShowWindow()
        self.buildAdminViewShowWindow(self.adminViewShowWindow)
        self.chooseAdminFunctionalityWindow.withdraw()

    def chooseAdminFunctionalityWindowViewAnimalsLabelClicked(self,event):
        self.createShowAnimalWindowAdmin()
        self.buildShowAnimalWindowAdmin(self.showAnimalWindowAdmin)
        self.chooseAdminFunctionalityWindow.withdraw()

    def chooseAdminFunctionalityWindowViewStaffLabelClicked(self,event):
        self.createViewStaffWindow()
        self.buildViewStaffWindow(self.viewStaffWindow)
        self.chooseAdminFunctionalityWindow.withdraw()

    def chooseAdminFunctionalityWindowViewShowAddLabelClicked(self,event):
        self.createAdminAddShowWindow()
        self.buildAdminAddShowWindow(self.adminAddShowWindow)
        self.chooseAdminFunctionalityWindow.withdraw()

    def chooseAdminFunctionalityWindowAddAnimalLabelClicked(self,event):
        self.createAdminAddAnimalWindow()
        self.buildAdminAddAnimalWindow(self.adminAddAnimalWindow)
        self.chooseAdminFunctionalityWindow.withdraw()

    def chooseAdminFunctionalityWindowLogOutButtonClicked(self):
        # Click Log Out Buttion on Choose Functionality Window:
        # Destroy Choose Functionality Window
        # Display Login Window
        self.chooseAdminFunctionalityWindow.destroy()
        self.loginWindow.deiconify()


#-------------------ADMIN PAGES--------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#-------------------ADMIN VIEW VISITORS PAGE------------------------------

    def createViewVisitorsWindow(self):
        self.viewVisitorsWindow = Toplevel()
        self.viewVisitorsWindow.title("Zoo Atlanta")
        self.viewVisitorsWindow.geometry("800x600")
        self.viewVisitorsWindow.resizable(0,0)

    def buildViewVisitorsWindow(self, viewVisitorsWindow):

        # Title Label
        titleLabel = Label(viewVisitorsWindow, text = "View Vistors", font = "Verdana 16 bold ")
        titleLabel.place(x=350, y=25)

        self.columns = ("1", "2")

        # Table of all the visitors
        self.visitorsTree = ttk.Treeview(viewVisitorsWindow, columns=self.columns, selectmode="extended")
        self.visitorsTree['show'] = "headings"
        self.visitorsTree.column("1", width = 300, anchor = "center")
        self.visitorsTree.column("2", width = 300, anchor = "center")
        
        self.visitorsTree.heading("1", text = "Username")
        self.visitorsTree.heading("2", text = "Email")

        self.visitorsTree.place(x=400, y=200, anchor="center")

        adminShowVisitorSort = self.visitorsTree

        for col in self.columns:
            self.visitorsTree.heading(col, command=lambda _col=col: \
                self.sortAdminViewVisitors(adminShowVisitorSort, _col, False))

        self.cursor.execute("SELECT Username, Email FROM User WHERE Type = 'visitor'")

        self.viewVisitorsTuple = self.cursor.fetchall()
        self.usernameList = []
        self.emailList = []

        for i in self.viewVisitorsTuple:
            self.usernameList.append(i[0])
            self.emailList.append(i[1])

        # Insert data into the treeview
        for i in range(len(self.viewVisitorsTuple)):
            self.visitorsTree.insert('', i , values=(self.usernameList[i], self.emailList[i]))

        # Back Button
        backButton = Button(viewVisitorsWindow, text="Back", command=self.viewVisitorsBackButtonClicked)
        backButton.place(x=10,y=570)

        removeVisitorsButton = Button(viewVisitorsWindow, text="Delete Visitor", command=self.showVisitorsWindowAdminRemoveVisitorButtonClicked)
        removeVisitorsButton.place(x=670,y=570)

    def sortAdminViewVisitors(self, tv, column, resort):
        for i in self.visitorsTree.get_children():
            self.visitorsTree.delete(i)

        if (column == "1" and resort == False):
            self.cursor.execute("SELECT Username, Email FROM User WHERE Type = 'visitor' ORDER BY Username ASC")

            self.viewVisitorsTuple = self.cursor.fetchall()
            self.usernameList = []
            self.emailList = []

            for i in self.viewVisitorsTuple:
                self.usernameList.append(i[0])
                self.emailList.append(i[1])

            # Insert data into the treeview
            for i in range(len(self.viewVisitorsTuple)):
                self.visitorsTree.insert('', i , values=(self.usernameList[i], self.emailList[i]))

            tv.heading(column, command=lambda: \
                self.sortAdminViewVisitors(tv, column, not resort))

        if (column == "1" and resort == True):
            self.cursor.execute("SELECT Username, Email FROM User WHERE Type = 'visitor' ORDER BY Username DESC")

            self.viewVisitorsTuple = self.cursor.fetchall()
            self.usernameList = []
            self.emailList = []

            for i in self.viewVisitorsTuple:
                self.usernameList.append(i[0])
                self.emailList.append(i[1])

            # Insert data into the treeview
            for i in range(len(self.viewVisitorsTuple)):
                self.visitorsTree.insert('', i , values=(self.usernameList[i], self.emailList[i]))

            tv.heading(column, command=lambda: \
                self.sortAdminViewVisitors(tv, column, not resort))

        if (column == "2" and resort == False):
            self.cursor.execute("SELECT Username, Email FROM User WHERE Type = 'visitor' ORDER BY Email ASC")

            self.viewVisitorsTuple = self.cursor.fetchall()
            self.usernameList = []
            self.emailList = []

            for i in self.viewVisitorsTuple:
                self.usernameList.append(i[0])
                self.emailList.append(i[1])

            # Insert data into the treeview
            for i in range(len(self.viewVisitorsTuple)):
                self.visitorsTree.insert('', i , values=(self.usernameList[i], self.emailList[i]))

            tv.heading(column, command=lambda: \
                self.sortAdminViewVisitors(tv, column, not resort))

        if (column == "2" and resort == True):
            self.cursor.execute("SELECT Username, Email FROM User WHERE Type = 'visitor' ORDER BY Email DESC")

            self.viewVisitorsTuple = self.cursor.fetchall()
            self.usernameList = []
            self.emailList = []

            for i in self.viewVisitorsTuple:
                self.usernameList.append(i[0])
                self.emailList.append(i[1])

            # Insert data into the treeview
            for i in range(len(self.viewVisitorsTuple)):
                self.visitorsTree.insert('', i , values=(self.usernameList[i], self.emailList[i]))

            tv.heading(column, command=lambda: \
                self.sortAdminViewVisitors(tv, column, not resort))


    def showVisitorsWindowAdminRemoveVisitorButtonClicked(self):
        if not self.visitorsTree.focus():
            messagebox.showwarning("Error","You haven't selected any Visitor.")
            return False

        treeIndexString = self.visitorsTree.focus()
        valueRemoved = self.visitorsTree.item(treeIndexString)

        messagebox.showwarning('Remove Visitor', 'Are you sure?')
        valueslist = list(valueRemoved.values())
        valueslist = valueslist[2]
        uname = valueslist[0]
        eml = valueslist[1]

        self.cursor.execute("DELETE FROM User WHERE Username= %s OR Email = %s AND Type = 'visitor'",(uname, eml))

        self.viewVisitorsWindow.destroy()
        self.createViewVisitorsWindow()
        self.buildViewVisitorsWindow(self.viewVisitorsWindow)


    def viewVisitorsBackButtonClicked(self):
        self.viewVisitorsWindow.destroy()
        self.chooseAdminFunctionalityWindow.deiconify()

#-------------------ADMIN ADD ANIMAL PAGE------------------------------

    def createAdminAddAnimalWindow(self):
        # Create blank Search Animal Window
        self.adminAddAnimalWindow=Toplevel()
        self.adminAddAnimalWindow.title("Zoo Atlanta")
        self.adminAddAnimalWindow.geometry("800x600")

    def buildAdminAddAnimalWindow(self, adminAddAnimalWindow):
        titleLabel= Label(adminAddAnimalWindow,text = "Add Animal", font = "Verdana 16 bold ")
        titleLabel.grid(row=1,column=2, sticky=W+E, padx=200,pady=20)


        nameLabel = Label(adminAddAnimalWindow,text = "Name")
        nameLabel.grid(row=2, column=1,pady=15)


        self.animalNameSV = StringVar()
        animalNameEntry = Entry(adminAddAnimalWindow, textvariable=self.animalNameSV, width=20)
        animalNameEntry.grid(row=2, column=2,pady=15)

        #populate exhibit menu with sql
        self.cursor.execute("SELECT Name FROM Exhibit")
        self.exhibitTuple = self.cursor.fetchall()
        self.exhibitList = []
        for i in self.exhibitTuple:
            self.exhibitList.append(i[0])

        exhibitLabel = Label(adminAddAnimalWindow,text = "Exhibit")
        exhibitLabel.grid(row=3,column=1,pady=15)
        self.exhibitDefault = StringVar()
        self.exhibitDefault.set("")
        exhibitMenu = OptionMenu(adminAddAnimalWindow, self.exhibitDefault, *self.exhibitList)
        exhibitMenu.grid(row=3, column=2,pady=15)

        typeLabel = Label(adminAddAnimalWindow,text = "Type")
        typeLabel.grid(row=4, column=1,pady=15)
        # Name Entry
        self.typeDefault = StringVar()
        self.typeDefault.set("")
        typeMenu = OptionMenu(adminAddAnimalWindow, self.typeDefault, "mammal", "bird", "amphibian", "reptile", "fish", "invertebrate")
        typeMenu.grid(row=4, column=2,pady=15)

        speciesLabel = Label(adminAddAnimalWindow,text = "Species")
        speciesLabel.grid(row=5,column=1,pady=15)
        self.speciesNameSV = StringVar()
        speciesNameEntry = Entry(adminAddAnimalWindow, textvariable=self.speciesNameSV, width=20)
        speciesNameEntry.grid(row=5, column=2,pady=15)

        ageLabel=Label(adminAddAnimalWindow,text="Age")
        ageLabel.grid(row=6,column=1,pady=15)
        self.ageSpinBox = Spinbox(adminAddAnimalWindow, from_=0, to=100)
        self.ageSpinBox.grid(row=6, column=2,pady=15)


        addAnimalButton = Button(adminAddAnimalWindow, text="Add Animal", command=self.adminAddAnimalWindowAddButtonClicked)
        addAnimalButton.grid(row=4, column =3, pady=15)

        backButton = Button(adminAddAnimalWindow, text="Back", command=self.adminAddAnimalWindowBackButtonClicked)
        backButton.place(x=360, y=400)

    def adminAddAnimalWindowAddButtonClicked(self):
        self.animalAge = self.ageSpinBox.get()
        self.animalType = self.typeDefault.get()
        self.animalName = self.animalNameSV.get()
        self.animalSpecies = self.speciesNameSV.get()
        self.animalExhibit = self.exhibitDefault.get()

        if self.animalAge =="" or self.animalType =="" or self.animalName =="" or self.animalSpecies =="" or self.animalExhibit =="":
            messagebox.showwarning("every field needs to be filled out")
            return False

        self.cursor.execute("INSERT INTO Animal(Age, Type, Name, Species, E_Name)VALUES(%s, %s, %s, %s, %s)",(self.animalAge, self.animalType, self.animalName, self.animalSpecies, self.animalExhibit))
        
        self.adminAddAnimalWindow.destroy()
        self.chooseAdminFunctionalityWindow.deiconify()

    def adminAddAnimalWindowBackButtonClicked(self):
        self.adminAddAnimalWindow.destroy()
        self.chooseAdminFunctionalityWindow.deiconify()

#-------------------ADMIN ADD SHOW------------------------------

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

        self.showNameSV = StringVar()
        showName = Entry(adminAddShowWindow, textvariable = self.showNameSV, width=20)
        showName.grid(row=2, column=2,pady=15)

        #populate exhibit menu with sql
        self.cursor.execute("SELECT Name FROM Exhibit")
        self.exhibitTuple = self.cursor.fetchall()
        self.exhibitList = []
        for i in self.exhibitTuple:
            self.exhibitList.append(i[0])

        exhibitLabel = Label(adminAddShowWindow,text = "Exhibit")
        exhibitLabel.grid(row=3,column=1,pady=15)
        self.exhibitDefault = StringVar()
        self.exhibitDefault.set("")
        exhibitMenu = OptionMenu(adminAddShowWindow, self.exhibitDefault, *self.exhibitList)
        exhibitMenu.grid(row=3, column=2,pady=15)

        staffLabel = Label(adminAddShowWindow,text = "Staff")
        staffLabel.grid(row=4, column=1,pady=15)
        
        #populate staff menu with sql
        self.cursor.execute("SELECT Username FROM User WHERE Type = 'staff'")
        self.staffTuple = self.cursor.fetchall()
        self.staffList = []
        for i in self.staffTuple:
            self.staffList.append(i[0])

        self.staffDefault = StringVar()
        self.staffDefault.set("")
        staffMenu = OptionMenu(adminAddShowWindow, self.staffDefault, *self.staffList)
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

        backButton = Button(adminAddShowWindow, text="Back", command=self.adminAddShowWindowBackButtonClicked)
        backButton.place(x=360, y=400)

    def adminAddShowWindowAddButtonClicked(self):
        self.showName = self.showNameSV.get()
        self.dateTime = self.dateNameSV.get() + " " + self.timeNameSV.get()
        self.hostName = self.staffDefault.get()
        self.exhibitName = self.exhibitDefault.get()

        #date validation
        try:
            datetime.strptime(self.dateTime, '%Y-%m-%d %I:%M%p')
        except ValueError:
            messagebox.showwarning("Error", "Date needs to be in format yyyy-mm-dd and time needs to be in format hh:mmAM/PM")
            return False


        self.dateTimeObject = datetime.strptime(self.dateTime, '%Y-%m-%d %I:%M%p')

        if self.showName =="" or self.dateTime =="" or self.hostName =="" or self.exhibitName =="":
            messagebox.showwarning("Error", "Every field needs to be filled out")
            return False

        #staff cannot host two shows at the same time
        self.cursor.execute("SELECT * from Performance WHERE Host = %s AND Time = %s", (self.hostName, self.dateTime))
        self.isDuplicate = self.cursor.fetchall()

        if self.isDuplicate == ():
            self.cursor.execute("INSERT INTO Performance(Name, Time, Host, E_Name) VALUES(%s, %s, %s, %s)",(self.showName, self.dateTime, self.hostName, self.exhibitName))
            self.adminAddShowWindow.destroy()

            self.chooseAdminFunctionalityWindow.deiconify()
        else:
            messagebox.showwarning("Error", "This staff member is already hosting another show at this time")
            return False

    def adminAddShowWindowBackButtonClicked(self):
        self.adminAddShowWindow.destroy()
        self.chooseAdminFunctionalityWindow.deiconify()

#-------------------SHOW ANIMALS ADMIN PAGE------------------------------

    def createShowAnimalWindowAdmin(self):
        # Create blank Search Animal Window
        self.showAnimalWindowAdmin=Toplevel()
        self.showAnimalWindowAdmin.title("Zoo Atlanta")

    def buildShowAnimalWindowAdmin(self,showAnimalWindowAdmin):

        # Title Label
        titleLabel= Label(showAnimalWindowAdmin,text = "Search Animals", font = "Verdana 16 bold ")
        titleLabel.grid(row=1,column=2,sticky=W +E)

        nameLabel = Label(showAnimalWindowAdmin,text = "Name")
        nameLabel.grid(row=2, column=0)

        self.animalNameSV = StringVar()
        animalNameEntry = Entry(showAnimalWindowAdmin, textvariable=self.animalNameSV, width=20)
        animalNameEntry.grid(row=2, column=1)

        speciesLabel = Label(showAnimalWindowAdmin,text = "Species")
        speciesLabel.grid(row=3,column=0)
        self.speciesNameSV = StringVar()
        speciesNameEntry = Entry(showAnimalWindowAdmin, textvariable=self.speciesNameSV, width=20)
        speciesNameEntry.grid(row=3, column=1)

        #populate exhibit menu with sql
        self.cursor.execute("SELECT Name FROM Exhibit")
        self.exhibitTuple = self.cursor.fetchall()
        self.exhibitList = []
        for i in self.exhibitTuple:
            self.exhibitList.append(i[0])

        exhibitLabel = Label(showAnimalWindowAdmin,text = "Exhibit")
        exhibitLabel.grid(row=4,column=0)
        self.exhibitDefault = StringVar()
        self.exhibitDefault.set("")
        exhibitMenu = OptionMenu(showAnimalWindowAdmin, self.exhibitDefault,"", *self.exhibitList)
        exhibitMenu.grid(row=4, column=1)

        minLabel=Label(showAnimalWindowAdmin,text="Min")
        minLabel.grid(row=2,column=3, sticky=W)

        maxLabel=Label(showAnimalWindowAdmin,text="Max")
        maxLabel.grid(row=2,column=4, sticky=W)

        ageLabel = Label(showAnimalWindowAdmin,text = "Age")
        ageLabel.grid(row=3,column=2)

        self.minSpinBox = Spinbox(showAnimalWindowAdmin, from_=0, to=10000)
        self.minSpinBox.grid(row=3, column=3,pady=10,sticky=W)

        self.maxSpinBox = Spinbox(showAnimalWindowAdmin, from_=0, to=10000)
        self.maxSpinBox.grid(row=3, column=4,pady=10,sticky=W)

        typeLabel = Label(showAnimalWindowAdmin,text = "Type")
        typeLabel.grid(row=4, column=2)
        # Name Entry
        self.typeDefault = StringVar()
        self.typeDefault.set("")
        typeMenu = OptionMenu(showAnimalWindowAdmin, self.typeDefault,"", "mammal", "bird", "amphibian", "reptile", "fish", "invertebrate")
        typeMenu.grid(row=4, column=3, sticky=W)

        self.columns = ("1", "2", "3", "4","5")

        # Display Table for Results
        self.selectAnimalTree = ttk.Treeview(showAnimalWindowAdmin, columns=self.columns, selectmode="extended")
        self.selectAnimalTree['show'] = "headings"
        self.selectAnimalTree.heading('1', text = "Name")
        self.selectAnimalTree.heading('2', text = "Species")
        self.selectAnimalTree.heading('3', text = "Exhibit")
        self.selectAnimalTree.heading('4', text = "Age")
        self.selectAnimalTree.heading('5', text = "Type")
        self.selectAnimalTree.column('1', width = 150, anchor = "center")
        self.selectAnimalTree.column('2', width = 150, anchor = "center")
        self.selectAnimalTree.column('3', width = 150, anchor = "center")
        self.selectAnimalTree.column('4', width = 150, anchor = "center")
        self.selectAnimalTree.column('5', width = 150, anchor = "center")
        self.selectAnimalTree.grid(row=5, columnspan=4, sticky = 'nsew')

        adminSelectAnimalTreeSort = self.selectAnimalTree

        for col in self.columns:
            self.selectAnimalTree.heading(col, command=lambda _col=col: \
                self.sortAdminViewAnimals(adminSelectAnimalTreeSort, _col, False))



        self.cursor.execute("SELECT * FROM Animal")

        self.adminViewAnimalTuple = self.cursor.fetchall()
        self.nameList = []
        self.speciesList = []
        self.exhibitList = []
        self.ageList = []
        self.typeList = []

        for i in self.adminViewAnimalTuple:
            self.nameList.append(i[2])
            self.speciesList.append(i[3])
            self.exhibitList.append(i[4])
            self.ageList.append(i[0])
            self.typeList.append(i[1])

        for i in range(len(self.adminViewAnimalTuple)):
            self.selectAnimalTree.insert('', i, values=(self.nameList[i], self.speciesList[i], self.exhibitList[i], self.ageList[i], self.typeList[i]))


        # Button
        findAnimalsButton = Button(showAnimalWindowAdmin, text="Find Animals", command=self.showAnimalWindowAdminFindAnimalsButtonClicked)
        findAnimalsButton.grid(row=6,column=2)

        removeAnimalsButton = Button(showAnimalWindowAdmin, text="Remove Animal", command=self.showAnimalWindowAdminRemoveAnimalWindowButtonClicked)
        removeAnimalsButton.grid(row=6,column=3)

        backButton = Button(showAnimalWindowAdmin, text="Back", command=self.showAnimalWindowAdminBackButtonClicked)
        backButton.grid(row=6,column=1)

    def sortAdminViewAnimals(self, tv, column, resort):
        for i in self.selectAnimalTree.get_children():
            self.selectAnimalTree.delete(i)  

        attributes = ["Name", "Species", "Type", "Age", "E_Name",]

        # Entry is a list of the filter inputs
        entry = []
        entry.append(str(self.animalNameSV.get()))
        entry.append(str(self.speciesNameSV.get()))
        entry.append(self.typeDefault.get())
        entry.append("")
        entry.append(self.exhibitDefault.get())
        

        if (column == "1" and resort == False):

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
            sql = sql + "ORDER BY Name ASC;"
            self.cursor.execute(sql)
            self.sortColumnsTuple = self.cursor.fetchall()

            #print(self.sortColumnsTuple)

            self.nameListSorted = []
            self.speciesListSorted = []
            self.exhibitListSorted = []
            self.ageListSorted = []
            self.typeListSorted = []

            for i in self.sortColumnsTuple:
                self.nameListSorted.append(i[2])
                self.speciesListSorted.append(i[3])
                self.exhibitListSorted.append(i[4])
                self.ageListSorted.append(i[0])
                self.typeListSorted.append(i[1])

            #print(self.nameListSorted)

            for i in range(len(self.sortColumnsTuple)):
                self.selectAnimalTree.insert('', i, values=(self.nameListSorted[i], self.speciesListSorted[i], self.exhibitListSorted[i], self.ageListSorted[i], self.typeListSorted[i]))

            tv.heading(column, command=lambda: \
                self.sortAdminViewAnimals(tv, column, not resort))

        elif (column == "1" and resort == True):

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
            sql = sql + "ORDER BY Name DESC;"
            self.cursor.execute(sql)
            self.sortColumnsTuple = self.cursor.fetchall()

            #print(self.sortColumnsTuple)

            self.nameListSorted = []
            self.speciesListSorted = []
            self.exhibitListSorted = []
            self.ageListSorted = []
            self.typeListSorted = []

            for i in self.sortColumnsTuple:
                self.nameListSorted.append(i[2])
                self.speciesListSorted.append(i[3])
                self.exhibitListSorted.append(i[4])
                self.ageListSorted.append(i[0])
                self.typeListSorted.append(i[1])

            #print(self.nameListSorted)

            for i in range(len(self.sortColumnsTuple)):
                self.selectAnimalTree.insert('', i, values=(self.nameListSorted[i], self.speciesListSorted[i], self.exhibitListSorted[i], self.ageListSorted[i], self.typeListSorted[i]))

            tv.heading(column, command=lambda: \
                self.sortAdminViewAnimals(tv, column, not resort))

        elif (column == "2" and resort == False):

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
            sql = sql + "ORDER BY Species ASC;"
            self.cursor.execute(sql)
            self.sortColumnsTuple = self.cursor.fetchall()

            #print(self.sortColumnsTuple)

            self.nameListSorted = []
            self.speciesListSorted = []
            self.exhibitListSorted = []
            self.ageListSorted = []
            self.typeListSorted = []

            for i in self.sortColumnsTuple:
                self.nameListSorted.append(i[2])
                self.speciesListSorted.append(i[3])
                self.exhibitListSorted.append(i[4])
                self.ageListSorted.append(i[0])
                self.typeListSorted.append(i[1])

            #print(self.nameListSorted)

            for i in range(len(self.sortColumnsTuple)):
                self.selectAnimalTree.insert('', i, values=(self.nameListSorted[i], self.speciesListSorted[i], self.exhibitListSorted[i], self.ageListSorted[i], self.typeListSorted[i]))

            tv.heading(column, command=lambda: \
                self.sortAdminViewAnimals(tv, column, not resort))

        elif (column == "2" and resort == True):

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
            sql = sql + "ORDER BY Species DESC;"
            self.cursor.execute(sql)
            self.sortColumnsTuple = self.cursor.fetchall()

            #print(self.sortColumnsTuple)

            self.nameListSorted = []
            self.speciesListSorted = []
            self.exhibitListSorted = []
            self.ageListSorted = []
            self.typeListSorted = []

            for i in self.sortColumnsTuple:
                self.nameListSorted.append(i[2])
                self.speciesListSorted.append(i[3])
                self.exhibitListSorted.append(i[4])
                self.ageListSorted.append(i[0])
                self.typeListSorted.append(i[1])

            #print(self.nameListSorted)

            for i in range(len(self.sortColumnsTuple)):
                self.selectAnimalTree.insert('', i, values=(self.nameListSorted[i], self.speciesListSorted[i], self.exhibitListSorted[i], self.ageListSorted[i], self.typeListSorted[i]))

            tv.heading(column, command=lambda: \
                self.sortAdminViewAnimals(tv, column, not resort))

        elif (column == "3" and resort == False):

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
            sql = sql + "ORDER BY E_Name ASC;"
            self.cursor.execute(sql)
            self.sortColumnsTuple = self.cursor.fetchall()

            #print(self.sortColumnsTuple)

            self.nameListSorted = []
            self.speciesListSorted = []
            self.exhibitListSorted = []
            self.ageListSorted = []
            self.typeListSorted = []

            for i in self.sortColumnsTuple:
                self.nameListSorted.append(i[2])
                self.speciesListSorted.append(i[3])
                self.exhibitListSorted.append(i[4])
                self.ageListSorted.append(i[0])
                self.typeListSorted.append(i[1])

            #print(self.nameListSorted)

            for i in range(len(self.sortColumnsTuple)):
                self.selectAnimalTree.insert('', i, values=(self.nameListSorted[i], self.speciesListSorted[i], self.exhibitListSorted[i], self.ageListSorted[i], self.typeListSorted[i]))

            tv.heading(column, command=lambda: \
                self.sortAdminViewAnimals(tv, column, not resort))

        elif (column == "3" and resort == True):

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
            sql = sql + "ORDER BY E_Name DESC;"
            self.cursor.execute(sql)
            self.sortColumnsTuple = self.cursor.fetchall()

            #print(self.sortColumnsTuple)

            self.nameListSorted = []
            self.speciesListSorted = []
            self.exhibitListSorted = []
            self.ageListSorted = []
            self.typeListSorted = []

            for i in self.sortColumnsTuple:
                self.nameListSorted.append(i[2])
                self.speciesListSorted.append(i[3])
                self.exhibitListSorted.append(i[4])
                self.ageListSorted.append(i[0])
                self.typeListSorted.append(i[1])

            #print(self.nameListSorted)

            for i in range(len(self.sortColumnsTuple)):
                self.selectAnimalTree.insert('', i, values=(self.nameListSorted[i], self.speciesListSorted[i], self.exhibitListSorted[i], self.ageListSorted[i], self.typeListSorted[i]))

            tv.heading(column, command=lambda: \
                self.sortAdminViewAnimals(tv, column, not resort))

        elif (column == "4" and resort == False):

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
            sql = sql + "ORDER BY Age ASC;"
            self.cursor.execute(sql)
            self.sortColumnsTuple = self.cursor.fetchall()

            #print(self.sortColumnsTuple)

            self.nameListSorted = []
            self.speciesListSorted = []
            self.exhibitListSorted = []
            self.ageListSorted = []
            self.typeListSorted = []

            for i in self.sortColumnsTuple:
                self.nameListSorted.append(i[2])
                self.speciesListSorted.append(i[3])
                self.exhibitListSorted.append(i[4])
                self.ageListSorted.append(i[0])
                self.typeListSorted.append(i[1])

            #print(self.nameListSorted)

            for i in range(len(self.sortColumnsTuple)):
                self.selectAnimalTree.insert('', i, values=(self.nameListSorted[i], self.speciesListSorted[i], self.exhibitListSorted[i], self.ageListSorted[i], self.typeListSorted[i]))

            tv.heading(column, command=lambda: \
                self.sortAdminViewAnimals(tv, column, not resort))

        elif (column == "4" and resort == True):

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
            sql = sql + "ORDER BY Age DESC;"
            self.cursor.execute(sql)
            self.sortColumnsTuple = self.cursor.fetchall()

            #print(self.sortColumnsTuple)

            self.nameListSorted = []
            self.speciesListSorted = []
            self.exhibitListSorted = []
            self.ageListSorted = []
            self.typeListSorted = []

            for i in self.sortColumnsTuple:
                self.nameListSorted.append(i[2])
                self.speciesListSorted.append(i[3])
                self.exhibitListSorted.append(i[4])
                self.ageListSorted.append(i[0])
                self.typeListSorted.append(i[1])

            #print(self.nameListSorted)

            for i in range(len(self.sortColumnsTuple)):
                self.selectAnimalTree.insert('', i, values=(self.nameListSorted[i], self.speciesListSorted[i], self.exhibitListSorted[i], self.ageListSorted[i], self.typeListSorted[i]))

            tv.heading(column, command=lambda: \
                self.sortAdminViewAnimals(tv, column, not resort))

        elif (column == "5" and resort == False):

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
            sql = sql + "ORDER BY Type ASC;"
            self.cursor.execute(sql)
            self.sortColumnsTuple = self.cursor.fetchall()

            #print(self.sortColumnsTuple)

            self.nameListSorted = []
            self.speciesListSorted = []
            self.exhibitListSorted = []
            self.ageListSorted = []
            self.typeListSorted = []

            for i in self.sortColumnsTuple:
                self.nameListSorted.append(i[2])
                self.speciesListSorted.append(i[3])
                self.exhibitListSorted.append(i[4])
                self.ageListSorted.append(i[0])
                self.typeListSorted.append(i[1])

            #print(self.nameListSorted)

            for i in range(len(self.sortColumnsTuple)):
                self.selectAnimalTree.insert('', i, values=(self.nameListSorted[i], self.speciesListSorted[i], self.exhibitListSorted[i], self.ageListSorted[i], self.typeListSorted[i]))

            tv.heading(column, command=lambda: \
                self.sortAdminViewAnimals(tv, column, not resort))

        elif (column == "5" and resort == True):

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
            sql = sql + "ORDER BY Type DESC;"
            self.cursor.execute(sql)
            self.sortColumnsTuple = self.cursor.fetchall()

            #print(self.sortColumnsTuple)

            self.nameListSorted = []
            self.speciesListSorted = []
            self.exhibitListSorted = []
            self.ageListSorted = []
            self.typeListSorted = []

            for i in self.sortColumnsTuple:
                self.nameListSorted.append(i[2])
                self.speciesListSorted.append(i[3])
                self.exhibitListSorted.append(i[4])
                self.ageListSorted.append(i[0])
                self.typeListSorted.append(i[1])

            #print(self.nameListSorted)

            for i in range(len(self.sortColumnsTuple)):
                self.selectAnimalTree.insert('', i, values=(self.nameListSorted[i], self.speciesListSorted[i], self.exhibitListSorted[i], self.ageListSorted[i], self.typeListSorted[i]))

            tv.heading(column, command=lambda: \
                self.sortAdminViewAnimals(tv, column, not resort))


    def showAnimalWindowAdminFindAnimalsButtonClicked(self):
        for i in self.selectAnimalTree.get_children():
            self.selectAnimalTree.delete(i)

        # Table is a list of table names"
        attributes = ["Name", "Species", "Type", "Age", "E_Name",]

        # Entry is a list of the filter inputs
        entry = []
        entry.append(str(self.animalNameSV.get()))
        entry.append(str(self.speciesNameSV.get()))
        entry.append(self.typeDefault.get())
        entry.append("")
        entry.append(self.exhibitDefault.get())

        #print(entry)

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


        

    def showAnimalWindowAdminRemoveAnimalWindowButtonClicked(self):
        self.selectedRow = self.selectAnimalTree.selection()[0]
        self.selectedRowItems = self.selectAnimalTree.item(self.selectedRow)['values']

        print(self.selectedRowItems)

        self.animalName = self.selectedRowItems[0]
        self.animalSpecies = self.selectedRowItems[1]
        

        self.cursor.execute("DELETE FROM Animal WHERE Name= %s AND Species= %s",(self.animalName,self.animalSpecies))

        self.selectAnimalTree.delete(self.selectedRow)

    def showAnimalWindowAdminBackButtonClicked(self):
        self.showAnimalWindowAdmin.destroy()
        self.chooseAdminFunctionalityWindow.deiconify()

#-------------------ADMIN VIEW STAFF PAGE------------------------------
    def createViewStaffWindow(self):
        self.viewStaffWindow = Toplevel()
        self.viewStaffWindow.title("Zoo Atlanta")
        self.viewStaffWindow.geometry("800x600")
        self.viewStaffWindow.resizable(0,0)

    def buildViewStaffWindow(self, viewStaffWindow):

        # Title Label
        titleLabel = Label(viewStaffWindow, text = "View Staff", font = "Verdana 16 bold ")
        titleLabel.place(x=350, y=25)

        self.columns = ("1", "2")

        # Table of all the staff members
        self.staffTree = ttk.Treeview(viewStaffWindow, columns=self.columns, selectmode="extended")
        self.staffTree['show'] = "headings"
        self.staffTree.column("1", width = 300, anchor = "center")
        self.staffTree.column("2", width = 300, anchor = "center")

        self.staffTree.heading("1", text = "Username")
        self.staffTree.heading("2", text = "Email")

        self.staffTree.place(x=400, y=200, anchor="center")

        adminShowStaffSort = self.staffTree

        for col in self.columns:
            self.staffTree.heading(col, command=lambda _col=col: \
                self.sortAdminViewStaff(adminShowStaffSort, _col, False))


        self.cursor.execute("SELECT Username, Email FROM User WHERE Type = 'staff'")

        self.viewStaffTuple = self.cursor.fetchall()
        self.usernameList = []
        self.emailList = []


        for i in self.viewStaffTuple:
            self.usernameList.append(i[0])
            self.emailList.append(i[1])

        # Insert data into the treeview
        for i in range(len(self.viewStaffTuple)):
            self.staffTree.insert('', i , values=(self.usernameList[i], self.emailList[i]))

        
        # Back Button
        backButton = Button(viewStaffWindow, text="Back", command=self.viewStaffBackButtonClicked)
        backButton.place(x=10,y=570)

        removeStaffButton = Button(viewStaffWindow, text="Delete Staff Member", command=self.showStaffWindowAdminRemoveStaffButtonClicked)
        removeStaffButton.place(x=670,y=570)

    def sortAdminViewStaff(self, tv, column, resort):
        for i in self.staffTree.get_children():
            self.staffTree.delete(i)

        if (column == "1" and resort == False):
            self.cursor.execute("SELECT Username, Email FROM User WHERE Type = 'staff' ORDER BY Username ASC")

            self.viewStaffTuple = self.cursor.fetchall()
            self.usernameList = []
            self.emailList = []

            for i in self.viewStaffTuple:
                self.usernameList.append(i[0])
                self.emailList.append(i[1])

            # Insert data into the treeview
            for i in range(len(self.viewStaffTuple)):
                self.staffTree.insert('', i , values=(self.usernameList[i], self.emailList[i]))

            tv.heading(column, command=lambda: \
                self.sortAdminViewStaff(tv, column, not resort))

        elif (column == "1" and resort == True):
            self.cursor.execute("SELECT Username, Email FROM User WHERE Type = 'staff' ORDER BY Username DESC")

            self.viewStaffTuple = self.cursor.fetchall()
            self.usernameList = []
            self.emailList = []

            for i in self.viewStaffTuple:
                self.usernameList.append(i[0])
                self.emailList.append(i[1])

            # Insert data into the treeview
            for i in range(len(self.viewStaffTuple)):
                self.staffTree.insert('', i , values=(self.usernameList[i], self.emailList[i]))

            tv.heading(column, command=lambda: \
                self.sortAdminViewStaff(tv, column, not resort))

        if (column == "2" and resort == False):
            self.cursor.execute("SELECT Username, Email FROM User WHERE Type = 'staff' ORDER BY Email ASC")

            self.viewStaffTuple = self.cursor.fetchall()
            self.usernameList = []
            self.emailList = []

            for i in self.viewStaffTuple:
                self.usernameList.append(i[0])
                self.emailList.append(i[1])

            # Insert data into the treeview
            for i in range(len(self.viewStaffTuple)):
                self.staffTree.insert('', i , values=(self.usernameList[i], self.emailList[i]))

            tv.heading(column, command=lambda: \
                self.sortAdminViewStaff(tv, column, not resort))

        if (column == "2" and resort == True):
            self.cursor.execute("SELECT Username, Email FROM User WHERE Type = 'staff' ORDER BY Email DESC")

            self.viewStaffTuple = self.cursor.fetchall()
            self.usernameList = []
            self.emailList = []

            for i in self.viewStaffTuple:
                self.usernameList.append(i[0])
                self.emailList.append(i[1])

            # Insert data into the treeview
            for i in range(len(self.viewStaffTuple)):
                self.staffTree.insert('', i , values=(self.usernameList[i], self.emailList[i]))

            tv.heading(column, command=lambda: \
                self.sortAdminViewStaff(tv, column, not resort))

    def showStaffWindowAdminRemoveStaffButtonClicked(self):

        if not self.staffTree.focus():
            messagebox.showwarning("Error","You haven't selected any Staff.")
            return False

        treeIndexString = self.staffTree.focus()
        valueRemoved = self.staffTree.item(treeIndexString)


        messagebox.showwarning('Remove Staff Member', 'Are you sure?')
        valueslist = list(valueRemoved.values())
        valueslist = valueslist[2]
        uname = valueslist[0]
        eml = valueslist[1]

        self.cursor.execute("DELETE FROM User WHERE Username= %s OR Email = %s AND Type = 'staff'",(uname, eml))

        self.viewStaffWindow.destroy()
        self.createViewStaffWindow()
        self.buildViewStaffWindow(self.viewStaffWindow)

    def viewStaffBackButtonClicked(self):
        self.viewStaffWindow.destroy()
        self.chooseAdminFunctionalityWindow.deiconify()



#-------------------ADMIN VIEW SHOW PAGE------------------------------

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


        self.showNameSV = StringVar()
        showNameEntry = Entry(adminViewShowWindow, textvariable=self.showNameSV, width=20)
        showNameEntry.grid(row=2, column=1, pady=10)

        #populate exhibit menu with sql
        self.cursor.execute("SELECT Name FROM Exhibit")
        self.exhibitTuple = self.cursor.fetchall()
        self.exhibitList = []
        for i in self.exhibitTuple:
            self.exhibitList.append(i[0])

        exhibitLabel = Label(adminViewShowWindow,text = "Exhibit")
        exhibitLabel.grid(row=3,column=0,pady=10)
        self.exhibitDefault = StringVar()
        self.exhibitDefault.set("")
        exhibitMenu = OptionMenu(adminViewShowWindow, self.exhibitDefault, "", *self.exhibitList)
        exhibitMenu.grid(row=3, column=1,pady=10)

        dateLabel=Label(adminViewShowWindow,text="Date")
        dateLabel.grid(row=2,column=2,pady=10)

        self.dateSV = StringVar()
        dateEntry = Entry(adminViewShowWindow, textvariable=self.dateSV, width=20)
        dateEntry.grid(row=2, column=3,pady=10,sticky=W)

        searchButton = Button(adminViewShowWindow, text="Search", command=self.adminViewShowWindowSearchButtonClicked)
        searchButton.grid(row=3, column =2,pady=10)

        self.columns = ("1", "2", "3")

        self.viewShowTree = ttk.Treeview(adminViewShowWindow, columns=self.columns, selectmode = "extended")
        self.viewShowTree['show'] = "headings"
        self.viewShowTree.heading('1', text = "Name")
        self.viewShowTree.heading('2', text = "Exhibit")
        self.viewShowTree.heading('3', text = "Date")
        self.viewShowTree.column('1', width = 200, anchor = "center")
        self.viewShowTree.column('2', width = 200, anchor = "center")
        self.viewShowTree.column('3', width = 200, anchor = "center")
        self.viewShowTree.place(x=20, y=130,width=600)

        adminViewShowTreeSort = self.viewShowTree

        for col in self.columns:
            self.viewShowTree.heading(col, command=lambda _col=col: \
                self.sortAdminViewShows(adminViewShowTreeSort, _col, False))


        self.cursor.execute("SELECT * FROM Performance")

        self.adminViewShowTuple = self.cursor.fetchall()

        self.nameList = []
        self.exhibitList = []
        self.dateList = []

        for i in self.adminViewShowTuple:
            self.nameList.append(i[0])
            self.dateList.append(i[1])
            self.exhibitList.append(i[3])


        for i in range(len(self.adminViewShowTuple)):
            self.viewShowTree.insert('', i, values = (self.nameList[i], self.exhibitList[i], self.dateList[i]))

        removeShowButton = Button(adminViewShowWindow, text="Remove Show", command=self.adminViewShowWindowRemoveButtonClicked)
        removeShowButton.place(x=220, y=400)

        backButton = Button(adminViewShowWindow, text="Back", command=self.adminViewShowWindowBackButtonClicked)
        backButton.place(x=360, y=400)

    def sortAdminViewShows(self, tv, column, resort):
        for i in self.viewShowTree.get_children():
            self.viewShowTree.delete(i)  

        attributes = ['Name', 'Time', 'E_Name']

        #Entry is a list of the filter inputs
        entry = []

        entry.append(str(self.showNameSV.get()))
        entry.append(str(self.dateSV.get()))
        entry.append(str(self.exhibitDefault.get()))

        #print(entry)

        if (column == "1" and resort == False):

            sql = "SELECT * FROM Performance WHERE "

            for i in range(len(entry)):
                if entry[i] != "":
                    sql = sql + attributes[i] + " = '" + entry[i] + "'"
                else:
                    sql = sql + attributes[i] + " LIKE '%'"
            #This is to check if the next box is filled as well so we add an AND statement to make sure all conditions are met. 
                if i < len(entry)-1:
                    sql = sql + " AND "

            sql = sql + "ORDER BY Name ASC;"
            self.cursor.execute(sql)
            self.sortColumnsTuple = self.cursor.fetchall()

            #print(self.sortColumnsTuple)

            self.nameListSorted = []
            self.timeListSorted = []
            self.exhibitListSorted = []

            for i in self.sortColumnsTuple:
                self.nameListSorted.append(i[0])
                self.timeListSorted.append(i[1])
                self.exhibitListSorted.append(i[3])

            #print(self.nameListSorted)

            for i in range(len(self.sortColumnsTuple)):
                self.viewShowTree.insert('', i, values=(self.nameListSorted[i], self.exhibitListSorted[i], self.timeListSorted[i]))

            tv.heading(column, command=lambda: \
                self.sortAdminViewShows(tv, column, not resort))

        elif (column == "1" and resort == True):

            sql = "SELECT * FROM Performance WHERE "

            for i in range(len(entry)):
                if entry[i] != "":
                    sql = sql + attributes[i] + " = '" + entry[i] + "'"
                else:
                    sql = sql + attributes[i] + " LIKE '%'"
            #This is to check if the next box is filled as well so we add an AND statement to make sure all conditions are met. 
                if i < len(entry)-1:
                    sql = sql + " AND "

            sql = sql + "ORDER BY Name DESC;"
            self.cursor.execute(sql)
            self.sortColumnsTuple = self.cursor.fetchall()

            #print(self.sortColumnsTuple)

            self.nameListSorted = []
            self.timeListSorted = []
            self.exhibitListSorted = []

            for i in self.sortColumnsTuple:
                self.nameListSorted.append(i[0])
                self.timeListSorted.append(i[1])
                self.exhibitListSorted.append(i[3])

            #print(self.nameListSorted)

            for i in range(len(self.sortColumnsTuple)):
                self.viewShowTree.insert('', i, values=(self.nameListSorted[i], self.exhibitListSorted[i], self.timeListSorted[i]))

            tv.heading(column, command=lambda: \
                self.sortAdminViewShows(tv, column, not resort))

        elif (column == "2" and resort == False):

            sql = "SELECT * FROM Performance WHERE "

            for i in range(len(entry)):
                if entry[i] != "":
                    sql = sql + attributes[i] + " = '" + entry[i] + "'"
                else:
                    sql = sql + attributes[i] + " LIKE '%'"
            #This is to check if the next box is filled as well so we add an AND statement to make sure all conditions are met. 
                if i < len(entry)-1:
                    sql = sql + " AND "

            sql = sql + "ORDER BY E_Name ASC;"
            self.cursor.execute(sql)
            self.sortColumnsTuple = self.cursor.fetchall()

            #print(self.sortColumnsTuple)

            self.nameListSorted = []
            self.timeListSorted = []
            self.exhibitListSorted = []

            for i in self.sortColumnsTuple:
                self.nameListSorted.append(i[0])
                self.timeListSorted.append(i[1])
                self.exhibitListSorted.append(i[3])

            #print(self.nameListSorted)

            for i in range(len(self.sortColumnsTuple)):
                self.viewShowTree.insert('', i, values=(self.nameListSorted[i], self.exhibitListSorted[i], self.timeListSorted[i]))

            tv.heading(column, command=lambda: \
                self.sortAdminViewShows(tv, column, not resort))

        elif (column == "2" and resort == True):

            sql = "SELECT * FROM Performance WHERE "

            for i in range(len(entry)):
                if entry[i] != "":
                    sql = sql + attributes[i] + " = '" + entry[i] + "'"
                else:
                    sql = sql + attributes[i] + " LIKE '%'"
            #This is to check if the next box is filled as well so we add an AND statement to make sure all conditions are met. 
                if i < len(entry)-1:
                    sql = sql + " AND "

            sql = sql + "ORDER BY E_Name DESC;"
            self.cursor.execute(sql)
            self.sortColumnsTuple = self.cursor.fetchall()

            #print(self.sortColumnsTuple)

            self.nameListSorted = []
            self.timeListSorted = []
            self.exhibitListSorted = []

            for i in self.sortColumnsTuple:
                self.nameListSorted.append(i[0])
                self.timeListSorted.append(i[1])
                self.exhibitListSorted.append(i[3])

            #print(self.nameListSorted)

            for i in range(len(self.sortColumnsTuple)):
                self.viewShowTree.insert('', i, values=(self.nameListSorted[i], self.exhibitListSorted[i], self.timeListSorted[i]))

            tv.heading(column, command=lambda: \
                self.sortAdminViewShows(tv, column, not resort))

        elif (column == "3" and resort == False):

            sql = "SELECT * FROM Performance WHERE "

            for i in range(len(entry)):
                if entry[i] != "":
                    sql = sql + attributes[i] + " = '" + entry[i] + "'"
                else:
                    sql = sql + attributes[i] + " LIKE '%'"
            #This is to check if the next box is filled as well so we add an AND statement to make sure all conditions are met. 
                if i < len(entry)-1:
                    sql = sql + " AND "

            sql = sql + "ORDER BY Time ASC;"
            self.cursor.execute(sql)
            self.sortColumnsTuple = self.cursor.fetchall()

            #print(self.sortColumnsTuple)

            self.nameListSorted = []
            self.timeListSorted = []
            self.exhibitListSorted = []

            for i in self.sortColumnsTuple:
                self.nameListSorted.append(i[0])
                self.timeListSorted.append(i[1])
                self.exhibitListSorted.append(i[3])

            #print(self.nameListSorted)

            for i in range(len(self.sortColumnsTuple)):
                self.viewShowTree.insert('', i, values=(self.nameListSorted[i], self.exhibitListSorted[i], self.timeListSorted[i]))

            tv.heading(column, command=lambda: \
                self.sortAdminViewShows(tv, column, not resort))

        elif (column == "3" and resort == True):

            sql = "SELECT * FROM Performance WHERE "

            for i in range(len(entry)):
                if entry[i] != "":
                    sql = sql + attributes[i] + " = '" + entry[i] + "'"
                else:
                    sql = sql + attributes[i] + " LIKE '%'"
            #This is to check if the next box is filled as well so we add an AND statement to make sure all conditions are met. 
                if i < len(entry)-1:
                    sql = sql + " AND "

            sql = sql + "ORDER BY Time DESC;"
            self.cursor.execute(sql)
            self.sortColumnsTuple = self.cursor.fetchall()

            #print(self.sortColumnsTuple)

            self.nameListSorted = []
            self.timeListSorted = []
            self.exhibitListSorted = []

            for i in self.sortColumnsTuple:
                self.nameListSorted.append(i[0])
                self.timeListSorted.append(i[1])
                self.exhibitListSorted.append(i[3])

            #print(self.nameListSorted)

            for i in range(len(self.sortColumnsTuple)):
                self.viewShowTree.insert('', i, values=(self.nameListSorted[i], self.exhibitListSorted[i], self.timeListSorted[i]))

            tv.heading(column, command=lambda: \
                self.sortAdminViewShows(tv, column, not resort))

    def adminViewShowWindowSearchButtonClicked(self):
        for i in self.viewShowTree.get_children():
            self.viewShowTree.delete(i)

        # Table is a list of table names"
        attributes = ["Name", "Time", "Host", "E_Name"]

        #date validation
        self.dateTime = self.dateSV.get()

        if self.dateTime != "":
            try:
                datetime.strptime(self.dateTime, '%Y-%m-%d %I:%M%p')
            except ValueError:
                messagebox.showwarning("date needs to be in format yyyy-mm-dd and time needs to be in format hh:mmAM/PM")
                return False
        if self.dateTime != "":
            self.dateTimeObject = datetime.strptime(self.dateTime, '%Y-%m-%d %I:%M%p')
            self.dateTimeObject = str(self.dateTimeObject)
        else:
            self.dateTimeObject = ""

        # Entry is a list of the filter inputs
        entry = []
        entry.append(str(self.showNameSV.get()))
        entry.append(self.dateTimeObject)
        entry.append("")
        entry.append(self.exhibitDefault.get())

        #print(entry)

        sql = "SELECT * FROM Performance WHERE "

        for i in range(len(entry)):
            if entry[i] != "":
                sql = sql + attributes[i] + " = " + "'" + entry[i] + "'"
            else:
                sql = sql + attributes[i] + " LIKE '%'"
        #This is to check if the next box is filled as well so we add an AND statement to make sure all conditions are met. 
            if i < len(entry)-1:
                sql = sql + " AND "
        #end of statement
        sql = sql + ";"

        print(sql)

        # print(sql)
        self.cursor.execute(sql)
        self.showResults = self.cursor.fetchall()
        # print(self.animalResults)

        self.showNameList = []
        self.dateList = []
        self.exhibitNameList = []

        for i in self.showResults:
            self.showNameList.append(i[0])
            self.dateList.append(i[1])
            self.exhibitNameList.append(i[3])
        
        for i in range(len(self.showResults)):
            self.viewShowTree.insert('', i , values=(self.showNameList[i], self.exhibitNameList[i], self.dateList[i]))



    def adminViewShowWindowRemoveButtonClicked(self):
        self.selectedRow = self.viewShowTree.selection()[0]
        self.selectedRowItems = self.viewShowTree.item(self.selectedRow)['values']

        self.showName = self.selectedRowItems[0]
        self.dateTime = self.selectedRowItems[2]
        self.cursor.execute("DELETE FROM Performance WHERE Name= %s AND Time= %s",(self.showName,self.dateTime))

        self.viewShowTree.delete(self.selectedRow)


    def adminViewShowWindowBackButtonClicked(self):
        self.adminViewShowWindow.destroy()
        self.chooseAdminFunctionalityWindow.deiconify()

#--------------------Staff Functionality Window--------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def createStaffChooseFunctionalityWindow(self):
            # Create blank chooseFunctionalityWindow
            self.chooseStaffFunctionalityWindow = Toplevel()
            self.chooseStaffFunctionalityWindow.title("Zoo Atlanta")
            self.chooseStaffFunctionalityWindow.geometry("800x600")
            self.chooseStaffFunctionalityWindow.resizable(0,0)

    def buildStaffChooseFunctionalityWindow(self,chooseStaffFunctionalityWindow):
        # Add component to chooseFunctionalityWindow

        #Choose Functionality Label
        chooseFunctionalityLabel = Label(chooseStaffFunctionalityWindow, text="Staff Functions",font = "Verdana 16 bold ")
        # chooseFunctionalityLabel.grid(row=1, column=1, sticky=W+E)
        chooseFunctionalityLabel.place(x=400, y = 25, anchor="center")

        # Search Exhibits Label
        searchAnimalsLabel = Label(chooseStaffFunctionalityWindow, text="Search Animals", font = "Verdana 13")
        # searchAnimalsLabel.grid(row=2, column=1)
        searchAnimalsLabel.bind("<ButtonPress-1>", self.chooseStaffFunctionalityWindowSearchAnimalsLabelClicked)
        searchAnimalsLabel.place(x=400, y = 100, anchor="center")

        # View Show History Label
        viewAssignedShows = Label(chooseStaffFunctionalityWindow, text="View Your Assigned Shows", font = "Verdana 13")
        # viewReviewLabel.grid(row=6,column=1)
        viewAssignedShows.bind("<ButtonPress-1>", self.chooseStaffFunctionalityWindowViewAssignedShowsLabelClicked)
        viewAssignedShows.place(x=400, y = 150, anchor="center")

        # Log Out Buttons

        logOutButton = Button(chooseStaffFunctionalityWindow, text="Log out", command=self.chooseStaffFunctionalityWindowLogOutButtonClicked)
        logOutButton.grid(row=8, column=2,sticky=E)
        logOutButton.place(x = 720, y = 570)


    def chooseStaffFunctionalityWindowSearchAnimalsLabelClicked(self,event):
        # Hide Choose Functionality Window.
        self.createStaffSearchAnimalsWindow()
        self.buildStaffSearchAnimalsWindow(self.searchStaffAnimalsWindow)
        self.chooseStaffFunctionalityWindow.withdraw()

    def chooseStaffFunctionalityWindowViewAssignedShowsLabelClicked(self,event):
        self.createStaffShowHistoryWindow()
        self.buildStaffShowHistoryWindow(self.staffShowHistoryWindow)
        self.chooseStaffFunctionalityWindow.withdraw()

    def chooseStaffFunctionalityWindowLogOutButtonClicked(self):
        # Click Log Out Buttion on Choose Functionality Window:
        # Destroy Choose Functionality Window
        # Display Login Window
        self.chooseStaffFunctionalityWindow.destroy()
        self.loginWindow.deiconify()


#-------------------STAFF PAGES------------------------------



#-------------------STAFF SEARCH ANIMALS------------------------------
    def createStaffSearchAnimalsWindow(self):
        # Create blank Search Animal Window
        self.searchStaffAnimalsWindow=Toplevel()
        self.searchStaffAnimalsWindow.title("Zoo Atlanta")

    def buildStaffSearchAnimalsWindow(self,searchStaffAnimalsWindow):

        # Title Label
        titleLabel= Label(searchStaffAnimalsWindow,text = "Search Animals", font = "Verdana 16 bold ")
        titleLabel.grid(row=1,column=2,sticky=W+E)

        
        nameLabel = Label(searchStaffAnimalsWindow,text = "Name")
        nameLabel.grid(row=2, column=0)


        self.animalNameSV = StringVar()
        animalNameEntry = Entry(searchStaffAnimalsWindow, textvariable=self.animalNameSV, width=20)
        animalNameEntry.grid(row=2, column=1)

        speciesLabel = Label(searchStaffAnimalsWindow,text = "Species")
        speciesLabel.grid(row=3,column=0)
        self.speciesNameSV = StringVar()
        speciesNameEntry = Entry(searchStaffAnimalsWindow, textvariable=self.speciesNameSV, width=20)
        speciesNameEntry.grid(row=3, column=1)

        #populate exhibit menu with sql
        self.cursor.execute("SELECT Name FROM Exhibit")
        self.exhibitTuple = self.cursor.fetchall()
        self.exhibitList = []
        for i in self.exhibitTuple:
            self.exhibitList.append(i[0])


        exhibitLabel = Label(searchStaffAnimalsWindow,text = "Exhibit")
        exhibitLabel.grid(row=4,column=0)
        self.exhibitDefault = StringVar()
        self.exhibitDefault.set("")
        exhibitMenu = OptionMenu(searchStaffAnimalsWindow, self.exhibitDefault,"", *self.exhibitList)
        exhibitMenu.grid(row=4, column=1)

        minLabel=Label(searchStaffAnimalsWindow,text="Min")
        minLabel.grid(row=2,column=3, sticky=W)

        maxLabel=Label(searchStaffAnimalsWindow,text="Max")
        maxLabel.grid(row=2,column=4, sticky=W)

        ageLabel = Label(searchStaffAnimalsWindow,text = "Age")
        ageLabel.grid(row=3,column=2)

        self.minSpinBox = Spinbox(searchStaffAnimalsWindow, from_=0, to=10000, width=5)
        self.minSpinBox.grid(row=3, column=3,pady=10,sticky=W)

        self.maxSpinBox = Spinbox(searchStaffAnimalsWindow, from_=0, to=10000, width=5)
        self.maxSpinBox.grid(row=3, column=4,pady=10,sticky=W)
        
        typeLabel = Label(searchStaffAnimalsWindow,text = "Type")
        typeLabel.grid(row=4, column=2)
        # Name Entry
        self.typeDefault = StringVar()
        self.typeDefault.set("")
        typeMenu = OptionMenu(searchStaffAnimalsWindow, self.typeDefault,"", "mammal", "bird", "amphibian", "reptile", "fish", "invertebrate")
        typeMenu.grid(row=4, column=3, sticky=W)

        self.columns = ("1", "2", "3", "4","5")
       
        self.selectAnimalTree = ttk.Treeview(searchStaffAnimalsWindow, columns=self.columns)
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

        self.selectAnimalTree.bind("<Double-1>", self.searchStaffAnimalsWindowAnimalClicked)

        self.selectAnimalTree.grid(row=5, columnspan=4, sticky = 'nsew')

        selectAnimalTreeSort = self.selectAnimalTree

        for col in self.columns:
            self.selectAnimalTree.heading(col, command=lambda _col=col: \
                self.sortColumnsClicked(selectAnimalTreeSort, _col, False))


        self.cursor.execute("SELECT * FROM Animal")

        self.staffSearchAnimalTuple = self.cursor.fetchall()
        self.nameList = []
        self.speciesList = []
        self.exhibitList = []
        self.ageList = []
        self.typeList = []

        for i in self.staffSearchAnimalTuple:
            self.nameList.append(i[2])
            self.speciesList.append(i[3])
            self.exhibitList.append(i[4])
            self.ageList.append(i[0])
            self.typeList.append(i[1])

        for i in range(len(self.staffSearchAnimalTuple)):
            self.selectAnimalTree.insert('', i, values=(self.nameList[i], self.speciesList[i], self.exhibitList[i], self.ageList[i], self.typeList[i]))


        findAnimalsButton = Button(searchStaffAnimalsWindow, text="Find Animals", command=self.searchStaffAnimalsWindowFindAnimalsButtonClicked)
        findAnimalsButton.grid(row=6,column=3)

        backButton = Button(searchStaffAnimalsWindow, text="Back", command=self.searchStaffAnimalsWindowBackButtonClicked)
        backButton.grid(row=6,column=1)

    #sort functionality
    def sortColumnsClicked(self, tv, column, resort):
        for i in self.selectAnimalTree.get_children():
            self.selectAnimalTree.delete(i)  

        attributes = ["Name", "Species", "Type", "Age", "E_Name",]

        # Entry is a list of the filter inputs
        entry = []
        entry.append(str(self.animalNameSV.get()))
        entry.append(str(self.speciesNameSV.get()))
        entry.append(self.typeDefault.get())
        entry.append("")
        entry.append(self.exhibitDefault.get())

        #print(entry)

        

        if (column == "1" and resort == False):

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
            sql = sql + "ORDER BY Name ASC;"
            self.cursor.execute(sql)
            self.sortColumnsTuple = self.cursor.fetchall()

            #print(self.sortColumnsTuple)

            self.nameListSorted = []
            self.speciesListSorted = []
            self.exhibitListSorted = []
            self.ageListSorted = []
            self.typeListSorted = []

            for i in self.sortColumnsTuple:
                self.nameListSorted.append(i[2])
                self.speciesListSorted.append(i[3])
                self.exhibitListSorted.append(i[4])
                self.ageListSorted.append(i[0])
                self.typeListSorted.append(i[1])

            #print(self.nameListSorted)

            for i in range(len(self.sortColumnsTuple)):
                self.selectAnimalTree.insert('', i, values=(self.nameListSorted[i], self.speciesListSorted[i], self.exhibitListSorted[i], self.ageListSorted[i], self.typeListSorted[i]))

            tv.heading(column, command=lambda: \
                self.sortColumnsClicked(tv, column, not resort))

        elif (column == "1" and resort == True):
            #print("reversed")
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
            sql = sql + "ORDER BY Name DESC;"

            self.cursor.execute(sql)

            self.sortColumnsTuple = self.cursor.fetchall()

            #print(self.sortColumnsTuple)

            self.nameListSorted = []
            self.speciesListSorted = []
            self.exhibitListSorted = []
            self.ageListSorted = []
            self.typeListSorted = []

            for i in self.sortColumnsTuple:
                self.nameListSorted.append(i[2])
                self.speciesListSorted.append(i[3])
                self.exhibitListSorted.append(i[4])
                self.ageListSorted.append(i[0])
                self.typeListSorted.append(i[1])

            #print(self.nameListSorted)

            for i in range(len(self.sortColumnsTuple)):
                self.selectAnimalTree.insert('', i, values=(self.nameListSorted[i], self.speciesListSorted[i], self.exhibitListSorted[i], self.ageListSorted[i], self.typeListSorted[i]))

            tv.heading(column, command=lambda: \
                self.sortColumnsClicked(tv, column, not resort))
        elif (column == "2" and resort == False):
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
            sql = sql + "ORDER BY Species ASC;"

            self.cursor.execute(sql)

            self.sortColumnsTuple = self.cursor.fetchall()

            #print(self.sortColumnsTuple)

            self.nameListSorted = []
            self.speciesListSorted = []
            self.exhibitListSorted = []
            self.ageListSorted = []
            self.typeListSorted = []

            for i in self.sortColumnsTuple:
                self.nameListSorted.append(i[2])
                self.speciesListSorted.append(i[3])
                self.exhibitListSorted.append(i[4])
                self.ageListSorted.append(i[0])
                self.typeListSorted.append(i[1])

            #print(self.nameListSorted)

            for i in range(len(self.sortColumnsTuple)):
                self.selectAnimalTree.insert('', i, values=(self.nameListSorted[i], self.speciesListSorted[i], self.exhibitListSorted[i], self.ageListSorted[i], self.typeListSorted[i]))

            tv.heading(column, command=lambda: \
                self.sortColumnsClicked(tv, column, not resort))
        elif (column == "2" and resort == True): 
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
            sql = sql + "ORDER BY Species DESC;"

            self.cursor.execute(sql)

            self.sortColumnsTuple = self.cursor.fetchall()

            #print(self.sortColumnsTuple)

            self.nameListSorted = []
            self.speciesListSorted = []
            self.exhibitListSorted = []
            self.ageListSorted = []
            self.typeListSorted = []

            for i in self.sortColumnsTuple:
                self.nameListSorted.append(i[2])
                self.speciesListSorted.append(i[3])
                self.exhibitListSorted.append(i[4])
                self.ageListSorted.append(i[0])
                self.typeListSorted.append(i[1])

            #print(self.nameListSorted)

            for i in range(len(self.sortColumnsTuple)):
                self.selectAnimalTree.insert('', i, values=(self.nameListSorted[i], self.speciesListSorted[i], self.exhibitListSorted[i], self.ageListSorted[i], self.typeListSorted[i]))

            tv.heading(column, command=lambda: \
                self.sortColumnsClicked(tv, column, not resort))

        elif (column == "3" and resort == False):
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
            sql = sql + "ORDER BY E_Name ASC;"

            self.cursor.execute(sql)

            self.sortColumnsTuple = self.cursor.fetchall()

            #print(self.sortColumnsTuple)

            self.nameListSorted = []
            self.speciesListSorted = []
            self.exhibitListSorted = []
            self.ageListSorted = []
            self.typeListSorted = []

            for i in self.sortColumnsTuple:
                self.nameListSorted.append(i[2])
                self.speciesListSorted.append(i[3])
                self.exhibitListSorted.append(i[4])
                self.ageListSorted.append(i[0])
                self.typeListSorted.append(i[1])

            #print(self.nameListSorted)

            for i in range(len(self.sortColumnsTuple)):
                self.selectAnimalTree.insert('', i, values=(self.nameListSorted[i], self.speciesListSorted[i], self.exhibitListSorted[i], self.ageListSorted[i], self.typeListSorted[i]))

            tv.heading(column, command=lambda: \
                self.sortColumnsClicked(tv, column, not resort))
        elif (column == "3" and resort == True): 
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
            sql = sql + "ORDER BY E_Name DESC;"

            self.cursor.execute(sql)

            self.sortColumnsTuple = self.cursor.fetchall()

            #print(self.sortColumnsTuple)

            self.nameListSorted = []
            self.speciesListSorted = []
            self.exhibitListSorted = []
            self.ageListSorted = []
            self.typeListSorted = []

            for i in self.sortColumnsTuple:
                self.nameListSorted.append(i[2])
                self.speciesListSorted.append(i[3])
                self.exhibitListSorted.append(i[4])
                self.ageListSorted.append(i[0])
                self.typeListSorted.append(i[1])

            #print(self.nameListSorted)

            for i in range(len(self.sortColumnsTuple)):
                self.selectAnimalTree.insert('', i, values=(self.nameListSorted[i], self.speciesListSorted[i], self.exhibitListSorted[i], self.ageListSorted[i], self.typeListSorted[i]))

            tv.heading(column, command=lambda: \
                self.sortColumnsClicked(tv, column, not resort))

        elif (column == "4" and resort == False):
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
            sql = sql + "ORDER BY Age ASC;"

            self.cursor.execute(sql)

            self.sortColumnsTuple = self.cursor.fetchall()

            #print(self.sortColumnsTuple)

            self.nameListSorted = []
            self.speciesListSorted = []
            self.exhibitListSorted = []
            self.ageListSorted = []
            self.typeListSorted = []

            for i in self.sortColumnsTuple:
                self.nameListSorted.append(i[2])
                self.speciesListSorted.append(i[3])
                self.exhibitListSorted.append(i[4])
                self.ageListSorted.append(i[0])
                self.typeListSorted.append(i[1])

            #print(self.nameListSorted)

            for i in range(len(self.sortColumnsTuple)):
                self.selectAnimalTree.insert('', i, values=(self.nameListSorted[i], self.speciesListSorted[i], self.exhibitListSorted[i], self.ageListSorted[i], self.typeListSorted[i]))

            tv.heading(column, command=lambda: \
                self.sortColumnsClicked(tv, column, not resort))
        elif (column == "4" and resort == True): 
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
            sql = sql + "ORDER BY Age DESC;"

            self.cursor.execute(sql)

            self.sortColumnsTuple = self.cursor.fetchall()

            #print(self.sortColumnsTuple)

            self.nameListSorted = []
            self.speciesListSorted = []
            self.exhibitListSorted = []
            self.ageListSorted = []
            self.typeListSorted = []

            for i in self.sortColumnsTuple:
                self.nameListSorted.append(i[2])
                self.speciesListSorted.append(i[3])
                self.exhibitListSorted.append(i[4])
                self.ageListSorted.append(i[0])
                self.typeListSorted.append(i[1])

            #print(self.nameListSorted)

            for i in range(len(self.sortColumnsTuple)):
                self.selectAnimalTree.insert('', i, values=(self.nameListSorted[i], self.speciesListSorted[i], self.exhibitListSorted[i], self.ageListSorted[i], self.typeListSorted[i]))

            tv.heading(column, command=lambda: \
                self.sortColumnsClicked(tv, column, not resort))

        elif (column == "5" and resort == False):
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
            sql = sql + "ORDER BY Type ASC;"

            self.cursor.execute(sql)

            self.sortColumnsTuple = self.cursor.fetchall()

            #print(self.sortColumnsTuple)

            self.nameListSorted = []
            self.speciesListSorted = []
            self.exhibitListSorted = []
            self.ageListSorted = []
            self.typeListSorted = []

            for i in self.sortColumnsTuple:
                self.nameListSorted.append(i[2])
                self.speciesListSorted.append(i[3])
                self.exhibitListSorted.append(i[4])
                self.ageListSorted.append(i[0])
                self.typeListSorted.append(i[1])

            #print(self.nameListSorted)

            for i in range(len(self.sortColumnsTuple)):
                self.selectAnimalTree.insert('', i, values=(self.nameListSorted[i], self.speciesListSorted[i], self.exhibitListSorted[i], self.ageListSorted[i], self.typeListSorted[i]))

            tv.heading(column, command=lambda: \
                self.sortColumnsClicked(tv, column, not resort))
        elif (column == "5" and resort == True): 
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
            sql = sql + "ORDER BY Type DESC;"

            self.cursor.execute(sql)

            self.sortColumnsTuple = self.cursor.fetchall()

            #print(self.sortColumnsTuple)

            self.nameListSorted = []
            self.speciesListSorted = []
            self.exhibitListSorted = []
            self.ageListSorted = []
            self.typeListSorted = []

            for i in self.sortColumnsTuple:
                self.nameListSorted.append(i[2])
                self.speciesListSorted.append(i[3])
                self.exhibitListSorted.append(i[4])
                self.ageListSorted.append(i[0])
                self.typeListSorted.append(i[1])

            #print(self.nameListSorted)

            for i in range(len(self.sortColumnsTuple)):
                self.selectAnimalTree.insert('', i, values=(self.nameListSorted[i], self.speciesListSorted[i], self.exhibitListSorted[i], self.ageListSorted[i], self.typeListSorted[i]))

            tv.heading(column, command=lambda: \
                self.sortColumnsClicked(tv, column, not resort))



    def searchStaffAnimalsWindowAnimalClicked(self, event):
    
        self.searchStaffAnimalsWindow.withdraw()
        self.createSearchAnimalCareWindow()
        self.selectedRow = self.selectAnimalTree.selection()[0]
    
        self.selectedRowItems = self.selectAnimalTree.item(self.selectedRow)['values']

        self.animalName = self.selectedRowItems[0]
        self.animalSpecies = self.selectedRowItems[1]
        self.animalExhibit = self.selectedRowItems[2]
        self.animalAge = self.selectedRowItems[3]
        self.animalType = self.selectedRowItems[4]

        self.buildSearchAnimalCareWindow(self.searchAnimalCareWindow, self.animalName, self.animalSpecies, self.animalExhibit, self.animalAge, self.animalType)


    def searchStaffAnimalsWindowFindAnimalsButtonClicked(self):
        for i in self.selectAnimalTree.get_children():
            self.selectAnimalTree.delete(i)  

        # Table is a list of table names"
        attributes = ["Name", "Species", "Type", "Age", "E_Name",]

        # Entry is a list of the filter inputs
        entry = []
        entry.append(str(self.animalNameSV.get()))
        entry.append(str(self.speciesNameSV.get()))
        entry.append(self.typeDefault.get())
        entry.append("")
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

    def  searchStaffAnimalsWindowBackButtonClicked(self):
        self.searchStaffAnimalsWindow.withdraw()
        self.chooseStaffFunctionalityWindow.deiconify()
        # import staffFunctionality

#-------------------STAFF ANIMAL CARE------------------------------

    def createSearchAnimalCareWindow(self):
        # Create blank Search Animal Window
        self.searchAnimalCareWindow=Toplevel()
        self.searchAnimalCareWindow.title("Zoo Atlanta")
        self.searchAnimalCareWindow.geometry("600x600")

    def buildSearchAnimalCareWindow(self,searchAnimalCareWindow, name, species, exhibit, age, animalType):

 
        titleLabel= Label(searchAnimalCareWindow,text = "Animal Detail", font = "Verdana 16 bold ")
        titleLabel.grid(row=1,column=1,sticky=W+E,pady=10)

        self.animalCareName = name

        nameLabel = Label(searchAnimalCareWindow,text = "Name:" + " " + self.animalCareName)
        nameLabel.grid(row=2, column=0,pady=10)

        self.animalCareSpecies = species

        speciesLabel = Label(searchAnimalCareWindow, text="Species:" + " " + self.animalCareSpecies)
        speciesLabel.grid(row=2, column=1,pady=10)

        self.animalCareAge = str(age)
        
        ageLabel = Label(searchAnimalCareWindow,text = "Age:" + " " + self.animalCareAge)
        ageLabel.grid(row=2,column=2,pady=10)

        self.animalCareExhibit = exhibit

        exhibitLabel = Label(searchAnimalCareWindow,text = "Exhibit:" + " " + self.animalCareExhibit)
        exhibitLabel.grid(row=3,column=0,pady=10)

        self.animalCareType = animalType

        typeLabel = Label(searchAnimalCareWindow,text = "Type:" + " " + self.animalCareType)
        typeLabel.grid(row=3,column=1,pady=10)


        self.animalCareNotes = StringVar()
        animalCareEntry = Entry(searchAnimalCareWindow, textvariable=self.animalCareNotes, width=20)
        animalCareEntry.grid(row=4, column=0,pady=10, padx=10)

        logCareButton = Button(searchAnimalCareWindow, text="Log Notes", command=self.logAnimalNotesButtonClicked)
        logCareButton.grid(row=4,column=1,pady=10)

        self.columns = ("1", "2", "3")
        
        self.selectAnimalTree = ttk.Treeview(searchAnimalCareWindow, columns=self.columns, selectmode = "extended")
        self.selectAnimalTree['show'] = "headings"
        self.selectAnimalTree.heading('1', text = "Staff Member")
        self.selectAnimalTree.heading('2', text = "Note")
        self.selectAnimalTree.heading('3', text = "Time")
        self.selectAnimalTree.column('1', width = 150, anchor = "center")
        self.selectAnimalTree.column('2', width = 150, anchor = "center")
        self.selectAnimalTree.column('3', width = 150, anchor = "center")
        self.selectAnimalTree.place(x=20, y=200,width=450)

        staffAnimalCareSort = self.selectAnimalTree

        for col in self.columns:
            self.selectAnimalTree.heading(col, command=lambda _col=col: \
                self.sortStaffAnimalCare(staffAnimalCareSort, _col, False))

        self.cursor.execute("SELECT U_Name, Notes, Time FROM Care_Log JOIN Animal ON Care_Log.Anim_Name = Animal.Name WHERE Care_Log.Anim_Name = %s AND Care_Log.Species = %s", (self.animalName, self.animalSpecies))
        self.animalCareTuple = self.cursor.fetchall()

        self.staffMemberList = []
        self.noteList = []
        self.dateTimeList = []

        for i in self.animalCareTuple:
            self.staffMemberList.append(i[0])
            self.noteList.append(i[1])
            self.dateTimeList.append(i[2])

        for i in range(len(self.animalCareTuple)):
            self.selectAnimalTree.insert('', i, values=(self.staffMemberList[i], self.noteList[i], self.dateTimeList[i]))

        backButton = Button(searchAnimalCareWindow, text="Back", command=self.searchAnimalCareWindowBackButtonClicked)
        backButton.place(x=240,y=440)

    def sortStaffAnimalCare(self, tv, column, resort):
        for i in self.selectAnimalTree.get_children():
            self.selectAnimalTree.delete(i)

        if (column == "1" and resort == False):

            self.cursor.execute("SELECT U_Name, Notes, Time FROM Care_Log JOIN Animal ON Care_Log.Anim_Name = Animal.Name WHERE Care_Log.Anim_Name = %s AND Care_Log.Species = %s ORDER BY U_Name ASC", (self.animalName, self.animalSpecies))
            self.animalCareTuple = self.cursor.fetchall()

            self.staffMemberList = []
            self.noteList = []
            self.dateTimeList = []

            for i in self.animalCareTuple:
                self.staffMemberList.append(i[0])
                self.noteList.append(i[1])
                self.dateTimeList.append(i[2])

            for i in range(len(self.animalCareTuple)):
                self.selectAnimalTree.insert('', i, values=(self.staffMemberList[i], self.noteList[i], self.dateTimeList[i]))

            tv.heading(column, command=lambda: \
                self.sortStaffAnimalCare(tv, column, not resort))

        elif (column == "1" and resort == True):

            self.cursor.execute("SELECT U_Name, Notes, Time FROM Care_Log JOIN Animal ON Care_Log.Anim_Name = Animal.Name WHERE Care_Log.Anim_Name = %s AND Care_Log.Species = %s ORDER BY U_Name DESC", (self.animalName, self.animalSpecies))
            self.animalCareTuple = self.cursor.fetchall()

            self.staffMemberList = []
            self.noteList = []
            self.dateTimeList = []

            for i in self.animalCareTuple:
                self.staffMemberList.append(i[0])
                self.noteList.append(i[1])
                self.dateTimeList.append(i[2])

            for i in range(len(self.animalCareTuple)):
                self.selectAnimalTree.insert('', i, values=(self.staffMemberList[i], self.noteList[i], self.dateTimeList[i]))

            tv.heading(column, command=lambda: \
                self.sortStaffAnimalCare(tv, column, not resort))
        elif (column == "2" and resort == False):

            self.cursor.execute("SELECT U_Name, Notes, Time FROM Care_Log JOIN Animal ON Care_Log.Anim_Name = Animal.Name WHERE Care_Log.Anim_Name = %s AND Care_Log.Species = %s ORDER BY Notes ASC", (self.animalName, self.animalSpecies))
            self.animalCareTuple = self.cursor.fetchall()

            self.staffMemberList = []
            self.noteList = []
            self.dateTimeList = []

            for i in self.animalCareTuple:
                self.staffMemberList.append(i[0])
                self.noteList.append(i[1])
                self.dateTimeList.append(i[2])

            for i in range(len(self.animalCareTuple)):
                self.selectAnimalTree.insert('', i, values=(self.staffMemberList[i], self.noteList[i], self.dateTimeList[i]))

            tv.heading(column, command=lambda: \
                self.sortStaffAnimalCare(tv, column, not resort))

        elif (column == "2" and resort == True):

            self.cursor.execute("SELECT U_Name, Notes, Time FROM Care_Log JOIN Animal ON Care_Log.Anim_Name = Animal.Name WHERE Care_Log.Anim_Name = %s AND Care_Log.Species = %s ORDER BY Notes DESC", (self.animalName, self.animalSpecies))
            self.animalCareTuple = self.cursor.fetchall()

            self.staffMemberList = []
            self.noteList = []
            self.dateTimeList = []

            for i in self.animalCareTuple:
                self.staffMemberList.append(i[0])
                self.noteList.append(i[1])
                self.dateTimeList.append(i[2])

            for i in range(len(self.animalCareTuple)):
                self.selectAnimalTree.insert('', i, values=(self.staffMemberList[i], self.noteList[i], self.dateTimeList[i]))

            tv.heading(column, command=lambda: \
                self.sortStaffAnimalCare(tv, column, not resort))

        elif (column == "3" and resort == False):

            self.cursor.execute("SELECT U_Name, Notes, Time FROM Care_Log JOIN Animal ON Care_Log.Anim_Name = Animal.Name WHERE Care_Log.Anim_Name = %s AND Care_Log.Species = %s ORDER BY Time ASC", (self.animalName, self.animalSpecies))
            self.animalCareTuple = self.cursor.fetchall()

            self.staffMemberList = []
            self.noteList = []
            self.dateTimeList = []

            for i in self.animalCareTuple:
                self.staffMemberList.append(i[0])
                self.noteList.append(i[1])
                self.dateTimeList.append(i[2])

            for i in range(len(self.animalCareTuple)):
                self.selectAnimalTree.insert('', i, values=(self.staffMemberList[i], self.noteList[i], self.dateTimeList[i]))

            tv.heading(column, command=lambda: \
                self.sortStaffAnimalCare(tv, column, not resort))

        elif (column == "3" and resort == True):

            self.cursor.execute("SELECT U_Name, Notes, Time FROM Care_Log JOIN Animal ON Care_Log.Anim_Name = Animal.Name WHERE Care_Log.Anim_Name = %s AND Care_Log.Species = %s ORDER BY Time DESC", (self.animalName, self.animalSpecies))
            self.animalCareTuple = self.cursor.fetchall()

            self.staffMemberList = []
            self.noteList = []
            self.dateTimeList = []

            for i in self.animalCareTuple:
                self.staffMemberList.append(i[0])
                self.noteList.append(i[1])
                self.dateTimeList.append(i[2])

            for i in range(len(self.animalCareTuple)):
                self.selectAnimalTree.insert('', i, values=(self.staffMemberList[i], self.noteList[i], self.dateTimeList[i]))

            tv.heading(column, command=lambda: \
                self.sortStaffAnimalCare(tv, column, not resort))


    def logAnimalNotesButtonClicked(self):
        self.staffName = self.loginUsername.get()
        self.animalCareLogNotes = self.animalCareNotes.get()
        self.animalCareDateNow = f"{datetime.now():%Y-%m-%d %H:%M:%S}"
        self.selectAnimalTree.insert("", 0, values=(self.staffName, self.animalCareLogNotes, self.animalCareDateNow))
        self.cursor.execute("INSERT INTO Care_Log(U_Name, Anim_Name, Species, Time, Notes) VALUES(%s, %s, %s, CURRENT_TIMESTAMP, %s)",(self.staffName,self.animalCareName,self.animalCareSpecies,self.animalCareLogNotes))


    def searchAnimalCareWindowBackButtonClicked(self):
        self.searchAnimalCareWindow.withdraw()
        self.createStaffSearchAnimalsWindow()
        self.buildStaffSearchAnimalsWindow(self.searchStaffAnimalsWindow)

#------------------- STAFF SHOW PERFORMANCES ------------------------------

    def createStaffShowHistoryWindow(self):
        # Create blank Search Animal Window
        self.staffShowHistoryWindow=Toplevel()
        self.staffShowHistoryWindow.title("Zoo Atlanta")
        self.staffShowHistoryWindow.geometry("800x600")

    def buildStaffShowHistoryWindow(self, staffShowHistoryWindow):
  
        titleLabel= Label(staffShowHistoryWindow,text = "Staff - Show History", font = "Verdana 16 bold ")
        titleLabel.grid(row=1,column=2, sticky=W+E, padx=200)

        self.columns = ("1", "2", "3")

        self.staffShowTree = ttk.Treeview(staffShowHistoryWindow, columns=self.columns)
        self.staffShowTree['show'] = "headings"
        self.staffShowTree.heading("1", text="Name")
        self.staffShowTree.heading("2", text="Time")
        self.staffShowTree.heading("3", text="Exhibit")
        self.staffShowTree.column("1", width=200, anchor="center")
        self.staffShowTree.column("2", width= 200, anchor="center")
        self.staffShowTree.column("3", width=200, anchor="center")

        self.staffShowTree.place(x=20,y=60,width=600)

        staffSearchShowTreeSort = self.staffShowTree

        for col in self.columns:
            self.staffShowTree.heading(col, command=lambda _col=col: \
                self.sortStaffViewShows(staffSearchShowTreeSort, _col, False))

        self.cursor.execute("SELECT Name, Time, E_Name FROM Performance WHERE Host = %s", (self.currentUser))

        self.viewShowsTuple = self.cursor.fetchall()

        self.performanceName = []
        self.showTimes = []
        self.showExhibit = []


        for i in self.viewShowsTuple:
            self.performanceName.append(i[0])
            self.showTimes.append(i[1])
            self.showExhibit.append(i[2])

        for i in range(len(self.viewShowsTuple)):
            self.staffShowTree.insert('', i , values=(self.performanceName[i], self.showTimes[i], self.showExhibit[i]))

        backButton = Button(staffShowHistoryWindow, text="Back", command=self.staffShowHistoryWindowBackButtonClicked)
        backButton.place(x=290, y=300)

    def sortStaffViewShows(self, tv, column, resort):
        for i in self.staffShowTree.get_children():
            self.staffShowTree.delete(i)  


        if (column == "1" and resort == False):

            self.cursor.execute("SELECT Name, Time, E_Name FROM Performance WHERE Host = %s ORDER BY Name ASC", (self.currentUser))

            self.sortColumnsTuple = self.cursor.fetchall()

            #print(self.sortColumnsTuple)

            self.nameListSorted = []
            self.timeListSorted = []
            self.exhibitListSorted = []

            for i in self.sortColumnsTuple:
                self.nameListSorted.append(i[0])
                self.timeListSorted.append(i[1])
                self.exhibitListSorted.append(i[2])

            #print(self.nameListSorted)

            for i in range(len(self.sortColumnsTuple)):
                self.staffShowTree.insert('', i, values=(self.nameListSorted[i], self.timeListSorted[i], self.exhibitListSorted[i]))

            tv.heading(column, command=lambda: \
                self.sortStaffViewShows(tv, column, not resort))
        elif (column == "1" and resort == True):

            self.cursor.execute("SELECT Name, Time, E_Name FROM Performance WHERE Host = %s ORDER BY Name DESC", (self.currentUser))

            self.sortColumnsTuple = self.cursor.fetchall()

            #print(self.sortColumnsTuple)

            self.nameListSorted = []
            self.timeListSorted = []
            self.exhibitListSorted = []

            for i in self.sortColumnsTuple:
                self.nameListSorted.append(i[0])
                self.timeListSorted.append(i[1])
                self.exhibitListSorted.append(i[2])

            #print(self.nameListSorted)

            for i in range(len(self.sortColumnsTuple)):
                self.staffShowTree.insert('', i, values=(self.nameListSorted[i], self.timeListSorted[i], self.exhibitListSorted[i]))

            tv.heading(column, command=lambda: \
                self.sortStaffViewShows(tv, column, not resort))

        elif (column == "2" and resort == False):

            self.cursor.execute("SELECT Name, Time, E_Name FROM Performance WHERE Host = %s ORDER BY Time ASC", (self.currentUser))

            self.sortColumnsTuple = self.cursor.fetchall()

            #print(self.sortColumnsTuple)

            self.nameListSorted = []
            self.timeListSorted = []
            self.exhibitListSorted = []

            for i in self.sortColumnsTuple:
                self.nameListSorted.append(i[0])
                self.timeListSorted.append(i[1])
                self.exhibitListSorted.append(i[2])

            #print(self.nameListSorted)

            for i in range(len(self.sortColumnsTuple)):
                self.staffShowTree.insert('', i, values=(self.nameListSorted[i], self.timeListSorted[i], self.exhibitListSorted[i]))

            tv.heading(column, command=lambda: \
                self.sortStaffViewShows(tv, column, not resort))

        elif (column == "2" and resort == True):

            self.cursor.execute("SELECT Name, Time, E_Name FROM Performance WHERE Host = %s ORDER BY Time DESC", (self.currentUser))

            self.sortColumnsTuple = self.cursor.fetchall()

            #print(self.sortColumnsTuple)

            self.nameListSorted = []
            self.timeListSorted = []
            self.exhibitListSorted = []

            for i in self.sortColumnsTuple:
                self.nameListSorted.append(i[0])
                self.timeListSorted.append(i[1])
                self.exhibitListSorted.append(i[2])

            #print(self.nameListSorted)

            for i in range(len(self.sortColumnsTuple)):
                self.staffShowTree.insert('', i, values=(self.nameListSorted[i], self.timeListSorted[i], self.exhibitListSorted[i]))

            tv.heading(column, command=lambda: \
                self.sortStaffViewShows(tv, column, not resort))

        elif (column == "3" and resort == False):

            self.cursor.execute("SELECT Name, Time, E_Name FROM Performance WHERE Host = %s ORDER BY E_Name ASC", (self.currentUser))

            self.sortColumnsTuple = self.cursor.fetchall()

            #print(self.sortColumnsTuple)

            self.nameListSorted = []
            self.timeListSorted = []
            self.exhibitListSorted = []

            for i in self.sortColumnsTuple:
                self.nameListSorted.append(i[0])
                self.timeListSorted.append(i[1])
                self.exhibitListSorted.append(i[2])

            #print(self.nameListSorted)

            for i in range(len(self.sortColumnsTuple)):
                self.staffShowTree.insert('', i, values=(self.nameListSorted[i], self.timeListSorted[i], self.exhibitListSorted[i]))

            tv.heading(column, command=lambda: \
                self.sortStaffViewShows(tv, column, not resort))

        elif (column == "3" and resort == True):

            self.cursor.execute("SELECT Name, Time, E_Name FROM Performance WHERE Host = %s ORDER BY E_Name DESC", (self.currentUser))

            self.sortColumnsTuple = self.cursor.fetchall()

            #print(self.sortColumnsTuple)

            self.nameListSorted = []
            self.timeListSorted = []
            self.exhibitListSorted = []

            for i in self.sortColumnsTuple:
                self.nameListSorted.append(i[0])
                self.timeListSorted.append(i[1])
                self.exhibitListSorted.append(i[2])

            #print(self.nameListSorted)

            for i in range(len(self.sortColumnsTuple)):
                self.staffShowTree.insert('', i, values=(self.nameListSorted[i], self.timeListSorted[i], self.exhibitListSorted[i]))

            tv.heading(column, command=lambda: \
                self.sortStaffViewShows(tv, column, not resort))


    def staffShowHistoryWindowBackButtonClicked(self):
        self.staffShowHistoryWindow.destroy()
        self.chooseStaffFunctionalityWindow.deiconify()


#--------------------Visitor Functionality Window-----------------
    
    def createVisitorChooseFunctionalityWindow(self):
            # Create blank chooseVisitorFunctionalityWindow
            self.chooseVisitorFunctionalityWindow = Toplevel()
            self.chooseVisitorFunctionalityWindow.title("Zoo Atlanta")
            self.chooseVisitorFunctionalityWindow.geometry("800x600")
            self.chooseVisitorFunctionalityWindow.resizable(0,0)

    def buildVisitorChooseFunctionalityWindow(self,chooseVisitorFunctionalityWindow):
        # Add component to chooseVisitorFunctionalityWindow

        #Choose Functionality Label
        chooseFunctionalityLabel = Label(chooseVisitorFunctionalityWindow, text="Choose Functionality",font = "Verdana 16 bold ")
        # chooseFunctionalityLabel.grid(row=1, column=1, sticky=W+E)
        chooseFunctionalityLabel.place(x=400, y = 25, anchor="center")

        # Search Exhibits Label
        searchExhibitLabel = Label(chooseVisitorFunctionalityWindow, text="Search Exhibits", font = "Verdana 13")
        # searchExhibitLabel.grid(row=2, column=1)
        searchExhibitLabel.bind("<ButtonPress-1>", self.chooseFunctionalityWindowSearchExhibitLabelClicked)
        searchExhibitLabel.place(x=400, y = 100, anchor="center")

        # Search Shows 
        searchShowsLabel = Label(chooseVisitorFunctionalityWindow, text="Search Shows", font = "Verdana 13")
        # searchShowsLabel.grid(row=3, column=1)
        searchShowsLabel.bind("<ButtonPress-1>", self.chooseFunctionalityWindowSearchShowsLabelClicked)
        searchShowsLabel.place(x=400, y = 200, anchor="center")

        # Search for Animals Label
        searchAnimalsLabel = Label(chooseVisitorFunctionalityWindow, text="Search for Animals", font = "Verdana 13")
        # searchAnimalsLabel.grid(row=4,column=1)
        searchAnimalsLabel.bind("<ButtonPress-1>", self.chooseFunctionalityWindowSearchAnimalsLabelClicked)
        searchAnimalsLabel.place(x=400, y = 300, anchor="center")

        # View Exhibit History
        viewExhibitHistoryLabel = Label(chooseVisitorFunctionalityWindow, text="View Exhibit History", font = "Verdana 13")
        # viewExhibitHistoryLabel.grid(row=5,column=1)
        viewExhibitHistoryLabel.bind("<ButtonPress-1>", self.chooseFunctionalityWindowViewExhibitHistoryLabelClicked)
        viewExhibitHistoryLabel.place(x=400, y = 400, anchor="center")


        # View Show History Label
        viewShowHistory = Label(chooseVisitorFunctionalityWindow, text="View Show History", font = "Verdana 13")
        # viewReviewLabel.grid(row=6,column=1)
        viewShowHistory.bind("<ButtonPress-1>", self.chooseFunctionalityWindowViewShowHistoryLabelClicked)
        viewShowHistory.place(x=400, y = 500, anchor="center")

        # Log Out Buttons

        logOutButton = Button(chooseVisitorFunctionalityWindow, text="Log out", command=self.chooseFunctionalityWindowLogOutButtonClicked)
        logOutButton.grid(row=8, column=2,sticky=E)
        logOutButton.place(x = 720, y = 570)

    def chooseFunctionalityWindowSearchExhibitLabelClicked(self,event):
        # Hide Choose Functionality Window.
        self.createSearchExhibitWindow()
        self.buildSearchExhibitWindow(self.searchExhibitWindow)
        self.chooseVisitorFunctionalityWindow.withdraw()

    def chooseFunctionalityWindowSearchShowsLabelClicked(self,event):
        # Hide Choose Functionality Window
        self.createVisitorSearchShowsWindow()
        self.buildVisitorSearchShowsWindow(self.searchVisitorShowsWindow)
        self.chooseVisitorFunctionalityWindow.withdraw()

    def chooseFunctionalityWindowSearchAnimalsLabelClicked(self,event):
        self.createSearchAnimalWindow()
        self.buildSearchAnimalWindow(self.searchAnimalWindow)
        self.chooseVisitorFunctionalityWindow.withdraw()

    def chooseFunctionalityWindowViewExhibitHistoryLabelClicked(self,event):
        self.createExhibitHistoryWindow()
        self.buildExhibitHistoryWindow(self.exhibitHistoryWindow)
        self.chooseVisitorFunctionalityWindow.withdraw()

    def chooseFunctionalityWindowViewShowHistoryLabelClicked(self,event):
        self.createShowHistoryWindow()
        self.buildShowHistoryWindow(self.showHistoryWindow)
        self.chooseVisitorFunctionalityWindow.withdraw()

    def chooseFunctionalityWindowLogOutButtonClicked(self):
        self.chooseVisitorFunctionalityWindow.destroy()
        self.loginWindow.deiconify()

#-------------------VISITOR PAGES------------------------------
#-------------------VISITOR SEARCH SHOWS------------------------------


    def createVisitorSearchShowsWindow(self):
        self.searchVisitorShowsWindow=Toplevel()
        self.searchVisitorShowsWindow.title("Zoo Atlanta")
        self.searchVisitorShowsWindow.geometry("800x600")

    def buildVisitorSearchShowsWindow(self, searchVisitorShowsWindow):
        titleLabel= Label(searchVisitorShowsWindow,text = "Search Shows", font = "Verdana 16 bold ")
        titleLabel.grid(row=1,column=2,sticky=W+E,pady=10)

        # Labels
        showLabel = Label(searchVisitorShowsWindow,text = "Name: ")
        showLabel.grid(row=2,column=0,pady=10)

        self.showNameString = StringVar()
        showNameEntry = Entry(searchVisitorShowsWindow, textvariable = self.showNameString, width=20)
        showNameEntry.grid(row=2, column=1,pady=10)
        
        #populate exhibit menu with sql
        self.cursor.execute("SELECT Name FROM Exhibit")
        self.exhibitTuple = self.cursor.fetchall()
        self.exhibitList = []
        for i in self.exhibitTuple:
            self.exhibitList.append(i[0])

        exhibitLabel = Label(searchVisitorShowsWindow,text = "Exhibit: ")
        exhibitLabel.grid(row=3,column=0,pady=10)
        self.exhibitDefault = StringVar()
        self.exhibitDefault.set("")
        exhibitMenu = OptionMenu(searchVisitorShowsWindow, self.exhibitDefault, "", *self.exhibitList)
        exhibitMenu.grid(row=3, column=1,pady=10)


        dateLabel = Label(searchVisitorShowsWindow,text = "Date")
        dateLabel.grid(row=2, column=2,pady=10)

        self.showDateSV = StringVar()
        showDateEntry = Entry(searchVisitorShowsWindow, textvariable = self.showDateSV, width=20)
        showDateEntry.grid(row=2, column=3,pady=10)

        self.columns = ("1", "2", "3")

        self.searchShowTree = ttk.Treeview(searchVisitorShowsWindow, columns=self.columns, selectmode = 'extended')
        self.searchShowTree['show'] = "headings"
        self.searchShowTree.heading("1", text = "Name")
        self.searchShowTree.heading("2", text = "Exhibit")
        self.searchShowTree.heading("3", text = "Date")
        self.searchShowTree.column("1", width = 175, anchor = "center")
        self.searchShowTree.column("2", width = 175, anchor = "center")
        self.searchShowTree.column("3", width = 175, anchor = "center")
        self.searchShowTree.place(x=350, y=280, anchor="center", width=525)

        searchShowTreeSort = self.searchShowTree

        for col in self.columns:
            self.searchShowTree.heading(col, command=lambda _col=col: \
                self.sortVisitorSearchShows(searchShowTreeSort, _col, False))

        # show All shows upon page load
        self.cursor.execute("SELECT * FROM Performance WHERE Name LIKE '%' AND Time LIKE '%' AND E_Name LIKE '%'")

        self.showResults = self.cursor.fetchall()
        # print(self.showResults)
        # ('Jungle Cruise', datetime.datetime(2010, 8, 18, 9, 0), 'martha_johnson', 'Jungle')

        self.pName = []
        self.pTime = []
        self.pHost = []
        self.ename = []

        for i in self.showResults:
            self.pName.append(i[0])
            self.pTime.append(i[1])
            self.pHost.append(i[2])
            self.ename.append(i[3])
        
        for i in range(len(self.showResults)):
            self.searchShowTree.insert('', i , values=(self.pName[i], self.ename[i], self.pTime[i]))


        # Buttons
        findShowsButton = Button(searchVisitorShowsWindow, text="Search", command=self.searchVisitorShowsWindowFindShowsButtonClicked)
        findShowsButton.grid(row=3,column=2,pady=10)

        logVisitButton = Button(searchVisitorShowsWindow, text="Log Visit", command = self.logVisitButtonClicked)  
        logVisitButton.place(x=320, y=415)

        exhibitDetailButton = Button(searchVisitorShowsWindow, text="View Exhibit Details", command = self.exhibitDetailsButtonClicked)  
        exhibitDetailButton.place(x=500, y=415)  

        backButton = Button(searchVisitorShowsWindow, text="Back", command=self.searchVisitorShowsWindowBackButtonClicked)
        backButton.place(x=120, y=415)

    def sortVisitorSearchShows(self, tv, column, resort):
        for i in self.searchShowTree.get_children():
            self.searchShowTree.delete(i)  

        attributes = ['Name', 'Time', 'E_Name']

        #Entry is a list of the filter inputs
        entry = []

        entry.append(str(self.showNameString.get()))
        entry.append(str(self.showDateSV.get()))
        entry.append(str(self.exhibitDefault.get()))

        #print(entry)

        if (column == "1" and resort == False):

            sql = "SELECT * FROM Performance WHERE "

            for i in range(len(entry)):
                if entry[i] != "":
                    sql = sql + attributes[i] + " = '" + entry[i] + "'"
                else:
                    sql = sql + attributes[i] + " LIKE '%'"
            #This is to check if the next box is filled as well so we add an AND statement to make sure all conditions are met. 
                if i < len(entry)-1:
                    sql = sql + " AND "

            sql = sql + "ORDER BY Name ASC;"
            self.cursor.execute(sql)
            self.sortColumnsTuple = self.cursor.fetchall()

            #print(self.sortColumnsTuple)

            self.nameListSorted = []
            self.timeListSorted = []
            self.exhibitListSorted = []

            for i in self.sortColumnsTuple:
                self.nameListSorted.append(i[0])
                self.timeListSorted.append(i[1])
                self.exhibitListSorted.append(i[3])

            #print(self.nameListSorted)

            for i in range(len(self.sortColumnsTuple)):
                self.searchShowTree.insert('', i, values=(self.nameListSorted[i], self.exhibitListSorted[i], self.timeListSorted[i]))

            tv.heading(column, command=lambda: \
                self.sortVisitorSearchShows(tv, column, not resort))

        elif (column == "1" and resort == True):

            sql = "SELECT * FROM Performance WHERE "

            for i in range(len(entry)):
                if entry[i] != "":
                    sql = sql + attributes[i] + " = '" + entry[i] + "'"
                else:
                    sql = sql + attributes[i] + " LIKE '%'"
            #This is to check if the next box is filled as well so we add an AND statement to make sure all conditions are met. 
                if i < len(entry)-1:
                    sql = sql + " AND "

            #end of statement
            sql = sql + "ORDER BY Name DESC;"
            self.cursor.execute(sql)
            self.sortColumnsTuple = self.cursor.fetchall()

            #print(self.sortColumnsTuple)

            self.nameListSorted = []
            self.timeListSorted = []
            self.exhibitListSorted = []

            for i in self.sortColumnsTuple:
                self.nameListSorted.append(i[0])
                self.timeListSorted.append(i[1])
                self.exhibitListSorted.append(i[3])

            #print(self.nameListSorted)

            for i in range(len(self.sortColumnsTuple)):
                self.searchShowTree.insert('', i, values=(self.nameListSorted[i], self.exhibitListSorted[i], self.timeListSorted[i]))

            tv.heading(column, command=lambda: \
                self.sortVisitorSearchShows(tv, column, not resort))

        elif (column == "2" and resort == False):

            sql = "SELECT * FROM Performance WHERE "

            for i in range(len(entry)):
                if entry[i] != "":
                    sql = sql + attributes[i] + " = '" + entry[i] + "'"
                else:
                    sql = sql + attributes[i] + " LIKE '%'"
            #This is to check if the next box is filled as well so we add an AND statement to make sure all conditions are met. 
                if i < len(entry)-1:
                    sql = sql + " AND "

            #end of statement
            sql = sql + "ORDER BY E_Name ASC;"
            self.cursor.execute(sql)
            self.sortColumnsTuple = self.cursor.fetchall()

            #print(self.sortColumnsTuple)

            self.nameListSorted = []
            self.timeListSorted = []
            self.exhibitListSorted = []

            for i in self.sortColumnsTuple:
                self.nameListSorted.append(i[0])
                self.timeListSorted.append(i[1])
                self.exhibitListSorted.append(i[3])

            #print(self.nameListSorted)

            for i in range(len(self.sortColumnsTuple)):
                self.searchShowTree.insert('', i, values=(self.nameListSorted[i], self.exhibitListSorted[i], self.timeListSorted[i]))

            tv.heading(column, command=lambda: \
                self.sortVisitorSearchShows(tv, column, not resort))

        elif (column == "2" and resort == True):

            sql = "SELECT * FROM Performance WHERE "

            for i in range(len(entry)):
                if entry[i] != "":
                    sql = sql + attributes[i] + " = '" + entry[i] + "'"
                else:
                    sql = sql + attributes[i] + " LIKE '%'"
            #This is to check if the next box is filled as well so we add an AND statement to make sure all conditions are met. 
                if i < len(entry)-1:
                    sql = sql + " AND "

            #end of statement
            sql = sql + "ORDER BY E_Name DESC;"
            self.cursor.execute(sql)
            self.sortColumnsTuple = self.cursor.fetchall()

            #print(self.sortColumnsTuple)

            self.nameListSorted = []
            self.timeListSorted = []
            self.exhibitListSorted = []

            for i in self.sortColumnsTuple:
                self.nameListSorted.append(i[0])
                self.timeListSorted.append(i[1])
                self.exhibitListSorted.append(i[3])

            #print(self.nameListSorted)

            for i in range(len(self.sortColumnsTuple)):
                self.searchShowTree.insert('', i, values=(self.nameListSorted[i], self.exhibitListSorted[i], self.timeListSorted[i]))

            tv.heading(column, command=lambda: \
                self.sortVisitorSearchShows(tv, column, not resort))

        elif (column == "3" and resort == False):

            sql = "SELECT * FROM Performance WHERE "

            for i in range(len(entry)):
                if entry[i] != "":
                    sql = sql + attributes[i] + " = '" + entry[i] + "'"
                else:
                    sql = sql + attributes[i] + " LIKE '%'"
            #This is to check if the next box is filled as well so we add an AND statement to make sure all conditions are met. 
                if i < len(entry)-1:
                    sql = sql + " AND "

            #end of statement
            sql = sql + "ORDER BY Time ASC;"
            self.cursor.execute(sql)
            self.sortColumnsTuple = self.cursor.fetchall()

            #print(self.sortColumnsTuple)

            self.nameListSorted = []
            self.timeListSorted = []
            self.exhibitListSorted = []

            for i in self.sortColumnsTuple:
                self.nameListSorted.append(i[0])
                self.timeListSorted.append(i[1])
                self.exhibitListSorted.append(i[3])

            #print(self.nameListSorted)

            for i in range(len(self.sortColumnsTuple)):
                self.searchShowTree.insert('', i, values=(self.nameListSorted[i], self.exhibitListSorted[i], self.timeListSorted[i]))

            tv.heading(column, command=lambda: \
                self.sortVisitorSearchShows(tv, column, not resort))

        elif (column == "3" and resort == True):

            sql = "SELECT * FROM Performance WHERE "

            for i in range(len(entry)):
                if entry[i] != "":
                    sql = sql + attributes[i] + " = '" + entry[i] + "'"
                else:
                    sql = sql + attributes[i] + " LIKE '%'"
            #This is to check if the next box is filled as well so we add an AND statement to make sure all conditions are met. 
                if i < len(entry)-1:
                    sql = sql + " AND "

            #end of statement
            sql = sql + "ORDER BY Time DESC;"
            self.cursor.execute(sql)
            self.sortColumnsTuple = self.cursor.fetchall()

            #print(self.sortColumnsTuple)

            self.nameListSorted = []
            self.timeListSorted = []
            self.exhibitListSorted = []

            for i in self.sortColumnsTuple:
                self.nameListSorted.append(i[0])
                self.timeListSorted.append(i[1])
                self.exhibitListSorted.append(i[3])

            #print(self.nameListSorted)

            for i in range(len(self.sortColumnsTuple)):
                self.searchShowTree.insert('', i, values=(self.nameListSorted[i], self.exhibitListSorted[i], self.timeListSorted[i]))

            tv.heading(column, command=lambda: \
                self.sortVisitorSearchShows(tv, column, not resort))


    def searchVisitorShowsWindowFindShowsButtonClicked(self):

        for i in self.searchShowTree.get_children():
            self.searchShowTree.delete(i)

        self.performanceDateTime = self.showDateSV.get()

        if self.performanceDateTime is not "":
            try:
                datetime.strptime(self.performanceDateTime, '%Y-%m-%d %I:%M%p')
            except ValueError:
                messagebox.showwarning("Error!", "Date needs to be in format yyyy-mm-dd and time needs to be in format hh:mmAM/PM")
                return False
        
        attributes = ['Name', 'Time', 'E_Name']

        #Entry is a list of the filter inputs
        entry = []

        entry.append(str(self.showNameString.get()))
        entry.append(str(self.performanceDateTime))
        entry.append(str(self.exhibitDefault.get()))

        sql = "SELECT * FROM Performance WHERE "

        for i in range(len(entry)):
            if entry[i] != "":
                sql = sql + attributes[i] + " = '" + entry[i] + "'"
            else:
                sql = sql + attributes[i] + " LIKE '%'"
        #This is to check if the next box is filled as well so we add an AND statement to make sure all conditions are met. 
            if i < len(entry)-1:
                sql = sql + " AND "
        #end of statement
        sql = sql + ";"
        # print(sql)
        # SELECT * FROM Performance WHERE Perform_Name LIKE % AND Time LIKE % AND Exhibit LIKE %;

        self.cursor.execute(sql)

        self.showResults = self.cursor.fetchall()
        # print(self.showResults)
        # ('Jungle Cruise', datetime.datetime(2010, 8, 18, 9, 0), 'martha_johnson', 'Jungle')

        self.pName = []
        self.pTime = []
        self.pHost = []
        self.ename = []

        for i in self.showResults:
            self.pName.append(i[0])
            self.pTime.append(i[1])
            self.pHost.append(i[2])
            self.ename.append(i[3])
        
        for i in range(len(self.showResults)):
            self.searchShowTree.insert('', i , values=(self.pName[i], self.ename[i], self.pTime[i]))


    def exhibitDetailsButtonClicked(self):    
        if not self.searchShowTree.focus():
            messagebox.showwarning("Error","You have not selected an Exhibit.")
            return False

        treeIndexString = self.searchShowTree.focus()
        valueDetail = self.searchShowTree.item(treeIndexString)

        valueslist = list(valueDetail.values())
        valueslist = valueslist[2]
        # print(valueslist)
        self.exhibitOfInterest = valueslist[1]
        self.searchVisitorShowsWindow.destroy()
        self.createExhibitDetailWindow()
        self.buildExhibitDetailWindow(self.exhibitDetailWindow)

    def logVisitButtonClicked(self):
        if not self.searchShowTree.focus():
            messagebox.showwarning("Error","You have not selected a Show.")
            return False

        treeIndexString = self.searchShowTree.focus()
        valueDetail = self.searchShowTree.item(treeIndexString)

        valueslist = list(valueDetail.values())
        valueslist = valueslist[2]
        self.exhibitOfInterest = valueslist[1]
        self.cursor.execute("INSERT INTO Performance_History(U_Name, Perform_Name, Time) VALUES(%s, %s, CURRENT_TIMESTAMP)",(self.currentUser, valueslist[0]))
        self.cursor.execute("INSERT INTO Exhibit_History(U_Name, E_Name, Time) VALUES (%s, %s, %s)",(self.currentUser, valueslist[1], datetime.now()))
        messagebox.showwarning("Show Visit","You have successfully logged your visit to the Show and the Exhibit.")


    def searchVisitorShowsWindowBackButtonClicked(self):
        self.searchVisitorShowsWindow.withdraw()
        self.chooseVisitorFunctionalityWindow.deiconify()

#-------------------VISITOR SEARCH EXHIBITS------------------------------


    def createSearchExhibitWindow(self):
        # Create blank Search Exhibit Window
        self.searchExhibitWindow=Toplevel()
        self.searchExhibitWindow.title("Zoo Atlanta")

    def buildSearchExhibitWindow(self, searchExhibitWindow):

        # Title Label
        titleLabel= Label(searchExhibitWindow,text = "Search Exhibits", font = "Verdana 16 bold ")
        titleLabel.grid(row=1,column=2,sticky=W+E)

        nameLabel = Label(searchExhibitWindow,text = "Name:")
        nameLabel.grid(row=2, column=0)

        self.exhibitNameSV = StringVar()
        animalNameEntry = Entry(searchExhibitWindow, textvariable=self.exhibitNameSV, width=20)
        animalNameEntry.grid(row=2, column=1)

        minLabel=Label(searchExhibitWindow,text="Min:")
        minLabel.grid(row=2,column=4, sticky=W)

        maxLabel=Label(searchExhibitWindow,text="Max:")
        maxLabel.grid(row=2,column=5, sticky=W)

        numAnimalsLabel = Label(searchExhibitWindow,text = "Number of Animals:")
        numAnimalsLabel.grid(row=3,column=3)

        #number of Animals min spin box
        self.minSpinBox = Spinbox(searchExhibitWindow, from_=0, to=10000, width=5)
        self.minSpinBox.grid(row=3, column=4,pady=10,sticky=W)

        # number of Animals max spin box
        self.maxSpinBox = Spinbox(searchExhibitWindow, from_=0, to=10000, width=5)
        self.maxSpinBox.grid(row=3, column=5,pady=10,sticky=W)


        waterLabel = Label(searchExhibitWindow,text = "Water Feature:")
        waterLabel.grid(row=4, column=3)
        # Water Feature Entry
        self.typeDefault = StringVar()
        self.typeDefault.set("No")
        typeMenu = OptionMenu(searchExhibitWindow, self.typeDefault, "Yes", "No")
        typeMenu.grid(row=4, column=4, sticky=W)
        
        min2Label=Label(searchExhibitWindow,text="Min:")
        min2Label.grid(row=3,column=1, sticky=W)
        
        max2Label=Label(searchExhibitWindow,text="Max:")
        max2Label.grid(row=3,column=2, sticky=W)

        sizeLabel = Label(searchExhibitWindow,text = "Size:")
        sizeLabel.grid(row=4,column=0)

        # size min spin box
        self.min2SpinBox = Spinbox(searchExhibitWindow, from_=0, to=10000, width=5)
        self.min2SpinBox.grid(row=4, column=1,pady=5,sticky=W)

        # size max spin box
        self.max2SpinBox = Spinbox(searchExhibitWindow, from_=0, to=10000, width=5)
        self.max2SpinBox.grid(row=4, column=2,pady=5,sticky=W)

        # Button
        findExhibitsButton = Button(searchExhibitWindow, text="Find Exhibits", command=self.searchExhibitWindowFindExhibitsButtonClicked)
        findExhibitsButton.grid(row=7,column=3)

        getExhibitDetailsButton = Button(searchExhibitWindow, text="Get Exhibit Details", command=self.searchExhibitWindowGetDetailsButtonClicked)
        getExhibitDetailsButton.grid(row=7,column=2)

        backButton = Button(searchExhibitWindow, text="Back", command=self.searchExhibitWindowBackButtonClicked)
        backButton.grid(row=7,column=1)

        self.columns = ("1", "2", "3", "4")

        self.searchExhibitTree = ttk.Treeview(searchExhibitWindow, columns=self.columns, selectmode='extended')
        self.searchExhibitTree['show'] = "headings"
        self.searchExhibitTree.column("1", width = 150, anchor = "center")
        self.searchExhibitTree.column("2", width = 150, anchor = "center")
        self.searchExhibitTree.column("3", width = 150, anchor = "center")
        self.searchExhibitTree.column("4", width = 150, anchor = "center")
        self.searchExhibitTree.heading("1", text = "Name")
        self.searchExhibitTree.heading("2", text = "Size")
        self.searchExhibitTree.heading("3", text = "NumAnimals")
        self.searchExhibitTree.heading("4", text = "Water")

        self.searchExhibitTree.grid(row=6, columnspan=4, sticky = 'nsew')

        searchExhibitTreeSort = self.searchExhibitTree

        for col in self.columns:
            self.searchExhibitTree.heading(col, command=lambda _col=col: \
                self.sortVisitorSearchExhibit(searchExhibitTreeSort, _col, False))


        # pre-populate table
        self.cursor.execute("SELECT * FROM (SELECT Name, Size, Has_Water FROM Exhibit WHERE Name LIKE '%'  AND Size BETWEEN 0 AND 1500) AS t1 JOIN (SELECT E_Name, COUNT(Name) FROM Animal GROUP BY E_Name HAVING COUNT(Name)>0 AND COUNT(Name)<100) AS t2 ON t2.E_Name = t1.Name;")
        self.exhibitResults = self.cursor.fetchall()

        self.eName = []
        self.eSize = []
        self.eNumAnimals = []
        self.hasWater = []

        for i in self.exhibitResults:
            self.eName.append(i[0])
            self.eSize.append(i[1])
            # print(ord(i[2]))
            if ord(i[2]) == 1:
                self.hasWater.append(True)
            else:
                self.hasWater.append(False)
            self.eNumAnimals.append(i[4])

        for i in range(len(self.exhibitResults)):
            self.searchExhibitTree.insert('', i , values=(self.eName[i], self.eSize[i], self.eNumAnimals[i], self.hasWater[i]))

    def sortVisitorSearchExhibit(self, tv, column, resort):
        for i in self.searchExhibitTree.get_children():
            self.searchExhibitTree.delete(i)  

        attributes =  ["Name","Size","Has_Water"]

        # Entry is a list of the filter inputs
        entry = []
        entry.append(str(self.exhibitNameSV.get()))

        #for size attribute
        entry.append("")
        
        # might need to fix this to accurately reflect boolean values in the SQL table
        if self.typeDefault.get() == 'No':
            entry.append(False)
        else:
            entry.append(True)

        if (column == "1" and resort == False):
                sql = "SELECT * FROM (SELECT Name, Size, Has_Water FROM Exhibit WHERE " 
                for i in range(len(entry)):
                #min and max will never be empty
                        if type(entry[i]) != str:
                                sql = sql + attributes[i] + " = " + str(entry[i]) + " AND "
                        if i == 2:
                                sql = sql + attributes[i-1] + " BETWEEN " + self.min2SpinBox.get() + " AND " + self.max2SpinBox.get()

                        if i == 2:
                                sql = sql + ") AS t1 JOIN (SELECT E_Name, COUNT(Name) FROM Animal GROUP BY E_Name HAVING COUNT(Name)>" + self.minSpinBox.get() + " AND COUNT(Name)<" + self.maxSpinBox.get() + ") AS t2 ON t2.E_Name = t1.Name"
                        elif type(entry[i]) == str and entry[i] != "":
                                sql = sql + attributes[i] + " = '" + entry[i] +"'"
                        else:
                                sql = sql + attributes[i] + " LIKE '%' "
                                #This is to check if the next box is filled as well so we add an AND statement to make sure all conditions are met. 
                        if i<len(entry)-1:
                                sql = sql + " AND "
                sql = sql + " ORDER BY Name ASC;"

                #print(sql)

                self.cursor.execute(sql)
                self.sortColumnsTuple = self.cursor.fetchall()

                #print(self.sortColumnsTuple)

                self.nameListSorted = []
                self.hasWaterSorted = []
                self.sizeListSorted = []
                self.numAnimalsSorted = []

                for i in self.sortColumnsTuple:
                    self.nameListSorted.append(i[0])
                    if i[2] == b'\x01':
                        self.hasWaterSorted.append("True")
                    if i[2] == b'\x00':
                        self.hasWaterSorted.append("False")
                    self.sizeListSorted.append(i[1])
                    self.numAnimalsSorted.append(i[4])

                for i in range(len(self.sortColumnsTuple)):
                    self.searchExhibitTree.insert('', i, values =(self.nameListSorted[i], self.sizeListSorted[i], self.numAnimalsSorted[i], self.hasWaterSorted[i]))

                tv.heading(column, command=lambda: \
                self.sortVisitorSearchExhibit(tv, column, not resort))

        if (column == "1" and resort == True):
                sql = "SELECT * FROM (SELECT Name, Size, Has_Water FROM Exhibit WHERE " 
                for i in range(len(entry)):
                #min and max will never be empty
                        if type(entry[i]) != str:
                                sql = sql + attributes[i] + " = " + str(entry[i]) + " AND "
                        if i == 2:
                                sql = sql + attributes[i-1] + " BETWEEN " + self.min2SpinBox.get() + " AND " + self.max2SpinBox.get()

                        if i == 2:
                                sql = sql + ") AS t1 JOIN (SELECT E_Name, COUNT(Name) FROM Animal GROUP BY E_Name HAVING COUNT(Name)>" + self.minSpinBox.get() + " AND COUNT(Name)<" + self.maxSpinBox.get() + ") AS t2 ON t2.E_Name = t1.Name"
                        elif type(entry[i]) == str and entry[i] != "":
                                sql = sql + attributes[i] + " = '" + entry[i] +"'"
                        else:
                                sql = sql + attributes[i] + " LIKE '%' "
                                #This is to check if the next box is filled as well so we add an AND statement to make sure all conditions are met. 
                        if i<len(entry)-1:
                                sql = sql + " AND "
                sql = sql + " ORDER BY Name DESC;"

                #print(sql)

                self.cursor.execute(sql)
                self.sortColumnsTuple = self.cursor.fetchall()

                #print(self.sortColumnsTuple)

                self.nameListSorted = []
                self.hasWaterSorted = []
                self.sizeListSorted = []
                self.numAnimalsSorted = []

                for i in self.sortColumnsTuple:
                    self.nameListSorted.append(i[0])
                    if i[2] == b'\x01':
                        self.hasWaterSorted.append("True")
                    if i[2] == b'\x00':
                        self.hasWaterSorted.append("False")
                    self.sizeListSorted.append(i[1])
                    self.numAnimalsSorted.append(i[4])

                for i in range(len(self.sortColumnsTuple)):
                    self.searchExhibitTree.insert('', i, values =(self.nameListSorted[i], self.sizeListSorted[i], self.numAnimalsSorted[i], self.hasWaterSorted[i]))

                tv.heading(column, command=lambda: \
                self.sortVisitorSearchExhibit(tv, column, not resort))

        if (column == "2" and resort == False):
                sql = "SELECT * FROM (SELECT Name, Size, Has_Water FROM Exhibit WHERE " 
                for i in range(len(entry)):
                #min and max will never be empty
                        if type(entry[i]) != str:
                                sql = sql + attributes[i] + " = " + str(entry[i]) + " AND "
                        if i == 2:
                                sql = sql + attributes[i-1] + " BETWEEN " + self.min2SpinBox.get() + " AND " + self.max2SpinBox.get()

                        if i == 2:
                                sql = sql + ") AS t1 JOIN (SELECT E_Name, COUNT(Name) FROM Animal GROUP BY E_Name HAVING COUNT(Name)>" + self.minSpinBox.get() + " AND COUNT(Name)<" + self.maxSpinBox.get() + ") AS t2 ON t2.E_Name = t1.Name"
                        elif type(entry[i]) == str and entry[i] != "":
                                sql = sql + attributes[i] + " = '" + entry[i] +"'"
                        else:
                                sql = sql + attributes[i] + " LIKE '%' "
                                #This is to check if the next box is filled as well so we add an AND statement to make sure all conditions are met. 
                        if i<len(entry)-1:
                                sql = sql + " AND "
                sql = sql + " ORDER BY Size ASC;"

                #print(sql)

                self.cursor.execute(sql)
                self.sortColumnsTuple = self.cursor.fetchall()

                #print(self.sortColumnsTuple)

                self.nameListSorted = []
                self.hasWaterSorted = []
                self.sizeListSorted = []
                self.numAnimalsSorted = []

                for i in self.sortColumnsTuple:
                    self.nameListSorted.append(i[0])
                    if i[2] == b'\x01':
                        self.hasWaterSorted.append("True")
                    if i[2] == b'\x00':
                        self.hasWaterSorted.append("False")
                    self.sizeListSorted.append(i[1])
                    self.numAnimalsSorted.append(i[4])

                for i in range(len(self.sortColumnsTuple)):
                    self.searchExhibitTree.insert('', i, values =(self.nameListSorted[i], self.sizeListSorted[i], self.numAnimalsSorted[i], self.hasWaterSorted[i]))

                tv.heading(column, command=lambda: \
                self.sortVisitorSearchExhibit(tv, column, not resort))

        if (column == "2" and resort == True):
                sql = "SELECT * FROM (SELECT Name, Size, Has_Water FROM Exhibit WHERE " 
                for i in range(len(entry)):
                #min and max will never be empty
                        if type(entry[i]) != str:
                                sql = sql + attributes[i] + " = " + str(entry[i]) + " AND "
                        if i == 2:
                                sql = sql + attributes[i-1] + " BETWEEN " + self.min2SpinBox.get() + " AND " + self.max2SpinBox.get()

                        if i == 2:
                                sql = sql + ") AS t1 JOIN (SELECT E_Name, COUNT(Name) FROM Animal GROUP BY E_Name HAVING COUNT(Name)>" + self.minSpinBox.get() + " AND COUNT(Name)<" + self.maxSpinBox.get() + ") AS t2 ON t2.E_Name = t1.Name"
                        elif type(entry[i]) == str and entry[i] != "":
                                sql = sql + attributes[i] + " = '" + entry[i] +"'"
                        else:
                                sql = sql + attributes[i] + " LIKE '%' "
                                #This is to check if the next box is filled as well so we add an AND statement to make sure all conditions are met. 
                        if i<len(entry)-1:
                                sql = sql + " AND "
                sql = sql + " ORDER BY Size DESC;"

                #print(sql)

                self.cursor.execute(sql)
                self.sortColumnsTuple = self.cursor.fetchall()

                #print(self.sortColumnsTuple)

                self.nameListSorted = []
                self.hasWaterSorted = []
                self.sizeListSorted = []
                self.numAnimalsSorted = []

                for i in self.sortColumnsTuple:
                    self.nameListSorted.append(i[0])
                    if i[2] == b'\x01':
                        self.hasWaterSorted.append("True")
                    if i[2] == b'\x00':
                        self.hasWaterSorted.append("False")
                    self.sizeListSorted.append(i[1])
                    self.numAnimalsSorted.append(i[4])

                for i in range(len(self.sortColumnsTuple)):
                    self.searchExhibitTree.insert('', i, values =(self.nameListSorted[i], self.sizeListSorted[i], self.numAnimalsSorted[i], self.hasWaterSorted[i]))

                tv.heading(column, command=lambda: \
                self.sortVisitorSearchExhibit(tv, column, not resort))

        if (column == "3" and resort == False):
                sql = "SELECT * FROM (SELECT Name, Size, Has_Water FROM Exhibit WHERE " 
                for i in range(len(entry)):
                #min and max will never be empty
                        if type(entry[i]) != str:
                                sql = sql + attributes[i] + " = " + str(entry[i]) + " AND "
                        if i == 2:
                                sql = sql + attributes[i-1] + " BETWEEN " + self.min2SpinBox.get() + " AND " + self.max2SpinBox.get()

                        if i == 2:
                                sql = sql + ") AS t1 JOIN (SELECT E_Name, COUNT(Name) AS Count FROM Animal GROUP BY E_Name HAVING COUNT(Name)>" + self.minSpinBox.get() + " AND COUNT(Name)<" + self.maxSpinBox.get() + ") AS t2 ON t2.E_Name = t1.Name"
                        elif type(entry[i]) == str and entry[i] != "":
                                sql = sql + attributes[i] + " = '" + entry[i] +"'"
                        else:
                                sql = sql + attributes[i] + " LIKE '%' "
                                #This is to check if the next box is filled as well so we add an AND statement to make sure all conditions are met. 
                        if i<len(entry)-1:
                                sql = sql + " AND "
                sql = sql + " ORDER BY Count ASC;"

                #print(sql)

                self.cursor.execute(sql)
                self.sortColumnsTuple = self.cursor.fetchall()

                #print(self.sortColumnsTuple)

                self.nameListSorted = []
                self.hasWaterSorted = []
                self.sizeListSorted = []
                self.numAnimalsSorted = []

                for i in self.sortColumnsTuple:
                    self.nameListSorted.append(i[0])
                    if i[2] == b'\x01':
                        self.hasWaterSorted.append("True")
                    if i[2] == b'\x00':
                        self.hasWaterSorted.append("False")
                    self.sizeListSorted.append(i[1])
                    self.numAnimalsSorted.append(i[4])

                for i in range(len(self.sortColumnsTuple)):
                    self.searchExhibitTree.insert('', i, values =(self.nameListSorted[i], self.sizeListSorted[i], self.numAnimalsSorted[i], self.hasWaterSorted[i]))

                tv.heading(column, command=lambda: \
                self.sortVisitorSearchExhibit(tv, column, not resort))

        if (column == "3" and resort == True):
                sql = "SELECT * FROM (SELECT Name, Size, Has_Water FROM Exhibit WHERE " 
                for i in range(len(entry)):
                #min and max will never be empty
                        if type(entry[i]) != str:
                                sql = sql + attributes[i] + " = " + str(entry[i]) + " AND "
                        if i == 2:
                                sql = sql + attributes[i-1] + " BETWEEN " + self.min2SpinBox.get() + " AND " + self.max2SpinBox.get()

                        if i == 2:
                                sql = sql + ") AS t1 JOIN (SELECT E_Name, COUNT(Name) AS Count FROM Animal GROUP BY E_Name HAVING COUNT(Name)>" + self.minSpinBox.get() + " AND COUNT(Name)<" + self.maxSpinBox.get() + ") AS t2 ON t2.E_Name = t1.Name"
                        elif type(entry[i]) == str and entry[i] != "":
                                sql = sql + attributes[i] + " = '" + entry[i] +"'"
                        else:
                                sql = sql + attributes[i] + " LIKE '%' "
                                #This is to check if the next box is filled as well so we add an AND statement to make sure all conditions are met. 
                        if i<len(entry)-1:
                                sql = sql + " AND "
                sql = sql + " ORDER BY Count DESC;"

                #print(sql)

                self.cursor.execute(sql)
                self.sortColumnsTuple = self.cursor.fetchall()

                #print(self.sortColumnsTuple)

                self.nameListSorted = []
                self.hasWaterSorted = []
                self.sizeListSorted = []
                self.numAnimalsSorted = []

                for i in self.sortColumnsTuple:
                    self.nameListSorted.append(i[0])
                    if i[2] == b'\x01':
                        self.hasWaterSorted.append("True")
                    if i[2] == b'\x00':
                        self.hasWaterSorted.append("False")
                    self.sizeListSorted.append(i[1])
                    self.numAnimalsSorted.append(i[4])

                for i in range(len(self.sortColumnsTuple)):
                    self.searchExhibitTree.insert('', i, values =(self.nameListSorted[i], self.sizeListSorted[i], self.numAnimalsSorted[i], self.hasWaterSorted[i]))

                tv.heading(column, command=lambda: \
                self.sortVisitorSearchExhibit(tv, column, not resort))

        if (column == "4" and resort == False):
                sql = "SELECT * FROM (SELECT Name, Size, Has_Water FROM Exhibit WHERE " 
                for i in range(len(entry)):
                #min and max will never be empty
                        if type(entry[i]) != str:
                                sql = sql + attributes[i] + " = " + str(entry[i]) + " AND "
                        if i == 2:
                                sql = sql + attributes[i-1] + " BETWEEN " + self.min2SpinBox.get() + " AND " + self.max2SpinBox.get()

                        if i == 2:
                                sql = sql + ") AS t1 JOIN (SELECT E_Name, COUNT(Name) FROM Animal GROUP BY E_Name HAVING COUNT(Name)>" + self.minSpinBox.get() + " AND COUNT(Name)<" + self.maxSpinBox.get() + ") AS t2 ON t2.E_Name = t1.Name"
                        elif type(entry[i]) == str and entry[i] != "":
                                sql = sql + attributes[i] + " = '" + entry[i] +"'"
                        else:
                                sql = sql + attributes[i] + " LIKE '%' "
                                #This is to check if the next box is filled as well so we add an AND statement to make sure all conditions are met. 
                        if i<len(entry)-1:
                                sql = sql + " AND "
                sql = sql + " ORDER BY Has_Water ASC;"

                #print(sql)

                self.cursor.execute(sql)
                self.sortColumnsTuple = self.cursor.fetchall()

                #print(self.sortColumnsTuple)

                self.nameListSorted = []
                self.hasWaterSorted = []
                self.sizeListSorted = []
                self.numAnimalsSorted = []

                for i in self.sortColumnsTuple:
                    self.nameListSorted.append(i[0])
                    if i[2] == b'\x01':
                        self.hasWaterSorted.append("True")
                    if i[2] == b'\x00':
                        self.hasWaterSorted.append("False")
                    self.sizeListSorted.append(i[1])
                    self.numAnimalsSorted.append(i[4])

                for i in range(len(self.sortColumnsTuple)):
                    self.searchExhibitTree.insert('', i, values =(self.nameListSorted[i], self.sizeListSorted[i], self.numAnimalsSorted[i], self.hasWaterSorted[i]))

                tv.heading(column, command=lambda: \
                self.sortVisitorSearchExhibit(tv, column, not resort))

        if (column == "4" and resort == True):
                sql = "SELECT * FROM (SELECT Name, Size, Has_Water FROM Exhibit WHERE " 
                for i in range(len(entry)):
                #min and max will never be empty
                        if type(entry[i]) != str:
                                sql = sql + attributes[i] + " = " + str(entry[i]) + " AND "
                        if i == 2:
                                sql = sql + attributes[i-1] + " BETWEEN " + self.min2SpinBox.get() + " AND " + self.max2SpinBox.get()

                        if i == 2:
                                sql = sql + ") AS t1 JOIN (SELECT E_Name, COUNT(Name) FROM Animal GROUP BY E_Name HAVING COUNT(Name)>" + self.minSpinBox.get() + " AND COUNT(Name)<" + self.maxSpinBox.get() + ") AS t2 ON t2.E_Name = t1.Name"
                        elif type(entry[i]) == str and entry[i] != "":
                                sql = sql + attributes[i] + " = '" + entry[i] +"'"
                        else:
                                sql = sql + attributes[i] + " LIKE '%' "
                                #This is to check if the next box is filled as well so we add an AND statement to make sure all conditions are met. 
                        if i<len(entry)-1:
                                sql = sql + " AND "
                sql = sql + " ORDER BY Has_Water DESC;"

                #print(sql)

                self.cursor.execute(sql)
                self.sortColumnsTuple = self.cursor.fetchall()

                #print(self.sortColumnsTuple)

                self.nameListSorted = []
                self.hasWaterSorted = []
                self.sizeListSorted = []
                self.numAnimalsSorted = []

                for i in self.sortColumnsTuple:
                    self.nameListSorted.append(i[0])
                    if i[2] == b'\x01':
                        self.hasWaterSorted.append("True")
                    if i[2] == b'\x00':
                        self.hasWaterSorted.append("False")
                    self.sizeListSorted.append(i[1])
                    self.numAnimalsSorted.append(i[4])

                for i in range(len(self.sortColumnsTuple)):
                    self.searchExhibitTree.insert('', i, values =(self.nameListSorted[i], self.sizeListSorted[i], self.numAnimalsSorted[i], self.hasWaterSorted[i]))

                tv.heading(column, command=lambda: \
                self.sortVisitorSearchExhibit(tv, column, not resort))

    def searchExhibitWindowFindExhibitsButtonClicked(self):

        # clear existing information in the table
        for i in self.searchExhibitTree.get_children():
            self.searchExhibitTree.delete(i)

        # Table is a list of table names"
        attributes =  ["Name","Size","Has_Water"]

        # Entry is a list of the filter inputs
        entry = []
        entry.append(str(self.exhibitNameSV.get()))

        #for size attribute
        entry.append("")
        
        # might need to fix this to accurately reflect boolean values in the SQL table
        if self.typeDefault.get() == 'No':
            entry.append(False)
        else:
            entry.append(True)

        #print(entry)

        sql = "SELECT * FROM (SELECT Name, Size, Has_Water FROM Exhibit WHERE " 

        for i in range(len(entry)):
            #min and max will never be empty
            if type(entry[i]) != str:
                sql = sql + attributes[i] + " = " + str(entry[i]) + " AND "
            if i == 2:
                sql = sql + attributes[i-1] + " BETWEEN " + self.min2SpinBox.get() + " AND " + self.max2SpinBox.get()
            
            if i == 2:
                sql = sql + ") AS t1 JOIN (SELECT E_Name, COUNT(Name) FROM Animal GROUP BY E_Name HAVING COUNT(Name)>" + self.minSpinBox.get() + " AND COUNT(Name)<" + self.maxSpinBox.get() + ") AS t2 ON t2.E_Name = t1.Name;"
            elif type(entry[i]) == str and entry[i] != "":
                sql = sql + attributes[i] + " = '" + entry[i] +"'"
            else:
                sql = sql + attributes[i] + " LIKE '%' "
            #This is to check if the next box is filled as well so we add an AND statement to make sure all conditions are met. 
            if i<len(entry)-1:
                sql = sql + " AND "

        #print(sql)

        self.cursor.execute(sql)
        self.exhibitResults = self.cursor.fetchall()
        # print(self.exhibitResults)
        # ('Birds', 1000, b'\x01', 'Birds', 2), ('Jungle', 600, b'\x00', 'Jungle', 1),

        self.eName = []
        self.eSize = []
        self.eNumAnimals = []
        self.hasWater = []

        for i in self.exhibitResults:
            self.eName.append(i[0])
            self.eSize.append(i[1])
            # print(ord(i[2]))
            if ord(i[2]) == 1:
                self.hasWater.append(True)
            else:
                self.hasWater.append(False)
            self.eNumAnimals.append(i[4])

        for i in range(len(self.exhibitResults)):
            self.searchExhibitTree.insert('', i , values=(self.eName[i], self.eSize[i], self.eNumAnimals[i], self.hasWater[i]))

    def searchExhibitWindowGetDetailsButtonClicked(self):    
        if not self.searchExhibitTree.focus():
            messagebox.showwarning("Error","You have not selected an Exhibit.")
            return False

        treeIndexString = self.searchExhibitTree.focus()
        valueDetail = self.searchExhibitTree.item(treeIndexString)

        valueslist = list(valueDetail.values())
        valueslist = valueslist[2]
        print(valueslist)

        self.exhibitOfInterest = valueslist[0]
        self.searchExhibitWindow.destroy()
        self.createExhibitDetailWindow()
        self.buildExhibitDetailWindow(self.exhibitDetailWindow)

    def searchExhibitWindowBackButtonClicked(self):
        self.searchExhibitWindow.destroy()
        self.chooseVisitorFunctionalityWindow.deiconify()

#-------------------VISITOR EXHIBIT HISTORY------------------------------


    def createExhibitHistoryWindow(self):

        self.exhibitHistoryWindow=Toplevel()
        self.exhibitHistoryWindow.title("Zoo Atlanta")
        self.exhibitHistoryWindow.geometry("800x600")

    def buildExhibitHistoryWindow(self, exhibitHistoryWindow):
        titleLabel= Label(exhibitHistoryWindow,text = "Exhibit History", font = "Verdana 16 bold ")
        titleLabel.grid(row=1,column=2,sticky=W+E)

        minLabel = Label(exhibitHistoryWindow, text="Min")
        minLabel.grid(row=2, column=3,pady=10,sticky=W)

        maxLabel = Label(exhibitHistoryWindow, text="Max")
        maxLabel.grid(row=2, column=4,pady=10,sticky=W)

        exhibitLabel = Label(exhibitHistoryWindow,text = "Name")
        exhibitLabel.grid(row=3,column=0,pady=10)
        self.exhibitNameString = StringVar()
        exhibitNameEntry = Entry(exhibitHistoryWindow, textvariable=self.exhibitNameString, width=20)
        exhibitNameEntry.grid(row=3,column=1,pady=10)

        numVisitsLabel = Label(exhibitHistoryWindow,text = "Number of Visits")
        numVisitsLabel.grid(row=3,column=2,pady=10)

        self.minSpinBox = Spinbox(exhibitHistoryWindow, from_=0, to=10000, width=5)
        self.minSpinBox.grid(row=3, column=3,pady=10,sticky=W)

        self.maxSpinBox = Spinbox(exhibitHistoryWindow, from_=0, to=10000, width=5)
        self.maxSpinBox.grid(row=3, column=4,pady=10,sticky=W)


        dateLabel = Label(exhibitHistoryWindow,text = "Date:")
        dateLabel.grid(row=4, column=0,pady=10)

        #showDateEntry = CalendarDialog.main()
        self.exhibitDateSV = StringVar()
        exhibitDateEntry = Entry(exhibitHistoryWindow, textvariable = self.exhibitDateSV, width=20)
        exhibitDateEntry.grid(row=4, column=1,pady=10)

        # Buttons
        findExhibitsButton = Button(exhibitHistoryWindow, text="Search", command=self.exhibitHistoryWindowFindHistoryButtonClicked)
        findExhibitsButton.grid(row=4,column=2,pady=10)

        getExhibitDetailsButton = Button(exhibitHistoryWindow, text="Get Exhibit Details", command=self.searchExhibitHistoryWindowGetDetailsButtonClicked)
        getExhibitDetailsButton.grid(row=6,column=2)

        backButton = Button(exhibitHistoryWindow, text="Back", command=self.exhibitHistoryWindowBackButtonClicked)
        backButton.place(x=310, y=440)

        self.columns = ("1", "2", "3")
        
        # self.selectExhibitTree['show'] = "headings"
        self.exhibitHistoryTree = ttk.Treeview(exhibitHistoryWindow, columns=self.columns, selectmode="extended")
        self.exhibitHistoryTree['show'] = "headings"
        self.exhibitHistoryTree.column("1", width = 200, anchor = "center")
        self.exhibitHistoryTree.column("2", width = 200, anchor = "center")
        self.exhibitHistoryTree.column("3", width = 200, anchor = "center")
        self.exhibitHistoryTree.heading("1", text = "Name")
        self.exhibitHistoryTree.heading("2", text = "Time")
        self.exhibitHistoryTree.heading("3", text = "Number of Visits")

        self.exhibitHistoryTree.place(x=20, y=200,width=600)

        exhibitHistoryTreeSort = self.exhibitHistoryTree

        for col in self.columns:
            self.exhibitHistoryTree.heading(col, command=lambda _col=col: \
                self.sortVisitorExhibitHistory(exhibitHistoryTreeSort, _col, False))


        self.cursor.execute("SELECT t2.Count, t1.E_Name, t1.Time  FROM (SELECT E_Name, Time FROM Exhibit_History WHERE U_Name = %s) AS t1 LEFT JOIN (SELECT COUNT(U_Name AND E_Name AND Time) as Count, E_Name as Name FROM Exhibit_History WHERE U_Name = %s GROUP BY E_Name) AS t2 on (t2.Name = t1.E_Name)",(self.currentUser ,self.currentUser))
        self.historyResults = self.cursor.fetchall()
        # print(self.historyResults)
        # (1, 'Pacific', datetime.datetime(2018, 12, 2, 14, 59, 4))

        self.timesVisited = []
        self.exhibitTime = []
        self.exhibitVisited = []

        for i in self.historyResults:
            self.timesVisited.append(i[0])
            self.exhibitVisited.append(i[1])
            self.exhibitTime.append(i[2])
            

        for i in range(len(self.historyResults)):
            self.exhibitHistoryTree.insert('', i , values=(self.exhibitVisited[i], self.exhibitTime[i], self.timesVisited[i]))

    def sortVisitorExhibitHistory(self, tv, column, resort):
        for i in self.exhibitHistoryTree.get_children():
            self.exhibitHistoryTree.delete(i)  

        attributes = ['E_name', 'Time', 'NumVisits']

        #Entry is a list of the filter inputs
        entry = []

        entry.append(str(self.exhibitNameString.get()))
        entry.append(self.exhibitDateSV.get())

        if (column == "1" and resort == False):

            sql = "SELECT t1.E_Name, t1.Time, t2.Count FROM(SELECT E_Name, TIME FROM Exhibit_History WHERE U_Name = '" + self.currentUser + "' AND "

            for i in range(len(entry)):
            #min and max will never be empty
                if i == 1:
                    sql = sql + ") t1 JOIN (SELECT COUNT(E_Name AND TIME) AS Count, E_Name AS Name FROM Exhibit_History WHERE U_Name = '" + self.currentUser + "' GROUP BY E_Name HAVING COUNT(E_Name AND TIME)>" + self.minSpinBox.get() + " AND COUNT(E_Name AND TIME)<" + self.maxSpinBox.get() + ") t2 ON (t2.Name = t1.E_Name)"
                elif entry[i] != "":
                    sql = sql + attributes[i] + " = " + entry[i]
                else:
                    sql = sql + attributes[i] + " LIKE '%'"
                if i < len(entry)-2:
                    sql = sql + "AND "

            sql = sql + " ORDER BY E_name ASC;"
            self.cursor.execute(sql)
            self.sortColumnsTuple = self.cursor.fetchall()

            #print(self.sortColumnsTuple)

            self.nameListSorted = []
            self.timeListSorted = []
            self.numVisitsSorted = []

            for i in self.sortColumnsTuple:
                self.nameListSorted.append(i[0])
                self.timeListSorted.append(i[1])
                self.numVisitsSorted.append(i[2])

            #print(self.nameListSorted)

            for i in range(len(self.sortColumnsTuple)):
                self.exhibitHistoryTree.insert('', i, values=(self.nameListSorted[i], self.timeListSorted[i], self.numVisitsSorted[i]))

            tv.heading(column, command=lambda: \
                self.sortVisitorExhibitHistory(tv, column, not resort))

        elif (column == "1" and resort == True):

            sql = "SELECT t1.E_Name, t1.Time, t2.Count FROM(SELECT E_Name, TIME FROM Exhibit_History WHERE U_Name = '" + self.currentUser + "' AND "

            for i in range(len(entry)):
            #min and max will never be empty
                if i == 1:
                    sql = sql + ") t1 JOIN (SELECT COUNT(E_Name AND TIME) AS Count, E_Name AS Name FROM Exhibit_History WHERE U_Name = '" + self.currentUser + "' GROUP BY E_Name HAVING COUNT(E_Name AND TIME)>" + self.minSpinBox.get() + " AND COUNT(E_Name AND TIME)<" + self.maxSpinBox.get() + ") t2 ON (t2.Name = t1.E_Name)"
                elif entry[i] != "":
                    sql = sql + attributes[i] + " = " + entry[i]
                else:
                    sql = sql + attributes[i] + " LIKE '%'"
                if i < len(entry)-2:
                    sql = sql + "AND "

            sql = sql + " ORDER BY E_name DESC;"
            self.cursor.execute(sql)
            self.sortColumnsTuple = self.cursor.fetchall()

            #print(self.sortColumnsTuple)

            self.nameListSorted = []
            self.timeListSorted = []
            self.numVisitsSorted = []

            for i in self.sortColumnsTuple:
                self.nameListSorted.append(i[0])
                self.timeListSorted.append(i[1])
                self.numVisitsSorted.append(i[2])

            #print(self.nameListSorted)

            for i in range(len(self.sortColumnsTuple)):
                self.exhibitHistoryTree.insert('', i, values=(self.nameListSorted[i], self.timeListSorted[i], self.numVisitsSorted[i]))

            tv.heading(column, command=lambda: \
                self.sortVisitorExhibitHistory(tv, column, not resort))

        if (column == "2" and resort == False):

            sql = "SELECT t1.E_Name, t1.Time, t2.Count FROM(SELECT E_Name, TIME FROM Exhibit_History WHERE U_Name = '" + self.currentUser + "' AND "

            for i in range(len(entry)):
            #min and max will never be empty
                if i == 1:
                    sql = sql + ") t1 JOIN (SELECT COUNT(E_Name AND TIME) AS Count, E_Name AS Name FROM Exhibit_History WHERE U_Name = '" + self.currentUser + "' GROUP BY E_Name HAVING COUNT(E_Name AND TIME)>" + self.minSpinBox.get() + " AND COUNT(E_Name AND TIME)<" + self.maxSpinBox.get() + ") t2 ON (t2.Name = t1.E_Name)"
                elif entry[i] != "":
                    sql = sql + attributes[i] + " = " + entry[i]
                else:
                    sql = sql + attributes[i] + " LIKE '%'"
                if i < len(entry)-2:
                    sql = sql + "AND "

            sql = sql + " ORDER BY Time ASC;"
            self.cursor.execute(sql)
            self.sortColumnsTuple = self.cursor.fetchall()

            #print(self.sortColumnsTuple)

            self.nameListSorted = []
            self.timeListSorted = []
            self.numVisitsSorted = []

            for i in self.sortColumnsTuple:
                self.nameListSorted.append(i[0])
                self.timeListSorted.append(i[1])
                self.numVisitsSorted.append(i[2])

            #print(self.nameListSorted)

            for i in range(len(self.sortColumnsTuple)):
                self.exhibitHistoryTree.insert('', i, values=(self.nameListSorted[i], self.timeListSorted[i], self.numVisitsSorted[i]))

            tv.heading(column, command=lambda: \
                self.sortVisitorExhibitHistory(tv, column, not resort))

        if (column == "2" and resort == True):

            sql = "SELECT t1.E_Name, t1.Time, t2.Count FROM(SELECT E_Name, TIME FROM Exhibit_History WHERE U_Name = '" + self.currentUser + "' AND "

            for i in range(len(entry)):
            #min and max will never be empty
                if i == 1:
                    sql = sql + ") t1 JOIN (SELECT COUNT(E_Name AND TIME) AS Count, E_Name AS Name FROM Exhibit_History WHERE U_Name = '" + self.currentUser + "' GROUP BY E_Name HAVING COUNT(E_Name AND TIME)>" + self.minSpinBox.get() + " AND COUNT(E_Name AND TIME)<" + self.maxSpinBox.get() + ") t2 ON (t2.Name = t1.E_Name)"
                elif entry[i] != "":
                    sql = sql + attributes[i] + " = " + entry[i]
                else:
                    sql = sql + attributes[i] + " LIKE '%'"
                if i < len(entry)-2:
                    sql = sql + "AND "

            sql = sql + " ORDER BY Time DESC;"
            self.cursor.execute(sql)
            self.sortColumnsTuple = self.cursor.fetchall()

            #print(self.sortColumnsTuple)

            self.nameListSorted = []
            self.timeListSorted = []
            self.numVisitsSorted = []

            for i in self.sortColumnsTuple:
                self.nameListSorted.append(i[0])
                self.timeListSorted.append(i[1])
                self.numVisitsSorted.append(i[2])

            #print(self.nameListSorted)

            for i in range(len(self.sortColumnsTuple)):
                self.exhibitHistoryTree.insert('', i, values=(self.nameListSorted[i], self.timeListSorted[i], self.numVisitsSorted[i]))

            tv.heading(column, command=lambda: \
                self.sortVisitorExhibitHistory(tv, column, not resort))

        if (column == "3" and resort == False):

            sql = "SELECT t1.E_Name, t1.Time, t2.Count FROM(SELECT E_Name, TIME FROM Exhibit_History WHERE U_Name = '" + self.currentUser + "' AND "

            for i in range(len(entry)):
            #min and max will never be empty
                if i == 1:
                    sql = sql + ") t1 JOIN (SELECT COUNT(E_Name AND TIME) AS Count, E_Name AS Name FROM Exhibit_History WHERE U_Name = '" + self.currentUser + "' GROUP BY E_Name HAVING COUNT(E_Name AND TIME)>" + self.minSpinBox.get() + " AND COUNT(E_Name AND TIME)<" + self.maxSpinBox.get() + ") t2 ON (t2.Name = t1.E_Name)"
                elif entry[i] != "":
                    sql = sql + attributes[i] + " = " + entry[i]
                else:
                    sql = sql + attributes[i] + " LIKE '%'"
                if i < len(entry)-2:
                    sql = sql + "AND "

            sql = sql + " ORDER BY Count ASC;"
            self.cursor.execute(sql)
            self.sortColumnsTuple = self.cursor.fetchall()

            #print(self.sortColumnsTuple)

            self.nameListSorted = []
            self.timeListSorted = []
            self.numVisitsSorted = []

            for i in self.sortColumnsTuple:
                self.nameListSorted.append(i[0])
                self.timeListSorted.append(i[1])
                self.numVisitsSorted.append(i[2])

            #print(self.nameListSorted)

            for i in range(len(self.sortColumnsTuple)):
                self.exhibitHistoryTree.insert('', i, values=(self.nameListSorted[i], self.timeListSorted[i], self.numVisitsSorted[i]))

            tv.heading(column, command=lambda: \
                self.sortVisitorExhibitHistory(tv, column, not resort))

        if (column == "3" and resort == True):

            sql = "SELECT t1.E_Name, t1.Time, t2.Count FROM(SELECT E_Name, TIME FROM Exhibit_History WHERE U_Name = '" + self.currentUser + "' AND "

            for i in range(len(entry)):
            #min and max will never be empty
                if i == 1:
                    sql = sql + ") t1 JOIN (SELECT COUNT(E_Name AND TIME) AS Count, E_Name AS Name FROM Exhibit_History WHERE U_Name = '" + self.currentUser + "' GROUP BY E_Name HAVING COUNT(E_Name AND TIME)>" + self.minSpinBox.get() + " AND COUNT(E_Name AND TIME)<" + self.maxSpinBox.get() + ") t2 ON (t2.Name = t1.E_Name)"
                elif entry[i] != "":
                    sql = sql + attributes[i] + " = " + entry[i]
                else:
                    sql = sql + attributes[i] + " LIKE '%'"
                if i < len(entry)-2:
                    sql = sql + "AND "

            sql = sql + " ORDER BY Count DESC;"
            self.cursor.execute(sql)
            self.sortColumnsTuple = self.cursor.fetchall()

            #print(self.sortColumnsTuple)

            self.nameListSorted = []
            self.timeListSorted = []
            self.numVisitsSorted = []

            for i in self.sortColumnsTuple:
                self.nameListSorted.append(i[0])
                self.timeListSorted.append(i[1])
                self.numVisitsSorted.append(i[2])

            #print(self.nameListSorted)

            for i in range(len(self.sortColumnsTuple)):
                self.exhibitHistoryTree.insert('', i, values=(self.nameListSorted[i], self.timeListSorted[i], self.numVisitsSorted[i]))

            tv.heading(column, command=lambda: \
                self.sortVisitorExhibitHistory(tv, column, not resort))

    def searchExhibitHistoryWindowGetDetailsButtonClicked(self):    
        if not self.exhibitHistoryTree.focus():
            messagebox.showwarning("Error","You have not selected an Exhibit.")
            return False

        treeIndexString = self.exhibitHistoryTree.focus()
        valueDetail = self.exhibitHistoryTree.item(treeIndexString)

        valueslist = list(valueDetail.values())
        valueslist = valueslist[2]
        # print(valueslist)
        self.exhibitOfInterest = valueslist[0]
        self.exhibitHistoryWindow.destroy()
        self.createExhibitDetailWindow()
        self.buildExhibitDetailWindow(self.exhibitDetailWindow)


    def exhibitHistoryWindowFindHistoryButtonClicked(self):

        for i in self.exhibitHistoryTree.get_children():
            self.exhibitHistoryTree.delete(i)

        self.exhibitDateTime = self.exhibitDateSV.get()

        if self.exhibitDateTime is not "":
            try:
                datetime.strptime(self.exhibitDateTime, '%Y-%m-%d %I:%M%p')
            except ValueError:
                messagebox.showwarning("Error!", "Date needs to be in format yyyy-mm-dd and time needs to be in format hh:mmAM/PM")
                return False


        #attributes is a list of attribute names
        attributes = ['E_name', 'Time', 'NumVisits']

        #Entry is a list of the filter inputs
        entry = []

        entry.append(str(self.exhibitNameString.get()))
        entry.append(self.exhibitDateTime)
        # entry.append([self.minSpinBox.get(),self.maxSpinBox.get()])


        sql = "SELECT t1.E_Name, t1.Time, t2.Count FROM(SELECT E_Name, TIME FROM Exhibit_History WHERE U_Name = '" + self.currentUser + "' AND "

        for i in range(len(entry)):
        #min and max will never be empty
            if i == 1:
                sql = sql + ") t1 JOIN (SELECT COUNT(E_Name AND TIME) AS Count, E_Name AS Name FROM Exhibit_History WHERE U_Name = '" + self.currentUser + "' GROUP BY E_Name HAVING COUNT(E_Name AND TIME)>" + self.minSpinBox.get() + " AND COUNT(E_Name AND TIME)<" + self.maxSpinBox.get() + ") t2 ON (t2.Name = t1.E_Name);"
            elif entry[i] != "":
                sql = sql + attributes[i] + " = " + entry[i]
            else:
                sql = sql + attributes[i] + " LIKE '%'"
            if i < len(entry)-2:
                sql = sql + "AND "

        print(sql)
        self.historyResults = self.cursor.fetchall()
        print(self.historyResults)
        # (1, 'Pacific', datetime.datetime(2018, 12, 2, 14, 59, 4))

        self.timesVisited = []
        self.exhibitTime = []
        self.exhibitVisited = []

        for i in self.historyResults:
            self.timesVisited.append(i[0])
            self.exhibitVisited.append(i[1])
            self.exhibitTime.append(i[2])
            

        for i in range(len(self.historyResults)):
            self.exhibitHistoryTree.insert('', i , values=(self.exhibitVisited[i], self.exhibitTime[i], self.timesVisited[i]))


    def exhibitHistoryWindowBackButtonClicked(self):
        self.exhibitHistoryWindow.withdraw()
        self.chooseVisitorFunctionalityWindow.deiconify()

#-------------------VISITOR SHOW HISTORY------------------------------


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

        #populate exhibit menu with sql
        self.cursor.execute("SELECT Name FROM Exhibit")
        self.exhibitTuple = self.cursor.fetchall()
        self.exhibitList = []
        for i in self.exhibitTuple:
            self.exhibitList.append(i[0])

        exhibitLabel = Label(showHistoryWindow,text = "Exhibit")
        exhibitLabel.grid(row=2,column=2,pady=10)
        self.exhibitDefault = StringVar()
        self.exhibitDefault.set("")
        exhibitMenu = OptionMenu(showHistoryWindow, self.exhibitDefault, "", *self.exhibitList)
        exhibitMenu.grid(row=2, column=3,pady=10)

        dateLabel = Label(showHistoryWindow,text = "Date")
        dateLabel.grid(row=3, column=0,pady=10)

        #showDateEntry = CalendarDialog.main()
        self.showDateNameSV = StringVar()
        showDateEntry = Entry(showHistoryWindow, textvariable = self.showDateNameSV, width=20)
        showDateEntry.grid(row=3, column=1,pady=10)

        self.columns = ("1", "2", "3")

        self.selectShowTree = ttk.Treeview(showHistoryWindow, columns=self.columns, selectmode = 'extended')
        self.selectShowTree['show'] = "headings"
        self.selectShowTree.heading("1", text = "Name")
        self.selectShowTree.heading("2", text = "Date")
        self.selectShowTree.heading("3", text = "Exhibit")
        self.selectShowTree.column("1", width = 200, anchor = "center")
        self.selectShowTree.column("2", width = 200, anchor = "center")
        self.selectShowTree.column("3", width = 200, anchor = "center")
        self.selectShowTree.place(x=50, y=130,width=600)

        visitorShowHistoryTreeSort = self.selectShowTree

        for col in self.columns:
            self.selectShowTree.heading(col, command=lambda _col=col: \
                self.sortVisitorShowHistory(visitorShowHistoryTreeSort, _col, False))


        # Get all Initial Unfiltered Records of the Visitors Show History
        self.cursor.execute("SELECT Perform_Name, Performance_History.Time, E_Name FROM Performance_History JOIN Performance ON Performance.Name = Perform_Name WHERE U_Name = %s", (self.currentUser))
        self.userShowHistory = self.cursor.fetchall()
        # print(self.userShowHistory)

        self.pName = []
        self.pTime = []
        self.ename = []

        for i in self.userShowHistory:
            self.pName.append(i[0])
            self.pTime.append(i[1])
            self.ename.append(i[2])
        
        for i in range(len(self.userShowHistory)):
            self.selectShowTree.insert('', i , values=(self.pName[i], self.pTime[i], self.ename[i]))
       
        # Buttons
        findShowsButton = Button(showHistoryWindow, text="Search History", command=self.showHistoryWindowFindShowsButtonClicked)
        findShowsButton.grid(row=3,column=2,pady=10)

        backButton = Button(showHistoryWindow, text="Back", command=self.showHistoryWindowBackButtonClicked)
        backButton.place(x=310,y=370)

    def sortVisitorShowHistory(self, tv, column, resort):
        for i in self.selectShowTree.get_children():
            self.selectShowTree.delete(i)  

        attributes = ['Perform_Name', 'P.Time', 'P.E_Name']

        entry = []

        entry.append(str(self.showNameString.get()))
        entry.append(self.showDateNameSV.get())
        entry.append(str(self.exhibitDefault.get()))


        if (column == "1" and resort == False):

            sql = "SELECT Perform_Name, P.Time, E_Name FROM Performance_History JOIN Performance  AS P WHERE U_Name = '" + self.currentUser + "' AND "

            for i in range(len(entry)):
                if entry[i] != "":
                    sql = sql + attributes[i] + " = '" + entry[i] + "'"
                else:
                    sql = sql + attributes[i] + " LIKE '%'"
            #This is to check if the next box is filled as well so we add an AND statement to make sure all conditions are met. 
                if i<len(entry)-1:
                    sql = sql + " AND "
            #end of statement
            sql = sql + " ORDER BY Perform_Name ASC;"

            print(sql)

            self.cursor.execute(sql)
            self.userShowHistory = self.cursor.fetchall()

            self.pName = []
            self.pTime = []
            self.ename = []

            for i in self.userShowHistory:
                self.pName.append(i[0])
                self.pTime.append(i[1])
                self.ename.append(i[2])
            
            for i in range(len(self.userShowHistory)):
                self.selectShowTree.insert('', i , values=(self.pName[i], self.pTime[i], self.ename[i]))

            
            tv.heading(column, command=lambda: \
                self.sortVisitorShowHistory(tv, column, not resort))

        elif (column == "1" and resort == True):

            sql = "SELECT Perform_Name, P.Time, E_Name FROM Performance_History JOIN Performance  AS P WHERE U_Name = '" + self.currentUser + "' AND "

            for i in range(len(entry)):
                if entry[i] != "":
                    sql = sql + attributes[i] + " = '" + entry[i] + "'"
                else:
                    sql = sql + attributes[i] + " LIKE '%'"
            #This is to check if the next box is filled as well so we add an AND statement to make sure all conditions are met. 
                if i<len(entry)-1:
                    sql = sql + " AND "
            #end of statement
            sql = sql + " ORDER BY Perform_Name DESC;"


            self.cursor.execute(sql)
            self.userShowHistory = self.cursor.fetchall()

            self.pName = []
            self.pTime = []
            self.ename = []

            for i in self.userShowHistory:
                self.pName.append(i[0])
                self.pTime.append(i[1])
                self.ename.append(i[2])
            
            for i in range(len(self.userShowHistory)):
                self.selectShowTree.insert('', i , values=(self.pName[i], self.pTime[i], self.ename[i]))

            
            tv.heading(column, command=lambda: \
                self.sortVisitorShowHistory(tv, column, not resort))

        if (column == "2" and resort == False):

            sql = "SELECT Perform_Name, P.Time, E_Name FROM Performance_History JOIN Performance  AS P WHERE U_Name = '" + self.currentUser + "' AND "

            for i in range(len(entry)):
                if entry[i] != "":
                    sql = sql + attributes[i] + " = '" + entry[i] + "'"
                else:
                    sql = sql + attributes[i] + " LIKE '%'"
            #This is to check if the next box is filled as well so we add an AND statement to make sure all conditions are met. 
                if i<len(entry)-1:
                    sql = sql + " AND "
            #end of statement
            sql = sql + " ORDER BY P.Time ASC;"

            print(sql)

            self.cursor.execute(sql)
            self.userShowHistory = self.cursor.fetchall()

            self.pName = []
            self.pTime = []
            self.ename = []

            for i in self.userShowHistory:
                self.pName.append(i[0])
                self.pTime.append(i[1])
                self.ename.append(i[2])
            
            for i in range(len(self.userShowHistory)):
                self.selectShowTree.insert('', i , values=(self.pName[i], self.pTime[i], self.ename[i]))

            
            tv.heading(column, command=lambda: \
                self.sortVisitorShowHistory(tv, column, not resort))

        if (column == "2" and resort == True):

            sql = "SELECT Perform_Name, P.Time, E_Name FROM Performance_History JOIN Performance  AS P WHERE U_Name = '" + self.currentUser + "' AND "

            for i in range(len(entry)):
                if entry[i] != "":
                    sql = sql + attributes[i] + " = '" + entry[i] + "'"
                else:
                    sql = sql + attributes[i] + " LIKE '%'"
            #This is to check if the next box is filled as well so we add an AND statement to make sure all conditions are met. 
                if i<len(entry)-1:
                    sql = sql + " AND "
            #end of statement
            sql = sql + " ORDER BY P.Time DESC;"

            self.cursor.execute(sql)
            self.userShowHistory = self.cursor.fetchall()

            self.pName = []
            self.pTime = []
            self.ename = []

            for i in self.userShowHistory:
                self.pName.append(i[0])
                self.pTime.append(i[1])
                self.ename.append(i[2])
            
            for i in range(len(self.userShowHistory)):
                self.selectShowTree.insert('', i , values=(self.pName[i], self.pTime[i], self.ename[i]))

            
            tv.heading(column, command=lambda: \
                self.sortVisitorShowHistory(tv, column, not resort))

        if (column == "3" and resort == False):

            sql = "SELECT Perform_Name, P.Time, E_Name FROM Performance_History JOIN Performance  AS P WHERE U_Name = '" + self.currentUser + "' AND "

            for i in range(len(entry)):
                if entry[i] != "":
                    sql = sql + attributes[i] + " = '" + entry[i] + "'"
                else:
                    sql = sql + attributes[i] + " LIKE '%'"
            #This is to check if the next box is filled as well so we add an AND statement to make sure all conditions are met. 
                if i<len(entry)-1:
                    sql = sql + " AND "
            #end of statement
            sql = sql + " ORDER BY E_Name ASC;"

            print(sql)

            self.cursor.execute(sql)
            self.userShowHistory = self.cursor.fetchall()

            self.pName = []
            self.pTime = []
            self.ename = []

            for i in self.userShowHistory:
                self.pName.append(i[0])
                self.pTime.append(i[1])
                self.ename.append(i[2])
            
            for i in range(len(self.userShowHistory)):
                self.selectShowTree.insert('', i , values=(self.pName[i], self.pTime[i], self.ename[i]))

            
            tv.heading(column, command=lambda: \
                self.sortVisitorShowHistory(tv, column, not resort))

        if (column == "3" and resort == True):

            sql = "SELECT Perform_Name, P.Time, E_Name FROM Performance_History JOIN Performance  AS P WHERE U_Name = '" + self.currentUser + "' AND "

            for i in range(len(entry)):
                if entry[i] != "":
                    sql = sql + attributes[i] + " = '" + entry[i] + "'"
                else:
                    sql = sql + attributes[i] + " LIKE '%'"
            #This is to check if the next box is filled as well so we add an AND statement to make sure all conditions are met. 
                if i<len(entry)-1:
                    sql = sql + " AND "
            #end of statement
            sql = sql + " ORDER BY E_Name DESC;"

            self.cursor.execute(sql)
            self.userShowHistory = self.cursor.fetchall()

            self.pName = []
            self.pTime = []
            self.ename = []

            for i in self.userShowHistory:
                self.pName.append(i[0])
                self.pTime.append(i[1])
                self.ename.append(i[2])
            
            for i in range(len(self.userShowHistory)):
                self.selectShowTree.insert('', i , values=(self.pName[i], self.pTime[i], self.ename[i]))

            
            tv.heading(column, command=lambda: \
                self.sortVisitorShowHistory(tv, column, not resort))

    def showHistoryWindowFindShowsButtonClicked(self):

        for i in self.selectShowTree.get_children():
            self.selectShowTree.delete(i)

        self.showDateTime = self.showDateNameSV.get()

        if self.showDateTime is not "":
            try:
                datetime.strptime(self.showDateTime, '%Y-%m-%d %I:%M%p')
            except ValueError:
                messagebox.showwarning("Error!", "Date needs to be in format yyyy-mm-dd and time needs to be in format hh:mmAM/PM")
                return False


        attributes = ['Perform_Name', 'P.Time', 'P.E_Name']

        entry = []

        entry.append(str(self.showNameString.get()))
        entry.append(self.showDateTime)
        entry.append(str(self.exhibitDefault.get()))

        sql = "SELECT Perform_Name, P.Time, E_Name FROM Performance_History JOIN Performance  AS P WHERE U_Name = '" + self.currentUser + "' AND "

        for i in range(len(entry)):
            if entry[i] != "":
                sql = sql + attributes[i] + " = '" + entry[i] + "'"
            else:
                sql = sql + attributes[i] + " LIKE '%'"
        #This is to check if the next box is filled as well so we add an AND statement to make sure all conditions are met. 
            if i<len(entry)-1:
                sql = sql + " AND "
        #end of statement
        sql = sql + ";"

        print(sql)

        self.cursor.execute(sql)
        self.userShowHistory = self.cursor.fetchall()

        self.pName = []
        self.pTime = []
        self.ename = []

        for i in self.userShowHistory:
            self.pName.append(i[0])
            self.pTime.append(i[1])
            self.ename.append(i[2])
        
        for i in range(len(self.userShowHistory)):
            self.selectShowTree.insert('', i , values=(self.pName[i], self.pTime[i], self.ename[i]))

    def showHistoryWindowBackButtonClicked(self):
        self.showHistoryWindow.withdraw()
        self.chooseVisitorFunctionalityWindow.deiconify()


#-------------------VISITOR SEARCH ANIMAL-----------------------------

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

        self.columns = ("1", "2", "3", "4","5")
       
        self.selectAnimalTree = ttk.Treeview(searchAnimalWindow, columns=self.columns, selectmode="extended")
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

        selectAnimalTreeSort = self.selectAnimalTree

        for col in self.columns:
            self.selectAnimalTree.heading(col, command=lambda _col=col: \
                self.sortVisitorSearchAnimal(selectAnimalTreeSort, _col, False))

        findAnimalsButton = Button(searchAnimalWindow, text="Find Animals", command=self.searchAnimalWindowFindAnimalsButtonClicked)
        findAnimalsButton.grid(row=6,column=3)

        getDetailsButton = Button(searchAnimalWindow, text="Get Details", command=self.searchAnimalWindowGetDetailsButtonClicked)
        getDetailsButton.grid(row=6,column=2)

        backButton = Button(searchAnimalWindow, text="Back", command=self.searchAnimalWindowBackButtonClicked)
        backButton.grid(row=6,column=1)

    def sortVisitorSearchAnimal(self, tv, column, resort):
        for i in self.selectAnimalTree.get_children():
            self.selectAnimalTree.delete(i)  

        attributes = ["Name", "Species", "Type", "Age", "E_Name",]

        # Entry is a list of the filter inputs
        entry = []
        entry.append(str(self.animalNameSV.get()))
        entry.append(str(self.speciesNameSV.get()))
        entry.append(self.typeDefault.get())
        entry.append("")
        entry.append(self.exhibitDefault.get())

        if (column == "1" and resort == False):

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
            sql = sql + "ORDER BY Name ASC;"
            self.cursor.execute(sql)
            self.sortColumnsTuple = self.cursor.fetchall()

            #print(self.sortColumnsTuple)

            self.nameListSorted = []
            self.speciesListSorted = []
            self.exhibitListSorted = []
            self.ageListSorted = []
            self.typeListSorted = []

            for i in self.sortColumnsTuple:
                self.nameListSorted.append(i[2])
                self.speciesListSorted.append(i[3])
                self.exhibitListSorted.append(i[4])
                self.ageListSorted.append(i[0])
                self.typeListSorted.append(i[1])

            #print(self.nameListSorted)

            for i in range(len(self.sortColumnsTuple)):
                self.selectAnimalTree.insert('', i, values=(self.nameListSorted[i], self.speciesListSorted[i], self.exhibitListSorted[i], self.ageListSorted[i], self.typeListSorted[i]))

            tv.heading(column, command=lambda: \
                self.sortVisitorSearchAnimal(tv, column, not resort))

        elif (column == "1" and resort == True):
            #print("reversed")
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
            sql = sql + "ORDER BY Name DESC;"

            self.cursor.execute(sql)

            self.sortColumnsTuple = self.cursor.fetchall()

            #print(self.sortColumnsTuple)

            self.nameListSorted = []
            self.speciesListSorted = []
            self.exhibitListSorted = []
            self.ageListSorted = []
            self.typeListSorted = []

            for i in self.sortColumnsTuple:
                self.nameListSorted.append(i[2])
                self.speciesListSorted.append(i[3])
                self.exhibitListSorted.append(i[4])
                self.ageListSorted.append(i[0])
                self.typeListSorted.append(i[1])

            #print(self.nameListSorted)

            for i in range(len(self.sortColumnsTuple)):
                self.selectAnimalTree.insert('', i, values=(self.nameListSorted[i], self.speciesListSorted[i], self.exhibitListSorted[i], self.ageListSorted[i], self.typeListSorted[i]))

            tv.heading(column, command=lambda: \
                self.sortVisitorSearchAnimal(tv, column, not resort))
        elif (column == "2" and resort == False):
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
            sql = sql + "ORDER BY Species ASC;"

            self.cursor.execute(sql)

            self.sortColumnsTuple = self.cursor.fetchall()

            #print(self.sortColumnsTuple)

            self.nameListSorted = []
            self.speciesListSorted = []
            self.exhibitListSorted = []
            self.ageListSorted = []
            self.typeListSorted = []

            for i in self.sortColumnsTuple:
                self.nameListSorted.append(i[2])
                self.speciesListSorted.append(i[3])
                self.exhibitListSorted.append(i[4])
                self.ageListSorted.append(i[0])
                self.typeListSorted.append(i[1])

            #print(self.nameListSorted)

            for i in range(len(self.sortColumnsTuple)):
                self.selectAnimalTree.insert('', i, values=(self.nameListSorted[i], self.speciesListSorted[i], self.exhibitListSorted[i], self.ageListSorted[i], self.typeListSorted[i]))

            tv.heading(column, command=lambda: \
                self.sortVisitorSearchAnimal(tv, column, not resort))
        elif (column == "2" and resort == True): 
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
            sql = sql + "ORDER BY Species DESC;"

            self.cursor.execute(sql)

            self.sortColumnsTuple = self.cursor.fetchall()

            #print(self.sortColumnsTuple)

            self.nameListSorted = []
            self.speciesListSorted = []
            self.exhibitListSorted = []
            self.ageListSorted = []
            self.typeListSorted = []

            for i in self.sortColumnsTuple:
                self.nameListSorted.append(i[2])
                self.speciesListSorted.append(i[3])
                self.exhibitListSorted.append(i[4])
                self.ageListSorted.append(i[0])
                self.typeListSorted.append(i[1])

            #print(self.nameListSorted)

            for i in range(len(self.sortColumnsTuple)):
                self.selectAnimalTree.insert('', i, values=(self.nameListSorted[i], self.speciesListSorted[i], self.exhibitListSorted[i], self.ageListSorted[i], self.typeListSorted[i]))

            tv.heading(column, command=lambda: \
                self.sortVisitorSearchAnimal(tv, column, not resort))

        elif (column == "3" and resort == False):
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
            sql = sql + "ORDER BY E_Name ASC;"

            self.cursor.execute(sql)

            self.sortColumnsTuple = self.cursor.fetchall()

            #print(self.sortColumnsTuple)

            self.nameListSorted = []
            self.speciesListSorted = []
            self.exhibitListSorted = []
            self.ageListSorted = []
            self.typeListSorted = []

            for i in self.sortColumnsTuple:
                self.nameListSorted.append(i[2])
                self.speciesListSorted.append(i[3])
                self.exhibitListSorted.append(i[4])
                self.ageListSorted.append(i[0])
                self.typeListSorted.append(i[1])

            #print(self.nameListSorted)

            for i in range(len(self.sortColumnsTuple)):
                self.selectAnimalTree.insert('', i, values=(self.nameListSorted[i], self.speciesListSorted[i], self.exhibitListSorted[i], self.ageListSorted[i], self.typeListSorted[i]))

            tv.heading(column, command=lambda: \
                self.sortVisitorSearchAnimal(tv, column, not resort))
        elif (column == "3" and resort == True): 
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
            sql = sql + "ORDER BY E_Name DESC;"

            self.cursor.execute(sql)

            self.sortColumnsTuple = self.cursor.fetchall()

            #print(self.sortColumnsTuple)

            self.nameListSorted = []
            self.speciesListSorted = []
            self.exhibitListSorted = []
            self.ageListSorted = []
            self.typeListSorted = []

            for i in self.sortColumnsTuple:
                self.nameListSorted.append(i[2])
                self.speciesListSorted.append(i[3])
                self.exhibitListSorted.append(i[4])
                self.ageListSorted.append(i[0])
                self.typeListSorted.append(i[1])

            #print(self.nameListSorted)

            for i in range(len(self.sortColumnsTuple)):
                self.selectAnimalTree.insert('', i, values=(self.nameListSorted[i], self.speciesListSorted[i], self.exhibitListSorted[i], self.ageListSorted[i], self.typeListSorted[i]))

            tv.heading(column, command=lambda: \
                self.sortVisitorSearchAnimal(tv, column, not resort))

        elif (column == "4" and resort == False):
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
            sql = sql + "ORDER BY Age ASC;"

            self.cursor.execute(sql)

            self.sortColumnsTuple = self.cursor.fetchall()

            #print(self.sortColumnsTuple)

            self.nameListSorted = []
            self.speciesListSorted = []
            self.exhibitListSorted = []
            self.ageListSorted = []
            self.typeListSorted = []

            for i in self.sortColumnsTuple:
                self.nameListSorted.append(i[2])
                self.speciesListSorted.append(i[3])
                self.exhibitListSorted.append(i[4])
                self.ageListSorted.append(i[0])
                self.typeListSorted.append(i[1])

            #print(self.nameListSorted)

            for i in range(len(self.sortColumnsTuple)):
                self.selectAnimalTree.insert('', i, values=(self.nameListSorted[i], self.speciesListSorted[i], self.exhibitListSorted[i], self.ageListSorted[i], self.typeListSorted[i]))

            tv.heading(column, command=lambda: \
                self.sortVisitorSearchAnimal(tv, column, not resort))
        elif (column == "4" and resort == True): 
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
            sql = sql + "ORDER BY Age DESC;"

            self.cursor.execute(sql)

            self.sortColumnsTuple = self.cursor.fetchall()

            #print(self.sortColumnsTuple)

            self.nameListSorted = []
            self.speciesListSorted = []
            self.exhibitListSorted = []
            self.ageListSorted = []
            self.typeListSorted = []

            for i in self.sortColumnsTuple:
                self.nameListSorted.append(i[2])
                self.speciesListSorted.append(i[3])
                self.exhibitListSorted.append(i[4])
                self.ageListSorted.append(i[0])
                self.typeListSorted.append(i[1])

            #print(self.nameListSorted)

            for i in range(len(self.sortColumnsTuple)):
                self.selectAnimalTree.insert('', i, values=(self.nameListSorted[i], self.speciesListSorted[i], self.exhibitListSorted[i], self.ageListSorted[i], self.typeListSorted[i]))

            tv.heading(column, command=lambda: \
                self.sortVisitorSearchAnimal(tv, column, not resort))

        elif (column == "5" and resort == False):
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
            sql = sql + "ORDER BY Type ASC;"

            self.cursor.execute(sql)

            self.sortColumnsTuple = self.cursor.fetchall()

            #print(self.sortColumnsTuple)

            self.nameListSorted = []
            self.speciesListSorted = []
            self.exhibitListSorted = []
            self.ageListSorted = []
            self.typeListSorted = []

            for i in self.sortColumnsTuple:
                self.nameListSorted.append(i[2])
                self.speciesListSorted.append(i[3])
                self.exhibitListSorted.append(i[4])
                self.ageListSorted.append(i[0])
                self.typeListSorted.append(i[1])

            #print(self.nameListSorted)

            for i in range(len(self.sortColumnsTuple)):
                self.selectAnimalTree.insert('', i, values=(self.nameListSorted[i], self.speciesListSorted[i], self.exhibitListSorted[i], self.ageListSorted[i], self.typeListSorted[i]))

            tv.heading(column, command=lambda: \
                self.sortVisitorSearchAnimal(tv, column, not resort))
        elif (column == "5" and resort == True): 
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
            sql = sql + "ORDER BY Type DESC;"

            self.cursor.execute(sql)

            self.sortColumnsTuple = self.cursor.fetchall()

            #print(self.sortColumnsTuple)

            self.nameListSorted = []
            self.speciesListSorted = []
            self.exhibitListSorted = []
            self.ageListSorted = []
            self.typeListSorted = []

            for i in self.sortColumnsTuple:
                self.nameListSorted.append(i[2])
                self.speciesListSorted.append(i[3])
                self.exhibitListSorted.append(i[4])
                self.ageListSorted.append(i[0])
                self.typeListSorted.append(i[1])

            #print(self.nameListSorted)

            for i in range(len(self.sortColumnsTuple)):
                self.selectAnimalTree.insert('', i, values=(self.nameListSorted[i], self.speciesListSorted[i], self.exhibitListSorted[i], self.ageListSorted[i], self.typeListSorted[i]))

            tv.heading(column, command=lambda: \
                self.sortVisitorSearchAnimal(tv, column, not resort))

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

    def searchAnimalWindowGetDetailsButtonClicked(self):
        if not self.selectAnimalTree.focus():
            messagebox.showwarning("Error","You haven't selected any Animals.")
            return False

        treeIndexString = self.selectAnimalTree.focus()
        valueDetail = self.selectAnimalTree.item(treeIndexString)

        valueslist = list(valueDetail.values())
        valueslist = valueslist[2]
        # print(valueslist)
        # ['Goldy', 'Goldfish', 'Pacific', 1, 'fish']
        self.exhibitOfInterest = valueslist[2]
        self.searchAnimalWindow.destroy()
        self.createExhibitDetailWindow()
        self.buildExhibitDetailWindow(self.exhibitDetailWindow)


    def searchAnimalWindowBackButtonClicked(self):
        self.searchAnimalWindow.destroy()
        self.chooseVisitorFunctionalityWindow.deiconify()

#-------------------VISITOR EXHIBIT DETAIL------------------------------


    def createExhibitDetailWindow(self):
            # Create blank chooseFunctionalityWindow
            self.exhibitDetailWindow = Toplevel()
            self.exhibitDetailWindow.title("Zoo Atlanta")
            self.exhibitDetailWindow.geometry("800x600")
            self.exhibitDetailWindow.resizable(0,0)

    def buildExhibitDetailWindow(self, exhibitDetailWindow):
        # Add component to chooseFunctionalityWindow

        self.cursor.execute("SELECT * FROM (SELECT Name, Size, Has_Water FROM Exhibit WHERE Name = %s) AS t1 JOIN (SELECT E_Name, COUNT(Name) FROM Animal GROUP BY E_Name) AS t2 ON t2.E_Name = t1.Name JOIN (SELECT E_Name,Name as A_Name, Species FROM Animal) AS t3 ON t2.E_Name = t3.E_Name;", (self.exhibitOfInterest))
        self.exhibitFacts = self.cursor.fetchall()
        # print(self.exhibitFacts)
        #(('Pacific', 850, b'\x01', 'Pacific', 2, 'Pacific', 'Goldy', 'Goldfish'), ('Pacific', 850, b'\x01', 'Pacific', 2, 'Pacific', 'Nemo', 'Clownfish'))

        self.exhibitName = self.exhibitOfInterest
        self.eSize = ""
        self.numAnimals = 0
        self.animalName = []
        self.species = []
        self.hasWater = False

        for i in self.exhibitFacts:
            self.eSize = i[1]
            # print(ord(i[2]))
            if ord(i[2]) == 1:
                self.hasWater = True
            self.numAnimals = i[4]
            self.animalName.append(i[6])
            self.species.append(i[7])

        # Title Label
        exhibitDetailLabel = Label(exhibitDetailWindow, text="Exhibit Details",font = "Verdana 16 bold ")
        # chooseFunctionalityLabel.grid(row=1, column=1, sticky=W+E)
        exhibitDetailLabel.place(x=400, y = 25, anchor="center")


        ## Name , Num Animals, Water Feature, List of Animals in the exhibit
        nameLabel = Label(exhibitDetailWindow, text = "Name:")
        nameLabel.place(x=355, y=150, anchor="center")

        foundName = Label(exhibitDetailWindow, text = self.exhibitName)
        foundName.place(x = 415, y=150, anchor="center")
        
        numAnimalsLabel= Label(exhibitDetailWindow, text = "Number of Animals:")
        numAnimalsLabel.place(x=400, y=175, anchor="center")

        actualNumAnimalsLabel= Label(exhibitDetailWindow, text = self.numAnimals)
        actualNumAnimalsLabel.place(x=500, y=175, anchor="center")

        sizeLabel= Label(exhibitDetailWindow, text = "Size:")
        sizeLabel.place(x=350, y=200, anchor="center")

        actualSizeLabel= Label(exhibitDetailWindow, text = self.eSize)
        actualSizeLabel.place(x=400, y=200, anchor="center")

        waterFeatureLabel= Label(exhibitDetailWindow, text = "Water Feature:")
        waterFeatureLabel.place(x=375, y=225, anchor="center")

        hasWaterFeatureLabel= Label(exhibitDetailWindow, text = str(self.hasWater))
        hasWaterFeatureLabel.place(x=455, y=225, anchor="center")


        # Buttons

        logVisitButton = Button(exhibitDetailWindow, text="Log Visit", command=self.exhibitDetailWindowLogVisitButtonClicked)
        # logVisitButton.grid(row=8, column=2,sticky=E)
        logVisitButton.grid(row=4)
        logVisitButton.place(x = 400, y=300, anchor="center")


        getDetailsButton = Button(exhibitDetailWindow, text="Get Animal Details", command=self.exhibitDetailsAnimalGetDetailsButtonClicked)
        getDetailsButton.place(x = 500, y=575, anchor="center")

        backButton = Button(exhibitDetailWindow, text="Back", command=self.exhibitDetailWindowBackButtonClicked)
        backButton.place(x = 300, y=575, anchor="center")

        self.columns = ("1", "2")

        # Table of Animals in Exhibit
        self.detailExhibitTree = ttk.Treeview(exhibitDetailWindow, columns=self.columns, selectmode="extended")
        self.detailExhibitTree['show'] = "headings"
        self.detailExhibitTree.heading("1", text = "Name")
        self.detailExhibitTree.heading("2", text = "Species")
        self.detailExhibitTree.column("1", width = 150, anchor = "center")
        self.detailExhibitTree.column("2", width = 150, anchor = "center")
        # detailExhibitTree.grid(row=5, columnspan=4, sticky = 'nsew')
        self.detailExhibitTree.place(x=400, y=450, anchor="center")

        visitorExhibitDetailSort = self.detailExhibitTree

        for col in self.columns:
            self.detailExhibitTree.heading(col, command=lambda _col=col: \
                self.sortVisitorExhibitDetail(visitorExhibitDetailSort, _col, False))


        for i in range(len(self.exhibitFacts)):
            self.detailExhibitTree.insert('', i , values=(self.animalName[i], self.species[i]))

    def sortVisitorExhibitDetail(self, tv, column, resort):

        for i in self.detailExhibitTree.get_children():
            self.detailExhibitTree.delete(i)  


        if (column == "1" and resort == False):

            self.cursor.execute("SELECT * FROM (SELECT Name, Size, Has_Water FROM Exhibit WHERE Name = %s) AS t1 JOIN (SELECT E_Name, COUNT(Name) FROM Animal GROUP BY E_Name) AS t2 ON t2.E_Name = t1.Name JOIN (SELECT E_Name,Name as A_Name, Species FROM Animal) AS t3 ON t2.E_Name = t3.E_Name ORDER BY A_Name ASC;", (self.exhibitOfInterest))
            self.exhibitFacts = self.cursor.fetchall()

            #print(self.exhibitFacts)
    
            self.animalName = []
            self.species = []


            for i in self.exhibitFacts:
                self.animalName.append(i[6])
                self.species.append(i[7])


            for i in range(len(self.exhibitFacts)):
                self.detailExhibitTree.insert('', i, values=(self.animalName[i], self.species[i]))

            tv.heading(column, command=lambda: \
                self.sortVisitorExhibitDetail(tv, column, not resort))

        elif (column == "1" and resort == True):

            self.cursor.execute("SELECT * FROM (SELECT Name, Size, Has_Water FROM Exhibit WHERE Name = %s) AS t1 JOIN (SELECT E_Name, COUNT(Name) FROM Animal GROUP BY E_Name) AS t2 ON t2.E_Name = t1.Name JOIN (SELECT E_Name,Name as A_Name, Species FROM Animal) AS t3 ON t2.E_Name = t3.E_Name ORDER BY A_Name DESC;", (self.exhibitOfInterest))
            self.exhibitFacts = self.cursor.fetchall()

            #print(self.exhibitFacts)
    
            self.animalName = []
            self.species = []


            for i in self.exhibitFacts:
                self.animalName.append(i[6])
                self.species.append(i[7])


            for i in range(len(self.exhibitFacts)):
                self.detailExhibitTree.insert('', i, values=(self.animalName[i], self.species[i]))

            tv.heading(column, command=lambda: \
                self.sortVisitorExhibitDetail(tv, column, not resort))

        elif (column == "2" and resort == False):

            self.cursor.execute("SELECT * FROM (SELECT Name, Size, Has_Water FROM Exhibit WHERE Name = %s) AS t1 JOIN (SELECT E_Name, COUNT(Name) FROM Animal GROUP BY E_Name) AS t2 ON t2.E_Name = t1.Name JOIN (SELECT E_Name,Name as A_Name, Species FROM Animal) AS t3 ON t2.E_Name = t3.E_Name ORDER BY Species ASC;", (self.exhibitOfInterest))
            self.exhibitFacts = self.cursor.fetchall()

            #print(self.exhibitFacts)
    
            self.animalName = []
            self.species = []


            for i in self.exhibitFacts:
                self.animalName.append(i[6])
                self.species.append(i[7])


            for i in range(len(self.exhibitFacts)):
                self.detailExhibitTree.insert('', i, values=(self.animalName[i], self.species[i]))

            tv.heading(column, command=lambda: \
                self.sortVisitorExhibitDetail(tv, column, not resort))

        elif (column == "2" and resort == True):

            self.cursor.execute("SELECT * FROM (SELECT Name, Size, Has_Water FROM Exhibit WHERE Name = %s) AS t1 JOIN (SELECT E_Name, COUNT(Name) FROM Animal GROUP BY E_Name) AS t2 ON t2.E_Name = t1.Name JOIN (SELECT E_Name,Name as A_Name, Species FROM Animal) AS t3 ON t2.E_Name = t3.E_Name ORDER BY Species DESC;", (self.exhibitOfInterest))
            self.exhibitFacts = self.cursor.fetchall()

            #print(self.exhibitFacts)
    
            self.animalName = []
            self.species = []


            for i in self.exhibitFacts:
                self.animalName.append(i[6])
                self.species.append(i[7])


            for i in range(len(self.exhibitFacts)):
                self.detailExhibitTree.insert('', i, values=(self.animalName[i], self.species[i]))

            tv.heading(column, command=lambda: \
                self.sortVisitorExhibitDetail(tv, column, not resort))


    def exhibitDetailWindowBackButtonClicked(self):
        self.exhibitDetailWindow.destroy()
        self.chooseVisitorFunctionalityWindow.deiconify()

    # Log Visit Button

    def exhibitDetailWindowLogVisitButtonClicked(self):
            self.cursor.execute("INSERT INTO Exhibit_History(U_Name, E_Name, Time) VALUES (%s, %s, %s)",(self.currentUser, self.exhibitName, datetime.now()))
            messagebox.showwarning("Exhibit Visit","You have successfully logged your visit!")

    def exhibitDetailsAnimalGetDetailsButtonClicked(self):
        if not self.detailExhibitTree.focus():
            messagebox.showwarning("Error","You haven't selected an Animal.")
            return False

        treeIndexString = self.detailExhibitTree.focus()
        valueDetail = self.detailExhibitTree.item(treeIndexString)

        valueslist = list(valueDetail.values())
        valueslist = valueslist[2]
        # print(valueslist)
        # ['Goldy', 'Goldfish', 'Pacific', 1, 'fish']
        self.animalOfInterest = valueslist[0]
        self.animalSpeciesOfInterest = valueslist[1]
        self.exhibitDetailWindow.withdraw()
        self.createAnimalDetailWindow()
        self.buildAnimalDetailWindow(self.animalDetailWindow)

#-------------------VISITOR ANIMAL DETAIL------------------------------
# Can only get to from Exhibit detail page

    def createAnimalDetailWindow(self):
            # Create blank chooseFunctionalityWindow
            self.animalDetailWindow = Toplevel()
            self.animalDetailWindow.title("Zoo Atlanta")
            self.animalDetailWindow.geometry("800x600")
            self.animalDetailWindow.resizable(0,0)

    def buildAnimalDetailWindow(self, animalDetailWindow):
         # Title Label

        self.cursor.execute("SELECT * FROM Animal WHERE Name = %s AND Species = %s", (self.animalOfInterest, self.animalSpeciesOfInterest))
        self.animaldetailfocus = self.cursor.fetchall()
        # print(self.animaldetailfocus)
        # ('1', 'fish', 'Goldy', 'Goldfish', 'Pacific')
        results = self.animaldetailfocus[0]

        age = results[0]
        animaltype = results[1]
        name = results[2]
        species = results[3]
        animalExhibit = results[4]




        titleLabel= Label(animalDetailWindow,text = "Animal Details", font = "Verdana 16 bold ")
        titleLabel.place(x=350,y=25)
        # titleLabel.grid(row=1, column=2)

        # Labels
        nameLabel = Label(animalDetailWindow,text = "Name:")
        nameLabel.place(x=130,y=60)

        actualnameLabel = Label(animalDetailWindow,text = name)
        actualnameLabel.place(x=200,y=60)

        speciesLabel = Label(animalDetailWindow,text = "Species:")
        speciesLabel.place(x=130,y=90)

        actualspeciesLabel = Label(animalDetailWindow,text = species)
        actualspeciesLabel.place(x=200,y=90)

        exhibitLabel = Label(animalDetailWindow,text = "Exhibit:")
        exhibitLabel.place(x=130,y=120)

        actualexhibitLabel = Label(animalDetailWindow,text = animalExhibit)
        actualexhibitLabel.place(x=200,y=120)

        ageLabel = Label(animalDetailWindow,text = "Age:")
        ageLabel.place(x=130,y=150)

        actualageLabel = Label(animalDetailWindow,text = age)
        actualageLabel.place(x=200,y=150)

        typeLabel = Label(animalDetailWindow,text = "Type:")
        typeLabel.place(x=130,y=180)

        actualtypeLabel = Label(animalDetailWindow,text = animaltype)
        actualtypeLabel.place(x=200,y=180)

        # Back Button
        backButton = Button(animalDetailWindow, text="Back", command=self.animalDetailWindowBackButtonClicked)
        backButton.place(x=400,y=370)



    def animalDetailWindowBackButtonClicked(self):
        self.animalDetailWindow.destroy()
        self.exhibitDetailWindow.deiconify()


#--------------------Database Connection-----------------
    def connect(self):
        try:
            db = pymysql.connect(host = 'academic-mysql.cc.gatech.edu',
                                 db = 'cs4400_group33', user = 'cs4400_group33', passwd = '9dpzV4ce')
            return db
        except:
            messagebox.showwarning('Error!','Cannot connect. Please check your internet connection.')
            return False



a=ATLzoo()
a.db.close()
