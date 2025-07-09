import random

nums = []
sum_three = 0
sum_evens = 0
counter = 1

while counter <= 16:
    nums.append(random.randint(10, 100))
    counter += 1
    print(nums)
print(nums)

for i in range(len(nums)):
    if nums[i] % 2 == 0:
        sum_evens += nums[i]
    else:
        nums[i]%3 == 0
        sum_three += nums[i]

print(f"Juft sonlarning yigindisidan 3 ga bolinadigan sonalr yigindisi ayirmasi {sum_evens-sum_three}")
