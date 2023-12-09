def choose_plural(amount, declesions):
    if 11 <= amount % 100 <= 19:
        return (f'{amount} {declesions[2]}')
    elif amount % 10 == 1:
        return (f'{amount} {declesions[0]}')
    elif 1 < amount % 10 < 5:
        return (f'{amount} {declesions[1]}')
    else:
        return (f'{amount} {declesions[2]}')

# TEST_9:
print(choose_plural(240, ('курица', 'курицы', 'куриц')))