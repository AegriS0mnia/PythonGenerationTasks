class Const:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __getattribute__(self, item):
        return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        if self.__dict__.get(key) is None:
            self.__dict__[key] = value
            return
        raise AttributeError('Изменение значения атрибута невозможно')

    def __delattr__(self, item):
        raise AttributeError('Удаление атрибута невозможно')
