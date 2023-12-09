import csv

with open('titanic.csv', 'r', encoding='utf-8') as csv_file:
    lines = list(csv.reader(csv_file, delimiter=';'))

    del lines[0]

    lines = list(filter(lambda x: x[0] == '1' and float(x[3]) < 18, lines))

    male_list = list(filter(lambda x: x[2] == 'male', lines))
    female_list = list(filter(lambda x: x[2] == 'female', lines))

    male_female_list = male_list + female_list

    for i in male_female_list:
        if i != male_female_list[-1]:
            print(i[1])
        else:
            print(i[1], end='')
