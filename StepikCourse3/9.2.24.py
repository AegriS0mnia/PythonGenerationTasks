import functools


def ignore_exception(*exs):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                func_call = func(*args, **kwargs)
                return func_call
            except exs as err:
                return print(f'Исключение {type(err).__name__} обработано')

        return wrapper

    return decorator
