name = input('Enter your name: ')
s_name = input('Enter your surname: ')
phone = input('Enter your phone number example -> <<998991234567>>: ')

if len(name) >= 2 and len(s_name) >= 2:
    if phone.isdigit():
        if phone.startswith("998") and len(phone) == 12:
            print("W E L C O M E ! !")
        else:
            print("Enter a correct uzbek phone number!")
    else:
        print("Use only numbers")
else:
    print("Enter a full name!!")





