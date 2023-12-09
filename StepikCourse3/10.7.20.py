def stop_on(iterable, obj):
    for i in iterable:
        if i == obj:
            break
        yield i
