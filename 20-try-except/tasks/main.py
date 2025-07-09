import file_mng
try:
    name = input("Enter your name: ")
    age = int(input("Age: "))
    data = [name, age]
    file_mng.write_to_csv("users.csv", data)
except ValueError:
    print("Age should be int")


