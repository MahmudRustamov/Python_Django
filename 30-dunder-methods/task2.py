"""2. __add__ — Savat (shopping cart)
Vazifa: Ikkita savatdagi mahsulotlarni birlashtiring."""


class Shopping_cart:
    def __init__(self, price):
        self.price = price


    def __add__(self, other):
        return self.price + other.price
    

shop = Shopping_cart(25)
shop1 = Shopping_cart(12)

print(shop+shop1)