import json
import os


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


    def read(self):
            if os.path.exists("products.json") and os.path.getsize("products.json") > 0:
                with open(file="products.json", mode="r") as file:
                    return json.load(file)
            return []
    

    def calculate_total_price(self):
        total_price = 0
        products = self.read()
        for product in products:
            if product["price"]:
                total_price += product["price"]
        return f"Total price for all Products: {total_price}"
    


class Electronics(Product):
    def __init__(self, name, price,  made_in, year):
        super().__init__(name, price)
        self.product_type = "electronics"
        self.made_in = made_in
        self.year = year

    
    def add_to_file(self):
        products = self.read()
        data = {
            "type": self.product_type,
            "name": self.name,
            "price": self.price,
            "made_in": self.made_in,
            "year": self.year
        }
        products.append(data) 

        with open(file="products.json", mode="w") as file:
            json.dump(products, file, indent=4)


    def calculate_total_price(self):
        total_price = 0
        products = self.read()
        for product in products:
            if product["type"] == "electronics":
                total_price += product["price"]
        return f"Total price for electronics: {total_price}"
    

    def show_data(self):
        products = self.read()
        for product in products:
            if product["type"] == "electronics":
                print(f"Product Name: {product["name"]}\nPrice: {product["price"]}\nYear: {product["year"]}\nMade in: {product["made_in"]}")



class Book(Product):
    def __init__(self, name, price, pages):
        super().__init__(name, price)
        self.product_type = "book"
        self.pages = pages

    
    def add_to_file(self):
        products = self.read()
        data = {
            "type": self.product_type,
            "name": self.name,
            "price": self.price,
            "pages": self.pages,
        }
        products.append(data)  

        with open(file="products.json", mode="w") as file:
            json.dump(products, file, indent=4)   

    
    def show_data(self):
        products = self.read()
        for product in products:
            if product["type"] == "book":
                print(f"Book Title: {product["name"]}\nPrice: {product["price"]}\nPages: {product["pages"]}")


    def calculate_total_price(self):
        total_price = 0
        products = self.read()
        for product in products:
            if product["type"] == "book":
                total_price += product["price"]
        return f"Total price for books: {total_price}"
       

class Clothing(Product):
    def __init__(self, name, price, color):
        super().__init__(name, price)
        self.product_type = "clothing"
        self.color = color
 

    def add_to_file(self):
        products = self.read()
        data = {
                "type": self.product_type,
                "name": self.name,
                "price": self.price,
                "color": self.color,
            }  
        products.append(data)

        with open(file="products.json", mode="w") as file:
            json.dump(products, file, indent=4)


    def show_data(self):
            products = self.read()
            for product in products:
                if product["type"] == "clothing":
                    print(f"Name: {product["name"]}\nPrice: {product["price"]}\nColor: {product["color"]}")


    def calculate_total_price(self):
        total_price = 0
        products = self.read()
        for product in products:
            if product["type"] == "clothing":
                total_price += product["price"]
        return f"Total price for clothing: {total_price}"
                

    
product = Product(name="product", price=1200) 
print(product.calculate_total_price())

electronics = Electronics(name="iPhone 16 Pro Max", price=1200, made_in="China", year="2025")
# electronics.add_to_file()
# electronics.show_data()
print(electronics.calculate_total_price())

book = Book(name="The peace and war", price=12000, pages=120)
# book.add_to_file()
# book.show_data()
print(book.calculate_total_price())

clothing = Clothing(name="Nike", price=20, color="white")
# clothing.add_to_file()
# clothing.show_data()
# print(clothing.calculate_total_price())