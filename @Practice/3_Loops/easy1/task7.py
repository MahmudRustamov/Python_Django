"""A dan B gacha bo'lgan sonlarni ekranga chiqaring. Shu sonlarni toqlari
 o'z holicha ekranga chiqarilsin, va juftlari manfiy bo'lsin."""

a = int(input("a= "))
b = int(input("b= "))

for num in range(a, b+1):
    if num % 2 == 0:
        print(-1 * num)
    else:
        print(num)