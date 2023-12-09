from functools import total_ordering


@total_ordering
class Word:
    def __init__(self, word):
        self.word = word

    def __repr__(self):
        return f"Word('{self.word}')"

    def __str__(self):
        return f'{self.word.capitalize()}'

    def __eq__(self, other):
        if isinstance(other, Word):
            return len(self.word.__str__()) == len(other.__str__())
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Word):
            return len(self.word.__str__()) > len(other.__str__())
        return NotImplemented
