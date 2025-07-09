"""Butun sonni oqib olib, unda yonma-yon 2 ta bir xil son bor yoki yoqligini aniqlovchi dastur yozing."""

num = input("Enter a number: ")

for i in range(len(num)-1):
    if num[i] == num[i+1]:
        print("Bor")
        break
else:
    print("yoq")