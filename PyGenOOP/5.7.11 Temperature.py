class Temperature:
    def __init__(self, temperature):
        self.temperature = temperature

    def __str__(self):
        return f"{round(self.temperature, 2)}°C"

    def __int__(self):
        return int(self.temperature)

    def __bool__(self):
        return self.temperature > 0

    def __float__(self):
        return float(self.temperature)

    def to_fahrenheit(self):
        return self.temperature * (9/5) + 32

    @classmethod
    def from_fahrenheit(cls, temperature):
        return Temperature((temperature - 32) * (5/9))
