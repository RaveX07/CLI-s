import random
import string

num = int(input("Wie viele Stellen soll ihr Passwort haben? "))
password = "".join(random.choice(string.ascii_letters + string.digits) for i in range(num))
print(password)
