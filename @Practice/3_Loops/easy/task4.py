"""Foydalanuvchi natural son kiritadi. Shu sonning raqamlar yigindisini ekranga chiqaring."""

num = int(input("Enter a number: "))

result = 0
while num > 0:
    result += num % 10
    num = num // 10

print(result)