from typing import Any

def is_iterator(obj:Any) -> bool:
    return True if '__iter__' in dir(obj) and '__next__' in dir(obj) else False
