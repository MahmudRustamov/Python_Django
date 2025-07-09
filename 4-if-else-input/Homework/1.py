weather = int(input("Haroratni kiriting: "))

if weather < 0:
    print("Havo juda sovuq. Issiq kiyining!")
elif 0 < weather <= 20:
    print("Havo salqin, kurtka kiying!")
else:
    print("Havo issiq, yengil kiyinishingiz mumkin.")