import sys

news = []

for line in sys.stdin:
    news.append(line.split(' /'))

category = news.pop(-1)[0]


news = filter(lambda x: category in x[1], news)
news = sorted(news, key=lambda x: (float(x[2]), ''.join(x)))

for line in news:
    print(line[0])
