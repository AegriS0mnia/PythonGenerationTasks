def zip_longest(*args, fill=None):
    len_longest = len(max(args, key=len))

    for index, obj in enumerate(args):
        if len(obj) < len_longest:
            args[index].extend([fill] * (len_longest - len(obj)))

    return list(zip(*args))


print(zip_longest([1, 2, 3, 4, 5], ['a', 'b', 'c'], fill='_'))
