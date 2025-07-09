"""Internet tezligi - Foydalanuvchi uchun eng yaxshi tarifni tanlash.
    foydalanuvchidan qancha puli borligini so'raysiz, usha puli yetadigan
    eng yaxshi tarifni chiqarib berasiz"""


def suitable_plan(best_plans: list, money: int) -> list: 
    offers = list()
    for plan in best_plans:
        if money >= plan['price']:
            offers.append(f"Name: {plan['name']}\nPrice: {plan['price']}\nSpeed: {plan['speed']}")
    return offers


plans = [
    {"name": "Basic", "price": 30000, "speed": 5},
    {"name": "Standard", "price": 50000, "speed": 10},
    {"name": "Plus", "price": 75000, "speed": 20},
    {"name": "Fast", "price": 100000, "speed": 50},
    {"name": "Ultra", "price": 150000, "speed": 100},
]

budget = int(input("How much money can you afford for your Internet Traffic: "))
offers = suitable_plan(plans, budget)

if len(offers) == 0:
    print(f"There are no plans for {budget} som")
else:
    for i in range(len(offers)):
        print(f"Here You can see plans\n------ {i+1} ------\n{offers[i]}")