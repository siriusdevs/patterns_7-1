# Написать декоратор классов, который принимает название атрибута, и делает этот
# атрибут в классе скрытым и работающим через property, в котором сеттер проверяет число
# на то, что это положительный (>=0) integer.

# Написать класс Person: age: int, name: str, использовать на нём написанный декоратор
# для атрибута age.

class Person:

    def __init__(self, name: str) -> None:
        self.name = name
    
    def __str__(self) -> str:
        return f'My name is {self.name}'

def validator(age):
    return age >= 0

def creator(age, validator: function):
    def decorator(some_class):
        private_attr = f'__{age}'

        def getter(self):
            return getattr(self, private_attr)
        
        def setter(self, value):
            if validator(value):
                setattr(self, private_attr, value)
            else:
                print('wrong age')
        
        setattr(some_class, age, property(getter, setter))
        return some_class
    return decorator
