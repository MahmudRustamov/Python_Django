for i in range(10):
    print()
    for j in range(10):
        if i == 0 or j == 0 or i == 9 or j == 9:
            print("*", end=" ")
        elif i +1 > j:
            print("*", end=" ")
        else:
            print(" ", end=" ")