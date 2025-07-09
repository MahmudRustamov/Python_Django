"""Foydalanuvchi son kiritiadi. Agarda son 3ga bo'linsa ekranga "Fizz",
yokida 5ga bo'linsa "Buzz", ikkalasiga ham bo'linsa, FizzBuzz chiqsin."""


num = int(input("Enter a number: "))

if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
elif num % 5 == 0:
    print("Buzz")
elif num % 3 == 0:
    print("Fizz")
