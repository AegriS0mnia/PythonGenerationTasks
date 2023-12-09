class DefaultObject:
    def __init__(self, default=None, **kwargs):
        self.default = default
        for key, value in kwargs.items():
            self.__dict__[key] = value

    def __getattr__(self, item):
        return self.default
