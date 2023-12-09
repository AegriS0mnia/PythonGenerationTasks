class AttrsNumberObject:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            self.__dict__[key] = value
        self.attrs_num = 0

    def __getattribute__(self, item):
        if item == 'attrs_num':
            return len(self.__dict__)
        return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        self.__dict__[key] = value
        self.__dict__['attrs_num'] += 1
