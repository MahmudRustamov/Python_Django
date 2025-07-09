"""Foydalanavchi belgi kiritiladi. Agar shu belgi unli harf bo'lsa ekranga 
"unli harf" degan yozuvni chiqaring, agar undosh harf kiritgan bo'lsa "undosh harf" 
degan yozuv chiqaring, aksa holda "bunday harf yo'q" degan yozuvni chiqaring."""

letter = input("Enter a letter: ").lower()
print(len("o'"))
if letter.isalpha():
    if letter in ["a", "i", "u", "e", "o"] or letter == "o'":
        print("Vowel")
    else:
        print("Consonant")
else:
    print("There is no such kind of letter!")
