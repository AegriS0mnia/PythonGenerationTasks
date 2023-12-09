import math


class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.diameter = radius * 2
        self.area = math.pi * radius ** 2
