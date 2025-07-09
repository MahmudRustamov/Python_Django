"""Oy raqami berilgan. Kiritilgan oy qaysi faslga tegishli ekanini aniqlovchi dastur yozing"""

month = input("Enter a number")

if 1 <= int(month) <= 12:
    if month in ['1', '3', '5', '7', '8', '10', '11']:
        print('31')
    elif month == '2':
        print('28')
    else:
        print('30')
else:
    print("Enter a number between 1-12")