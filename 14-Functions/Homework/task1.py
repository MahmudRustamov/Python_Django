"""1. Valyuta kurslari

exchange_rates = {
    "USD": 12500,
    "EUR": 13500,
    "RUB": 150,
}

Berilgan so'mni foydalanuvchi tanlagan
valyutaga o'giradigan funksiya yozing.
"""

import os
os.system("cls")



# --------------------- FIRST VERSION ----------------------------------


exchange_rates = {
    "USD": 12500,
    "EUR": 13500,
    "RUB": 150,
}

def money_exchange(option, uzs):
    if uzs.isdigit():
        uzs = int(uzs)
        return f"{uzs / exchange_rates[option]} {option}\n"
    return f"{uzs} is invalid"


while True: 

    print("Sum -> USD\nSum -> EURO\nSum -> RUB\nExit")

    choice =  input("Enter your choice: (USD, EUR, RUB): ").upper().strip()
    if choice in exchange_rates:
        amount = input("Enter the amount: ") 
        print(money_exchange(choice, amount))
    elif choice.startswith('EX'):
        print("Exiting the program!")
        break
    else:
        print("Please, check your currency name!\n")
        




# --------------------- SECOND VERSION ---------------------------------



# def uzs_to_usd(uzs):
#     usd = f"{uzs / 12500} $"
#     return usd

# def uzs_to_euro(uzs):
#     euro = f"{uzs / 13500} €"
#     return euro

# def uzs_to_rub(uzs):
#     rubl = f"{uzs / 150} ₽"
#     return rubl

# while True: 
#     print("Welcome to Exchange Rate Program") 
#     amount = input("Enter the amount: ") 
#     if amount.isdigit(): 
#         amount = int(amount)
#         print("1. Sum -> USD\n2. Sum -> EURO\n3. Sum -> RUB\n4. Exit")
#         choice =  input("Enter your choice: ")

#         if choice == '1':
#             print(uzs_to_usd(amount))
#         elif choice == '2':
#             print(uzs_to_euro(amount))
#         elif choice == '3':
#             print(uzs_to_rub(amount))
#         elif choice == '4':
#             print("Thank you for using our program. Exiting...")
#             break
#         else:
#             print("Invalid choice! Emter only numbers\n")
#     else:
#         print(f"You should use only numbers!\n")
        
