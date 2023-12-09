from datetime import date
from functools import singledispatchmethod


class BirthInfo:
    @singledispatchmethod
    def __init__(self, birth_date):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @__init__.register(date)
    def _(self, birth_date):
        self.__birth_date = birth_date

    @__init__.register(str)
    def _(self, birth_date):
        self.__birth_date = date.fromisoformat(birth_date)

    @__init__.register(list)
    @__init__.register(tuple)
    def _(self, birth_date):
        self.__birth_date = date(*birth_date)

    @property
    def birth_date(self):
        return self.__birth_date

    @property
    def age(self):
        if date.today().day < self.__birth_date.day and date.today().month <= self.__birth_date.month:
            return abs(date.today().year - self.__birth_date.year) - 1
        return abs(date.today().year - self.__birth_date.year)
