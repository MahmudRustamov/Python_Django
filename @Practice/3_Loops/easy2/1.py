"""n natural soni berilgan (n > 0). Ildizdan chiqaruvchi funksiyadan foydalanmasdan kvadrati n dan
 katta bo'ladigan eng kichik butun к sonini (k^2 > n) aniqlovchi programma tuzing."""


number = int(input("Enter a number: "))
if number > 0:
    temp = int(number ** 0.5) + 1
    print(temp * temp, ">", number) 
else:
    print("Number should be greater than 0 !!")
