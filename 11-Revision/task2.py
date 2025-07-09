ls = []
count = 0 

while True:
    text = input("Enter text here: ").lower()
    if text == "exit":
        break
    else:
        if text not in ls:
            ls.append(text)


print(ls)   
    