from functions import get_info

def main():
    print("""
    1. Save personal data
    2. Read personal data
    3. Delete email
    4.Exit""")

    choice = input("Enter your choice: ")

    if choice == "1":
        get_info()
    elif choice == "2":
        pass
    elif choice == "3":
        pass
    elif choice == "4":
        print("Bye")
        return

    else:
        print("Invalid choice")
    return main()

if __name__ == "__main__":
    main()