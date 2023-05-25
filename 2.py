from datetime import datetime


class Product:
    def __init__(self, name: str, due_date: datetime):
        self.name = name
        self.due_date = due_date


class Sklad:
    class_product = Product

    def __init__(self, name: str):
        self.name = name
        self.__products = []

    def add(self, product: Product):
        if not isinstance(product, Product):
            print(f"{product.__class__.__name__} is not {Product.__class__.__name__} class")
            return
        if product.due_date < datetime.now():
            print(f"product {product.name} broken")
            return
        self.__products.append(product)

    def remove(self, product: Product):
        if not isinstance(product, Product):
            print(f"{product.__class__.__name__} is not {Product.__class__.__name__} class")
            return
        if product not in self.__products:
            print(f"{product.name} not found in {self.name} sklad")
            return
        self.__products.remove(product)

    def clean(self):
        for product in self.__products:
            if product.due_date < datetime.now():
                # если в складе будет несколько одинаковых обьектов то мы тут ляжем
                self.__products.remove(product)

