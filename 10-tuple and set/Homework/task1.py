"""Sizda bir foydalanuvchi sotib olgan mahsulotlar ro'yxati 
bor, va hozirda bozorda bor mahsulotlar ham ro'yxati bor
sizni vazifangiz foydalanuvchi sotib olmagan 3 ta 
boshqa mahsulotni unga ko'rsatadigan funksiya yozish"""

purchased = ['phone', 'pen', 'notebook', 'book', 'charger']
market = ['laptop', 'phone', 'pen', 'notebook', 'headphones', 'book', 'charger','case']

print("Products which you should buy :", set(market).difference(purchased))