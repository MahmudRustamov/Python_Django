"""Foydalanuvchi sizga bir gap va malum bir so'z kiritadi sizni vazifangiz usha gapni
   ichidan usha so'zlarni olib tashlash"""


text = input("Enter your text: ")
word = input("Enter a word to delete: ")

if word in text:
    text = text.replace(word, " ")
else:
    print(f"{word} is not in the text")

print(text)