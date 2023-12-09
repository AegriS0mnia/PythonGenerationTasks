from typing import NoReturn

class TextHandler:
    def __init__(self):
        self.words: list[str] = []

    def add_words(self, line: str) -> NoReturn:
        self.words.extend(line.split())

    def get_shortest_words(self) -> list[str]:
        shortest_word_len = len(min(self.words, default='', key=len))
        return list(filter(lambda word: len(word) == shortest_word_len, self.words))

    def get_longest_words(self) -> list[str]:
        longest_word_len = len(max(self.words, default='', key=len))
        return list(filter(lambda word: len(word) == longest_word_len, self.words))
