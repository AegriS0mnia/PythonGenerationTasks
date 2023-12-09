def likes(names):
    if len(names) == 0:
        answer = 'Никто не оценил данную запись'
    elif len(names) == 1:
        answer = f'{names[0]} оценил(а) данную запись'
    elif len(names) == 2:
        answer = f'{names[0]} и {names[1]} оценили данную запись'
    elif len(names) == 3:
        answer = f'{names[0]}, {names[1]} и {names[2]} оценили данную запись'
    else:
        answer = f'{", ".join(names[:2])} и {len(names) - 2} других оценили данную запись'

    return answer
