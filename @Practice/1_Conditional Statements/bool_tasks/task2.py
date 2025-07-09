"""Rostlikka tekshiring. Foydalanuvchi kiritgan son 3 ga bo'linadi ammo 2 ga bo'linmaydi."""

num = int (input("Enter a number: "))
number = True
if num % 3 == 0 and num % 2 != 0:
    print(True)
else:
    print(False)
