"""Haqiqiy son A va butun son N(>0) berilgan. A ning N chi darjasini
toping: AN = A·A··A(A soni N martta ko`paytiriladi)"""

n= int(input("Enter a number: "))
m= int(input("Enter a power: "))
nums = ""
# print(n ** m)

if n > 0:
    for num in range(1, m+1):
        nums += f"{n} * " 
    print(f"{n}^{m} -> {nums[:-2]}= {n ** m}")
else:
    print("Enter a number which should be greater than 0")


