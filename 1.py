class Ball:
    __balls = []

    def __new__(cls, *args, **kwargs):
        # CUSTOM new

        color = kwargs.get("color", args[0])
        radius = kwargs.get("radius", args[1])
        for ball in Ball.__balls:
            if ball.radius == radius and ball.color == color:
                # setattr(cls, "radius", ball.radius)
                # setattr(cls, "color", ball.color)
                return ball
        setattr(cls, "radius", radius)
        setattr(cls, "color", color)
        Ball.__balls.append(cls)
        return cls

    def __init__(self, color, radius):

        self.color = color
        self.radius = radius


