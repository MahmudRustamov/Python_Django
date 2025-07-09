import functions


def main():
    print("""
    1. Kitob qo'shish
    2. Kitoblarni ko'rish
    3. Kitobni o'chirish
    4. Kitobni nomini o'zgartirish
    """)

    choice = input("Enter your choice: ")

    if choice == "1":
        functions.add_book()
    elif choice == "2":
        functions.show_books()
    elif choice == "3":
        functions.delete_book()
    elif choice == "4":
        functions.update_book()
    else:
        print("Invalid choice")
    return main()


if __name__ == '__main__':
    main()
