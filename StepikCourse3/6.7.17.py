from collections import Counter

words = input().split(',')
words_counter = Counter(words)

for word in sorted(words_counter):
    print(f'{word}: {words_counter[word]}')
