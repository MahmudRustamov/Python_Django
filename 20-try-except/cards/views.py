from file_manager import append, read

def add_card():
    try:
        name = input("Enter your full name: ")
        card_num = input("Enter card number: ")
        password = input("Enter your password: ")

        data = [name, card_num, 0, password]
        append("cards", data)
    except Exception as error:
        print("Something went wrong", error)


def add_money():
    card_num = input("Enter card number: ")

    data = read("cards")
    for user in data:
        if user[0] == card_num:
            amount = int(input("Enter the amount"))
            user[2] += amount
            print("Your car")


def transfer_money():
    card_num = input("Enter card number: ")
    amount = int(input("Enter the amount"))