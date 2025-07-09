age = int(input("Enter your age: "))

if 0 < age <= 6:
    print(f"Chiptaning narxi {age} yosh uchun tekin!")
elif 0 < age <= 18:
    print(f"{age} yosh uchun chipta narxi -> 20 000")
elif age <= 0:
    print("Xatolik! Yoshingizni qayta kiriting")    
else:
    print(f"{age} yosh uchun chipta narxi -> 40 000")