import re

word = input()
text = input()

pattern = fr'\b{word[:-2]}(se|ze)\b'

answer = len(re.findall(pattern, text, flags=re.IGNORECASE | re.MULTILINE))

print(answer)
