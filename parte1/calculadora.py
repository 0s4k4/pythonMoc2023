number1 = int(input("Number 1: "))
number2 = int(input("Number 2: "))

Operation = input("Operation: ")



if Operation == 'add':
    add = number1 + number2
    print(f"ñ{number1} + {number2} = {add}")
    
if Operation == 'multiply':
    multiply = number1 * number2
    print(f"{number1} * {number2} = {multiply}")
    
if Operation == 'subtract':
    subtract = number1 - number2
    print(f"{number1} - {number2} = {subtract}")
    