# Написать декоратор классов, который принимает название атрибута, и делает этот
# атрибут в классе скрытым и работающим через property, в котором сеттер проверяет число
# на то, что это положительный (>=0) integer.

# Написать класс Person: age: int, name: str, использовать на нём написанный декоратор
# для атрибута age.



def checker(attr, validator):

    def decorator(class_):
        private = f'__{attr}'
        
        def getter(self):
            print(1)
            return getattr(self, private)
        
        def setter(self, value):
            validator(value)
            setattr(self, private, value)

        setattr(class_, attr, property(getter, setter))
        return class_

    return decorator

def is_positive_number(number: int):
    if isinstance(number, int) and number >= 0:
        return number
    raise Exception(f'{number} is not valid number')

def is_name(name: str):
    if isinstance(name, str) :
        return name
    raise Exception(f'{name} is not valid name')


@checker('age', is_positive_number)
@checker('name', is_name)
class Person:

    def __init__(self, age: int, name :str) -> None:
        self.age, self.name = age, name


a = Person(5,"5")

print(a.name)