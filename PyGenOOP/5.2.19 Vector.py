class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __eq__(self, other):
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        elif isinstance(other, tuple):
            return len(other) == 2 and (self.x == other[0] and self.y == other[1])
        return NotImplemented
