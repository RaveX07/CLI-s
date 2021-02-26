
datei = input("\nGeben sie den Dateinamen ein, der Datei ein in der sie für ein Wort suchen wollen(mit Dateiendung): " )
text1 = open(datei, "r")
text = text1.readlines()
round = 0
word = input("Geben sie ein Wort ein nach dem sie suchen: ")
check = False
newList = []

for line in text:
    if line[-1] == "\n":
        newList.append(line[:-1])
    else:
        newList.append(line)
for x in newList:
    round += 1
    if x == word:
        print("Wort in Datei enthalten. und zwar in Zeile " + str(round) + "\n")
        check = True
if check == False:
    print("Wort nicht in Datei enthalten\n")
