# Написать следующую структуру классов: 
# Есть класс продукт, каждый продукт имеет свойства: 
# name: str - имя, 
# due_date : datetime (можно и другой формат) - срок годности.  

# Используя паттерн компоновщик (Composite), написать класс Склад,
#  который имеет 	внутри скрытую коллекцию продуктов, умеет добавлять и удалять продукты внешними методами 
#  add(product: Product) -> None и remove(product: Product) -> None, 
#  а также 	имеет метод clean() -> None, который удаляет все просроченные продукты со склада.
from datetime import datetime


class Product:
    
    def __init__(self, name: str, due_date: datetime) -> None:
        self.name = name
        self.due_date = due_date

class Sklad:
    def __init__(self, collect: list = []) -> None:
        self.__collect = collect

    def add(self, product: Product) -> None:
        if isinstance(product, Product):
            self.__collect.append(product)
        else:
            raise Exception('Attr must be product')
    
    def remove(self, product: Product) -> None:
        if isinstance(product, Product) and product in self.__collect:
            self.__collect.remove(product)
        else:
            raise Exception('Attr must be product or in sklad')
    
    def clean(self) -> None:
        now = datetime.now()
        cnt = 0
        for product in self._collect:
            if product.due_date < now:
                self.__collect.remove(product)
                cnt += 1
        print(f'{cnt} products was deleted')

pr = Product('ya', datetime.now())
pr2 = Product('neya', datetime.now())
skl = Sklad([pr, pr2])
print(skl)
skl.remove(pr)