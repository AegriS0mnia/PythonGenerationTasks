from typing import Iterable, Self


class QuadraticPolynomial:
    def __init__(self, a: int, b: int, c: int):
        self.__a = a
        self.__b = b
        self.__c = c

    @property
    def a(self):
        return self.__a

    @property
    def b(self):
        return self.__b

    @property
    def c(self):
        return self.__c

    @classmethod
    def from_iterable(cls, iterable: Iterable) -> Self:
        return cls(*iterable)

    @classmethod
    def from_str(cls, line: str) -> Self:
        return cls(*map(float, line.split()))
