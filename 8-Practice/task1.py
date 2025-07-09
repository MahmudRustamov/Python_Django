num = int(input("Enter a number: "))

for i in range(10, num):
    result = 0
    for j in str(i):
        result += int(j)
    print(f"{i} -> {result}")

