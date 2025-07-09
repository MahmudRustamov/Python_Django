num = int(input("Enter a number: "))

ls = []

for i in range(1, num):
    if i % 2 == 1:
        ls.append(i)
print(ls)