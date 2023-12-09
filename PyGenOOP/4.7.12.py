class Rectangle:
    def __init__(self, length: int | float, width: int | float):
        self.__length = length
        self.__width = width

    @property
    def length(self):
        return self.__length

    @property
    def width(self):
        return self.__width

    @classmethod
    def square(cls, side: int | float):
        return cls(side, side)
