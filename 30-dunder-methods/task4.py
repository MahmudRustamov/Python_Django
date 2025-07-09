"""__contains__ va __len__ — Ishchilar ro'yxati
Vazifa: Ishchilar ro'yxatini tekshirish"""

class Contact:
    def __init__(self, name, users):            
        self.name = name
        self.lst = users  

    def __contains__(self, other):
        return other in self.lst 
            
    def __len__(self):
        return len(self.lst) 

it_company = Contact("TechSoft", ["Ali", "Laylo", "Bobur"])

print("Ali" in it_company) 
print(len(it_company))