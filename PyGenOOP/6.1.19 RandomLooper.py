import random as rd


class RandomLooper:
    def flatten(self, obj):
        flat_list = []
        for index, value in enumerate(obj):
            if isinstance(value, (list, tuple, set, dict)):
                flat_list.extend(value)
            if isinstance(value, (int, float, str)):
                flat_list += value
        return flat_list

    def __init__(self, *args):
        self.iterables = list(args)
        self.objects = self.flatten(self.iterables)

    def __iter__(self):
        return self

    def __next__(self):

        while self.objects:
            rd.shuffle(self.objects)
            return self.objects.pop(0)
        else:
            raise StopIteration
