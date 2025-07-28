nums = {1, 2, 3, 6, 7}

is_found = False
for i in nums:
    if i == 7:
        is_found = True

# if is_found:
#     print("The number you enter is in the set")
# else:
#     print("Number is not found")

digit = 6
if digit in list(nums):
    print(digit, 'in the set')
else:
    print("noooooooo")