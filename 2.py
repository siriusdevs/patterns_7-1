
class Ball:

    __instances_balls = {}

    def __init__(self, color: str, radius: int) -> None:
        self.color = color
        self.radius = radius

    def __new__(cls, color: str, radius: int):
        key = f'{color}_{radius}'
        if key in cls.__instances_balls:
            return cls.__instances_balls[key]
        instance_ball = type(cls.__name__, (object,), {'c': color, 'r': radius})()
        cls.__instances_balls[key] = instance_ball
        return instance_ball


b1 = Ball("Red", 7)
b2 = Ball("Green", 9)
agen_b1 = Ball("Red", 7)

print(b1)
print(agen_b1)
