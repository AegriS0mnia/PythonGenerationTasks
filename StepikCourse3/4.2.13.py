import csv

with open('salary_data.csv', 'r', encoding='utf=8') as csv_file:
    salaries_data = list(csv.reader(csv_file, delimiter=';'))
    del salaries_data[0]
    keys = set()

    for key in salaries_data:
        keys.add(key[0])

    keys = sorted(keys)

    average_salaries = []

    for company in keys:
        _sum = 0
        number_of_employers = 0
        for data in salaries_data:
            if company in data:
                _sum += int(data[1])
                number_of_employers += 1

        average_salary = _sum / number_of_employers
        average_salaries.append((company, average_salary))

    average_salaries = sorted(average_salaries, key=lambda company: (company[1], company))

    for company in average_salaries:
        print(company[0])
