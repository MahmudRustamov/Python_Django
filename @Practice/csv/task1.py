import csv 

data = ["User3", "2005", "35"]

# with open(file="users.csv", mode="w", encoding="UTF-8", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerow(data)
#     print("data is added")

# with open(file="users.csv", mode="a", encoding="UTF-8", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerows(data)
#     print("data is added")

with open(file="users.csv", mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    print(list(reader))