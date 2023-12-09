from random import randint


class Dice:
    def __init__(self, sides):
        self.sides = sides

    def __call__(self):
        return randint(1, self.sides)
