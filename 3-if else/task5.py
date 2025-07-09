x = int(input("x = "))
y = int(input("y = "))

if x > 0 and y > 0:
    print("1-chorak")
elif x > 0 and y < 0:
    print("4-chorak")
elif x < 0 and y < 0:
    print("3-chorak")
elif x == 0 and y != 0:
    print("Nuqta y oqida yotadi")
elif x != 0 and y == 0:
    print("Nuqta x oqida yotadi")
elif x == 0 and y == 0:
    print("x va y Nolga teng")
else:
    print("2-chorak")