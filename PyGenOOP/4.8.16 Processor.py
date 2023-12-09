from functools import singledispatchmethod


class Processor:

    @singledispatchmethod
    @staticmethod
    def process(data):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @process.register(int)
    @process.register(float)
    @staticmethod
    def _numeric_process(data):
        return data * 2

    @process.register(str)
    @staticmethod
    def _str_process(data):
        return data.upper()

    @process.register(list)
    @staticmethod
    def _list_process(data):
        return sorted(data)

    @process.register(tuple)
    @staticmethod
    def _tuple_process(data):
        return tuple(sorted(data))
