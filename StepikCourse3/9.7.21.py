from typing import Callable
from typing import Any

def do_twice(func: Callable) -> Callable:
    def wrapper(*args, **kwargs) -> Any:
        call_1 = func(*args, **kwargs)
        func(*args, **kwargs)
        return call_1
    return wrapper

