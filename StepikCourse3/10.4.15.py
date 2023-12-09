import random


class RandomNumbers:
    def __init__(self, left, right, times):
        self.left = left
        self.right = right
        self.times = times

    def __iter__(self):
        return self

    def __next__(self):
        if self.times <= 0:
            raise StopIteration
        self.times -= 1

        return random.randint(self.left, self.right)
