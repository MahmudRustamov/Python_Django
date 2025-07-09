m = 0
passwordl = "admin"

while m != 3:
    password = input("Enter your password: ")
    if password == passwordl:
        print("Welcome")
        break
    m += 1
else:
    print("You had only 3 attempt and you used all of them")