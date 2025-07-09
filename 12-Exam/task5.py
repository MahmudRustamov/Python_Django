# numbers = [8, 78, 90, 16, 88, 55, 1024, 70]
# maks = int(max(numbers)/2)

# digit = int(input("Enter a number: "))

# for i in range(len(numbers)):
#     for j in range(1, maks):
#         if digit ** j == numbers[i]:
#             print(f"{numbers[i]} -> {digit} ** {j}")

# step - 2 
numbers = [8, 78, 90, 16, 88, 55, 1024, 70]
digit = int(input("Enter a number: "))

for num in numbers:
    power = 1
    while pow(digit, power) <= num: 
        if pow(digit, power) == num:
            print(f"{num} -> {digit} ** {power}")
            break
        power += 1
