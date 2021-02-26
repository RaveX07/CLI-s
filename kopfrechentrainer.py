from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget
import sys
import string
import random
import time


class mainWin(QWidget):
    def __init__(self):
        super().__init__()

        self.score = 0
        self.lose = False

        self.title = QtWidgets.QLabel(self)
        self.title.setGeometry(QtCore.QRect(80, 10, 251, 18))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.title.setText("Kopfrechentrainer für Leo")

        self.num2Label = QtWidgets.QLabel(self)
        self.num2Label.setGeometry(QtCore.QRect(200, 100, 91, 18))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.num2Label.setFont(font)
        self.num2Label.setObjectName("num2Label")

        self.opLabel = QtWidgets.QLabel(self)
        self.opLabel.setGeometry(QtCore.QRect(180, 100, 21, 18))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.opLabel.setFont(font)
        self.opLabel.setObjectName("opLabel")

        self.num1Label = QtWidgets.QLabel(self)
        self.num1Label.setGeometry(QtCore.QRect(90, 100, 81, 18))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.num1Label.setFont(font)
        self.num1Label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.num1Label.setObjectName("num1Label")

        self.ErgrbnisLabel = QtWidgets.QLabel(self)
        self.ErgrbnisLabel.setGeometry(QtCore.QRect(60, 180, 81, 18))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.ErgrbnisLabel.setFont(font)
        self.ErgrbnisLabel.setObjectName("ErgrbnisLabel")
        self.ErgrbnisLabel.setText("Ergebnis:")

        self.Entry = QtWidgets.QLineEdit(self)
        self.Entry.setGeometry(QtCore.QRect(150, 180, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Entry.setFont(font)
        self.Entry.setObjectName("Entry")

        self.ScoreText = QtWidgets.QLabel(self)
        self.ScoreText.setGeometry(QtCore.QRect(310, 280, 51, 18))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.ScoreText.setFont(font)
        self.ScoreText.setObjectName("ScoreText")
        self.ScoreText.setText("Score:")

        self.ScoreLabel = QtWidgets.QLabel(self)
        self.ScoreLabel.setGeometry(QtCore.QRect(360, 280, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.ScoreLabel.setFont(font)
        self.ScoreLabel.setObjectName("ScoreLabel")
        self.ScoreLabel.setText(str(self.score))

        self.FeedbackLabel = QtWidgets.QLabel(self)
        self.FeedbackLabel.setGeometry(QtCore.QRect(10, 280, 241, 18))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.FeedbackLabel.setFont(font)
        self.FeedbackLabel.setObjectName("FeedbackLabel")

        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(160, 210, 88, 34))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("Bestätigen")
        self.pushButton.clicked.connect(lambda: self.checkSolution())

        self.countdownlanel = QtWidgets.QLabel(self)
        self.countdownlanel.setGeometry(QtCore.QRect(190, 140, 21, 18))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.countdownlanel.setFont(font)
        self.countdownlanel.setObjectName("label")

        self.highscorelabel2 = QtWidgets.QLabel(self)
        self.highscorelabel2.setGeometry(QtCore.QRect(0, 50, 81, 18))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.highscorelabel2.setFont(font)
        self.highscorelabel2.setObjectName("highscorelabel2")
        self.highscorelabel2.setText("Highscore:")

        self.highscorelabel = QtWidgets.QLabel(self)
        self.highscorelabel.setGeometry(QtCore.QRect(90, 50, 58, 18))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.highscorelabel.setFont(font)
        self.highscorelabel.setObjectName("highscorelabel")

        self.exitbutton = QtWidgets.QPushButton(self)
        self.exitbutton.setGeometry(QtCore.QRect(310, 240, 88, 34))
        self.exitbutton.setObjectName("exitbutton")
        self.exitbutton.setText("EXIT")
        self.exitbutton.clicked.connect(lambda: self.exit())

        self.getHighscore()

        self.giveCalc()

        self.show()
    
    def exit(self):
        self.writeScore()
        self.close()

    def getHighscore(self):
        file = open("scores.txt", "r+")
        self.scorelist = []
        for line in file.readlines():
            if line[-1] == "\n":
                self.scorelist.append(line[:-1])
            else:
                self.scorelist.append(line)
        self.scorelist.sort()
        highscore = self.scorelist[-1]
        print(highscore)
        print(self.scorelist)
        self.highscorelabel.setText(str(highscore))
        file.close()

    def giveCalc(self):
        numbers1 = [1,2,3,4,5,6,7,8,9,10]
        ops = ["+", "-", "*"]

        op = random.choice(ops)
        
        if op == "+" or op == "-":
            num1 = "".join(random.choice(string.digits) for i in range(2))
            num2 = "".join(random.choice(string.digits) for i in range(2))
            while op == "-" and num1 <= num2:
                num1 = "".join(random.choice(string.digits) for i in range(2))
                num2 = "".join(random.choice(string.digits) for i in range(2))
        else:
            num1 = "".join(random.choice(string.digits))
            num2 = "".join(random.choice(string.digits))
        
        self.num1Label.setText(num1)
        self.num2Label.setText(num2)
        self.opLabel.setText(op)
        
    
    def checkSolution(self):
        self.input = int(self.Entry.text())
        num1 = int(self.num1Label.text())
        num2 = int(self.num2Label.text())
        op = self.opLabel.text()
        
        if op == "+":
            ergebnis = num1 + num2
        elif op == "-":
            ergebnis = num1 - num2
        elif op == "*":
            ergebnis = num1 * num2
        elif op == "/":
            ergebnis = num1 / num2
        
        print(ergebnis)

        if self.input == ergebnis:
            self.FeedbackLabel.setText("Das war richtig. Score +1")
            self.score += 1
            self.ScoreLabel.setText(str(self.score))
            self.Entry.clear()
            self.giveCalc()
        else:
            self.FeedbackLabel.setText("Das war falsch. Score -1")
            self.score -= 1
            self.ScoreLabel.setText(str(self.score))
            self.giveCalc()

    
    def writeScore(self):
        file = open("scores.txt", "r+")
        file.write(f"\n{self.score}")
        file.close()
        

app = QApplication(sys.argv)
main = mainWin()
sys.exit(app.exec_())

