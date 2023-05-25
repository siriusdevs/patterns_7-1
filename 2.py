from datetime import datetime


class Product:
    def __init__(self, name, due_date):
        self.name = name
        self.due_date = due_date


class Warehouse:
    _collection = []

    def add(self, product):
        self._collection.append(product)

    def remove(self, product):
        self._collection.remove(product)

    def clean(self):
        self._collection = [product for product in self._collection if product <= datetime.now()]
