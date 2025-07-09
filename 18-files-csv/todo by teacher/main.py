from crud import add_task, all_tasks, delete_task
from crud import update_status, clear_tasks, daily_check

def main():
    print("""
    1. All tasks
    2. Add a new task
    3. Delete a task
    4. Update task status
    5. Daily check
    6. Clear all tasks
    7. Exit
    """)

    choice = input("Enter you choice: ")
    if choice == "1":
        all_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        update_status()
    elif choice == "5":
        daily_check()
    elif choice == "6":
        clear_tasks("tasks")
    elif choice == "7":
        print("Bye!!")
        return 0
    else:
        print("Invalid choice")
    return main()


if __name__ == "__main__":
    main()
