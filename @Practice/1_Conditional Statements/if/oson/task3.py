"""Foydalanuvchi baho kiritadi. Agar bu baho
[80-100] oraliqda bo'lsa —> ekranga "5" chiqsin
[60-79] oraliqda bo'lsa —> ekranga "4" chiqsin
[40-59] oraliqda bo'lsa —> ekranga "3" chiqsin
[20-39] oraliqda bo'lsa —> ekranga "2" chiqsin
[0-19] oraliqda bo'lsa —> ekranga "1" chiqsin
aks holda -> "Siz bebahosiz" degan yozuv chiqsin"""

grade = int(input("Enter your grades (0-100): "))
if not 0 <= grade <= 100:
    print("Error: Grade must be between 0 and 100.")
elif grade >= 80:
    print("5")
elif grade >= 60:
    print("4")
elif grade >= 40:
    print("3")
elif grade >= 20:
    print("2")
else:
    print("1")