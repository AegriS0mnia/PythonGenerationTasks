def pairwise(iterable):
    if not iterable:
        pass
    else:
        iterable = list(iterable)
        for index in range(1, len(iterable)):
            yield (iterable[index - 1], iterable[index])
        yield iterable[-1], None
