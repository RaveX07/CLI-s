
num1 = float(input("Type in the first number: "))
op = input("Type in the operator: ")
num2 = float(input("Type in the second number: "))


if op == "+":
    result = num1 + num2
    result1 = str(result)
    print("Das Ergebnis ist " + result1)
elif op == "-":
    result = num1 - num2
    result1 = str(result)
    print("Das Ergebnis ist " + result1)
elif op == "*":
    result = num1 * num2
    result1 = str(result)
    print("Das Ergebnis ist " + result1)
elif op == "/":
    result = num1 / num2
    result1 = str(result)
    print("Das Ergebnis ist " + result1)
