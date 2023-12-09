import re

word = input()
text = input()

pattern = fr"\b(({word})|({(word.replace('our', 'or'))}))\b"

answer = len(re.findall(pattern, text, flags=re.IGNORECASE | re.MULTILINE))

print(answer)
