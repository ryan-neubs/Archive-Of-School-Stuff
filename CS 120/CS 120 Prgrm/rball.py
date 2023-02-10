# rball.py

from random import random

def printIntro():
    print("This program simulates a game of racquetball based on player win percentages.")

def getInputs():
    # get value for probA
    # get value of probB
    # get value for n
    # return the values
    probA = float(input("Enter the win probability for player A: "))
    probB = float(input("Enter the win probability for player B: "))
    n = int(input("Enter the number of games to simulate: "))
    return probA, probB, n
    

def simNGames(n, probA, probB):
    winsA = 0
    winsB = 0
    for i in range(n):
        scoreA, scoreB = simOneGame(probA, probB)
        if scoreA > scoreB:
            winsA = winsA + 1
        else:
            winsB = winsB + 1
    return winsA, winsB

def simOneGame(probA, probB):
    scoreA = 0
    scoreB = 0
    serving = "A"
    while not gameOver(scoreA, scoreB):
        if serving == "A":
            if random() < probA:
                scoreA = scoreA + 1
            else:
                serving = "B"
        else:
            if random() < probB:
                scoreB = scoreB + 1
            else:
                serving = "A"
    return scoreA, scoreB

def gameOver(scoreA, scoreB):
    if scoreA == 15 or scoreB == 15:
        return True
    else:
        return False

def printReport(winsA, winsB):
    print(winsA, winsB)



def main():
    printIntro()
    probA, probB, n = getInputs()
    winsA, winsB = simNGames(n, probA, probB)
    printReport(winsA, winsB)




if __name__ == "__main__":
    main()
