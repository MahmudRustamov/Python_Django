"""1-1999 son berilgan. Shu sonni Ikki honali juft, uch honali toq tarzida yozib beradigan dastur yozing"""

num = int(input("Enter a number: "))

if 1 <= num <= 2000:
    if num % 2 == 0:
        print(f"{len(str(num))} digit number -> Even number")
    else:
        print(f"{len(str(num))} digit number -> Odd number")
else:
    print("Enter numbers between 1-1999")