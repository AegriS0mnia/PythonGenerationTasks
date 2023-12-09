from typing import Any


def transpose(matrix: list[list[Any]]) -> list[list[Any]]:
    new_matrix: list[list[Any]] = list(map(list, zip(*matrix)))
    return new_matrix
