class Logger:
    def __getattribute__(self, item):
        return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        print(f'Изменение значения атрибута {key} на {value}')
        self.__dict__[key] = value

    def __delattr__(self, item):
        print(f'Удаление атрибута {item}')
        del self.__dict__[item]
