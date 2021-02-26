import random
import string

scores = open("rechenscore.txt", "r+")
scoresr = scores.readlines()
scorelist = []
failed = False
for line in scoresr:
    if line[-1] == "\n":
        scorelist.append(int(line[:-1]))
    else:
        scorelist.append(int(line))
scorelist.sort()
try:
    highscore = scorelist[-1]
except:
    highscore = 0
score = 0
lastlvl = False

ok = input("Willst du ein Kopfrechenspiel spielen? ")
if ok == "ja":
    num1 = "".join(random.choice(string.digits) for i in range(1))
    num11 = "".join(random.choice(string.digits) for i in range(1))
    num2 = "".join(random.choice(string.digits) for i in range(2))
    num21 = "".join(random.choice(string.digits) for i in range(2))
    num22 = "".join(random.choice(string.digits) for i in range(2))
    num23 = "".join(random.choice(string.digits) for i in range(2))
    num3 = "".join(random.choice(string.digits) for i in range(3))
    num31 = "".join(random.choice(string.digits) for i in range(3))
    num4 = "".join(random.choice(string.digits) for i in range(4))
    num41 = "".join(random.choice(string.digits) for i in range(4))
    num5 = "".join(random.choice(string.digits) for i in range(5))
    num51 = "".join(random.choice(string.digits) for i in range(5))
    ok = input("Das ist ein Ratespiel. Willst du es spielen? (ja/nein)  ").lower()
    if ok == "ja":
        print(f"Dein Highscore ist {highscore}.")
        guess = int(input(f"Was ist {num2} + {num21}? "))
        if guess == int(num2) + int(num21):
            score += 1
            print("Richtig. Weiter mit Level 2.\n")
            print(f"Dein jetziger Score ist {str(score)}.")
            guess = int(input(f"Was ist {str(num1)} * {str(num11)}? "))
            if guess == int(num1) * int(num11):
                score += 1
                print("Gut, das war wieder richtig.")
                print(f"Dein Score ist {str(score)}.")
                guess = int(input(f"Was ist {str(num3)} + {str(num31)}? "))
                if guess == int(num3) + int(num31):
                    score += 1
                    print("Gut, das war wieder richtig. Du bist ja richtig gut! ")
                    print(f"Dein Score ist {str(score)}.")
                    guess = int(input(f"Was ist {str(num4)} + {str(num41)}? "))
                    if guess == int(num4) + int(num41):
                        score += 1
                        print("Du bist wirklich gut! Das war wieder richtig. ")
                        print(f"Dein Score ist {str(score)}.")
                        guess = int(input(f"Was ist {str(num23)} * {str(num22)}? "))
        if not lastlvl:
            print("Das war leider falsch. ")
        else:
            print("Gut das war das letzte Level. ")
