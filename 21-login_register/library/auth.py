from file_manager import read_csv, append, writerows
from random import randint
from utils import send_mail


def register():
    try:
        data = read_csv("users")
    except FileNotFoundError:
        print("File is not found")
        data = []
    full_name = input("Enter your full name: ")
    email = input("Enter your email: ")
    
    is_found = False
    for mail in data:
        if email == mail[1]:
            is_found = True
            break
    if is_found:
        print("This account is already registered")
        return   
    else:
        password = input("Enter a new password: ")
        password2 = input("Enter your password again: ")


    while password != password2:
        password = input("Enter a new password: ")
        password2 = input("Confirm your password: ") 

    code = randint(1000, 9999)

    send_mail(receiver_email=email, body=str(code))
    append(filename="codes", data=[email, code])
  
    counter = 1
    confirmed = False
    while counter <= 3:
        confirmation_code = input("Enter the verification code: ")
        if confirmation_code == str(code):
            confirmed = True
            break
        counter += 1

    if confirmed:
        append(filename="users", data=[full_name, email, password, "complete"])
        print("You are all set - your account is ready to use!!!")
    else:
        append(filename="users", data=[full_name, email, password, "incomplete"])
        print("Verification code did not match!!")


def login():
    print("<<< Log in >>>")
    email = input("Enter your email: ")
    password = input("Password: ")
    data = read_csv("users")
    is_found = False
    for user in data:
        if user[1] == email and user[2] == password:
            user[-1] = True
            is_found = True
           

    if not is_found:
        return False
    else:
        writerows("users", data=data)
        return True




def logout():
    data = read_csv("users")
    for user in data:
        user[-1] = False
    writerows("users", data=data)
    print("Log out")