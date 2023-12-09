import string


def verification(login, password, success, failure):
    if not(any(map(lambda l: l in string.ascii_letters, password))):
        return failure(login, 'в пароле нет ни одной буквы')
    elif not(any(map(lambda l: l in string.ascii_uppercase, password))):
        return failure(login, 'в пароле нет ни одной заглавной буквы')
    elif not(any(map(lambda l: l in string.ascii_lowercase, password))):
        return failure(login, 'в пароле нет ни одной строчной буквы')
    elif password.isalpha():
        return failure(login, 'в пароле нет ни одной цифры')
    else:
        return success(login)
