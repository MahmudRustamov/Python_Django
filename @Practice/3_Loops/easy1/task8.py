"""Foydalanuvchi natural son kiritadi. Shu sonning necha xonali son ekanligini ekranga chiqaring."""

n = int(input("n = "))
temp = n

counter = 0
while n > 0:
    n = n // 10
    counter += 1

print(f"{temp} soni {counter} xonali son")