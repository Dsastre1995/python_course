import unittest
from card import Card
from deck import Deck

class DeckTestActivity(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()

    def test_init(self):
        self.assertTrue(self.deck.count() == Deck.deck_size)

    def test_repr(self):
        self.assertEqual(repr(self.deck), 'Deck of 52 cards')

    def test_count(self):
        self.assertTrue(self.deck.count() == 52)
        self.deck.cards.pop()
        self.assertTrue(self.deck.count() == 51)

    def test_deal(self):
        cards = self.deck._deal(8)
        self.assertTrue(any(card not in self.deck.cards for card in cards))
        with self.assertRaises(ValueError):
            self.deck._deal(53)

    def test_deck_shuffle(self):
        self.deck.shuffle()
        self.assertTrue(self.deck.count() == len(self.deck.cards))

    def test_desk_deal_card(self):
        card = self.deck.deal_card()
        self.assertTrue(card not in self.deck.cards)

    def test_deal_hand(self):
        hand = self.deck.deal_hand(5)
        self.assertTrue(any(card not in self.deck.cards for card in hand))

class CardTestActivity(unittest.TestCase):
    def setUp(self):
        self.card = Card('A', 'Hearts')

    def test_init(self):
        card = Card('A', 'Hearts')
        self.assertTrue(card.suit and card.value)

    def test_repr(self):
        self.assertEqual(repr(self.card), 'A of Hearts')    
        

if __name__ == '__main__':
    unittest.main()