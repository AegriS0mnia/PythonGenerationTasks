from typing import Generator, Any

def interleave(*args: Any) -> Generator:
    for collection in range(len(args[0])):
        for elem in args:
            yield elem[collection]
