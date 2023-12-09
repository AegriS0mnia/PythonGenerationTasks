class Vector:
    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y

    def abs(self) -> float:
        return (self.x**2 + self.y**2)**0.5
