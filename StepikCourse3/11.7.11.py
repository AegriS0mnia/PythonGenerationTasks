import re

text = input()
word = input()
pattern = fr'\B{word}\B'

answer = len(re.findall(pattern, text))

print(answer)
