name = input("Enter your name: ")
count = 0
n = 0

while n < len(name):
    if name[n].istitle():
        count += 1
    n += 1
print(count)   
