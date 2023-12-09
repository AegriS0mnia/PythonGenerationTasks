import json

try:
    file_name = input()
    with open(file_name, encoding='utf-8') as json_file:
        json_data = json.load(json_file)
        print(json_data)
except FileNotFoundError:
    print('Файл не найден')
except json.decoder.JSONDecodeError:
    print('Ошибка при десериализации')
