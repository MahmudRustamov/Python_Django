""" X va Y sonlari berilgan. Bu sonlar koordinata o'qining qaysi chorakgida ekanligni aniqlang."""

x = int(input("x = "))
y = int(input("y = "))


if x > 0 and y > 0:
    print("I chorak")
elif x < 0 and y > 0:
    print("II chorak")
elif x < 0 and y < 0:
    print("III chorak")
elif x > 0 and y < 0:
    print("IV chorak")
elif x == 0 and y != 0:
    print("")
else:
    print("Something is wrong!")