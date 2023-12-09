def with_previous(iterable):
    iterable = list(iterable)
    for index, elem in enumerate(iterable):
        if index == 0:
            yield (elem, None)
        else:
            yield (elem, iterable[index - 1])
