class Cycle:
    def __init__(self, iterable):
        self.iterable = iterable
        self.counter = -1
    def __iter__(self):
        return self

    def __next__(self):
        self.counter += 1
        return self.iterable[self.counter % len(self.iterable)]

