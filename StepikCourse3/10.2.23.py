import copy
from typing import Any, Optional


def get_min_max(data: Any) -> Optional:
    if data:
        try:
            data = iter(data)
            min_el = next(data)
            max_el = copy.deepcopy(min_el)
            for el in data:
                if min_el >= el:
                    min_el = el
                if max_el <= el:
                    max_el = el
            return min_el, max_el
        except StopIteration:
            pass
