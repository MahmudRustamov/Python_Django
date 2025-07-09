"""# 7-vazifa: Metod orqali boshqarish
# Employee klassini yarating, __salary private atributi bo‘lsin.
# increase_salary(percent) metodi orqali maoshni faqat 1-100 oralig‘ida oshirishga ruxsat bering."""

class Employee:
    def __init__(self, salary):
        self.__salary = salary

    @property
    def salary(self):
        return  self.__salary


    @salary.setter
    def salary(self, amount):
        if 1< amount <= 100:
            self.__salary = amount
        else:
            raise ValueError("Wrong Data")


e = Employee(1200)
e.salary = 77
print(e.salary)
