from file_manager import append, read, writerows
from utils import generate_new_id


def all_tasks():
    tasks = read("tasks")
    for task in tasks:
        print(f"ID: {task[0]}\tTask: {task[1]}\t>> Status: {task[2]}")


def add_task():
    new_id = generate_new_id(filename="tasks")
    name = input("Enter task name: ")

    task = [new_id, name, 0]
    append(filename="tasks", data=task)
    print("New task is added")


def delete_task():
    task_id = input("Enter task id: ")
    tasks = read("tasks")
    is_found = True
    for task in tasks:
        if task[0] == task_id:
            tasks.remove(task)
            is_found = True
            print("Task is deleted")
            break
    if is_found:
        writerows(filename="tasks", data=tasks)
    else:
        print("Task is not found")


def update_status():
    task_id = input("Enter task id: ")
    tasks = read("tasks")
    is_found = True
    for task in tasks:
        if task[0] == task_id:
            status = input("Enter status (Complete-> 1 or Incomplete-> 0): ")
            task[2] = status
            is_found = True
            print("Status is updated")
            break

    if is_found:
        writerows(filename="tasks", data=tasks)
    else:
        print("Task is not found")


def daily_check():
    tasks = read("tasks")
    completed_tasks = ""
    incompleted_tsk = ""
    for task in tasks:
        if task[2] == "1":
            completed_tasks += f"ID: {task[0]}\tTask: {task[1]}\t>> Status: {task[2]}\n"
        else:
            incompleted_tsk += f"ID: {task[0]}\tTask: {task[1]}\t>> Status: {task[2]}\n"
    print(f"<<Completed Tasks for today ✅\n{completed_tasks}\nIncompleted Tasks ❌\n{incompleted_tsk}")



def clear_tasks(filename: str):
    path = f"data/{filename}.csv"
    with open(file=path, mode="w", encoding="UTF-8", newline="") as file:
        print("Tasks have been cleared")
        return



