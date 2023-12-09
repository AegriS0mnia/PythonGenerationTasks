def hide_card(card_number):
    return '*' * 12 + card_number.replace(' ', '')[-4:]


card = '905 678123 45612 56'

print(hide_card(card))
