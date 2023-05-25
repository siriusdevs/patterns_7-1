from typing import List

class Ball:
    def __init__(self, color: str, radius: int):
        self.color = color
        self.radius = radius

class Ball_creator:
    def __init__(self):
        self.keys = list()
        self.balls = list()

    def create_ball(self, color: str, radius: int):
        if (color, radius) in self.keys:
            return self.balls[self.keys.index((color, radius))]
        ball = Ball(color, radius)
        self.keys.append((color, radius))
        self.balls.append(ball)
        return ball

creator = Ball_creator()
ball1 = creator.create_ball('Red', 20)
ball2 = creator.create_ball('Blue', 100065423)
ball3 = creator.create_ball('Red', 20)
print(ball1)
print(ball2)
print(ball3)