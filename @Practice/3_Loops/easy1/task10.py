"""Barcha uch xonali sonlar orasidagi raqamlaridan kamida bittasida 3 raqami bolgan sonlani chiqaruvchi dastur tuzing.
Masalan, 103, 113 …. 333, 343 …. 993 va hokazo"""

for i in range(103,999):
    if "3" in str(i):
        print(i)