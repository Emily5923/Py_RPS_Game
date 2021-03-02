import random, sys

def getInput():
    print("Enter your move: (R)ock, (P)aper, (S)cissors or (Q)uit")
    return input()

def findWinner(playerMove, comMove):
    if playerMove == "R":
        if comMove == 0:
            return "Tie"
        if comMove == 1:
            return "Loss"
        if comMove == 2:
            return "Win"
    if playerMove == "P":
        if comMove == 0:
            return "Win"
        if comMove == 1:
            return "Tie"
        if comMove == 2:
            return "Loss"
    if playerMove == "S":
        if comMove == 0:
            return "Loss"
        if comMove == 1:
            return "Win"
        if comMove == 2:
            return "Tie"

def main(wins, losses, ties):

    print("ROCK, PAPER, SCISSORS")
    print("%d Wins, %d Losses, %d Ties" % (wins, losses, ties))

    move = getInput() 

    if(move == "Q"):
        sys.exit()

    if(move != "Q" and move != "S" and move != "P" and move != "R"):
        print("Invalid move")
        main(wins, losses, ties)
    else:
        pcMove = random.randint(0,2)
    
    if(move == "R"):
        print("ROCK vs...")
    elif(move == "P"):
        print("PAPER vs...")
    elif(move == "S"):
        print("SCiSSOR vs...")

    if(pcMove == 0):
        print("ROCK")
    elif(pcMove == 1):
        print("PAPER")
    elif(pcMove == 2):
        print("SCISSOR")

    winState = findWinner(move, pcMove)
    print (winState)
    print("\n\n")

    if winState == "Tie":
        ties += 1
    if winState == "Win":
        wins += 1
    elif winState == "Loss":
        losses += 1
        
    main(wins, losses, ties)
    
if __name__ == "__main__":
    wins = 0
    losses = 0
    ties = 0
    main(wins, losses, ties)