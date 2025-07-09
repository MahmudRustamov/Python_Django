txt = "stop"
word = ' '
while True:
    text = input("Enter a number: ")
    if text == txt:
        break
    else:
        word += f"{text} "
print(word)