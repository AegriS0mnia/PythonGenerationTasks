class CaseHelper:

    @staticmethod
    def is_snake(line: str):
        is_snake = line == line.lower() and not(line.startswith('_'))
        return is_snake

    @staticmethod
    def is_upper_camel(line: str):
        is_camel = line[0] == line[0].upper()  and '_' not in line
        return is_camel

    @staticmethod
    def to_snake(line: str):
        _line = list(line)
        counter = 0
        for index, c in enumerate(line):
            if c.isupper() and c.isalpha() and index != 0:
                _line.insert(index + counter, '_')
                counter += 1
        return ''.join(_line).lower()

    @staticmethod
    def to_upper_camel(line: str):
        _line = list(line)
        counter = 0
        for index, c in enumerate(line):
            if c == '_' and index != 0:
                _line[index + 1 - counter] = _line[index + 1 - counter].upper()
                _line.pop(index - counter)
                counter += 1
        _line[0] = _line[0].capitalize()

        return ''.join(_line)
