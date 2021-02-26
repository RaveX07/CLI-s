
#open emails
file = open("/Textfiles/emails.txt", "r+")
emails = file.readlines()
emaillist = []
passwordlist = []

#read emails and passwords
for line in emails:
    komma = line.find(",")
    komma1 = komma + 1
    if line[-1] == "\n":
        passwordlist.append(line[komma1:-1])
        emaillist.append(line[:komma])
    else:
        passwordlist.append(line[komma1:])
        emaillist.append(line[:komma])

#succes
loginsucces = True
regsucces = True
registered = False

#functions for login and register
def login():
    print("LOGIN:\n")
    email = input("Was ist deine email? ")
    try:
        indexemail = emaillist.index(email)
        password = input("Tippe dein Passwort ein: ")
        if passwordlist[indexemail] == password:
            print("Du bist erfolgreich eingelogt. ")
        else:
            print("Passwort falsch. ")
            loginsucces = False      
    except:
        loginsucces = False
        print("Die e-mail ist leider noch nicht regristriert. ")

def register():
    print("NEW EMAIL:\n")
    email = input("Was ist deine e-mail: ")
    if email in emaillist:
        print("Du bist schon regristriert. ")
        registered = True
        login()       
        return()
    password = input("Neues Passwort: ")
    passwordconfirm = input("Bestätige Passwort: ")
    confirm = input(f"Willst du dich mit der E-Mail {email} einloggen? ")
    if confirm == "ja":
        if password == passwordconfirm:
            print("Erfolgreich regristriert.")
            file.write(f"\n{email},{password}")
        elif password != passwordconfirm:
            print("Passwörter stimmen nicht überein. ")
            regsucces = False

#the main program
typ = input("Willst du dich mit deinem Account einlogen oder willst du einen neuen Account erstellen? [login/new]  ").lower()
if typ == "login":
    login()
    if not loginsucces:
        login()
elif typ == "new":
    register()
    if not regsucces:
        register()
    elif registered:
        login()
file.close()

