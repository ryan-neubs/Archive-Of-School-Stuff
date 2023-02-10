# testbreakthroughgame.py
# By Ryan Neubauer and Andrew Poock
""" Tests for Implementation of Breakthrough game rules

Initial Board: White moves first.

    0   1   2   3   4   5   6   7
  +---+---+---+---+---+---+---+---+
0 | B | B | B | B | B | B | B | B |
  +---+---+---+---+---+---+---+---+
1 | B | B | B | B | B | B | B | B |
  +---+---+---+---+---+---+---+---+
2 |   |   |   |   |   |   |   |   |
  +---+---+---+---+---+---+---+---+
3 |   |   |   |   |   |   |   |   |
  +---+---+---+---+---+---+---+---+
4 |   |   |   |   |   |   |   |   |
  +---+---+---+---+---+---+---+---+
5 |   |   |   |   |   |   |   |   |
  +---+---+---+---+---+---+---+---+
6 | W | W | W | W | W | W | W | W |
  +---+---+---+---+---+---+---+---+
7 | W | W | W | W | W | W | W | W |
  +---+---+---+---+---+---+---+---+
"""

import unittest
from breakthroughgame import BreakthroughGame, BLACK, WHITE


class TestBreakthrough(unittest.TestCase):

    def setUp(self):
      self.btg = BreakthroughGame()

    # Board Setup Tests
    def test_index_8_is_out_of_range(self):
      with self.assertRaises(IndexError):
        self.btg.get_piece_at((8,0))
      with self.assertRaises(IndexError):
        self.btg.get_piece_at((8,8))
      with self.assertRaises(IndexError):
        self.btg.get_piece_at((0,8))

    def test_row_zero_and_one_are_black(self):
      for i in range(2):
        for piece in self.btg.board[i]:
          self.assertEqual(BLACK, piece)

    def test_row_six_and_seven_are_white(self):
      for i in range(6,7):
        for piece in self.btg.board[i]:
          self.assertEqual(WHITE, piece)

    # Test Turn Switching
    def test_white_moves_first(self):
      self.assertEqual(self.btg.get_player_in_turn(), WHITE)

    def test_black_moves_second(self):
      self.btg.move((6,0), (5,0))
      self.assertEqual(self.btg.get_player_in_turn(), BLACK)

    # Winner Tests
    def test_get_winner_works_for_white(self):
      for i in range(8):
        self.btg.move((7,i),(0,i))
        self.assertEqual(WHITE, self.btg.get_winner())
        self.btg = BreakthroughGame()

    def test_get_winner_works_for_black(self):
      for i in range(8):
        self.btg.move((0,i), (7,i))
        self.assertEqual(BLACK, self.btg.get_winner())
        self.btg = BreakthroughGame()

    def test_fresh_board_returns_none_for_winner(self):
      self.assertEqual(None, self.btg.get_winner())
    
    def test_winner_is_none_for_white_pieces_in_row_1_through_7(self):
      for row in range(8):
        if row == 0:
          continue
        for col in range(8):
          self.btg.board[row][col] = WHITE
      self.assertEqual(None, self.btg.get_winner())

    def test_winner_is_none_for_black_pieces_in_row_0_through_6(self):
      for row in range(8):
        if row == 7:
          continue
        for col in range(8):
          self.btg.board[row][col] = BLACK
      self.assertEqual(None, self.btg.get_winner())

    # Test valid move checker
    def test_cannot_move_into_same_color_piece(self):
      for i in range(8):
        if i != 7:
          self.assertEqual(False, self.btg.is_valid_move((7,i),(6,i)))
          self.assertEqual(False, self.btg.is_valid_move((7,i),(6,i+1)))

      self.btg.turn = BLACK
      for i in range(8):
        if i != 7:
          self.assertEqual(False, self.btg.is_valid_move((0,i),(1,i)))
          self.assertEqual(False, self.btg.is_valid_move((0,i),(1,i-1)))

    def test_cannot_move_more_than_1_space(self):
      for i in range(8):
        self.assertEqual(False, self.btg.is_valid_move((7,i),(5,i)))
        self.assertEqual(False, self.btg.is_valid_move((7,i),(6,i+2)))

      self.btg.turn == BLACK
      for i in range(8):
        self.assertEqual(False, self.btg.is_valid_move((0,i),(2,i)))
        self.assertEqual(False, self.btg.is_valid_move((0,i),(1,i-2)))

    # Test Move
    def test_move(self):
      self.btg.move((6,6), (5,5))
      self.assertEqual(WHITE, self.btg.get_piece_at((5,5)))
      self.assertEqual(None, self.btg.get_piece_at((6,6)))

    def test_cannot_move_backwards(self):
      for i in range(8):
        self.btg.move((1,i), (2,i))
        self.btg.turn = WHITE
        self.assertEqual(False, self.btg.is_valid_move((1,i), (2,i)))
      
      for i in range(8):
        self.btg.move((6,i), (5,i))
        self.btg.turn = BLACK
        self.assertEqual(False, self.btg.is_valid_move((6,i), (5,i)))

      
    





if __name__ == "__main__":
    unittest.main()
