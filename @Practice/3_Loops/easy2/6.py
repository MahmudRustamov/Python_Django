"""Foydalanuvchi 5 kiritsa, rasmdagi natija chiqsin.

11111
10001
10001
10001
11111

"""


num = int(input("n= "))


for i in range(num):
    print()
    for j in range(num):
        if i == 0 or i == 4 or j == 0 or j == 4:
            print("1", end="")
        else:
            print("0", end="")

