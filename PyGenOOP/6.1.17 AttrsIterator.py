class AttrsIterator:
    def __init__(self, obj):
        self.attrs = [pair for pair in obj.__dict__.items()]

    def __iter__(self):
        return self

    def __next__(self):
        if self.attrs:
            return self.attrs.pop(0)
        else:
            raise StopIteration
