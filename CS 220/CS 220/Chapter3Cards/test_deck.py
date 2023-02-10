# test_deck.py

import unittest

from deck import Deck


class TestStackedDeck(unittest.TestCase):

    def setUp(self):
        self.deck = Deck("deck1.txt")

    def test_deck_from_file(self):
        deck = Deck("deck1.txt")
        self.assertEqual(deck.size(), 52)
        c = deck.deal()
        self.assertEqual(c.suit(), 'h')
        self.assertEqual(c.rank(), 4)
        for _ in range(51):
            c = deck.deal()
        self.assertEqual(c.suit(), 'd')
        self.assertEqual(c.rank(), 8)


if __name__ == '__main__':
    unittest.main()
