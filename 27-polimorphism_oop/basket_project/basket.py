from utils import FileManager


class Basket:
    def __init__(self, filename):
        self.filemanager = FileManager("products.json")
        self.path = filename


    def show_products(self):
        pass


    def __add__(self):
        pass


    def show(self):
        pass


    def create_order(self):
        pass


    def clear(self):
        pass


    def show_orders(self):
        pass