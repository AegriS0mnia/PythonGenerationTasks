class DictItemsIterator:
    def __init__(self, info):
        self.info = info
        self.keys = [*info]
    def __iter__(self):
        return self
    def __next__(self):
        if self.keys:
            key = self.keys.pop(0)
            return key, self.info[key]
        else:
            raise StopIteration
