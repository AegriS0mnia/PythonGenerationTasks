import sys
import re

tag_pattern = fr'(?P<tag><\w*>|<\w* )'
tags = []
unique = []
with open('htmlparse', encoding='utf-8') as text:
    lines = text.readlines()
    for l in lines:
        tags += re.findall(tag_pattern, l, flags=re.MULTILINE)

for tag in tags:

print(tags)