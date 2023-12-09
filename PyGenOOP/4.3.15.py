import copy


class Wordplay:
    def __init__(self, words=None):
        if words is None:
            self.words = []
        else:
            self.words = copy.deepcopy(words)

    def add_word(self, word):
        if word not in self.words:
            self.words.append(word)
        else:
            pass

    def words_with_length(self, length):
        if self.words:
            return [word for word in self.words if len(word) == length]
        return []

    def only(self, *args):
        if self.words:
            return [word for word in self.words if set(word).issubset(set(args))]
        return []

    def avoid(self, *args):
        if self.words:
            return [word for word in self.words if set(word).isdisjoint(set(args))]
        return []

