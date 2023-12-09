from typing import NoReturn


class Scales:
    def __init__(self):
        self.left_scale_pan: int = 0
        self.right_scale_pan: int = 0

    def add_left(self, weight: int) -> NoReturn:
        self.left_scale_pan += weight

    def add_right(self, weight: int) -> NoReturn:
        self.right_scale_pan += weight

    def get_result(self) -> str:
        if self.left_scale_pan > self.right_scale_pan:
            return 'Левая чаша тяжелее'
        elif self.left_scale_pan < self.right_scale_pan:
            return 'Правая чаша тяжелее'
        else:
            return 'Весы в равновесии'
