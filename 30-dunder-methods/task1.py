"""1. __str__ va __repr__ — Kontaktlar ro'yxati
Vazifa: Telefon kontaktlarini saqlovchi klass yozing.
"""


class GetNumber:
    def __init__(self,phone_number, name):
        self.name = name
        self.phone_number = phone_number
    

    def __str__(self):
        return self.phone_number
    

    def __repr__(self):
        return f"Name: {self.name}\tPhone: {self.phone_number}"
    


getnum = GetNumber("User", "+998")
print(getnum)


    


