"""
"""
def most_experienced_worker(emplyees: list) -> str:
    experienced_worker = None
    for employee in emplyees:
        if experienced_worker is None:
            experienced_worker = employee
        elif employee['experience'] > experienced_worker['experience']:
            experienced_worker = employee
    return f"Name: {experienced_worker['name']}\nAge: {experienced_worker['age']}\nExperience: {experienced_worker['experience']}"



workers = [
    {"name": "Ali", "age": 28, "experience": 5},
    {"name": "Botir", "age": 34, "experience": 10},
    {"name": "Diyor", "age": 41, "experience": 15},
    {"name": "Javohir", "age": 25, "experience": 3},
    {"name": "Sardor", "age": 38, "experience": 12},
]


print(most_experienced_worker(workers))
