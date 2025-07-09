tpl = (1, 2, 3, 4, 5, 6, 7, 8, 9)
even = []
odd =[]

for i in range(len(tpl)):
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print(f"Even numbers: {even}\nOdd numbers: {odd}")