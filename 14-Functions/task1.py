def add(num1, num2):
    return num1 + num2

def subtruction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num1 != 0:
        return num1 / num2
    return "Number can not be divided by 0"


while True:
    number1 = int(input("Enter a number1 = "))
    number2 = int(input("Enter a number2 = "))

    sign = input("Enter a sign: ")

    if sign == '+':
        print(add(number1, number2))
    elif sign == '-':
        print(subtruction(number1, number2))
    elif sign == '*':
        print(multiplication(number1, number2))
    elif sign == '/':
        print(division(number1, number2))
    else:
        print("Invalid choice")