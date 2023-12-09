import functools


def strip_range(start: int, end: int, char: str = '.'):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            _string = list(func(*args, **kwargs))
            nonlocal end
            if end > len(_string) - 1:
                end = len(_string)
            for index in range(start, end):
                _string[index] = char
            _string = ''.join(_string)
            return _string
        return wrapper
    return decorator
