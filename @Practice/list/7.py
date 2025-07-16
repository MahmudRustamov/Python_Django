"""1 va 100 oraliqda 20 ta tasodifiy sonlardan iborat ro'yxatini hosil qilib,  chop etadigan dastur yozing."""
from random import randint

ls = []
counter = 1
while counter <= 20:
    ls.append(randint(1, 100))
    counter += 1

for item in ls:
    print(item)