import csv
user = list()

counter = 0
while counter < 3:
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    gender = input("Gender: ")



header = ['name', 'age', 'gender']
with open(file="tasks.csv", mode="w+", encoding="UTF-8", newline="") as file:
    writer = csv.writer(file)
