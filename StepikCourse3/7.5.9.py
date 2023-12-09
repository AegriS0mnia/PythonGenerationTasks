import sys


class PasswordError(Exception):
    pass


class LengthError(PasswordError):
    pass


class LetterError(PasswordError):
    pass


class DigitError(PasswordError):
    pass


def is_good_password(_string):
    if len(_string) < 9:
        raise LengthError
    elif (_string.lower() == _string) or (_string == _string.upper()):
        raise LetterError
    elif _string.isalpha():
        raise DigitError

    return True


for line in sys.stdin:
    try:
        is_good_password(line.strip())
    except LengthError:
        print('LengthError')
    except LetterError:
        print('LetterError')
    except DigitError:
        print('DigitError')
    else:
        print('Success!')
        break
