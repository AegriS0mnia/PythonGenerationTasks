import re

line = input()

match = bool(re.match(r'(здравствуйте)|(доброе утро)|(добрый день)|(добрый вечер)', line, flags=re.IGNORECASE))

print(match)
