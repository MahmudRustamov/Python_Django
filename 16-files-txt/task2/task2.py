
with open(file = "fruits1.txt", mode = "r") as file:
    fruits1 = file.readlines()

with open(file = "fruits2.txt", mode = "r") as file1:
    fruits2 = file1.readlines()

# print(fruits1, fruits2)

with open(file = "fruits3.txt", mode = "w") as file3:
    for fruit in fruits1:
        if fruit in fruits2:
            file3.write(fruit)
            
