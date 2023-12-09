from typing import NoReturn


class Bee:
    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y

    def move_up(self, n) -> NoReturn:
        self.y += n

    def move_down(self, n) -> NoReturn:
        self.y -= n

    def move_right(self, n) -> NoReturn:
        self.x += n

    def move_left(self, n) -> NoReturn:
        self.x -= n
