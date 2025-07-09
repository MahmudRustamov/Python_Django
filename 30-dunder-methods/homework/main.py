

class Student:
    def __init__(self, full_name, age, birthday, gender, courses):
        self.full_name = full_name
        self.age = age
        self.birthday = birthday
        self.gender = gender
        self.courses = courses


    def __add__(self, other):
        return f"Name: {self.full_name}\tAge: {self.age}\nName: {other.full_name}\tAge: {other.age}"
    

    def __sub__(self, other):
        if self.age > other.age:
            return f"{self.full_name} is older"
        else:
            return f"{other.full_name} is older"
        

    def __mul__(self, other):
        return f"Result of ages: {self.age * other.age}"
    

    def __truediv__(self, other):
         return f"Result of ages: {self.age / other.age}"
    

    def __iadd__(self, other):
        self.age += other.age
        return self


    def __isub__(self, other):
        other.age -= self.age
        return self


    def __imul__(self, other):
        self.age *= other.age
        return self
    

    def __itruediv__(self, other):
        self.age /= other.age
        return self
    

    def __len__(self):
        return len(self.courses)
    

    def __iter__(self):
        return iter(self.courses)
    

    def __contains__(self, item):
        return item in self.courses



student = Student("Ali", 21, "20-12-2000", "male", ["Math", "Python", "Java", "English", "Fullstack", "PHP"])
student2 = Student("Vali", 23, "21-11-2003", "male", ["Russian", "German", "HTML", "NodeJS"])
print(student + student2)
print(student - student2)
print(student * student2)
print(student / student2)


student += student2
print(student.age)
student -= student2
# print(student.age)
student *= student2
student /= student2

print(f"Number of courses: {len(student)}\n")

for subject in student2:
    print(subject)

print("Python" in student)