"""1dan Ngachan sonlarni juftlarini yigindisini ekranga chiqaruvchi dastur tuzing."""

n = int(input("Enter a number: "))
result = 0

for i in range(n):
    if i % 2 == 0:
        result += i
print(result)