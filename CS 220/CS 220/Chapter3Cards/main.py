# This program deals out hands for a game of bridge
# bridge.py
# by Ryan Neubauer with help from Sam Schmitz

from card import *
from deck import *
from hand import *

def rand_deal():
    deck = Deck()
    deck.shuffle()
    
    north = Hand('North')
    east = Hand('East')
    south = Hand('South')
    west = Hand('West')

    while deck.size() != 0:
        north.add(deck.deal())
        east.add(deck.deal())
        south.add(deck.deal())
        west.add(deck.deal())
        
    return north, east, south, west

def select_deal():
    fname = str(input("Enter file name for the deck: "))
    deck = Deck(fname)
    deck.shuffle()
    
    north = Hand('North')
    east = Hand('East')
    south = Hand('South')
    west = Hand('West')

    while deck.size() != 0:
        north.add(deck.deal())
        east.add(deck.deal())
        south.add(deck.deal())
        west.add(deck.deal())
    
    return north, east, south, west

def hand_info(north, east, south, west):
    north.dump()
    print("\nPoints: ", north.totalPoints(), "\nCan Open: ", north.canOpen(), "\n")
    input("Press <Enter> to continue\n")

    east.dump()
    print("\nPoints: ", east.totalPoints(), "\nCan Open: ", east.canOpen(), "\n")
    input("Press <Enter> to continue\n")

    south.dump()
    print("\nPoints: ", south.totalPoints(), "\nCan Open: ", south.canOpen(), "\n")
    input("Press <Enter> to continue\n")

    west.dump()
    print("\nPoints: ", west.totalPoints(), "\nCan Open: ", west.canOpen(), "\n")
    input("Press <Enter> to continue\n")
        
def main():
    print("This program simulates dealing bridge hands.")
    while 0 == 0:
        print("Please choose an option", "\n\n\t'r' for random deal",
          "\n\t'f' to deal from a file", "\n\t'q' to quit the program", "\n")

        choice = str(input("Your choice? "))
        print("")
    
        if choice == 'f':
            north, east, south, west = select_deal()
        elif choice == 'r':
            north, east, south, west = rand_deal()
        elif choice == 'q':
            break

        hand_info(north, east, south, west)

if  __name__ == "__main__":
    main()

        
