from collections import Counter

words = input().split(',')
words_counter = Counter(words)
longest_word = len(max(words_counter, key=len))

for word in sorted(words_counter):
    price = sum(ord(i) for i in word if not (i).isspace())
    print(f'{word.ljust(longest_word)}: {price} UC x {words_counter[word]} = {price * words_counter[word]} UC')
