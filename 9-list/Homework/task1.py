import random

nums = []
counter = 1
while counter <= 17:
    nums.append( random.randint(10, 100)) 
    counter += 1
print(nums)

summ = 0

for num in nums:
    summ += num
print("The sum of the 17 numbers is", summ)

