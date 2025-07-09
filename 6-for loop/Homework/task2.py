n = int(input("Enter a number: "))

for is_odd in range(n, 0, -1):
    if is_odd % 2 == 1:
        print(is_odd)