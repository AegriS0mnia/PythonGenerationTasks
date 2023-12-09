def top_grade(grades: dict[str, str | list[int]]) -> dict[str, str | int]:
    """Возвращает словарь с парами name:имя ученика и
    top_grade: наивысшая оценка ученика"""

    result = {'name': grades['name'], 'top_grade': max(grades['grades'])}

    return result