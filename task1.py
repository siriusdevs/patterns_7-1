def age_checker(attr, validator):
    def decorate(cls):
        pr_attr = f'__{attr}'
        def getter(self):
            return getattr(self, pr_attr)
        def setter(self, new_value):
            if validator(new_value):
                setattr(self, pr_attr, new_value)
        setattr(cls, attr, property(getter, setter))
        return cls
    return decorate


def check_age(age: int):
    if isinstance(age, int):
        return age >= 0
    raise Exception('Attr age must be integer > 0')

@age_checker('age', check_age)
class Person:
    def __init__(self, age: int, name: str):
        self.age, self.name = age, name

p = Person(10, 'John')
print(p.age)
p.age = 12
print(p.age)
p.age = 'ksme'
