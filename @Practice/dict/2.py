# login = {
#     "jeymsBond": "agent007",
#     "tony_stark": "ironman101",
#     "piterParker": "spider.12.12",
#     "sherlok": "sher.l04",
# }

# username = input("Enter your user: ")
# password = input("Enter your password: ")

# is_found = False
# for user, passwd in login.items():
#     if user == user and password == passwd:
#         is_found =True
#         break

# if is_found:
#     print("You succesfully entered the system!!")
# else:
#     print("Something went wrong check your username and passsword")


login = {
    "jeymsBond": "agent007",
    "tony_stark": "ironman101",
    "piterParker": "spider.12.12",
    "sherlok": "sher.l04",
}

username = input("Enter your user: ")
password = input("Enter your password: ")

# Avval username lug'atda bormi, tekshiriladi
if username in login:
    print(login)
    # Agar bor bo'lsa, uning paroli kiritilgan parolga tengmi, tekshiriladi
    if login[username] == password:
        print("You successfully entered the system!!")
    else:
        print("Something went wrong, check your username and password")
else:
    # Agar username umuman topilmasa
    print("Something went wrong, check your username and password")