def best_seller(products: list) -> str:
    max_quantity = None
    names = []
    for product in products:
        if max_quantity is None:
            max_quantity = product
        elif product["quantity"] > max_quantity["quantity"]:
            max_quantity = product
        elif product["name"] in max_quantity["name"]:
            max_quantity["quantity"] += product["quantity"]

    return f"Name: {max_quantity["name"]}\nPrice: {max_quantity["price"]}\nQuantity: {max_quantity["quantity"]}"


market = [ 
    {"name": "Non", "price": 3000, "quantity": 120, "in_stock": True},
    {"name": "Yog'", "price": 25000, "quantity": 35, "in_stock": True},
    {"name": "Un", "price": 7000, "quantity": 0, "in_stock": False},
    {"name": "Shakar", "price": 10000, "quantity": 40, "in_stock": True},
    {"name": "Tuxum", "price": 1200, "quantity": 40, "in_stock": True},
    {"name": "Choy", "price": 15000, "quantity": 25, "in_stock": True},
    {"name": "Tuz", "price": 2000, "quantity": 60, "in_stock": True},
    {"name": "Makaron", "price": 8000, "quantity": 50, "in_stock": True},
    {"name": "Sut", "price": 9000, "quantity": 0, "in_stock": False},
    {"name": "Tuxum", "price": 1200, "quantity": 300, "in_stock": True},
    {"name": "Non", "price": 65000, "quantity": 200, "in_stock": True}
]

print(best_seller(market)) 