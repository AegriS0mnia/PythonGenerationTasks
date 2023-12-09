import functools
from typing import Any, Callable


def returns(datatype: Any):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            func_call: Callable = func(*args, **kwargs)
            if isinstance(func_call, datatype):
                return func_call
            else:
                raise TypeError

        return wrapper

    return decorator

