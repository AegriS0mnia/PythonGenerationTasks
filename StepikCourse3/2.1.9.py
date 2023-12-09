def filter_anagrams(word, words):
    anagrams = list(filter(lambda _w: sorted(_w) == sorted(word), words))

    return anagrams
