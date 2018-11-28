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
            self.createStaffChooseFunctionalityWindow()
            self.buildStaffChooseFunctionalityWindow(self.chooseStaffFunctionalityWindow)
        elif isAdminName:
            self.loginWindow.withdraw()
            self.createAdminChooseFunctionalityWindow()
            self.buildAdminChooseFunctionalityWindow(self.chooseAdminFunctionalityWindow)
        else:
            self.loginWindow.withdraw()
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
        self.createViewAnimalsWindow()
        self.buildViewAnimalsWindow(self.viewAnimalsWindow)
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

        # # Search Shows 
        # searchShowsLabel = Label(chooseFunctionalityWindow, text="Search Shows", font = "Verdana 13")
        # # searchShowsLabel.grid(row=3, column=1)
        # searchShowsLabel.bind("<ButtonPress-1>", self.chooseFunctionalityWindowSearchShowsLabelClicked)
        # searchShowsLabel.place(x=400, y = 200, anchor="center")


        # # Search for Animals Label
        # searchAnimalsLabel = Label(chooseFunctionalityWindow, text="Search for Animals", font = "Verdana 13")
        # # searchAnimalsLabel.grid(row=4,column=1)
        # searchAnimalsLabel.bind("<ButtonPress-1>", self.chooseFunctionalityWindowSearchAnimalsLabelClicked)
        # searchAnimalsLabel.place(x=400, y = 300, anchor="center")

        # # View Exhibit History
        # viewExhibitHistoryLabel = Label(chooseFunctionalityWindow, text="View Exhibit History", font = "Verdana 13")
        # # viewExhibitHistoryLabel.grid(row=5,column=1)
        # viewExhibitHistoryLabel.bind("<ButtonPress-1>", self.chooseFunctionalityWindowViewExhibitHistoryLabelClicked)
        # viewExhibitHistoryLabel.place(x=400, y = 400, anchor="center")

    def chooseStaffFunctionalityWindowSearchAnimalsLabelClicked(self,event):
        # Hide Choose Functionality Window.
        self.createSearchAnimalsWindow()
        self.buildSearchAnimalsWindow(self.viewSearchAnimalsWindow)
        self.chooseStaffFunctionalityWindow.withdraw()



    def chooseStaffFunctionalityWindowViewAssignedShowsLabelClicked(self,event):
        self.createViewAssignedShowsWindow()
        self.buildViewAssignedShowsWindow(self.viewAssignedShowsWindow)
        self.chooseStaffFunctionalityWindow.withdraw()

    def chooseStaffFunctionalityWindowLogOutButtonClicked(self):
        # Click Log Out Buttion on Choose Functionality Window:
        # Destroy Choose Functionality Window
        # Display Login Window
        self.chooseStaffFunctionalityWindow.destroy()
        self.loginWindow.deiconify()



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
        self.buildSearchExhibitWindow(self.viewSearchExhibitWindow)
        self.chooseVisitorFunctionalityWindow.withdraw()

    def chooseFunctionalityWindowSearchShowsLabelClicked(self,event):
        # Hide Choose Functionality Window
        self.createSearchShowWindow()
        self.buildSearchShowWindow(self.searchShowWindow)
        self.chooseVisitorFunctionalityWindow.withdraw()

    def chooseFunctionalityWindowSearchAnimalsLabelClicked(self,event):
        self.createSearchAnimalWindow()
        self.buildSearchAnimalWindow(self.searchAnimalWindow)
        self.chooseVisitorFunctionalityWindow.withdraw()

    def chooseFunctionalityWindowViewExhibitHistoryLabelClicked(self,event):
        self.createViewExhibitHistoryWindow()
        self.buildViewExhibitHistoryWindow(self.viewExhibitHistoryWindow)
        self.chooseVisitorFunctionalityWindow.withdraw()

    def chooseFunctionalityWindowViewShowHistoryLabelClicked(self,event):
        self.createViewShowHistoryWindow()
        self.buildViewShowHistoryWindow(self.viewShowHistoryWindow)
        self.chooseVisitorFunctionalityWindow.withdraw()

    def chooseFunctionalityWindowLogOutButtonClicked(self):
        # Click Log Out Buttion on Choose Functionality Window:
        # Destroy Choose Functionality Window
        # Display Login Window
        self.chooseVisitorFunctionalityWindow.destroy()
        self.loginWindow.deiconify()


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
        visitorsTree = ttk.Treeview(viewVisitorsWindow, columns=("Name"))
        visitorsTree.heading('#0', text = "Name")
        visitorsTree.heading('#1', text = "Email")
        visitorsTree.column('#0', width = 300, anchor = "center")
        visitorsTree.column('#1', width = 300, anchor = "center")
        visitorsTree.place(x=400, y=200, anchor="center")

        # Back Button
        backButton = Button(viewVisitorsWindow, text="Back", command=self.viewVisitorsBackButtonClicked)
        backButton.place(x=10,y=570)



    def viewVisitorsBackButtonClicked(self):
        self.viewVisitorsWindow.destroy()
        self.chooseAdminFunctionalityWindow.deiconify()

#-------------------STAFF PAGES------------------------------

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