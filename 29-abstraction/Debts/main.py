from utils import MarketDebts


def main():
    print("""
    1. Show all debts
    2. Add Debt
    3. Search person
    4. Delete a debt
    5. Exit
    """)
    market = MarketDebts("","","","")
    choice = input("Enter your choice: ")

    if choice == "1":
        market.all_debts()
    elif choice == "2":
        phone_number = input("Phone: ")
        name = input("Name: ")
        debt = input("Debt: ")
        comment = input("Comment: ")
        market = MarketDebts(phone_number=phone_number, name=name, debt=debt, comment=comment)
        market.add_debt()
    elif choice == "3":
        market.search_person()
    elif choice == "4":
        market.delete_debt()
    elif choice == "5":
        print("Good Bye!!")
        return None
    else:
        print("Invalid choice!!!")
    return main()


if __name__ == "__main__":
    main()