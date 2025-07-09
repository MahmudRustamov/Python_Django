from functions import add_worker, calculate_penalties, delete_worker
from functions import calc_employees, see_employee_list


def main():
    print("""
    1. Add an employee
    2. Delete an employee
    3. Calculate fine
    4. Calculate All employees' fine
    5. Show all employees
    6. Exit
    """)

    choice = input("Enter your choice: ")

    if choice == "1":
        add_worker()
    elif choice == "2":
        delete_worker()
    elif choice == "3":
        calculate_penalties()
    elif choice == "4":
        calc_employees()
    elif choice == "5":
        see_employee_list()
    elif choice == "6":
        print("GoodBye!!")
        return None
    else:
        print("Invalid choice!!!")
    return main()

if __name__ == "__main__":
    main()
