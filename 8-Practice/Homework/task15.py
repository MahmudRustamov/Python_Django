"""5 ga karrali raqamlarni topin N gacha"""

n = int(input("Enter n= "))

if n > 0:
    for i in range(n):
        if i % 5 == 0:
            print(i)
else:
    print("number should be greater than 0")