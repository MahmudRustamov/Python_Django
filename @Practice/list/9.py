"""Tasodifiy sonlardan hosil bolgan ro'yxatdagi eng katta va eng kichik qiymatlarni chop eting."""

from random import randint

ls = []
counter = 1
while counter <= 20:
    ls.append(randint(1, 100))
    counter += 1

# print(min(ls))
# print(max(ls))

max_num = 0
min_num = ls[0]
print(ls)
for i in ls:
    if i > max_num:
        max_num = i
    elif i < min_num:
        min_num = i
print("this is max num: ", max_num)
print("this is min num: ", min_num)