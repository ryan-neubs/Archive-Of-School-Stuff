# hand.py
# By Ryan Neubauer with help from Sam Schmitz

from card import *

class Hand:
    """A labeled collection of cards that can be sorted"""

    def __init__(self, label=""):
        """Create an empty collection with the given label."""

        self.label = label
        self.cards = []

    def add(self, card):
        """ Add card to the hand """

        self.cards.append(card)

    def sort(self):
        """ Arrange the cards in descending bridge order."""

        self.cards.sort()
        self.cards.reverse()

    def dump(self):
        """ Print out contents of the Hand."""

        print(self.label + "'s Cards:")
        for c in self.cards:
            print("   ", c)

    #----------------------------------------------------------
    # These are just example methods of the sort you may want
    #    to use in order to complete the program
    
    def rankPoints(self):
        """ return number of points for high rank cards """
        points = 0
        for card in self.cards:
            if card.rank() == 10:
                points += 1
            elif card.rank() == 11:
                points += 2
            elif card.rank() == 12:
                points += 3
            elif card.rank() == 13:
                points += 4
        return points

    def suitCount(self, suit):
        """ return number of cards of the given suit """
        suitCount = 0
        for card in self.cards:
            if card.suit() == suit:
                suitCount += 1
        return suitCount 

    def suitPoints(self):
        """ return points for short suits """
        points = 0
        for suit in Card.SUITS.split():
            if self.suitCount(suit) == 0:
                points += 3
            elif self.suitCount(suit) == 1:
                points += 2
            elif self.suitCount(suit) == 2:
                points += 1
        return points
                

    def totalPoints(self):
        """ return total hand points (rankPoints + suitsPoints) """
        return (self.suitPoints() + self.rankPoints())

    def hasHonor(self, suit):
        """ return whether hand has a face card (including ace) in suit """
        suitCheck = suit
        for card in self.cards:
            if (card.suit() == suitCheck) and (card.rank() == 10 or 11 or 12 or 13): 
                return True
        return False

    def hasBiddibleSuit(self):
        """ return whether hand contains a biddable suit """
        return (self.suitCount('c') == 4 or self.suitCount('d') == 4 or
                self.suitCount('h') == 4 or self.suitCount('s') == 4)
                

    def canOpen(self):
        """return whether the hand can open"""
        return ((self.totalPoints() >= 13) and ((self.suitCount('c') >= 5 or self.suitCount('d') >= 5 or self.suitCount('h') >= 5 or self.suitCount('s') >= 5) or
                (self.hasBiddibleSuit() and self.hasHonor('c') or self.hasHonor('d') or self.hasHonor('h') or self.hasHonor('s'))))
