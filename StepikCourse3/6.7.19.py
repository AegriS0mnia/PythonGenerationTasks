from collections import Counter

with open('pythonzen.txt', encoding='utf-8') as text_file:
    letters_counter = Counter([c for c in text_file.read().lower() if c.isalpha()])

    for c in sorted(letters_counter):
        print(f'{c}: {letters_counter[c]}')