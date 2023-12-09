import itertools as it

def tabulate(func):
    iterator = it.count(start=1)
    while True:
        yield func(next(iterator))
