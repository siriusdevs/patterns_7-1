from datetime import datetime


class Product:
    def __init__(self, name: str, due_date: datetime):
        self.name = name
        self.due_date = due_date

class Warehouse:
    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def remove(self, product: Product):
        self.products.remove(product)

    def clean(self):
        current_time = datetime.now()
        self.products = [product for product in self.products if product.due_date > current_time]



product1 = Product("Чурчхела", datetime(2023, 8, 10))
product2 = Product("Сулугуни", datetime(2023, 8, 7))
product3 = Product("Хачапури", datetime(2023, 8, 15))
warehouse = Warehouse()
warehouse.add(product1)
warehouse.add(product2)
warehouse.add(product3)
warehouse.remove(product2)
warehouse.clean()
