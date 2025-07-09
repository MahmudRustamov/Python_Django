import random

a = []
b = []
same_elements = []
counter = 1
while counter <= 17:
    a.append(random.randint(10, 100)) 
    b.append(random.randint(10, 100)) 
    counter += 1
print(a)
print(b)

summ = 0

for num in range(len(a)):
    if a[num] in b:
        same_elements.append(a[num])

if len(same_elements) > 0:
    print(f"The same elements are {same_elements}")
else:
    print("There are no same elemnts in A and B lists ")