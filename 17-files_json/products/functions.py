from file_manager import read_from_json, write_to_json

def view_products():
    products = read_from_json(file = "products.json")
    for product in products:
        print(f"Name: {product['name']}\nQuantity: {product['quantity']}\n")


def add_product():
    name = input("Enter a name: ")
    quantity = int(input("Enter quantity: "))

    data = {
        "name": name,
        "quantity": quantity
    }

    products = read_from_json(file="products.json")
    products.append(data)
    write_to_json(file="products.json", data = products)
    print("New product is added")


def delete_product():
    name = input("Enter the product name: ")
    products = read_from_json(file = "products.json")
    for index, product in enumerate(products):
        if name == product['name']:
            products.pop(index)
            write_to_json(file="products.json", data=products)
            print(f"{name} is deleted")
            return
    print("Product not found")


def clear_file():
    with open(file="products.json", mode="w") as file:
        pass
    print("File cleared successfully")

