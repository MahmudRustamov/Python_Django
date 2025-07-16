"""Foydalanuvchidan satrlar ro'yxatini kiritishni so'rang. (Bu jarayon foydalanuvchi bo'sh satrni 
kiritguncha davom etsin). Ushbu satrlardan birinchi harfini olib tashlangan boshqa yangi ro'yxat yarating"""


words = []
while True:
    text = input("Enter your text here: ")
    if text == " ":
        break
    else:
        words.append(text[1::])
print(words)
    
