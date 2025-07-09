"""Haqiqiy son A va butun son N(>0) berilgan. A ning barcha 1 dan N
gacha bo`lgan darajalarini toping. """

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))

if num2 > 0 and num1 > 0:
    for num in range(1, num2+1):
        print(f"{num1}^{num} = {num1 ** num}")
else:
    print("Number that you entered should be grater than 0")