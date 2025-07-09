names = []

while True:
    name = input("Enter name: ")
    if name != 'break':
         if name not in names:
            names.append(name)
         else:
            answer = input("Do you want to delete this message?:(yes/no): ").lower()
            if answer == 'yes':
                names.remove(name)
    else:
        break
print(names)