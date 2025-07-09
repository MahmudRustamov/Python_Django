from file_manager import read, writerows, append
from datetime import datetime

def add_worker():
    name = input("Enter your name: ")
    time = input("Enter time: (hour:minute)")
    worker = [name, time]
    append(filename="workers", data= worker)


def calculate_penalties():
    worker_info = read("workers")
    start_time = "9:00"
    name = input("Enter an employee name: ")
    is_found = False
    for worker in worker_info:
        if worker[0] == name:
            is_found = True
            came_time = worker[1]
            start_obj = datetime.strptime(start_time, "%H:%M")
            came_obj = datetime.strptime(came_time, "%H:%M")
            diff = (came_obj - start_obj).total_seconds() // 60
            if int(diff) > 0:
                print(f"Name: {name}\nLate {int(diff)} minutes\nFine: {int(diff)*1000} som")
            elif int(diff) == 0:
                print(f"Name: {name} came on time")
            else:
                print(f"{name} came {int(diff)} minutes early")
            break

    if not is_found:
        print(f"<<{name}>> not is not found in workers list")


def calc_employees():
    worker_info = read("workers")
    start_time = "9:00"
    total_late_time = 0
    for worker in worker_info:
        came_time = worker[1]
        start_obj = datetime.strptime(start_time, "%H:%M")
        came_obj = datetime.strptime(came_time, "%H:%M")
        diff = (came_obj - start_obj).total_seconds() // 60
        if int(diff) > 0:
            total_late_time += int(diff)
    print(f"Total late time: {total_late_time} minutes\tFine: {total_late_time * 1000} som")


def see_employee_list():
    worker_data = read("workers")
    for worker in worker_data:
        print(f"Name: {worker[0]}\t Came time: {worker[1]}")


def delete_worker():
    data = read("workers")
    name = input("Enter an employee name to delete: ")
    is_found = False
    for index, worker in enumerate(data):
        if worker[0] == name:
            is_found = True
            data.pop(index)
            print("Employee is deleted!!!")
    if is_found:
        writerows("workers", data)
    else:
        print("Employee is not found")
