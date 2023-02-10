import unittest
from CardSpec import Card

class TestCard(unittest.TestCase):

    def setUp(self):
        self.ace_of_clubs = Card(1, 'c')
        self.ten_of_diamonds = Card(10, 'd')
        self.king_of_hearts = Card(13, 'h')
        self.three_of_spades = Card(3, 's')

    def test_suit(self):
        self.assertEqual(self.ace_of_clubs.suit(), 'c')
        self.assertEqual(self.ten_of_diamonds.suit(), 'd')
        self.assertEqual(self.king_of_hearts.suit(), 'h')
        self.assertEqual(self.three_of_spades.suit(), 's')

    def test_rank(self):
        self.assertEqual(self.ten_of_diamonds.rank(), 10)

    def test_suitName(self):
        self.assertEqual(self.ace_of_clubs.suitName(), 'Clubs')
        self.assertEqual(self.king_of_hearts.suitName(), 'Hearts')

    def test_rankName(self):
        self.assertEqual(self.ace_of_clubs.rankName(), 'Clubs')
        self.assertEqual(self.king_of_hearts.rankName(), 'Hearts')

    def test_str(self):
        self.assertEqual(str(self.ace_of_clubs), 'Ace of Clubs')
        self.assertEqual(str(self.king_of_hearts), 'King of Hearts')

if __name__ == "__main__":
    unittest.main()
