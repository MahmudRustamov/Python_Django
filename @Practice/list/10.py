"""Tasodifiy sonlardan hosil bolgan ro'yxatdagi ikkinchi 
eng katta va ikkinchi eng kichik yozuvlarni chop eting"""


from random import randint

ls = []
counter = 1
while counter <= 20:
    ls.append(randint(1, 100))
    counter += 1

print(ls)
ls.sort()
print(ls)
print(f"second min: {ls[1]}\nsecond max: {ls[-2]}")