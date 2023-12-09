from typing import Generator


def filter_names(names: list[str], ignore_char: str, max_names: int) -> Generator:
    removed_banned_char: Generator = (i for i in names if not(i.lower().startswith(ignore_char.lower())))
    removed_digits: Generator = (i for i in removed_banned_char if i.isalpha())
    counter: int = 0
    for i in removed_digits:
        if counter == max_names:
            break
        if not removed_digits:
            break
        yield i
        counter += 1
