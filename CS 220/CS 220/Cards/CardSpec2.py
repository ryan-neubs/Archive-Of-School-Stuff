class Card(object):
    '''A simple playing card. A Card is characterized by two components:
    rank: an integer value in the range 1-13, inclusive (Ace-King)
    suit: a character in 'cdhs' for clubs, diamonds, hearts, and
    spades.'''
    SUITS = 'cdhs'
    SUIT_NAMES = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    
    RANKS = list(range(1,14))
    RANK_NAMES = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six',
                  'Seven', 'Eight', 'Nine', 'Ten',
                  'Jack', 'Queen', 'King']

    def __init__(self, rank, suit):
        '''Constructor
        pre: rank in range(1,14) and suit in 'cdhs'
        post: self has the given rank and suit'''

        suiti = self.SUITS.index(suit)
        self.cardnum = suiti * 13 + rank - 1

    def suit(self):
        '''Card suit
        post: Returns the suit of self as a single character'''

        return self.SUITS[self.cardnum // 13]

    def rank(self):
        '''Card rank
        post: Returns the rank of self as an int'''

        return self.RANKS[self.cardnum % 13 + 1]
   
    def suitName(self):
        '''Card suit name
        post: Returns one of ('Clubs', 'Diamonds', 'Hearts',
              'Spades') corrresponding to self's suit.'''

        return self.SUIT_NAMES[self.cardnum // 13]

    def rankName(self):
        '''Card rank name
        post: Returns one of ('ace', 'two', 'three', ..., 'king')
              corresponding to self's rank.'''

        return self.RANK_NAMES[self.cardnum % 13]
        
    def __str__(self):
        '''String representation
        post: Returns string representing self, e.g. 'Ace of Spades' '''

        return self.rankName() + ' of ' + self.suitName()
