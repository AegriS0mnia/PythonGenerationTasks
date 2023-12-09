from functools import lru_cache


class CachedFunction:
    def __init__(self, func):
        self.func = func
        self.cache = {}

    @lru_cache()
    def __call__(self, *args):
        self.cache.setdefault(args, self.func(*args))
        return self.func(*args)
