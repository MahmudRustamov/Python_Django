text = input("Enter text here: ").split(' ')
ls= []

for word in text:
    ls.append(f"{word} - {text.count(word)} marta")

ls = list(set(ls))

for letter in ls:
    print(letter)