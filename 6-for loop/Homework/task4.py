name = input("Enter your name: ")

num_vowel = 0
for letter in name:
    if letter in 'auoieo':
        num_vowel += 1

if num_vowel > 0:
    print(f"Sizning ismingizda {num_vowel} ta unli harflar bor")
else:
    print("Your name has no vowel letters")