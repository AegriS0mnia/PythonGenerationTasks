def intersperse(iterable, delimiter):
    if not iterable:
        return

    iterable = iter(iterable)
    first_elem = next(iterable)
    yield first_elem

    for i in iterable:
        yield delimiter
        yield i
