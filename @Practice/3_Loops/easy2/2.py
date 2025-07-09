"""N soni kiritiladi. N sonining eng katta raqamini toping."""

num = (input("N= "))
max_num = 0

for i in num:
    if int(i) > max_num:
        max_num = int(i)
print(max_num)


#step 2:

# num = input("Enter a number: ")

# print(max(num))
