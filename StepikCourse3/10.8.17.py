import itertools as it
import string


def alnum_sequence():
    digits = it.cycle(range(1, 27))
    uppercase = it.cycle(string.ascii_uppercase)
    while True:
        yield next(digits)
        yield next(uppercase)
