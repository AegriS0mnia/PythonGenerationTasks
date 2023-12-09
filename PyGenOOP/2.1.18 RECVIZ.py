import functools


def recviz(func):
    calls = 1

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal calls

        _kwargs = f", {', '.join([f'{a}={repr(b)}' for a, b in kwargs.items()])}" if kwargs else ''
        _args = f"{','.join(repr(i) for i in args)}" if args else ''
        func_call = '    ' * (calls - 1) + f"-> {func.__name__}({_args}{_kwargs})"
        print(func_call)
        calls += 1
        call = func(*args, **kwargs)
        calls -= 1
        res = '    ' * (calls - 1) + f'<- {repr(call)}'
        print(res)
        return call
    return wrapper
