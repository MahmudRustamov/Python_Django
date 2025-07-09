"""Rostlikka tekshiring. Foydalanuvchi kiritgan sonning(aniq 3 xonali) birinchi raqami toq va oxirgisi juft"""


num = input("n = ")

if len(num) == 3:
    if int(num[0]) % 2 != 0 and int(num[-1]) %2 ==0:
        print(True)
    else:
        print(False)
else:
    print("Warning. Enter a three-digit number!")