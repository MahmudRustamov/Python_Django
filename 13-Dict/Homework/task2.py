"""
2. Kitob do'konidagi mahsulotlar haqida quyidagi ma'lumot bor:

books = {
    "Python asoslari": {"muallif": "Aliyev", "narx": 120000, "sotildi": 30},
    "Django": {"muallif": "Valiyev", "narx": 150000, "sotildi": 20},
    "Algoritmlar": {"muallif": "Karimov", "narx": 180000, "sotildi": 15},
}
2.1  Eng ko'p sotilgan kitobni toping.
2.2 Do'kondagi barcha kitoblarning umumiy daromadini hisoblang.

"""


books = {
    "Python asoslari": {"muallif": "Aliyev", "narx": 120000, "sotildi": 30},
    "Django": {"muallif": "Valiyev", "narx": 150000, "sotildi": 20},
    "Algoritmlar": {"muallif": "Karimov", "narx": 180000, "sotildi": 15},
}

max_sold_book = 0
book_name = None
total_price = 0


for key, value in books.items():
    if value['sotildi'] > max_sold_book:
        max_sold_book = value['sotildi']
        book_name = f"\nName: {key}\nAuthor: {value['muallif']}\nPrice: {value['narx']}\nSold: {value['sotildi']}"
    total_price += value['narx'] * value['sotildi']

print("Information about best-selling book. ", book_name)

print("Total income of those books is: ", total_price)
