import itertools as it


def drop_while_negative(iterable):
    yield from it.dropwhile(lambda num: num < 0, iterable)
