sum = 0

while True:
    number = int(input("Enter a number: "))
    if number == 0:
        break
    else:
        sum += number
print(sum)