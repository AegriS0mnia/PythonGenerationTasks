def quantify(iterable, predicate=None):
    return len(list(filter(predicate, iterable)))
