# Craps.py
# by Ryan Neubauer
# This program simulates a user selected amount of games of craps.

from random import randrange


""""
The rules of craps:

If first roll is 2, 3, or 12, the player loses.

If first roll is 7 or 11, the player wins.

Otherwise the value of the first roll is the "point" value and the player continues rolling until:
    a)  a 7 is rolled and player loses
    b)  the point value is rolled, player win
"""

#-------------------------------------------------------------------------------
#   This function returns a random value to simulate dice rolls

def roll_dice():
    die1 = randrange(1, 7)
    die2 = randrange(1, 7)
    return die1 + die2

#-------------------------------------------------------------------------------
#    Function that returns Boolean that indicates whether the
#    point value was made.

def point_made(point_value):
    while True:
        roll = roll_dice()
        if roll == 7:
            return False
        if roll == point_value:
            return True

#-------------------------------------------------------------------------------
#   Simulates playing one game of craps and returns a Boolean
#   value indicating whether the player "won" the game.

def craps_win():
    init_roll = roll_dice()
    if init_roll in [2, 3, 12]:
        return False
    if init_roll in [7, 11]:
        return True
    return point_made(init_roll)

#-------------------------------------------------------------------------------
#    This function simulates the playing of n games 
#    of craps and returns the number of games won.

def simulate_games(n):
    wins = 0
    for i in range(n):
        if craps_win():
            wins += 1
    return wins

#-------------------------------------------------------------------------------
#   This function collects the number of games from the user to simulate
#   "n" games of craps and prints the result of how many games were won

def main():
    print("This program will simullate a user-chosen number of craps games")
    print("The number of games won will be shown")
    print()
    print()
    n = int(input("Please enter the number of games to simulate ==>"))
    print()
    print("Please wait...")
    print()

    print("The number of wins in", n, "games is", simulate_games(n))
    print()
    input("Press [Enter} to quit.")


main()

