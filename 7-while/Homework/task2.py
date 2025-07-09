name = input("Enter Text: ")

count = 0
n = 0

while n < len(name):
    if name[n].isdigit():
        count += 1
    n += 1
print(f"Sizning ismingzida {count} ta raqam bor")   