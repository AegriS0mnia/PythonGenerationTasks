file_name = input()

try:
    with open(file_name, encoding='utf-8') as file:
        lines = file.read()
        print(lines)
except FileNotFoundError:
    print('Файл не найден')
