"""5. Foydalanuvchi 2 ta qiymat kiritadi: harf va n butun son. Siz esa, kiritilgan harf dan n ta keyingi harfni ekranga chiqaring.
    - Katta harf kiritilsa, natija katta harf bo'lsin
    - Agar kiritilgan son 26 dan katta bo'lsa, harflar yana boshidan keladi. (Masalan: a 27 -> b)"""


harf = input("Harf kiriting: ")
qadam = int(input("Qadam: "))

if harf.isupper():
    a = ord("A")
else:
    a = ord("a")

# 0-26 oraliqda sonni hosil qil
harf_raqam = ord(harf) - a 
# harf_raqamga qadamni qo'shib yana 
# 0-26 oraliqda sonni hosil qil
harf_raqam = (harf_raqam + qadam) % 26
# a ga qadamni qo'shib ush harfni chiqar
print(harf_raqam, chr(harf_raqam + a))
