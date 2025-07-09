"""Foydalanuvchi uchburchakning 3 ta ichki burchaklarini kiritadi. 
Shu burchaklarga qarab, bunday uchburchak mavjud yoki yo'qlini ayting"""

a = int(input("Enter a= "))
b = int(input("Enter b= "))
c = int(input("Enter c= "))

if a <= 0 or b <= 0 or c <= 0:
    print("Note! Angles must be positive numbers")
elif a + b + c:
    print("Yes, such a triangle is possible.")
else:
    print("Yes, such a triangle is not possible.")