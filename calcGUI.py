from tkinter import *
import tkinter.font as tkFont

class CalcWin:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("200x325")
        self.root.title("Taschenrechner")
        
        #fontstyles
        self.fontStyle = tkFont.Font(family="Lucida Grande", size=15)

        #entry
        self.e = Entry(self.root, width=30, borderwidth=5)
        self.e.grid(row=1, column=1, columnspan=5)

        #buttons
        self.button1 = Button(self.root, text="1", padx=10, pady=10, command=lambda: self.num("1"), font=self.fontStyle).grid(row=2, column=1)
        self.button2 = Button(self.root, text="2", padx=10, pady=10, command=lambda: self.num("2"), font=self.fontStyle).grid(row=2, column=2)
        self.button3 = Button(self.root, text="3", padx=10, pady=10, command=lambda: self.num("3"), font=self.fontStyle).grid(row=2, column=3)
        self.button4 = Button(self.root, text="4", padx=10, pady=10, command=lambda: self.num("4"), font=self.fontStyle).grid(row=3, column=1)
        self.button5 = Button(self.root, text="5", padx=10, pady=10, command=lambda: self.num("5"), font=self.fontStyle).grid(row=3, column=2)
        self.button6 = Button(self.root, text="6", padx=10, pady=10, command=lambda: self.num("6"), font=self.fontStyle).grid(row=3, column=3)
        self.button7 = Button(self.root, text="7", padx=10, pady=10, command=lambda: self.num("7"), font=self.fontStyle).grid(row=4, column=1)
        self.button8 = Button(self.root, text="8", padx=10, pady=10, command=lambda: self.num("8"), font=self.fontStyle).grid(row=4, column=2)
        self.button9 = Button(self.root, text="9", padx=10, pady=10, command=lambda: self.num("9"), font=self.fontStyle).grid(row=4, column=3)
        self.button0 = Button(self.root, text="0", padx=31, pady=10, command=lambda: self.num("0"), font=self.fontStyle).grid(row=5, column=2, columnspan=2)
        self.buttonequal = Button(self.root, text="=", padx=80, pady=10, command=lambda:self.equals(), font=self.fontStyle).grid(row=6, column=1, columnspan=4)
        self.buttonadd = Button(self.root, text="+", padx=10, pady=10, command=lambda: self.symbol("+"), font=self.fontStyle).grid(row=2, column=4)
        self.buttonminus = Button(self.root, text="-", padx=12, pady=10, command=lambda: self.symbol("-"), font=self.fontStyle).grid(row=3, column=4)
        self.buttontimes = Button(self.root, text="*", padx=12, pady=10, command=lambda: self.symbol("*"), font=self.fontStyle).grid(row=4, column=4)
        self.buttondurch = Button(self.root, text="/", padx=13, pady=10, command=lambda: self.symbol("/"), font=self.fontStyle).grid(row=5, column=4)
        self.buttonc = Button(self.root, text="C", padx=9, pady=10, command=lambda: self.fullclear(), font=self.fontStyle).grid(row=5, column=1)

        #init variables
        self.arten = []
        self.numbers = []
        self.succes = False

    def num(self, number):
        self.e.insert(END, number)
    
    def symbol(self, symbol):
        if not self.succes:
            self.arten.append(symbol)
            self.numbers.append(int(self.e.get()))
            self.e.delete(0, len(self.e.get()))
        else:
            self.arten.clear()
            self.numbers.clear()
            self.numbers.append(int(self.e.get()))
            self.arten.append(symbol)
            self.clear()

    
    def clear(self):
        self.e.delete(0, len(self.e.get()))

    def fullclear(self):
        self.clear()
        self.numbers.clear()
        self.arten.clear()

    def equals(self):
        self.numbers.append(int(self.e.get()))
        print(self.arten)
        print(self.numbers)
        self.result = 0
        self.result += int(self.numbers[0])
        for x in range(len(self.arten)):
            if self.arten[x] == '+':
                self.x1 = x + 1
                self.result = self.result + self.numbers[self.x1]
            elif self.arten[x] == '-':
                self.x1 = x + 1
                self.result = self.result - self.numbers[self.x1]
            elif self.arten[x] == '*':
                self.x1 = x + 1
                self.result = self.result * self.numbers[self.x1]
            elif self.arten[x] == '/':
                self.x1 = x + 1
                self.result = self.result / self.numbers[self.x1]
        self.clear()
        self.e.insert(END, str(self.result))
        self.succes = True
        print(self.result)

win = CalcWin()
win.root.mainloop()

