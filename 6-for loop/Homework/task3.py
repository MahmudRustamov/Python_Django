# Istalgan xonali sonning raqamlarini teskari tartibda chiqarib beruvchi dastur tuzing.
num = int(input("Enter a number: "))

reversed_num = 0
for i in range(len(str(num))):
    reversed_num = reversed_num * 10 + num % 10
    num = num // 10
print(reversed_num)
