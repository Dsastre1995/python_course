from card import Card
from random import shuffle

class Deck:
    deck_size = 52

    def __init__(self):
        self.cards = Card.get_cards()

    def __repr__(self):
        return f'Deck of { len(self.cards) } cards'

    def __iter__(self):
        return iter(self.cards)

    def _deal(self, cards_to_deal):
        removed_cards = []
        if len(self.cards) < cards_to_deal:
            removed_cards = self.cards
            self.cards = []
            raise ValueError('All cards have been dealt')

        for x in range(cards_to_deal):
            removed_cards.append(self.cards.pop())

        return removed_cards    

    def count(self):
        return len(self.cards)

    def shuffle(self):
        if (len(self.cards) < Deck.deck_size):
            raise ValueError('Only full decks can be shuffled')

        return shuffle(self.cards)

    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self, number_of_cards):
        return self._deal(number_of_cards)


# deck = Deck()
# print(deck)
# deck.shuffle()
# card = deck.deal_card()
# print(card)
# hand = deck.deal_hand(5)
# print(hand)
# print(deck)

# for card in deck:
#     print(card)


    
