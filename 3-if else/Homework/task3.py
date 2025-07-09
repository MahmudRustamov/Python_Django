num = int(input("Enter a number: "))

if num % 2 == 0:
    print(num, "is an even number")
elif num % 10 == 3:
    print("This number ends with 3")
else:
    print("OK")