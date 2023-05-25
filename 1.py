from faker import Faker
from random import randint as rnd
fake = Faker()


class PersonAttrsCreator(type):
    __instances = dict()

    @classmethod
    def age(mcs) -> int:
        return rnd(0, 100)

    @classmethod
    def name(mcs) -> str:
        return fake.name()

    def __call__(cls):
        if cls not in cls.__instances:
            cls.__instances[cls] = super().__call__()
        return cls.__instances[cls]


p1 = PersonAttrsCreator
p2 = PersonAttrsCreator
print(p1.name(), p1.age())
print(p2.name(), p2.age())
