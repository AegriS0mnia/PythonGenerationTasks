def get_digits(number: int | float) -> list[int]:
    """Возвращает список цифр числа"""
    
    return [int(i) for i in str(number) if i.isdigit()]
