# tt.py
# by Ryan Neubauer
# This program simulates a game of table tennis

from random import random

def service_change(scoreA, scoreB):
    total = scoreA + scoreB
    return total >= 20 or total % 2 == 0

def gameOver(scoreA, scoreB):
    return ((scoreA >= 11 or scoreB >= 11)
            and abs(scoreA - scoreB) >= 2)
        
def simOneGame(probA, probB):
    scoreA = 0
    scoreB = 0
    serving = "A"
    while not gameOver(scoreA, scoreB):
        if serving == "A":
            # simulate A serve
            if random() < probA:
                scoreA = scoreA + 1
                
            else:
                scoreB = scoreB + 1
                
            if service_change(scoreA, scoreB):
                serving = "B"
        else:
            # sim B serve
            if random() < probB:
                scoreB = scoreB + 1
                
            else:
                scoreA = scoreA + 1
                
            if service_change(scoreA, scoreB):
                serving = "A"

    return scoreA, scoreB

def simOneMatch(probA, probB, gpm):
    gamesA = 0
    gamesB = 0
    if gpm == 5:
        while not ((gamesA == 3 and gamesB == 0) or (gamesB == 3 and gamesA == 0)
        or (gamesA or gamesB == 5)):
            scoreA, scoreB = simOneGame(probA, probB)
            if scoreA > scoreB:
                gamesA = gamesA + 1
            else:
                gamesB = gamesB + 1
            
            

    elif gpm == 7:
        while not ((gamesA == 5 and gamesB == 0) or (gamesB == 5 and gamesA == 0)
        or (gamesA or gamesB == 7)):
            scoreA, scoreB = simOneGame(probA, probB)
            if scoreA > scoreB:
                gamesA = gamesA + 1
            else:
                gamesB = gamesB + 1
                
    elif gpm == 9:
        while not ((gamesA == 7 and gamesB == 0) or (gamesB == 7 and gamesA == 0)
        or (gamesA or gamesB == 9)):
            scoreA, scoreB = simOneGame(probA, probB)
            if scoreA > scoreB:
                gamesA = gamesA + 1
            else:
                gamesB = gamesB + 1
                
    return gamesA, gamesB
    

def simNmatches(n, probA, probB, gpm):
    winsA = 0
    winsB = 0
    for i in range(n):
        gamesA, gamesB = simOneMatch(probA, probB, gpm)
        if gamesA > gamesB:
            winsA = winsA + 1
        else:
            winsB = winsB + 1
    return winsA, winsB
    
    
    
def getInputs():
    
    probA = float(input("Enter the win probability for player A: "))
    probB = float(input("Enter the win probability for player B: "))
    n = int(input("Enter the number of matches to simulate: "))
    gpm = int(input("Enter the number of games per match: "))
    return probA, probB, n, gpm

def printIntro():
    print("This program simulates a match of table tennis based of player win percentages.")
    
def printReport(winsA, winsB):
    print("")
    print("Player A has won", winsA, "matches.")
    print("Player B has won", winsB, "matches.")
    
def main():
    printIntro()
    probA, probB, n, gpm = getInputs()
    winsA, winsB = simNmatches(n, probA, probB, gpm)
    printReport(winsA, winsB)
    print("")
    input("Press <Enter> to quit.")

if __name__ == "__main__":
    main()

