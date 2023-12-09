class Peekable:
    def __init__(self, iterable):
        self.iterable = list(iterable)
        self.iterator = iter(iterable)
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        return next(self.iterator)

    def peek(self, default=StopIteration):
        if self.index >= len(self.iterable):
            if default != StopIteration:
                return default
            raise StopIteration

        elem = self.iterable[self.index]

        return elem
