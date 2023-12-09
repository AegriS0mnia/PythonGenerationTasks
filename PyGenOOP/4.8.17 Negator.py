from functools import singledispatchmethod


class Negator:

    @singledispatchmethod
    @staticmethod
    def neg(value):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @neg.register(bool)
    @staticmethod
    def _bool_neg(value):
        return not value

    @neg.register(int)
    @neg.register(float)
    @staticmethod
    def _numeric_neg(value):
        return -value
