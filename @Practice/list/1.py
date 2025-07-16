"""Foydalanuvchidan butun son kiritishini so'rang, keyin shuncha marta son kiritsin, keyin usha har bir sonni 
royxatga qoshadigan dastur yozing. Song natijani ekranga chiqaring"""


n = 5
ls = []
counter = 1
while counter <= n:
    ls.append(int(input(f"Number{counter}: ")))
    counter += 1

print(ls)
