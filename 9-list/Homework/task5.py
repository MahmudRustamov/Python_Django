import random

counter = 0
nums = []

while counter <= 8:
    nums.append(random.randint(10, 100))
    counter += 1
print(nums)

max_odd_index = nums[0]
for i in range(1, len(nums)):
    if nums[i] % 2 != 0 and nums[i] > max_odd_index:
        max_odd_index = nums[i]
print(f" Musbat toq sonlarning eng katta indeksi {nums.index(max_odd_index)}")
