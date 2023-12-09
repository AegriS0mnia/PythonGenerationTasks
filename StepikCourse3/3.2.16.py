from datetime import date


counter = 0

while True:
    _date = input()
    if _date == 'end':
        break
    try:
        _date = list(map(int, _date.split('.')))
        date(_date[2], _date[1], _date[0])
        print('Корректная')

        counter += 1
    except ValueError:
        print('Некорректная')


print(counter)
