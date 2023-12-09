def unique(iterable):
    res = []
    for i in iterable:
        if i not in res:
            res.append(i)
    yield from res
