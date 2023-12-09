import csv
from datetime import datetime

with open('name_log.csv', 'r', encoding='utf-8') as csv_file:

    lines = list(csv.reader(csv_file))
    columns = lines.pop(0)
    emails = set()
    users = []
    for i in lines:
        emails.add(i[1])

    for email in emails:
        user = []

        for line in lines:
            if email in line:
                user.append(line)
                last_change = max(user, key=lambda x: datetime.strptime(x[2], '%d/%m/%Y %H:%M'))

        users.append(last_change)
    users.sort(key=lambda x: x[1])

with open('new_name_log.csv', 'w', encoding='utf-8', newline='') as output:
    writer = csv.writer(output)
    writer.writerow(columns)

    for row in users:
        writer.writerow(row)


