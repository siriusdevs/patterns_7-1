def decorator(*args, **kwargs):
    def set_attrs(cls):
        for i in args:
            setattr(cls, f'_{str(i)}', None)

        def decorate(age, _):
            try:
                if int(age) < 0:
                    return
            except ValueError:
                return
            setattr(cls, 'age', age)
            return cls

        return decorate

    return set_attrs


@decorator('new')
class Person:
    def __init__(self, name):
        self.name = name


print(Person(1000, 'name').__dict__)
