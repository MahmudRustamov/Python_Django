import json


data = dict()
name = input("Enter your name: ")
age = int(input("Enter your age: "))
birthdate = input("Enter your birth date: (dd.mm.yyyy): ")

data['name'] = name
data['age'] = age
data['birthdate'] = birthdate

with open(file="users.json", mode="w") as file:
    json.dump(data, file, indent = 4)
