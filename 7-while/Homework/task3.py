text = input("Enter text: ")
n_txt = " "
n = 0

while n < len(text):
    if text[n] not in "auieo":
        n_txt +=  text[n] 
    n += 1
print(n_txt)