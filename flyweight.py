# Написать класс Мяч (ball). У мяча есть color: str и radius: int.
# Использовать паттерн Flyweight (приспособленец), чтобы при инициализации
# мяча с параметрами, как уже у существующего мяча, возвращался тот самый существующий мяч.

class Ball:
    __balls = {}
    
    def __new__(cls, color: str, radius: str) -> object:
        key = f'{color}_{radius}'
        if key in cls.__balls:
            return cls.__balls[key]
        ball = type(Ball.__class__.__name__, (object,), {'color': color, 'radius': radius})()
        cls.__balls[key] = ball
        return ball

    def __init__(self, color: str, radius: str) -> None:
        self.color = color
        self.radius = radius
    

bl = Ball('gr', '12')
bl2 = Ball('gr', '12')
print(bl is bl2)