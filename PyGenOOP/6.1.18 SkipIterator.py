class SkipIterator:
    def __init__(self, iterable, n):
        self.n = n
        self.iterable = list(iterable)
        self.indexes = list(range(0, len(self.iterable), n + 1))

    def __iter__(self):
        return self

    def __next__(self):
        if self.indexes:
            return self.iterable[self.indexes.pop(0)]
        else:
            raise StopIteration
