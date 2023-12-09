class Alphabet:
    def __init__(self, language):
        self.language = language
        self.letters = {'ru': ('абвгдежзийклмнопрстуфхцчшщъыьэюя', 32),  'en': ('abcdefghijklmnopqrstuvwxyz', 26)}
        self.counter = -1
    def __iter__(self):
        return self

    def __next__(self):
        self.counter += 1
        return self.letters[self.language][0][self.counter % self.letters[self.language][1]]
