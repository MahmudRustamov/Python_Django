"""For loop yordamida quyidagi ro'yxatlarni yarating.
a) 0 dan 49 gacha bo'lgan butun sonlardan iborat ro'yxat

b) 1 dan 50 gacha bo'lgan butun sonlarning kvadratlarini o'z ichiga olgan ro'yxat.

c) ['a','bb','ccc','dddd', . . . ] kabi ohiri 26 ta harfdan iborat z bilan tugaydigan ro'yxat.
"""

# integers = []
# for i in range(50):
#     integers.append(i)
# print(integers)

# squares = []
# for j in range(1, 51):
#     squares.append(j*j)
# print(squares)

counter = 1
letters = []
for i in range(97, 123):
    letters.append(f"{chr(i)*counter}")
    counter += 1
print(letters)