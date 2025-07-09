"""Foydalanuvchi 5 kiritsa, rasmdagi natija chiqsin. P.S. Tuzilgan sonni 6,7,8 va boshqa sonlar kiritib ham tekshirib ko'ring

* * * * *
* * * *
* * * 
* *
*

"""

num = int(input("n= "))

for i in range(num, 0, -1):
    print()
    for j in range(i, 0, -1):
        print("*", end=" ")