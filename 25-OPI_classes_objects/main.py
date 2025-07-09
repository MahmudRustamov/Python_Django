import csv

class Calculator:
    def __init__(self, num1, num2, sign):
        self.num1 = num1
        self.num2 = num2
        self.sign = sign


    def calculate(self):
        if sign == "+":
            return f"{self.num1} + {self.num2} = {self.num1 / self.num2}"
        elif sign == "-":
            return f"{self.num1} - {self.num2} = {self.num1 / self.num2}"
        elif sign == "*":
            return f"{self.num1} * {self.num2} = {self.num1 * self.num2}"
        elif sign == "/":
            if self.num2 != 0:
                return f"{self.num1} / {self.num2} = {self.num1 / self.num2}"
            else:
                return "You can't divide by ZERO"
        else:
            return "Something went wrong!!!"

    def save(self):
        with open(file="results.csv", mode="a", encoding="UTF-8", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([self.calculate()])
            # print("Data is added!!")

    def results(self):
        with open(file="results.csv", mode="r", encoding="UTF-8", newline="") as file:
            reader = csv.reader(file)
            for data in reader:
                for result in data:
                    print(result)
            

try:
    number1 = int(input("Enter a number: "))
    number2 = int(input("Enter the second number: "))
    sign = input("Enter the sign: ")
except TypeError: 
    print("You have to enter only numbers")
    
calculator1 = Calculator(num1=number1, num2=number2, sign=sign)
calculator1.calculate()
print(calculator1.save())
calculator1.results()
