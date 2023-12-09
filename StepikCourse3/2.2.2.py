letters = [input() for i in range(3)]
russian = "АаВСсЕеНКМОоРрТХху"
english = "AaBCcEeHKMOoPpTXxy"

is_all_russian = all(map(lambda let: let in russian, letters))
is_all_english = all(map(lambda let: let in english, letters))

if is_all_russian:
    print('ru')
elif is_all_english:
    print('en')
else:
    print('mix')
