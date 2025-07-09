a = int(input("A(X0) ni kiriting: "))
b = int(input("A(Y0) ni kiriting: "))
c = int(input("B(X1) ni kiriting: "))
d = int(input("B(Y1) ni kiriting: "))

if ((a**2)+(b**2))*0.5 > ((c**2)+(d**2))*0.5:
    print("B nuqta O(0,0) nuqataga yaqin")
elif ((a**2)+(b**2))*0.5 == ((c**2)+(d**2))*0.5:
    print("Ikkala nuqta ham bir xil kordinatada joylashgan")
else:
    print("A nuqta O(0,0) nuqataga yaqin")
