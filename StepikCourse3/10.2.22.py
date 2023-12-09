from typing import Any, Optional


def get_min_max(data: list[Any]) -> Optional:
    if data:
        index_of_min: int = min(enumerate(data), key=lambda tup: tup[1], default=(0, 0))[0]
        index_of_max: int = max(enumerate(data), key=lambda tup: tup[1], default=(0, 0))[0]

        return index_of_min, index_of_max
