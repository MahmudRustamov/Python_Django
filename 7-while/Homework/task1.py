text = input("Enter Text: ")
sign = input("Enter a sign: ")

count = 0
n = 0

while n < len(text):
    if text[n] == sign:
        count += 1
    n += 1
print(count)   