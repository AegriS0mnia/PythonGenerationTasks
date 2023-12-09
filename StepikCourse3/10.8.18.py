def roundrobin(*args):
    iterables = list(list(i) for i in args)
    while iterables:
        if not any(iterables):
            break
        for index, iterable in enumerate(iterables):
            if iterable:
                elem = iterables[index][0]
                iterables[index] = iterables[index][1:]
                yield elem
