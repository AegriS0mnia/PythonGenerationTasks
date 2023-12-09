class CardDeck:
    def __init__(self):
        self.card_names = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз')
        self.card_suits = ('пик', 'треф', 'бубен', 'червей')
        self.card_counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.card_counter += 1
        try:
            return f'{self.card_names[(self.card_counter % 13 ) - 1]} {self.card_suits[(self.card_counter - 1) // 13]}'
        except IndexError:
            raise StopIteration
