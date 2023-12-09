from typing import Callable, Iterator, Iterable


def filterfalse(predicate: Callable, iterable: Iterable) -> Iterator:
    if predicate is None:
        return filter(lambda el: bool(el) is False, iterable)
    else:
        return filter(lambda el: predicate(el) is False, iterable)
