from functools import total_ordering


@total_ordering
class Month:
    def __init__(self, year, month):
        self.year = year
        self.month = month

    def __repr__(self):
        return f"Month({self.year}, {self.month})"

    def __str__(self):
        return f"{self.year}-{self.month}"

    def __eq__(self, other):
        if isinstance(other, Month):
            return self.year == other.year and self.month ==other.month
        elif isinstance(other, tuple):
            return len(other) == 2 and (self.year == other[0] and self.month == other[1])
        return NotImplemented
    def __gt__(self, other):
        if isinstance(other, Month):
            return self.year > other.year or (self.year == other.year and self.month > other.month)
        if isinstance(other, tuple):
            return len(other) == 2 and (self.year > other[0] or (self.year == other[0] and self.month > other[1]))
        return NotImplemented
