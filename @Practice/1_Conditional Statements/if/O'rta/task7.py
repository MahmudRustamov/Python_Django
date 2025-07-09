"""Barcha uch xonali sonlar orasidagi raqamlari 2 marta takrorlanadigan sonlarni chiqaruvchi dastur tuzing."""

for num in range(100, 1000):
    num = str(num)
    if num[0] == num[1] or num[0] == num[2] or num[1] == num[2]:
        print(num)
