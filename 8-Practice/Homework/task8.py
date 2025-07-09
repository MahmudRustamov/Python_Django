"""Berilgan soni palindrom deb xisoblasa bo`ladimi, ya’ni o`ngdan
chapga va chapdan o`ngga bir xil o`qiladimi. Misol: 123321, 202,
9889, 5555"""

num = input("Enter a number: ")

if num.isdigit() and num[::-1] == num:
    print("Number is polindrome")
else:
    print("Number is not Polindrome")