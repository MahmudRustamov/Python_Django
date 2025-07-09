"""Foydalanuvchi natural son kiritadi, shu son va shu sonning teskarisi orasidagi farqni aniqlovchi dastur tuzing."""

number = int(input("Enter a number: "))

print("The result is: ", number-int(str(number)[::-1]))