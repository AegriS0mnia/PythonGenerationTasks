number: int = int(input())
langs: set[str] = {lang for lang in input().split(', ')}
for i in range(number - 1):
    langs &= {lang for lang in input().split(', ')}
langs: str = ', '.join(sorted(langs))

if langs:
    print(langs)
else:
    print('Сериал снять не удастся')
