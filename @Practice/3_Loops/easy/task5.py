"""Kiritilgan natural sonni mukammal ekanligini aniqlovchi dastur tuzing.
6,28,496 sonlari mukammal chunki:

- 6: bo'luvchilari 1,2,3; va 1+2+3=6.
- 28: bo'luvchilari 1,2,4,7,14; va 1+2+4+7+14=28.
- 496: bo'luvchilari 1,2,4,8,16,31,62,124,248; va ularning yig‘indisi 496.
"""


num = int(input("Enter a number: "))
result = 0
for i in range(1, (num//2)+1):
    if num % i == 0:
        result += i

if num == result:
    print("Perfect number")
else:
    print("It is not a perfect number!!!")