from typing import Iterable, Iterator, Callable


def starmap(func: Callable, iterable: Iterable) -> Iterator:
    result = map(lambda el: func(*el), iterable)
    return result
