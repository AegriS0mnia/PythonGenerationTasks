def takes_positive(func):
    def wrapper(*args, **kwargs):
        if any(map(lambda el: isinstance(el, (str, float)), list(args) + list(kwargs.values()))):
            raise TypeError
        elif any(map(lambda el: el <= 0, list(args) + list(kwargs.values()))):
            raise ValueError
        return sum(args) + sum(kwargs.values())
    return wrapper

