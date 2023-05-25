# Написать класс Мяч (ball). У мяча есть color: str и radius: int.
# Использовать паттерн Flyweight (приспособленец), чтобы при инициализации
# мяча с параметрами, как уже у существующего мяча, возвращался тот самый существующий мяч.



class Ball:
    __instances = {}

    def __new__(cls, color: str, radius: int):
        key = f'{color}_{radius}'
        if key in cls.__instances:
            return cls.__instances[key]
        instance = type(cls.__name__, (object, ), {"color":color,"radius":radius})()
        cls.__instances[key] = instance
        return instance
        
    def __init__(self, color: str, radius: int) -> None:
        self.color, self.radius = color, radius


a = Ball("green", 5)
b = Ball('green', 5)
print(a)
print(b)
print(a is b)