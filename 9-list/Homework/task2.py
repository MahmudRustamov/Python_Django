num1 = [1, 16, 13, 67, 54, 87, 32]
num2 = [ 34, 56, 23, 46, 77, 12, 78, 30, 99]

num1.extend(num2)
num2.clear()
num1.sort()

print(num1)