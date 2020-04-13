class Card:
    allowed_card_values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    allowed_card_suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

    def __init__(self, value, suit):
        if value not in Card.allowed_card_values or suit not in Card.allowed_card_suits:
            raise ValueError(f'a { value } of { suit } is not a valid card')
        self.value = value
        self.suit = suit

    def __repr__(self):
        return f'{ self.value } of { self.suit }'

    @classmethod
    def get_cards(cls):
        return [Card(value, suit) for value in Card.allowed_card_values for suit in Card.allowed_card_suits]