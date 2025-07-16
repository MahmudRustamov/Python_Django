"""Tasodifiy sonlardan hosil bolgan ro'yxatdagi elementlarning o'rtacha qiymatini chop eting."""

from random import randint

ls = []
counter = 1
while counter <= 20:
    ls.append(randint(1, 100))
    counter += 1

print(sum(ls) / len(ls))
