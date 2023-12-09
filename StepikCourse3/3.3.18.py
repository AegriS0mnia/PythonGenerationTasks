from datetime import datetime

# Считываем содержимое файла в список строк
with open("diary.txt") as file:
    lines = file.read().split('\n\n')
    lines_lists = []
    for line in lines:
        lines_lists.append(line.split('\n'))
    pattern = '%d.%m%.%Y; %H:%M'

    report_tuples = []

    for report in lines_lists:
        date_str, time_str = report[0].strip().split("; ")
        date_time = datetime.strptime(date_str + " " + time_str, "%d.%m.%Y %H:%M")
        report_tuples.append((date_time, report))

    # Сортируем список кортежей по дате и времени
    sorted_reports = sorted(report_tuples, key=lambda date: date[0])

    # Выводим отсортированные отчёты
    for report in sorted_reports:
        print(*report[1], sep='\n')
        print()

