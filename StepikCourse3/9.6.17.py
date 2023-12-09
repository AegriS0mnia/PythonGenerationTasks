def matrix_to_dict(matrix: list[list[int | float]]) -> dict[int, list[int | float]]:
    return {index: row for index, row in enumerate(matrix, 1)}

