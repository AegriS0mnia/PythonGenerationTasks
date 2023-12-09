def get_vowels(word):
    vowels = 'ауоыиэяюёе'
    vowels_counter = 0
    vowels_indexes = []

    for i in range(len(word)):
        if word[i] in vowels:
            vowels_counter += 1
            vowels_indexes.append(i)

    return vowels_counter, vowels_indexes


word = input()
pattern = get_vowels(word)

words_quantity = int(input())
words = [input() for i in range(words_quantity)]

for w in words:
    word_check = get_vowels(w)
    if word_check == pattern:
        print(w)
