"""
1. Ishchilar haqida quyidagi lug'at berilgan:

workers.csv = {
    "Ali": {"yosh": 30, "maosh": 500, "lavozim": "Dasturchi"},n
    "Vali": {"yosh": 25, "maosh": 450, "lavozim": "Dizayner"},
    "Sardor": {"yosh": 28, "maosh": 600, "lavozim": "Muhandis"},
}

1.1 Eng katta maosh oladigan ishchini toping.
1.2 O'rtacha maoshni hisoblang.

"""

# -----------------------------------------------------------------------------------------

workers = {
    "Ali": {"yosh": 30, "maosh": 500, "lavozim": "Dasturchi"},
    "Vali": {"yosh": 25, "maosh": 450, "lavozim": "Dizayner"},
    "Sardor": {"yosh": 28, "maosh": 600, "lavozim": "Muhandis"},
}

max_salary = 0
average_salary = 0

# 1.1 and 1.2
for key in workers.keys():
    average_salary += workers[key]['maosh']
    if workers[key]['maosh'] > max_salary:
        max_salary = workers[key]['maosh']


print("Highest paid employee -> ")
for key in workers:
    if workers[key]['maosh'] == max_salary:
        print(f"Name: {key}\nSalary: {max_salary} $")

print(f"The average salary is:  {average_salary / len(workers):.2f}")

