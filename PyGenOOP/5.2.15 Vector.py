class Vector:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def __str__(self):
        return f"Вектор на плоскости с координатами ({self._x}, {self._y})"

    def __repr__(self):
        return f'Vector{self._x, self._y}'
