from typing import Hashable, Callable


def make_upper(func: Callable) -> Callable:
    def wrapper(*args: Hashable, sep: str = ' ', end: str = '\n') -> Callable:
        modified_result = sep.upper().join([str(i).upper() for i in args]) + end.upper()
        return func(modified_result, end='')

    return wrapper


print = make_upper(print)
