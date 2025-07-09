population = []

full_info = []
ls = []

while True: 
    choice = input("Would you like to add a person ? (yes/no) ").lower()
    if choice != 'yes':
        break

    ls.append(input("Enter your name: "))
    ls.append(input("Enter your surname: "))
    ls.append(int(input("Enter your age: ")))
    ls.append(input("Enter your address: "))
    ls.append(input("Enter your phone: "))
    full_info.extend(tuple(ls))

print(full_info)