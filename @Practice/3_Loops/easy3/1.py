"""Foydalanuchu son kiritadi uni quyidagi tarzda chiqaring!
    Input: 3
    Output: 1 2 3 2 1
    Input: 5
    Output: 1 2 3 4 5 4 3 2 1
"""


num = int(input("n= "))


for i in range(1, num+1):
    print(i, end=" ")

for j in range(num-1, 0, -1):
    print(j, end=" ")


