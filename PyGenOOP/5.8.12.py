class NonNegativeObject:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if isinstance(value, (int, float)):
                self.__dict__[key] = abs(value)
                continue
            self.__dict__[key] = value
