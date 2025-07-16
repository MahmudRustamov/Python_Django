"""Foydalanuvchidan ixtiyoriy raqamlarni kiritishni so'rang (Bu jarayon 
foydalanuvchi 0 ni kiritguncha davom etsin). Keyin barcha 10dan katta 
bolgan sonlarni 10 bilan almashtiring"""

ls = []
while True:
    number = int(input("Enter number: "))
    if number == 0:
        break
    ls.append(number)
# print(ls)
# ls.sort()
# print(ls)

