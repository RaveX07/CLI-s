import random 
import string
animal = ["dog", "cat", "frog", "bear", "mouse", "pig", "cow", "snake", "eagle", ""]

def random_string(num):
    random_string = "".join(random.choice(string.ascii_letters + string.digits) for i in range(num))
def random_nums(num):
    namrandom_nums = "".join(random.choice(string.digits) for i in range(num))
def random_password(num, password = ""):
    password = "".join(random.choice(string.ascii_letters + string.digits) for i in range(num))
def random_animal(animal):
    random_animal = random.choice(animal)
