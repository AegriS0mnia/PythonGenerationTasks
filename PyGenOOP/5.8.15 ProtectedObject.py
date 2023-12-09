class ProtectedObject:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            object.__setattr__(self, key, value)

    @staticmethod
    def protect():
        raise AttributeError('Доступ к защищенному атрибуту невозможен')

    def __getattribute__(self, item):
        if item == '__dict__':
            self.protect()
        if item.startswith('_'):
            self.protect()
        else:
            return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        if key.startswith('_'):
            self.protect()
        object.__setattr__(self, key, value)

    def __delattr__(self, item):
        if item.startswith('_'):
            self.protect()
        object.__delattr__(self, item)
