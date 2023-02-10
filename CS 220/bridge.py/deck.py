# deck.py
# by Ryan Neubauer with help from Sam Schmitz

from random import randrange
from card import Card


class Deck:

    def __init__(self, fname=None):
        """post: Creates a 52 card deck in standard order or
                'stacked' from a file.
        """
        cards = []
        if fname is None:
            for suit in Card.SUITS:
                for rank in Card.RANKS:
                    cards.append(Card(rank, suit))
        else:
            cards = []
            inFile = open(fname, 'r')
            for line in inFile:
                line = line.split()
                cards.append(Card(int(line[0]), line[1]))
        self.cards = cards

    def size(self):
        """Cards left
        post: Returns the number of cards in self"""

        return len(self.cards)

    def deal(self):

        """Deal a single card
        pre:  self.size() > 0
        post: Returns the next card in self, and removes it from self."""

        return self.cards.pop()

    def shuffle(self):
        """Shuffles the deck
        post: randomizes the order of cards in self"""

        n = self.size()
        cards = self.cards
        for i, card in enumerate(cards):
            pos = randrange(i, n)
            cards[i] = cards[pos]
            cards[pos] = card
