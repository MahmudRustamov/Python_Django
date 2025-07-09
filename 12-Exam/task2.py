"""Masala. 15 bal.
    Foydalanuvchidan ikkita malumotni input sifatida oling, biri uning
    ismi, ikkinchisi esa shunchaki bir harf. Vazifangiz usha harf ismini
    ichida nechta ekanligini hisoblab berish. Tekshirishingiz kerak bo'lgan
    narsalar: ism faqat harflardan tashkil topgan bo'lishi kerak, uzunligi kamida
    2 ta belgidan iborat bo'lishi kerak, ikkinchi inputni uzunligi esa faqat
    1 bo'lishi mumkin va u harf bo'lishi shart."""

while True:
    choice = input("Would you like to enter your name (yes/no): ").lower().strip()

    if choice == 'yes':
        name = input("Enter your name: ")
        sign = input("Enter a letter: ")

        if name.isalpha() and len(name) >= 2:
            if len(sign) == 1 and sign.isalpha():
                print(f"Your name has {name.count(sign)} letters of {sign}")
            else:
                print("Warning! Enter a letter not more or not numbers")
        else:
            print("You should only use letters and have 2 letters at least")
    else:
        print("Thank you for using our application!")
        break