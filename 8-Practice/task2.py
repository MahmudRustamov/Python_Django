import os
os.system("cls")
from random import randint

comp_guess = randint(1, 100)
attempt = 1

while attempt <= 5:
    user_guess = int(input(f"{attempt}. Guess the number: "))
    if user_guess == comp_guess:
        print(f"<<<<You win!!>>>>")
        break
    else:
        if user_guess > comp_guess:
            print(f"Enter lower number. {5-attempt} attempts left")
        elif user_guess < comp_guess:
            print(f"Enter higher numebr. {5-attempt} attempts left")
    attempt += 1
else:
    print("You loose")

