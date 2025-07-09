"""Haqiqiy son A va butun son N(>0) berilgan. Chiqaring: 1+A+A2+A3+
+ AN"""

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
nums = " "
summ = 0

if num2 > 0:
    for num in range(1, num2+1):
        nums += f"{num1 ** num} + "
        summ += num1 ** num
    nums = nums.split("+")[:-1]
    nums = "+".join(nums)    
    print(f"{num1}^{num2} = {nums}= {summ}")
else:
    print("Number that you entered should be grater than 0")