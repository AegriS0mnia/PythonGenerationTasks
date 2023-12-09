class StrExtension:
    def __init__(self):
        ...

    @staticmethod
    def remove_vowels(line: str):
        return ''.join(i for i in line if i not in 'aeiouyAEIOUY')

    @staticmethod
    def leave_alpha(line: str):
        return ''.join(i for i in line if i.isalpha())

    @staticmethod
    def replace_all(line: str, chars: str, char: str):
        for c in chars:
            line = line.replace(c, char)

        return line
