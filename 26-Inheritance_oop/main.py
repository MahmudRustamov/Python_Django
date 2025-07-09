class A:
    def __init__(self, name, year):
        self.name = name
        self.year = year


    def greeting(self):
        return f"Hello, {self.name}"
    

class B(A):
    def __init__(self, name, year, age):
        super().__init__(name, year)
        self.age = age


object1 = A(name = "Ali", year = 1001)
object2 = B(name = "Gani",  age = 10, year = 2002)


print(object1.greeting())
print(object2.name)
print(object2.age)
print(object2.year)