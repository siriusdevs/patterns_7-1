class Ball:
    __instances = {}

    def __new__(cls, color, radius):
        key = f'{color}_{radius}'
        if key not in cls.__instances:
            cls.__instances[key] = super().__new__(cls)
        return cls.__instances[key]

    def __init__(self, color: str, radius: int):
        self.color, self.radius = color, radius

b = Ball('red', 4)
b2 = Ball('white', 5)
b3 = Ball('red', 4)
print(b, b2, b3)
