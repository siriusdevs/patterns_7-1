from random import randint
from faker import Faker

class PersonAttrsCreator:
    _instance = None  

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    @staticmethod
    def age():
        return randint(0, 100)

    @staticmethod
    def name():
        fake = Faker()
        return fake.name()

person_creator = PersonAttrsCreator()
age = person_creator.age()
name = person_creator.name()
print(age, name)