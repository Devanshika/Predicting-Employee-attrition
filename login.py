from tkinter import *
from tkinter import messagebox
import bcrypt
from database import Database
db = Database()
db.createTable()
class Login:
    """
    Class for Login
    @param username
    @param password
    """
    def __init__(self, mainwindow):
        """
        Class Init Method for GUI
        :params — loginWindow, label, username
        """
        self.mainwindow=mainwindow
# Variables for Tkinter
        self.loginWindow = Tk()
        self.loginWindow.title("Login")
        self.loginWindow.geometry("300x250")
        self.label = Label(self.loginWindow, text="Login")
        self.label.place(x=95, y=40)
# variables
        self.usernameS = StringVar()
        self.passwordS = StringVar()
        self.usernameE = Entry(
        self.loginWindow, relief=FLAT, textvariable=self.usernameS)
        self.usernameE.place(x=70, y=80)
        self.passwordE = Entry(
        self.loginWindow, show="*", relief=FLAT, textvariable=self.passwordS)
        self.passwordE.place(x=70, y=120)

        
        self.submit = Button(self.loginWindow, text="Submit",
        pady=5, padx=20, command=self.validate)
        self.submit.place(x=100, y=150)
    def validate(self):
        # Actual Variales
        self.username = self.usernameE.get()
        self.password = self.passwordE.get()
        self.loginWindow.destroy()
        data = (self.username,)
        inputData = (self.username, self.password,)
        try:
            if (db.validateData(data, inputData)):
                messagebox.showinfo("Successful", "Login Was Successful")
                self.mainwindow.login_successful()
            else:
                messagebox.showerror("Error", "Wrong Credentials")
        except IndexError:
            messagebox.showerror("Error", "Wrong Credentials")
        

    def run(self):
        self.loginWindow.mainloop()
class Register:
    """
    Class for Register
    @param username
    @param password
    """
    def __init__(self, mainwindow):
        self.mainwindow=mainwindow
        self.registerWindow = Tk()
        self.registerWindow.title("Register with Python")
        self.registerWindow.geometry("300x250")
        self.label = Label(self.registerWindow, text="Register")
        self.label.place(x=95, y=40)
# variables
        self.usernameS = StringVar()
        self.passwordS = StringVar()
        self.usernameE = Entry(self.registerWindow,
        relief=FLAT, textvariable=self.usernameS)
        self.usernameE.place(x=70, y=80)
        self.passwordE = Entry(self.registerWindow, show="*",
        relief=FLAT, textvariable=self.passwordS)
        self.passwordE.place(x=70, y=120)
        self.submit = Button(self.registerWindow,
        text="Submit", pady=5, padx=20, command=self.add)
        self.submit.place(x=100, y=150)

        
    def run(self):
        self.registerWindow.mainloop()
    def add(self):
        # Actual Variales
        self.username = self.usernameE.get()
        self.password = self.passwordE.get()
        self.registerWindow.destroy()
        print(self.username)
        print(self.password)
        self.salt = bcrypt.gensalt()
        self.hashed = bcrypt.hashpw(self.password.encode(), self.salt)
        data = (self.username,)
        result = db.searchData(data)
        print(result)
        if result != 0:
            data = (self.username, self.hashed)
            db.insertData(data)
            messagebox.showinfo("Successful", "Username Was Added")
            self.mainwindow.login_successful()
        else:
            messagebox.showwarning("Warning", "Username already Exists")
       