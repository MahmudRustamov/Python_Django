"""Foydalanuvchidan N, M va K sonini kiritadi, N soni va M soni orasidagi K ta Fibonachi sonini chop eting"""



n = int(input("N= "))
m = int(input("M= "))
k = int(input("K= "))
a, b = 1, 1
counter = 0

if  (m == 1 or m == 2):
    print("1")
else:
    for i in range(3, m):
        temp = a
        a = b
        b = b + temp
        print(f"{i} => {b}")


#ozgina xatosi bor 
