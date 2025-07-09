"""5 ga karrali bo`lmagan va 3 ga karrali bo`lgan sonlarni toping,
shuningdek 5 ga karrali bo`lmagan va 3 ga karrali bo`lgan sonlarni
summasini toping."""

n = int(input("Enter a number (number > 2): "))

if n >= 3:
    for i in range(3, n+1):
        if i % 5 != 0 and i % 3 == 0:
            print(i)
else:
    print("Make sure the nuber is higher than 2")