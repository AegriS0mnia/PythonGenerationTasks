class Circle:
    def __init__(self, radius: int | float):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)
