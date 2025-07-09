from auth import login, register


def auth_menu():
    print("""
    1. Register
    2. Log in
    3. Exit
    """)

    choice = input("Enter your choice: ")

    if choice == "1":
        register()
    elif choice == "2":
        if login():
            return user_menu()
        else:
            print("Your password or email did not match!!")
    elif choice == "3":
        print("Good Bye!!")
        return None
    else:
        print("Invalid choice!!!")
    return auth_menu()


def user_menu():
    print("""
    1. Show my rented books
    2. Rent book
    3. Return book
    4. Logout
    """)

    print("Bu qismini keyin qilamiz deb ustoz etganidilar>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

if __name__ == "__main__":
    auth_menu()
