import functools
from typing import Any


def prefix(prefix: str, to_the_end: bool = False) -> Any:
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if to_the_end:
                string: str = func(*args, **kwargs) + prefix
            else:
                string: str = prefix + func(*args, **kwargs)
            return string

        return wrapper

    return decorator
