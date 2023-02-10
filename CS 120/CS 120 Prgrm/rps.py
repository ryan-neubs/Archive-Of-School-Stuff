# rockpaperscissors
# Ryan Neubauer

from random import random, randrange

def opposing():
    randnum = randrange(0,2)
    if randnum == 0:
        return "Rock"
    elif randnum == 1:
        return "Paper"
    elif randnum == 2:
        return "Scissors"
def result(move, opponent):
    if move == opponent:
        return "It's a tie!"
    elif move == "Rock" and opponent == "Scissors":
        return "You win!"
    elif move == "Scissors" and opponent == "Paper":
        return "You win!"
    elif move == "Paper" and opponent == "Rock":
        return "You win!"
    elif move == "Rock" and opponent == "Paper":
        return "You lose!"
    elif move == "Paper" and opponent == "Scissors":
        return "You lose!"
    elif move == "Scissors" and opponent == "Rock":
        return "You lose!"

def main():
    print("This is a program to play rock paper scissors against a computer.")
    print("")
    move = str(input("Enter your move <Enter> to quit: "))
    while move != "":
        opponent = opposing()
        print("")
        print("You chose: ", move)
        print("")
        print("The computer chose: ", opponent)
        print("")
        print(result(move, opponent))
        print("")
        move = str(input("Enter your move <Enter> to quit: "))

main()
        
