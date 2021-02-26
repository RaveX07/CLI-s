from tkinter import *
import tkinter.font as tkFont

signup = 0
logginsucces = False
file0 = open("emails.txt", "r+")
#check for emails, usernames and passwords
emails = []
passwords = []
usernames = []
def checkforemails():
    usernames.clear()
    emails.clear()
    passwords.clear()
    if signup == 1:
        file1 = open("emails.txt", "r+")
        for line in file1.readlines():
            komma = line.find(",")
            komma1 = komma + 1
            komma2 = line.rfind(",")
            komma3 = komma2 + 1
            if line[-1] == "\n":
                emails.append(line[:komma])
                passwords.append(line[komma1: komma2])
                usernames.append(line[komma3: -1])
            else:
                emails.append(line[:komma])
                passwords.append(line[komma1: komma2])
                usernames.append(line[komma3:])
        print(emails)
        print(passwords)
        print(usernames)
    else:
        for line in file0.readlines():
            komma = line.find(",")
            komma1 = komma + 1
            komma2 = line.rfind(",")
            komma3 = komma2 + 1
            if line[-1] == "\n":
                emails.append(line[:komma])
                passwords.append(line[komma1: komma2])
                usernames.append(line[komma3: -1])
            else:
                emails.append(line[:komma])
                passwords.append(line[komma1: komma2])
                usernames.append(line[komma3:])
        print(emails)
        print(passwords)
        print(usernames)
checkforemails()

#todo create Toplevel Window
class Window:
    def __init__(self, title, size):
        try:
            self.root.destroy()
        except:
            self.root = Tk()
            self.root.geometry(size)
            self.root.title(title)
            # font styles
            self.fontStyleBIG = tkFont.Font(family="Lucida Grande", size=20)
            self.fontStyle = tkFont.Font(family="Lucida Grande", size=15)

class Root(Window):
    def __init__(self, title, size):
        super().__init__(title, size)
        # caption + username entry
        self.caption = Label(self.root, text="Login: ", font=self.fontStyleBIG).grid(row=1, column=1, columnspan=3, padx=10)
        self.usernameLabel = Label(self.root, text="Username or E-Mail:", font=self.fontStyle).grid(row=3, column=1)
        self.empty = Label(self.root, text=" ").grid(row=2, column=1)
        self.usernameentry = Entry(self.root, width=25, font=self.fontStyle)
        self.usernameentry.grid(row=3, column=2)

        #passowrd
        self.passwordLabel = Label(self.root, text="Password:", font=self.fontStyle).grid(row=4, column=1)
        self.passwordentry = Entry(self.root, width=25, font=self.fontStyle)
        self.passwordentry.grid(row=4, column=2)

        # variables for submit
        self.rightemail = False
        self.rightpassword = False

        # submit button
        self.submit = Button(self.root, text="Submit", command=lambda: self.submitfunc(), font=self.fontStyle)
        self.submit.place(x=185, y=125)
        self.submit.config(width=15, height=1)
        # register button
        self.register = Button(self.root, text="Sign Up", command=lambda: self.signupwin(), font=self.fontStyle,
                               fg="white", bg="blue")
        self.register.place(x=10, y=125)

    def submitfunc(self):
        logginsucces = False
        self.email = self.usernameentry.get()
        print("email: " + self.email)
        self.password = self.passwordentry.get()
        print("passowrt: " + self.password)

        try:
            self.indexemail = emails.index(self.email)
            self.rightemail = True
            if passwords[self.indexemail] == self.password:
                self.rightpassword = True
                logginsucces = True
                self.logginwin()

            else:
                logginsucces = False
                self.error = Label(self.root, text="Falsche E-Mail oder falsches Passwort", font=self.fontStyle,
                                   fg="red").grid(row=2, column=1, columnspan=2, padx=10)
        except:
            try:
                self.indexusername = usernames.index(self.email)
                self.rightemail = True
                if passwords[self.indexusername] == self.password:
                    self.rightpassword = True
                    logginsucces = True
                    self.logginwin()

                else:
                    self.logginsucces = False
                    self.error = Label(self.root, text="Falsche E-Mail oder falsches Passwort", font=self.fontStyle, fg="red").grid(
                        row=2,
                        column=1, columnspan=2, padx=10)
            except:
                error = Label(self.root, text="Falsche E-Mail oder falsches Passwort", font=self.fontStyle, fg="red")
                error.grid(row=2, column=1, columnspan=2, padx=10)

    def logginwin(self):
        class LoggedIn(Window):
            def __init__(self, title, size):
                super().__init__(title, size)
                self.empty = Label(self.root, text="          ").grid(row=1, column=1)
                self.empty1 = Label(self.root, text=" ").grid(row=2, column=1)
                self.succesfull = Label(self.root, text="Succesfull Logged In!", font=self.fontStyleBIG,
                                                                fg="green").grid(row=3, column=2)
        loggedinwin = LoggedIn("Logged In", "500x300")


    #register func
    def signupwin(self):
        class SignUpWin(Window):
            def __init__(self, title, size):
                super().__init__(title, size)
                self.newcaption = Label(self.root, text="SignUp", font=self.fontStyleBIG).grid(row=1, column=1,
                                                                                               columnspan=3, padx=10)
                self.empty = Label(self.root, text="   ").grid(row=2, column=1)
                self.newusernamela = Label(self.root, text="New Username:", font=self.fontStyle).grid(row=3, column=1)
                self.newusernameent = Entry(self.root, width=25, font=self.fontStyle)
                self.newusernameent.grid(row=3, column=2)
                self.newemailla = Label(self.root, text="E-Mail:", font=self.fontStyle).grid(row=4, column=1)
                self.newemailent = Entry(self.root, width=25, font=self.fontStyle)
                self.newemailent.grid(row=4, column=2)
                self.newpasswordla = Label(self.root, text="New Password:", font=self.fontStyle).grid(row=5, column=1)
                self.newpasswordent = Entry(self.root, width=25, font=self.fontStyle)
                self.newpasswordent.grid(row=5, column=2)
                self.newpassword1la = Label(self.root, text="Confirm Password:", font=self.fontStyle).grid(row=6, column=1)
                self.newpassword1ent = Entry(self.root, width=25, font=self.fontStyle)
                self.newpassword1ent.grid(row=6, column=2)
                self.confirm = Button(self.root, text="Confirm", font=self.fontStyle, command=lambda: self.confirmButton())
                self.confirm.grid(row=8, column=2)

            def confirmButton(self):
                self.confirm = False
                self.newpass = self.newpasswordent.get()
                self.newpass1 = self.newpassword1ent.get()
                self.newuser = self.newusernameent.get()
                self.newemail = self.newemailent.get()
                if self.newpass == self.newpass1:
                   self.confirm = True
                else:
                    self.confirm = False
                if self.newpass != "" and self.newpass1 != "" and self.newuser != "" and self.newemail != "" and self.confirm:
                    file0.write("\n" + self.newemail + "," + self.newpass + "," + self.newuser)
                    file0.close()
                    global signup
                    signup += 1
                    checkforemails()
                    self.root.destroy()
                else:
                    self.signuperror = Label(self.root, text="Passwords are not the same!", font=self.fontStyle, fg="red").grid(row=2, column = 2,
                                                                                                                                columnspan=3, padx=10)

        signup = SignUpWin("Sign Up", "500x300")

menu = Root("Login: ", "500x300")
menu.root.mainloop()

file0.close()
