import re

pattern = r"(\b[a-z]*(\B|\b))|([A-Z][a-z]*)"

def abbreviate(phrase):
    substrings = list(filter(any, re.findall(pattern, phrase)))
    answer = ''
    for substr in substrings:
        for elem in substr:
            if elem:
                answer += elem[0].upper()
    return answer