"""Ikkita butun son A va B (A<B) berilgan. Shu sonlar oralig`ida
joylashgan barcha butun sonlarni o`sish tartibida toping ( shu sonlar
lan birgalikda) va ularni soni N ni ham"""

a = int(input("Enter a= "))
b = int(input("Enter b= "))

if a < b:
    temp = a
    while a <= b:
        print(a)
        a += 1   
    print(f"{temp} va {b} sonlari orasida {temp-a} ta butun son bor")
else:
    print("b should be greater than a")