# card.py
class Card:
    '''A simple playing card. A Card is characterized by two 
    components:
        rank: an integer value in the range 2-14, inclusive (Two-Ace)
    suit: a character in 'cdhs' for clubs, diamonds, hearts, and
    spades.'''

    SUITS = 'cdhs'
    SUIT_NAMES = ['Clubs', 'Diamonds', 'Hearts', 'Spades']

    RANKS = list(range(2,15))
    RANK_NAMES = ['Two', 'Three', 'Four', 'Five', 'Six',
                  'Seven', 'Eight', 'Nine', 'Ten',
                  'Jack', 'Queen', 'King', 'Ace']

    def __init__(self, rank, suit):
        '''Constructor
        pre: rank in range(1,14) and suit in 'cdhs'
        post: self has the given rank and suit'''

        self.rank_num = rank
        self.suit_char = suit

    def suit(self):
        '''Card suit
        post: Returns the suit of self as a single character'''

        return self.suit_char

    def rank(self):
        '''Card rank
        post: Returns the rank of self as an int'''

        return self.rank_num

    def suitName(self):
        '''Card suit name
        post: Returns one of ('clubs', 'diamonds', 'hearts',
              'spades') corrresponding to self's suit.'''

        index = self.SUITS.index(self.suit_char)
        return self.SUIT_NAMES[index]

    def rankName(self):
        '''Card rank name
        post: Returns one of ('ace', 'two', 'three', ..., 'king')
              corresponding to self's rank.'''

        index = self.RANKS.index(self.rank_num)
        return self.RANK_NAMES[index]

    def __str__(self):
        '''String representation
        post: Returns string representing self, e.g. 'Ace of Spades' '''

        return self.rankName() + ' of ' + self.suitName()

    def __eq__(self, other):
        '''post returns True if two cards are equal, False otherwise'''

        return (self.suit_char == other.suit_char
                and self.rank_num == other.rank_num)

    def __lt__(self, other):
        '''post: returns True if self < other, False otherwise'''

        if self.suit_char == other.suit_char:
            return self.rank_num < other.rank_num
        return self.suit_char < other.suit_char

    def __ne__(self, other):
        '''post: returns True if two cards are not equal, False otherwise'''

        return not self == other

    def __le__(self, other):
        '''post: returns True if self <= other, False otherwise'''

        return self < other or self == other
