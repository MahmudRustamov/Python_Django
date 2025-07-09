"""Berilgan sonni faktorialini hisoblang. N sonining faktorialini quyidagi
formula bo`yicha xisoblang: N!=1*2*3*…N"""

factorial = int(input("Enter factorial and this program calc: "))
num = 1

for i in range(1, factorial+1):
    num *= i

print("The factorial of ", factorial, 'is ', num)

