"""
3.Supermarket kassasi

cart = {
    "Olma": 3,
    "Banan": 2,
    "Uzum": 5,
}
prices = {
    "Olma": 12000,
    "Banan": 18000,
    "Uzum": 15000,
}
Jami xarid narxini hisoblang.

"""
def total_spending(shopping):
    total_expenses = 0
    for product, quantity_product in shopping.items():
        if product in prices:
            print(f"{product} -> {quantity_product * prices[product]} ")
            total_expenses += quantity_product * prices[product]
    return total_expenses

cart = {
    "Olma": 3,
    "Banan": 2,
    "Uzum": 5,
}
prices = {
    "Olma": 12000,
    "Banan": 18000,
    "Uzum": 15000,
}

print("Your total expenses: ", total_spending(cart))



