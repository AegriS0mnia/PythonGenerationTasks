def card_deck(suit):
    card_names = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз')
    card_suits = ['пик', 'треф', 'бубен', 'червей']
    card_counter = 0
    del card_suits[card_suits.index(suit)]
    while True:
        yield f'{card_names[(card_counter % 13)]} {card_suits[card_counter // 13 % 3]}'
        card_counter += 1
