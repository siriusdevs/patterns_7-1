
from typing import List
from datetime import datetime

class Product:
    def __init__(self, name: str, due_date: datetime):
        self.name = name
        self.due_date = due_date


class Warehouse:
    def __init__(self):
        self._products: List[Product] = []

    def add(self, product: Product) -> None:
        self._products.append(product)

    def remove(self, product: Product) -> None:
        if product in self._products:
            self._products.remove(product)

    def clean(self) -> None:
        current_time = datetime.now()
        self._products = [product for product in self._products if product.due_date > current_time]


milk = Product('Milk', '28.05.2023')
cocount = Product('Cocount', '23.05.2023')







