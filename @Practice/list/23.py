"""Bizga list berilgan va foydalanuvchi tomonidan bitta son kiritiladi. 
Agarda ikkita elementining yig'indisi kiritilgan songa teng bo'lsa,
 shu elementlarning indekslarini ekranga chiqaruvchi dastur tuzing."""


lst = [1, 2, 33, 5, 6, 7, 7]
num = int(input("Enter number: "))

for i in range(len(lst)-1):
    for j in range(i+1, len(lst)):
        if lst[i] + lst[j] == num:
            print(i, j)
        

