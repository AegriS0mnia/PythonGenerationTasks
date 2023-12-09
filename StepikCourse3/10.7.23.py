def around(iterable):
    iterable = list(iterable)
    if not iterable:
        pass
    elif len(iterable) == 1:
        yield None, iterable[0], None
    elif len(iterable) == 2:
        yield None, iterable[0], iterable[1]
        yield iterable[0], iterable[1], None
    else:
        for index in range(1, len(iterable) - 1):
            if index == 1:
                yield None, iterable[0], iterable[1]
            yield (iterable[index - 1], iterable[index], iterable[index + 1])

        yield iterable[-2], iterable[-1], None
