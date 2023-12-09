from functools import singledispatchmethod


class Formatter:

    @singledispatchmethod
    @staticmethod
    def format(data):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @format.register(int)
    @staticmethod
    def _(data):
        print(f'Целое число: {data}')

    @format.register(float)
    @staticmethod
    def _(data):
        print(f'Вещественное число: {data}')

    @format.register(dict)
    @staticmethod
    def _(data):
        print(f"Пары словаря: {', '.join(map(repr, data.items()))}")

    @format.register(list)
    @staticmethod
    def _(data):
        print(f"Элементы списка: {', '.join(map(repr, data))}")

    @format.register(tuple)
    @staticmethod
    def _(data):
        print(f"Элементы кортежа: {', '.join(map(repr, data))}")
