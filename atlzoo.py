from tkinter import *
from PIL import ImageTk, Image
import pymysql
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime, timedelta
import decimal




class ATLzoo:
    def __init__(self):
        # Invoke createLoginWindow; Invoke buildLoginWindow, Set loginWindow as mainloop
        #Connect to the database

        self.db = self.connect()
        self.cursor = self.db.cursor()
        self.currentUser = ""
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
        usernameAndPasswordMatch = self.cursor.execute(
           "SELECT * FROM User WHERE (Username = %s AND Password = %s)", (self.username, self.password))
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
        self.confirmPassword = self.registrationConfirmPassword.get()
        
        if not self.username:
            messagebox.showwarning("Username input is empty", "Please enter username.")
            return False
        if not self.emailAddress:
            messagebox.showwarning("E-mail input is empty", "Please enter E-mail.")
            return False
        if not self.password:
            messagebox.showwarning("Password input is empty", "Please enter password")
            return False
        if not self.confirmPassword:
            messagebox.showwarning("Confirm password input is empty", "Please enter confirm password")
            return False

        isUsername = self.cursor.execute("SELECT * FROM User WHERE Username = %s", self.username)
        if isUsername:
           messagebox.showwarning("This username has been used.",
                                  "Please input another username.")
           return False
        isEmail = self.cursor.execute("SELECT * FROM User WHERE Email = %s", self.emailAddress)
        if isEmail:
           messagebox.showwarning("This E-mail address has been used.",
                                  "Please input another E-mail address.")
           return False
        if not (self.password == self.confirmPassword):
           messagebox.showwarning("Password does not match the confirm password.",
                                  "Please reconfirm the password.")
           return False
        messagebox.showinfo("info","Registered successfully!")
        self.cursor.execute("INSERT INTO User VALUES (%s, %s, %s, %s)", (self.username, self.password, self.emailAddress, "visitor"))
        # self.cursor.execute("INSERT INTO User VALUES (%s, %s)", (self.username, self.password))
        self.currentUser = self.username
        self.createChooseFunctionalityWindow()
        self.buildChooseFunctionalityWindow(self.visitorFunctionalityWindow)
        self.newUserRegistrationWindow.destroy()


    def newUserRegistrationWindowCreateStaffButtonClicked(self):
        # Click the Create Button on New User Registration Window:
        # Invoke createChooseFunctionalityWindow; Invoke buildChooseFunctionalityWindow;
        # Destroy New User Registration Window
        self.username = self.registrationUsername.get()
        self.emailAddress = self.registrationEmailAddress.get()
        self.password = self.registrationPassword.get()
        self.confirmPassword = self.registrationConfirmPassword.get()
        
        if not self.username:
            messagebox.showwarning("Username input is empty", "Please enter username.")
            return False
        if not self.emailAddress:
            messagebox.showwarning("E-mail input is empty", "Please enter E-mail.")
            return False
        if not self.password:
            messagebox.showwarning("Password input is empty", "Please enter password")
            return False
        if not self.confirmPassword:
            messagebox.showwarning("Confirm password input is empty", "Please enter confirm password")
            return False

        isUsername = self.cursor.execute("SELECT * FROM User WHERE Username = %s", self.username)
        if isUsername:
           messagebox.showwarning("This username has been used.",
                                  "Please input another username.")
           return False
        isEmail = self.cursor.execute("SELECT * FROM User WHERE Email = %s", self.emailAddress)
        if isEmail:
           messagebox.showwarning("This E-mail address has been used.",
                                  "Please input another E-mail address.")
           return False
        if not (self.password == self.confirmPassword):
           messagebox.showwarning("Password does not match the confirm password.",
                                  "Please reconfirm the password.")
           return False
        messagebox.showinfo("info","Registered successfully!")
        self.cursor.execute("INSERT INTO User VALUES (%s, %s, %s, %s)", (self.username, self.password, self.emailAddress, "staff"))
        # self.cursor.execute("INSERT INTO User VALUES (%s, %s)", (self.username, self.password))
        self.currentUser = self.username
        self.createChooseFunctionalityWindow()
        self.buildChooseFunctionalityWindow(self.staffFunctionalityWindow)
        self.newUserRegistrationWindow.destroy()

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
        viewShowsLabel.place(x=400, y = 200, anchor="center")

        # View Animals Label
        viewAnimalsLabel = Label(chooseAdminFunctionalityWindow, text="View Animals", font = "Verdana 13")
        # viewAnimalsLabel.grid(row=4,column=1)
        viewAnimalsLabel.bind("<ButtonPress-1>", self.chooseAdminFunctionalityWindowViewAnimalsLabelClicked)
        viewAnimalsLabel.place(x=400, y = 300, anchor="center")

        # View Staff
        viewStaffLabel = Label(chooseAdminFunctionalityWindow, text="View Staff", font = "Verdana 13")
        # viewStaffLabel.grid(row=5,column=1)
        viewStaffLabel.bind("<ButtonPress-1>", self.chooseAdminFunctionalityWindowViewStaffLabelClicked)
        viewStaffLabel.place(x=400, y = 400, anchor="center")


        # View Show History Label
        viewShowAdd = Label(chooseAdminFunctionalityWindow, text="Add Show", font = "Verdana 13")
        # viewReviewLabel.grid(row=6,column=1)
        viewShowAdd.bind("<ButtonPress-1>", self.chooseAdminFunctionalityWindowViewShowAddLabelClicked)
        viewShowAdd.place(x=400, y = 500, anchor="center")

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
        self.createViewShowsWindow()
        self.buildViewShowsWindow(self.viewShowWindow)
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
        self.createViewShowAddWindow()
        self.buildViewShowAddWindow(self.viewShowAddWindow)
        self.chooseAdminFunctionalityWindow.withdraw()

    def chooseAdminFunctionalityWindowLogOutButtonClicked(self):
        # Click Log Out Buttion on Choose Functionality Window:
        # Destroy Choose Functionality Window
        # Display Login Window
        self.chooseAdminFunctionalityWindow.destroy()
        self.loginWindow.deiconify()

#--------------------Staff Functionality Window-----------------

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


        exhibitLabel = Label(searchStaffAnimalsWindow,text = "Exhibit")
        exhibitLabel.grid(row=4,column=0)
        exhibitDefault = StringVar()
        exhibitDefault.set("options")
        exhibitMenu = OptionMenu(searchStaffAnimalsWindow, exhibitDefault, "Pacific","Jungle","Sahara","Mountainous","Birds")
        exhibitMenu.grid(row=4, column=1)

        minLabel=Label(searchStaffAnimalsWindow,text="Min")
        minLabel.grid(row=2,column=3, sticky=W)

        maxLabel=Label(searchStaffAnimalsWindow,text="Max")
        maxLabel.grid(row=2,column=4, sticky=W)

        ageLabel = Label(searchStaffAnimalsWindow,text = "Age")
        ageLabel.grid(row=3,column=2)

        minDefault = StringVar()
        minDefault.set("3")
        minMenu = OptionMenu(searchStaffAnimalsWindow, minDefault, "0","1","2","3","4","5")
        minMenu.grid(row=3, column=3,pady=10,sticky=W)

        maxDefault = StringVar()
        maxDefault.set("3")
        maxMenu = OptionMenu(searchStaffAnimalsWindow, maxDefault, "0", "1","2","3","4","5")
        maxMenu.grid(row=3, column=4,pady=10, sticky=W)


        typeLabel = Label(searchStaffAnimalsWindow,text = "Type")
        typeLabel.grid(row=4, column=2)
        # Name Entry
        typeDefault = StringVar()
        typeDefault.set("mammal")
        typeMenu = OptionMenu(searchStaffAnimalsWindow, typeDefault, "mammal", "bird", "amphibian", "reptile", "fish", "invertebrate")
        typeMenu.grid(row=4, column=3, sticky=W)
       
        selectAnimalTree = ttk.Treeview(searchStaffAnimalsWindow, columns=("Name", "Size", "Exhibit", "Age"))
        selectAnimalTree.heading('#0', text = "Name")
        selectAnimalTree.heading('#1', text = "Species")
        selectAnimalTree.heading('#2', text = "Exhibit")
        selectAnimalTree.heading('#3', text = "Age")
        selectAnimalTree.heading('#4', text = "Type")
        selectAnimalTree.column('#0', width = 150, anchor = "center")
        selectAnimalTree.column('#1', width = 150, anchor = "center")
        selectAnimalTree.column('#2', width = 150, anchor = "center")
        selectAnimalTree.column('#3', width = 150, anchor = "center")
        selectAnimalTree.column('#4', width = 150, anchor = "center")
        selectAnimalTree.grid(row=5, columnspan=4, sticky = 'nsew')


        # self.cursor.execute( "SELECT * FROM Animal WHERE (Name = %s or %b) AND (Species = %s or %b) AND (Type = %s or %b)” ," (Name, Species,Type))

        findAnimalsButton = Button(searchStaffAnimalsWindow, text="Find Animals", command=self.searchStaffAnimalsWindowFindAnimalsButtonClicked)
        findAnimalsButton.grid(row=6,column=3)

        backButton = Button(searchStaffAnimalsWindow, text="Back", command=self.searchStaffAnimalsWindowBackButtonClicked)
        backButton.grid(row=6,column=1)


    def searchStaffAnimalsWindowFindAnimalsButtonClicked(self):

        self.searchStaffAnimalsWindow.destroy()
        self.createAnimalDetailWindow()

    def  searchStaffAnimalsWindowBackButtonClicked(self):
        self.searchStaffAnimalsWindow.withdraw()
        self.chooseStaffFunctionalityWindow.deiconify()
        # import staffFunctionality


    def createSearchAnimalWindow(self):
        # Create blank Search Animal Window
        self.searchAnimalWindow=Toplevel()
        self.searchAnimalWindow.title("Zoo Atlanta")
        self.searchAnimalWindow.geometry("600x600")

    def buildSearchAnimalWindow(self,searchAnimalWindow):

 
        titleLabel= Label(searchAnimalWindow,text = "Animal Detail", font = "Verdana 16 bold ")
        titleLabel.grid(row=1,column=1,sticky=W+E,pady=10)

        nameLabel = Label(searchAnimalWindow,text = "Name:")
        nameLabel.grid(row=2, column=0,pady=10)

        speciesLabel = Label(searchAnimalWindow, text="Species:")
        speciesLabel.grid(row=2, column=1,pady=10)
        
        ageLabel = Label(searchAnimalWindow,text = "Age:")
        ageLabel.grid(row=2,column=2,pady=10)

        exhibitLabel = Label(searchAnimalWindow,text = "Exhibit:")
        exhibitLabel.grid(row=3,column=0,pady=10)

        typeLabel = Label(searchAnimalWindow,text = "Type:")
        typeLabel.grid(row=3,column=1,pady=10)



        self.animalCareNotes = StringVar()
        animalCareEntry = Entry(searchAnimalWindow, textvariable=self.animalCareNotes, width=20)
        animalCareEntry.grid(row=4, column=0,pady=10, padx=10)

        logCareButton = Button(searchAnimalWindow, text="Log Notes", command=self.logAnimalNotesButtonClicked)
        logCareButton.grid(row=4,column=1,pady=10)
        
        selectAnimalTree = ttk.Treeview(searchAnimalWindow, columns=("Staff Member", "Note", "Time"))
        selectAnimalTree.heading('#0', text = "Staff Member")
        selectAnimalTree.heading('#1', text = "Note")
        selectAnimalTree.heading('#2', text = "Time")
        selectAnimalTree.column('#0', width = 150, anchor = "center")
        selectAnimalTree.column('#1', width = 150, anchor = "center")
        selectAnimalTree.column('#2', width = 150, anchor = "center")
        selectAnimalTree.place(x=20, y=200,width=450)

        backButton = Button(searchAnimalWindow, text="Back", command=self.searchAnimalWindowBackButtonClicked)
        backButton.place(x=240,y=440)


    def logAnimalNotesButtonClicked(self):

        self.searchAnimalWindow.destroy()
        self.createAnimalDetailWindow()

    def  searchAnimalWindowBackButtonClicked(self):
        self.searchAnimalWindow.destroy()


    def createStaffShowHistoryWindow(self):
        # Create blank Search Animal Window
        self.staffShowHistoryWindow=Toplevel()
        self.staffShowHistoryWindow.title("Zoo Atlanta")
        self.staffShowHistoryWindow.geometry("800x600")

    def buildStaffShowHistoryWindow(self, staffShowHistoryWindow):
  
        titleLabel= Label(staffShowHistoryWindow,text = "Staff - Show History", font = "Verdana 16 bold ")
        titleLabel.grid(row=1,column=2, sticky=W+E, padx=200)


        staffShowTree = ttk.Treeview(staffShowHistoryWindow, columns=("1", "2", "3"))
        staffShowTree['show'] = "headings"
        staffShowTree.heading("1", text="Name")
        staffShowTree.heading("2", text="Time")
        staffShowTree.heading("3", text="Exhibit")
        staffShowTree.column("1", width=200, anchor="center")
        staffShowTree.column("2", width= 200, anchor="center")
        staffShowTree.column("3", width=200, anchor="center")

        staffShowTree.place(x=20,y=60,width=600)

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
            staffShowTree.insert('', i , values=(self.performanceName[i], self.showTimes[i], self.showExhibit[i]))

        backButton = Button(staffShowHistoryWindow, text="Back", command=self.staffShowHistoryWindowBackButtonClicked)
        backButton.place(x=290, y=300)


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
        # Click Log Out Buttion on Choose Functionality Window:
        # Destroy Choose Functionality Window
        # Display Login Window
        self.chooseVisitorFunctionalityWindow.destroy()
        self.loginWindow.deiconify()

#-------------------VISITOR PAGES------------------------------


    def createVisitorSearchShowsWindow(self):
        self.searchVisitorShowsWindow=Toplevel()
        self.searchVisitorShowsWindow.title("Zoo Atlanta")
        self.searchVisitorShowsWindow.geometry("800x600")

    def buildVisitorSearchShowsWindow(self, searchVisitorShowsWindow):
        titleLabel= Label(searchVisitorShowsWindow,text = "Search Shows", font = "Verdana 16 bold ")
        titleLabel.grid(row=1,column=2,sticky=W+E,pady=10)

        # Labels
        showLabel = Label(searchVisitorShowsWindow,text = "Name")
        showLabel.grid(row=2,column=0,pady=10)

        self.showNameString = StringVar()
        showNameEntry = Entry(searchVisitorShowsWindow, textvariable=self.showNameString, width=20)
        showNameEntry.grid(row=2, column=1,pady=10)

        exhibitLabel = Label(searchVisitorShowsWindow,text = "Exhibit")
        exhibitLabel.grid(row=3,column=0,pady=10)
        exhibitDefault = StringVar()
        exhibitDefault.set("options")
        exhibitMenu = OptionMenu(searchVisitorShowsWindow, exhibitDefault, "Pacific","Jungle","Sahara","Mountainous","Birds")
        exhibitMenu.grid(row=3, column=1,pady=10)

        dateLabel = Label(searchVisitorShowsWindow,text = "Date")
        dateLabel.grid(row=2, column=2,pady=10)

        #showDateEntry = CalendarDialog.main()
        showDateEntry= Entry(searchVisitorShowsWindow)
        showDateEntry.grid(row=2, column=3,pady=10)

        # Button
        findShowsButton = Button(searchVisitorShowsWindow, text="Search", command=self.searchVisitorShowsWindowFindShowsButtonClicked)
        findShowsButton.grid(row=3,column=2,pady=10)

        
        # self.selectExhibitTree['show'] = "headings"
        selectShowTree = ttk.Treeview(searchVisitorShowsWindow, columns=("Name", "Exhibit", "Date"))
        selectShowTree.heading('#0', text = "Name")
        selectShowTree.heading('#1', text = "Exhibit")
        selectShowTree.heading('#2', text = "Date")
        selectShowTree.column('#0', width = 175, anchor = "center")
        selectShowTree.column('#1', width = 175, anchor = "center")
        selectShowTree.column('#2', width = 175, anchor = "center")
        selectShowTree.place(x=280, y=280, anchor="center", width=525)

        logVisitButton = Button(searchVisitorShowsWindow, text="Log Visit", command = self.logVisitButtonClicked)  
        logVisitButton.place(x=220, y=415)  

        backButton = Button(searchVisitorShowsWindow, text="Back", command=self.searchVisitorShowsWindowBackButtonClicked)
        backButton.place(x=320, y=415)

    def searchVisitorShowsWindowFindShowsButtonClicked(self):
        self.searchVisitorShowsWindow.destroy()
        self.createShowsDetailWindow()

    def logVisitButtonClicked(self):
        self.searchVisitorShowsWindow.withdraw()
        import searchShows

    def searchVisitorShowsWindowBackButtonClicked(self):
        self.searchVisitorShowsWindow.withdraw()
        self.chooseVisitorFunctionalityWindow.deiconify()


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

        minDefault = StringVar()
        minDefault.set("3")
        minMenu = OptionMenu(searchExhibitWindow, minDefault, "0","1","2","3","4","5")
        minMenu.grid(row=3, column=4,pady=10,sticky=W)

        maxDefault = StringVar()
        maxDefault.set("3")
        maxMenu = OptionMenu(searchExhibitWindow, maxDefault, "0", "1","2","3","4","5")
        maxMenu.grid(row=3, column=5,pady=10, sticky=W)


        waterLabel = Label(searchExhibitWindow,text = "Water Feature:")
        waterLabel.grid(row=4, column=3)
        # Name Entry
        typeDefault = StringVar()
        typeDefault.set("No")
        typeMenu = OptionMenu(searchExhibitWindow, typeDefault, "Yes", "No")
        typeMenu.grid(row=4, column=4, sticky=W)


        min2Label=Label(searchExhibitWindow,text="Min:")
        min2Label.grid(row=3,column=0, sticky=E)

        max2Label=Label(searchExhibitWindow,text="Max:")
        max2Label.grid(row=3,column=1, sticky=E)

        sizeLabel = Label(searchExhibitWindow,text = "Size:")
        sizeLabel.grid(row=4,column=0)

        min2Default = StringVar()
        min2Default.set("3")
        min2Menu = OptionMenu(searchExhibitWindow, min2Default, "0","1","2","3","4","5")
        min2Menu.grid(row=4, column=1,pady=5,sticky=E)

        max2Default = StringVar()
        max2Default.set("3")
        max2Menu = OptionMenu(searchExhibitWindow, max2Default, "0", "1","2","3","4","5")
        max2Menu.grid(row=4, column=2,pady=5, sticky=E)

        # Button
        findExhibitsButton = Button(searchExhibitWindow, text="Find Exhibits", command=self.searchExhibitWindowFindExhibitsButtonClicked)
        findExhibitsButton.grid(row=7,column=3)

        backButton = Button(searchExhibitWindow, text="Back", command=self.searchExhibitWindowBackButtonClicked)
        backButton.grid(row=7,column=1)

        selectExhibitTree = ttk.Treeview(searchExhibitWindow, columns=("Name", "Size", "NumAnimals"))
        # self.selectExhibitTree['show'] = "headings"
        selectExhibitTree.heading('#0', text = "Name")
        selectExhibitTree.heading('#1', text = "Size")
        selectExhibitTree.heading('#2', text = "NumAnimals")
        selectExhibitTree.heading('#3', text = "Water")
        selectExhibitTree.column('#0', width = 150, anchor = "center")
        selectExhibitTree.column('#1', width = 150, anchor = "center")
        selectExhibitTree.column('#2', width = 150, anchor = "center")
        selectExhibitTree.column('#3', width = 150, anchor = "center")
        selectExhibitTree.grid(row=6, columnspan=4, sticky = 'nsew')
        

    def searchExhibitWindowFindExhibitsButtonClicked(self):

        self.min = self.minSV.get()
        self.max = self.maxSV.get()
        self.name = self.nameSV.get()

        if self.min == self.max:
            return False

        # cur.execute("SELECT COUNT(Animal.Name AND Species), Exhibit.Name, Size, Has_Water FROM\
        #  Exhibit JOIN ON Animal.E_Name = Exhibit.Name ANIMAL \
        #  WHERE (Exhibit.Name = %) AND (Has_Water = %s OR %b) \
        #  AND (Size = %s OR %b)"\
        #  , [exhibit_name, has_water, size, boolean] GROUP BY Exhibit.Name)

        self.searchExhibitWindow.destroy()
        self.createExhibitDetailWindow()
        self.buildExhibitDetailWindow(self.exhibitDetailWindow)

    def searchExhibitWindowBackButtonClicked(self):
        self.searchExhibitWindow.destroy()
        self.chooseVisitorFunctionalityWindow.deiconify()


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

    
    def exhibitHistoryWindowBackButtonClicked(self):
        self.exhibitHistoryWindow.withdraw()
        self.chooseVisitorFunctionalityWindow.deiconify()


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
        exhibitMenu = OptionMenu(showHistoryWindow, exhibitDefault, "Pacific","Jungle","Sahara","Mountainous","Birds")
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

#-------------------ADMIN PAGES------------------------------


    def createViewVisitorsWindow(self):
        self.viewVisitorsWindow = Toplevel()
        self.viewVisitorsWindow.title("Zoo Atlanta")
        self.viewVisitorsWindow.geometry("800x600")
        self.viewVisitorsWindow.resizable(0,0)

    def buildViewVisitorsWindow(self, viewVisitorsWindow):

        # Title Label
        titleLabel = Label(viewVisitorsWindow, text = "View Vistors", font = "Verdana 16 bold ")
        titleLabel.place(x=350, y=25)

        # Table of all the visitors
        self.visitorsTree = ttk.Treeview(viewVisitorsWindow, columns=( "1", "2"), selectmode="extended")
        self.visitorsTree['show'] = "headings"
        self.visitorsTree.column("1", width = 300, anchor = "center")
        self.visitorsTree.column("2", width = 300, anchor = "center")
        
        self.visitorsTree.heading("1", text = "UserName")
        self.visitorsTree.heading("2", text = "Email")

        self.visitorsTree.place(x=400, y=200, anchor="center")


        self.cursor.execute("SELECT Username, Email FROM User WHERE Type = 'visitor'")

        self.viewVisitorsTuple = self.cursor.fetchall()
        self.usernameList = []
        self.emailList = []

        for i in self.viewVisitorsTuple:
            self.usernameList.append(i[0])
            self.emailList.append(i[1])

        # print(self.usernameList)
        # print(self.emailList)

        # Insert data into the treeview
        for i in range(len(self.viewVisitorsTuple)):
            self.visitorsTree.insert('', i , values=(self.usernameList[i], self.emailList[i]))

        # Back Button
        backButton = Button(viewVisitorsWindow, text="Back", command=self.viewVisitorsBackButtonClicked)
        backButton.place(x=10,y=570)

        removeVisitorsButton = Button(viewVisitorsWindow, text="Remove Staff", command=self.showVisitorsWindowAdminRemoveVisitorButtonClicked)
        removeVisitorsButton.place(x=670,y=570)


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

#-------------------SHOW ANIMAL ADMIN PAGE------------------------------

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

        exhibitLabel = Label(showAnimalWindowAdmin,text = "Exhibit")
        exhibitLabel.grid(row=4,column=0)
        exhibitDefault = StringVar()
        exhibitDefault.set("options")
        exhibitMenu = OptionMenu(showAnimalWindowAdmin, exhibitDefault, "Pacific","Jungle","Sahara","Mountainous","Birds")
        exhibitMenu.grid(row=4, column=1)

        minLabel=Label(showAnimalWindowAdmin,text="Min")
        minLabel.grid(row=2,column=3, sticky=W)

        maxLabel=Label(showAnimalWindowAdmin,text="Max")
        maxLabel.grid(row=2,column=4, sticky=W)

        ageLabel = Label(showAnimalWindowAdmin,text = "Age")
        ageLabel.grid(row=3,column=2)

        minDefault = StringVar()
        minDefault.set("3")
        minMenu = OptionMenu(showAnimalWindowAdmin, minDefault, "0","1","2","3","4","5")
        minMenu.grid(row=3, column=3,pady=10,sticky=W)

        maxDefault = StringVar()
        maxDefault.set("3")
        maxMenu = OptionMenu(showAnimalWindowAdmin, maxDefault, "0", "1","2","3","4","5")
        maxMenu.grid(row=3, column=4,pady=10, sticky=W)

        typeLabel = Label(showAnimalWindowAdmin,text = "Type")
        typeLabel.grid(row=4, column=2)
        # Name Entry
        typeDefault = StringVar()
        typeDefault.set("mammal")
        typeMenu = OptionMenu(showAnimalWindowAdmin, typeDefault, "mammal", "bird", "amphibian", "reptile", "fish", "invertebrate")
        typeMenu.grid(row=4, column=3, sticky=W)

        # Display Table for Results
        selectAnimalTree = ttk.Treeview(showAnimalWindowAdmin, columns=("Name", "Size", "Exhibit", "Age"))
        selectAnimalTree.heading('#0', text = "Name")
        selectAnimalTree.heading('#1', text = "Species")
        selectAnimalTree.heading('#2', text = "Exhibit")
        selectAnimalTree.heading('#3', text = "Age")
        selectAnimalTree.heading('#4', text = "Type")
        selectAnimalTree.column('#0', width = 150, anchor = "center")
        selectAnimalTree.column('#1', width = 150, anchor = "center")
        selectAnimalTree.column('#2', width = 150, anchor = "center")
        selectAnimalTree.column('#3', width = 150, anchor = "center")
        selectAnimalTree.column('#4', width = 150, anchor = "center")
        selectAnimalTree.grid(row=5, columnspan=4, sticky = 'nsew')

        # Button
        findAnimalsButton = Button(showAnimalWindowAdmin, text="Find Animals", command=self.showAnimalWindowAdminFindAnimalsButtonClicked)
        findAnimalsButton.grid(row=6,column=2)

        removeAnimalsButton = Button(showAnimalWindowAdmin, text="Remove Animal", command=self.showAnimalWindowAdminRemoveAnimalWindowButtonClicked)
        removeAnimalsButton.grid(row=6,column=3)

        backButton = Button(showAnimalWindowAdmin, text="Back", command=self.showAnimalWindowAdminBackButtonClicked)
        backButton.grid(row=6,column=1)


    def showAnimalWindowAdminFindAnimalsButtonClicked(self):
        self.showAnimalWindowAdmin.destroy()
        self.createAnimalDetailWindow()

    def showAnimalWindowAdminRemoveAnimalWindowButtonClicked(self):
        self.showAnimalWindowAdmin.destroy()
        self.chooseAdminFunctionalityWindow.deiconify()

    def showAnimalWindowAdminBackButtonClicked(self):
        self.showAnimalWindowAdmin.destroy()
        self.chooseAdminFunctionalityWindow.deiconify()


    def createViewStaffWindow(self):
        self.viewStaffWindow = Toplevel()
        self.viewStaffWindow.title("Zoo Atlanta")
        self.viewStaffWindow.geometry("800x600")
        self.viewStaffWindow.resizable(0,0)

    def buildViewStaffWindow(self, viewStaffWindow):

        # Title Label
        titleLabel = Label(viewStaffWindow, text = "View Staff", font = "Verdana 16 bold ")
        titleLabel.place(x=350, y=25)

        # Table of all the staff members
        self.staffTree = ttk.Treeview(viewStaffWindow, columns=("1", "2"), selectmode="extended")
        self.staffTree['show'] = "headings"
        self.staffTree.column("1", width = 300, anchor = "center")
        self.staffTree.column("2", width = 300, anchor = "center")

        self.staffTree.heading("1", text = "Name")
        self.staffTree.heading("2", text = "Email")

        self.staffTree.place(x=400, y=200, anchor="center")


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

        removeStaffButton = Button(viewStaffWindow, text="Remove Staff", command=self.showStaffWindowAdminRemoveStaffButtonClicked)
        removeStaffButton.place(x=670,y=570)


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


#-------------------VISITOR PAGES-----------------------------

    def createSearchAnimalWindow(self):
        # Create blank Search Animal Window
        self.searchAnimalWindow=Toplevel()
        self.searchAnimalWindow.title("Zoo Atlanta")

    def buildSearchAnimalWindow(self,searchAnimalWindow):

        # Title Label
        titleLabel= Label(searchAnimalWindow,text = "Search Animals", font = "Verdana 16 bold ")
        titleLabel.grid(row=1,column=2,sticky=W+E)

        # Labels
        exhibitLabel = Label(searchAnimalWindow,text = "Exhibit")
        exhibitLabel.grid(row=2,column=1)
        ageLabel = Label(searchAnimalWindow,text = "Age")
        ageLabel.grid(row=3,column=1)
        typeLabel = Label(searchAnimalWindow,text = "Type")
        typeLabel.grid(row=4,column=1)

        nameLabel = Label(searchAnimalWindow,text = "Name")
        nameLabel.grid(row=2, column=2)
        # Name Entry
        self.animalNameSV = StringVar()
        animalNameEntry = Entry(searchAnimalWindow, textvariable=self.animalNameSV, width=20)
        animalNameEntry.grid(row=2, column=3)

        speciesLabel = Label(searchAnimalWindow,text = "Species")
        speciesLabel.grid(row=3, column=2)
        # Name Entry
        self.animalSpeciesSV = StringVar()
        animalSpeciesEntry = Entry(searchAnimalWindow, textvariable=self.animalSpeciesSV, width=20)
        animalSpeciesEntry.grid(row=2, column=3)

        
        # self.selectExhibitTree['show'] = "headings"
        selectAnimalTree = ttk.Treeview(searchAnimalWindow, columns=("Name", "Size", "Exhibit", "Age"))
        selectAnimalTree.heading('#0', text = "Name")
        selectAnimalTree.heading('#1', text = "Species")
        selectAnimalTree.heading('#2', text = "Exhibit")
        selectAnimalTree.heading('#3', text = "Age")
        selectAnimalTree.heading('#4', text = "Type")
        selectAnimalTree.column('#0', width = 150, anchor = "center")
        selectAnimalTree.column('#1', width = 150, anchor = "center")
        selectAnimalTree.column('#2', width = 150, anchor = "center")
        selectAnimalTree.column('#3', width = 150, anchor = "center")
        selectAnimalTree.column('#4', width = 150, anchor = "center")
        selectAnimalTree.grid(row=5, columnspan=4, sticky = 'nsew')

        # Button
        findAnimalsButton = Button(searchAnimalWindow, text="Find Animals", command=self.searchAnimalWindowFindAnimalsButtonClicked)
        findAnimalsButton.grid(row=6,column=3)

        backButton = Button(searchAnimalWindow, text="Back", command=self.searchAnimalWindowBackButtonClicked)
        backButton.grid(row=6,column=1)


    def searchAnimalWindowFindAnimalsButtonClicked(self):
        self.searchAnimalWindow.destroy()
        self.createAnimalDetailWindow()

    def  searchAnimalWindowBackButtonClicked(self):
        self.searchAnimalWindow.destroy()
        self.chooseVisitorFunctionalityWindow.deiconify()

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