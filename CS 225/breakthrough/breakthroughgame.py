# breakthroughgame.py
# By Ryan Neubauer and Andrew Poock
""" Implementation of Breakthrough game rules

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

from pprint import pprint

# Constants to identify pieces and players
BLACK = "BLACK"
WHITE = "WHITE"

class BreakthroughGame:    
    """Implementation of the rules of breakthrough.  Assumes an 8x8 board
    with rows and columns numbered 0--7. A location on the board is
    given as a pair: (row, column). Black pawns start on rows 0 and 1 while
    white pawns start on rows 6 and 7.
    """

    def __init__(self):
      self.board = [[None for _ in range(8)] for x in range(8)]
      for i in range(8):
        self.board[0][i] = BLACK
        self.board[1][i] = BLACK
        self.board[6][i] = WHITE
        self.board[7][i] = WHITE
      self.turn = WHITE

    def get_piece_at(self, loc):
        """return owner of piece at loc (row, column)
        pre: loc is a valid (row,col) board location
        post: result in [BLACK, WHITE, None]
        """
        return self.board[loc[0]][loc[1]]

    def get_player_in_turn(self):
        """ return the player that is in turn, i.e. allowed to move.
        post: result in [BLACK, WHITE]
        """
        return self.turn

    def get_winner(self):
        """return the winner of the game or None, if game is still in progress
        post: result in [BLACK, WHITE, None]
        """
        if WHITE in self.board[0]:
          return WHITE
        if BLACK in self.board[7]:
          return BLACK
        return None

    def is_valid_move(self, fromloc, toloc):
        """validate a move from fromLoc to toLoc
        pre: fromloc and toloc are valid (row, column) board locations
        post: returns True if move is valid, False otherwise
        """

        frow, fcol = fromloc
        trow, tcol = toloc

        for num in fromloc: 
          if num > 7 or num < 0:
            return False
        for num in toloc:
          if num > 7 or num < 0:
            return False

        if (self.turn == WHITE and (trow-frow) == -1 and (self.get_piece_at(toloc) == None or self.get_piece_at(toloc) == BLACK) and (tcol-fcol in range(-1,2))):
          return True
        
        if (self.turn == BLACK and (trow-frow) == 1 and (self.get_piece_at(toloc) == None or self.get_piece_at(toloc) == WHITE) and (tcol-fcol in range(-1,2))):
          return True

        return False


    def move(self, fromloc, toloc):
        """ move piece from fromloc to toloc
        pre: fromloc and toloc are valid (row, column) board locations
             and there is a piece at fromloc
        post: the move is performed
        note: move does not have to be valid
        """
        fc, fr = fromloc
        tc, tr = toloc
        piece = self.get_piece_at(fromloc)
        self.board[fc][fr] = None
        self.board[tc][tr] = piece

        if self.turn == WHITE:
          self.turn = BLACK
        else:
          self.turn = WHITE

    def pretty_print(self):
      """ prints the board out in an orientation that's more readable
          using the pretty print library. 
          note: only used for debugging/testing and making sure pieces were in the correct spots
      """
      pprint(self.board)
