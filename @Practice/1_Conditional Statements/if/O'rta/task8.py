"""Oy raqami berilgan. Kiritilgan oy qaysi faslga tegishli ekanini aniqlovchi dastur yozing """

month = (input("Enter a number: "))

if 1 <= int(month) <= 12:
    if month in "345":
        print("Spring")
    elif month in "678":
        print("Summer")
    elif month in ["9","10","11"]:
        print("Autumn")
    else:
        print("Winter")
else:
    print("Enter a number between 1-12")

