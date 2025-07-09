file = open(file = "names.txt", mode = "a")

count = 1
while count <= 3:
    name = input("Enter your name: ")
    file.write(f"{name}\n")
    count += 1 

file.close()