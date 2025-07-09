"""Rostlikka tekshiring: Kiritilgan 3 xonali sonning teskarisi ham 3 xonali. Palindrom."""

number = input("N = ")

if number[0] != '-' and number == number[::-1]:
    print(True)
elif number.startswith('-') and number[1::] == number[:0:-1]:
    print(True)   
else:
    print(False)


number = input("N = ")

if number.startswith('-'):
    is_palindrome = number[1:] == number[:0:-1]
else:
    is_palindrome = number == number[::-1]

print(is_palindrome)
