from functions import create_file, check_file, delete_file
from functions import append_to_file, write_to_file, read_file
import os
print(os.getcwd())


def main():
    print("""
    1. Create file
    2. Delete file
    3. Check file
    4. Write to file
    5. Append to file
    6. Read file
    """)

    choice = input("Enter your choice: ")
    if choice == "1":
        create_file()
    elif choice == "2":
        delete_file()
    elif choice == "3":
        check_file()
    elif choice == "4":
        write_to_file()
    elif choice == "5":
        append_to_file()
    elif choice == "6":
        read_file()
    else:
        print("Invalid choice")
    return main()


if __name__ == "__main__":
    main()
