numbers = input("Enter numbers with space: ").split(" ")
n = input("n = ")
ls = []

for i in range(len(numbers)):
    if n in numbers[i]:
        print(numbers[i])