import functools

def add_attrs(**kwargs):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **_kwargs):
            _func = func
            for attr in kwargs:
                _func.__dict__[attr] = kwargs[attr]
            return _func
        return wrapper()
    return decorator

