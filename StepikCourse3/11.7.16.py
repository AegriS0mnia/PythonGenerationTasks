import sys
import re

pattern = fr'href=(?P<url_header>.*)</a>'

for line in sys.stdin:
    try:
        ans = re.search(pattern, line, flags=re.IGNORECASE | re.MULTILINE).group('url_header')
        url = ans.split('\">')[0][1:]
        header = ans.split('\">')[1]

        print(f'{url}, {header}')
    except AttributeError:
        continue
