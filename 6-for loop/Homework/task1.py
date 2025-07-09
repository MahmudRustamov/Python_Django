n = int(input("Enter a number: "))

for is_even in range(n, 0, -1):
    if is_even % 2 == 0:
        print(is_even)