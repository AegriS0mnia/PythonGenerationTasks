import itertools as it


def factorials(n):
    res = it.accumulate(range(1, n + 1), lambda x, y: x * y)
    yield from res
