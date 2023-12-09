import functools
from typing import Callable


def make_html(tag: str):
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            html_tag: str = f'<{tag}>{func(*args, **kwargs)}</{tag}>'

            return html_tag

        return wrapper

    return decorator
