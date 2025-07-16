"""2. Foydalanuvchi  probel bilan istalgancha son kiritsin. Song quyidagilarni bajaring:
- ro'yxatdagi elementlarning umumiy sonini chop eting.
- ro'yxatdagi oxirgi elementni chop eting.
- ro'yxatni teskari tartibda chop eting."""

numbers = input("Enter numbers with space: ").split(" ")
ls = []
for i in numbers:
    if i != "":
        ls.append(int(i))

print(ls)
print(len(ls))
print(ls[-1])
print(ls[::-1])