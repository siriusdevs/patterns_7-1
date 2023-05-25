# Написать декоратор классов, который принимает название атрибута, и делает этот
# атрибут в классе скрытым и работающим через property, в котором сеттер проверяет число
# на то, что это положительный (>=0) integer.

# Написать класс Person: age: int, name: str, использовать на нём написанный декоратор
# для атрибута age.
@staticmethod
def positive_integer_property(attribute_name):

    hidden_attribute = '_' + attribute_name

    def decorator(cls):
        setattr(cls, hidden_attribute, None)

        @property
        def prop(self):
            return getattr(self, hidden_attribute)
        
        @prop.setter
        def prop(self, value):
            if isinstance(value, int) and value >= 0:
                setattr(self, hidden_attribute, value)
            else:
                raise ValueError
        @prop.setter
        def prop(self, value):
            if isinstance(value, int) and value >= 0:
                setattr(self, hidden_attribute, value)
            else:
                raise ValueError(f'{attribute_name} слишком большое или не число')
        setattr(cls, attribute_name, prop)
        
        return cls
    
    return decorator

@positive_integer_property('age')
class Person:
    def __init__(self, name: str, age: int):
        self.name: str = name
        self.age: int = age

person = Person('Hero', 3)
print(person.name)  
print(person.age)  

person.age = 40
print(person.age)  



try:
    person.age = -10
except ValueError as e:
    print(str(e))
