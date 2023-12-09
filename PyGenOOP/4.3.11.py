from typing import NoReturn


class Numbers:
    def __init__(self):
        self.numbers: list[int] = []

    def add_number(self, number: int) -> NoReturn:
        self.numbers.append(number)

    def get_even(self) -> list[int]:
        return [i for i in self.numbers if i % 2 == 0]

    def get_odd(self) -> list[int]:
        return [i for i in self.numbers if i % 2 == 1]
