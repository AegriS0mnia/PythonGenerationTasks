from typing import Any

def is_iterable(obj:Any) -> bool:
    return True if '__iter__' in dir(obj) else False
