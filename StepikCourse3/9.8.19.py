import functools
from typing import Callable

def repeat(times: int = 1):
    """Декоратор, который вызывает функцию введенное количество раз"""

    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(times):
                value: Callable = func(*args, **kwargs)
            return value

        return wrapper

    return decorator
