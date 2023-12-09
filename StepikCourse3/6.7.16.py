from collections import Counter


def count_occurences(word, words):
    words_counter = Counter(words.lower().split())
    return words_counter[word.lower()]
