import functools


def takes(*types):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*_args, **kwargs):
            func_call = func(*_args, **kwargs)
            flag = True
            for argument in (list(_args) + list(kwargs.values())):
                if type(argument) not in types:
                    flag = False
                    break
            if flag:
                return func_call
            else:
                raise TypeError

        return wrapper

    return decorator
