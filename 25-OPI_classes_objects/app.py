import csv


class Student:
    def __init__(self, name, age, student_id):
        self.name = name
        self.age = age
        self.student_id = student_id

    
    def calculate_year(self):
        current_year = 2025
        return current_year - self.age
    

    def save(self):
        with open(file="students.csv", mode="a", encoding="UTF-8", newline="") as file:
            writer = csv.writer(file)
            data = [self.name, self.age, self.student_id]
            writer.writerow(data)
            print("Data is added!!")


student1 = Student(name="Ali", age="21", student_id="12121")
student2 = Student(name="Vali", age="22", student_id="11121")


student2.save()

