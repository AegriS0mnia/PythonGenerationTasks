class Rectangle:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    @property
    def length(self):
        return self._length

    @property
    def width(self):
        return self._width

    def __repr__(self):
        return f'Rectangle({self._length}, {self._width})'

