def all_together(*args):
    for i in args:
        yield from i
