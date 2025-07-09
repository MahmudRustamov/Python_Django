"""Rostlikka tekshiring. Foydalanuvchi kiritgan son 300 dan katta va 3 ga bo'linadi."""

num = int(input("Num = "))

if num > 300 and num % 3 == 0:
    print(True)
else:
    print(False)