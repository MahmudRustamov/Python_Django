"""Input orqali gap kiritiladi. Shu gapdagi so'zlarni bosh harfi orqali alfavit tartibida chiqarish kerak."""


text = input("Your text: ").split()

text.sort()

for i in text:
    print(f"{i} ", end="")

