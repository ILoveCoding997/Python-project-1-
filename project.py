num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
mode = input("Choose a mode: Addition, Subtraction, Multiplication and Division: ")
if mode == "addition" or mode == "Addition":
    results = float(num1) + float(num2)
    print(results)
if mode == "subtraction" or mode == "Subtraction":
    results = float(num1) - float(num2)
    print(results)
if mode == "multiplication" or mode == "Multiplication":
    results = float(num1) * float(num2)
    print(results)
if mode == "division" or mode == "Division":
    results = float(num1) / float(num2)
    print(results)