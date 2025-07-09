"""Mahsulot zaxiralari - Ombordagi kam qolgan mahsulotlarni chiqarish."""


def low_stock(products: list) -> str:
    low_quantity = None
    for product in products:
        if low_quantity is None:
            low_quantity = product
        elif product['stock'] < low_quantity['stock']:
            low_quantity = product
    return f"The least stocked product\nName: {low_quantity['name']}\nStock: {low_quantity['stock']}"


store = [
    {
        "name": "Sugar",
        "stock": 120},
    {
        "name": "Flour", 
        "stock": 35},
    {
        "name": "Rice", 
        "stock": 15},
    {
        "name": "Oil", 
        "stock": 5},
    {
        "name": "Tea", 
        "stock": 55},
    {
        "name": "Salt", 
        "stock": 8
    }
]

print(low_stock(store))
