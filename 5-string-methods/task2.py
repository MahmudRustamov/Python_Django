name = input("Enter your name: ")
age = input("Enter your age: ")

if name.isalpha() and age.isdigit() and 0 < int(age) < 200:
    print(f"{name} was born in {2025-int(age)}")
else:
    print("Something went wrong!")