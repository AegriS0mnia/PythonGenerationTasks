import re

text = input()

pattern = rf'\b{input()}(-[a-zA-Z]+)*\b'

answer = len(re.findall(pattern, text))

print(answer)

