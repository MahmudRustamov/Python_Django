"""Ikkita butun son A va B (A<B) berilgan. Shu sonlar oralig`ida
joylashgan barcha butun sonlarni kamayish tartibida toping ( bu
sonlarni hisobga olmay) va ularni soni N ni ham. """

a = int(input("Enter a= "))
b = int(input("Enter b= "))
counter = 0
counter = b-1
print(f"\n{a} dan {b} gacha bolgan sonlar soni: {counter-a} ->")

if a < b:
    while a < counter:
        print(counter)
        counter -= 1
else:
    print("b shoul be greater than a")