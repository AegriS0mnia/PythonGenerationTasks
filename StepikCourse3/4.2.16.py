import csv

with open('domains.csv', 'r', encoding='utf-8') as csv_file:
    data = list(csv.reader(csv_file))
    columns = data.pop(0)
    keys = set()
    domain_popularity = []

    for line in data:
         keys.add(line[2].split('@')[1])

    for key in keys:
        _sum = 0
        for line in data:
            if key in line[2]:
                _sum += 1
        domain_popularity.append((key, str(_sum)))

    domain_popularity = sorted(domain_popularity, key=lambda x: (int(x[1]), x[0]))

with open('domain_usage.csv', 'w', encoding='utf-8') as output:
    
    print('domain,count', file=output)
    for domain in domain_popularity:
        if domain != domain_popularity[-1]:
            print(','.join(domain), file=output)
        else:
            output.write(','.join(domain))
