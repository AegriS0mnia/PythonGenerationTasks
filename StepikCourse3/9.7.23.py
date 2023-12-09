def exception_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result, 'Функция выполнилась без ошибок'
        except TypeError:
            return None, 'При вызове функции произошла ошибка'

    return wrapper
