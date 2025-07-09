"""Foydalanuvchi natural son kiritadi. Shu sonning natural bo'luvchilarini toping:"""

n = int(input("n= "))

for num in range(1, n+1):
    if n % num == 0:
        print(num)

