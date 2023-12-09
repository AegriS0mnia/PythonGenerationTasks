import functools


class MaxRetriesException(Exception):
    pass


def retry(times=1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal times
            for i in range(times):
                try:
                            _func_call = func(*args, **kwargs)
                            return _func_call
                except:
                    times -= 1
            else:
                raise MaxRetriesException
        return wrapper
    return decorator
