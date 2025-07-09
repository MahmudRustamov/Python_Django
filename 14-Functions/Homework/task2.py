"""
2. Mashinalar ro'yxati

cars = {
    "Cobalt": {"narx": 12000, "yil": 2022},
    "Malibu": {"narx": 25000, "yil": 2023},
    "Damas": {"narx": 9000, "yil": 2021},
}
Eng arzon mashinani toping.
Eng yangi mashinani toping.
"""

def cheapest_car(automobiles):
    lowest_price = None
    for name, info in automobiles.items():
        if lowest_price is None:
            lowest_price = (name, info,)
        elif info['narx'] < lowest_price[1]['narx']:
            lowest_price = (name, info,)
    return f"The cheapest car\nName: {lowest_price[0]}\nPrice: {lowest_price[1]['narx']} $\n"

def new_car(vehicles):
    newest_car = None
    for name, info in vehicles.items():
        if newest_car is None:
            newest_car = (name, info,)
        elif info['yil'] > newest_car[1]['yil']:
            newest_car = (name, info,)
    return f"The Newest Car\nName: {newest_car[0]}\nYear: {newest_car[1]['yil']}"


cars = {
    "Cobalt": {"narx": 12000, "yil": 2022},
    "Malibu": {"narx": 25000, "yil": 2023},
    "Damas": {"narx": 9000, "yil": 2021},
}

print(cheapest_car(cars))
print(new_car(cars))