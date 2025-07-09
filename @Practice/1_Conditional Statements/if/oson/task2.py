"""Foydalanuvchi hafta kuni raqamini kiritadi"""

day = input("Enter a num: ")

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _ :
        print("Something went wrong!")