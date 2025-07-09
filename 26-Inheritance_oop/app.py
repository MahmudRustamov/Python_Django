"""
1. create a base class Vehicle(type) with a method move(). Then, create two subclasses,
    Car(type,name) and Boat(type,name), each overriding the move() method. Write a function that takes
    a Vehicle object and calls its move() method.
"""


class Vehicle:


    def __init__(self, type):
        self.type = type


    def move(self):
        return "Something is moving ...."


class Car(Vehicle):
    def __init__(self, type, name):
        super().__init__(type)
        self.name = name
    

    def move(self):
        return "Car is coming here "


class Boat(Vehicle):
    def __init__(self,type, name):
        super().__init__(type)
        self.name = name


    def move(self):
        return "Boat is moving!!!"
    


object1 = Vehicle("BMW")
object2 = Car("BMW", "M5")
object3 = Boat("Nimadir","User")

print(object1.move())
print(object2.move())
print(object3.move())


