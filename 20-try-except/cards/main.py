from traceback import print_tb


def main():
    print("""
    1. Add a card
    2. Add money
    3. Send money
    4. Exit
    """)

    choice = input("Enter your choice: ")

    if choice == "1":
        pass
    elif choice == "2":
        pass
    elif choice == "3":
        pass
    elif choice == "4":
        print("GoodBye!!")
        return None
    else:
        print("Invalid choice!!")
    return main()




if __name__ == "__main__":
    main()