import random

# Initial game config [stick,files,sticklose]]
STICK_NUM_INDEX = 0         #index of stick in configuration list
PILE_NUM_INDEX = 1          #index of pile in configuration list
STICKLOSE_NUM_INDEX = 2     #index of sticklose in configuration list

STICK_NUM_DEFAULT = 10      #defaul value of stick
PILE_NUM_DEFAULT = 5        #defaul value of pile
STICKLOSE_NUM_DEFAULT = 0   #defaul value of stick lose

STICK_NUM_MAX = 20
PILE_NUM_MAX = 20

# Default Game configuration
g_GameConfig = [STICK_NUM_DEFAULT,PILE_NUM_DEFAULT,STICKLOSE_NUM_DEFAULT]

# convert from string to integer
def convertStrToInt(in_str):
    if in_str.isdigit():
        resVal = int(in_str)
        if resVal >= 0:
            return resVal

    return -1

# Initialize general game configuration
def initializeGameConfig():
    # Initialize the piles with random number of sticks.
    initGameConfig = g_GameConfig
    retry_cnt = 0

    while True:
        # User input
        usrInput = input("Choose number of pile(2~%d): "%(PILE_NUM_MAX))
        numPile = convertStrToInt(usrInput)
    
        usrInput = input("Choose maximum number of stick(1~%d): "%(STICK_NUM_MAX))
        numStick = convertStrToInt(usrInput)

        #usrInput = input("Choose number of last sticks lose: ")
        numStickLose = 0  #convertStrToInt(usrInput)

        if numStick in range(1,STICK_NUM_MAX+1) and\
            numPile in range(2,PILE_NUM_MAX+1) and\
            numStickLose >= 0:

            initGameConfig[STICK_NUM_INDEX] = numStick
            initGameConfig[PILE_NUM_INDEX] = numPile
            initGameConfig[STICKLOSE_NUM_INDEX] = numStickLose
            break
        else:
            print("[ERR] Invalid input number!")
            retry_cnt += 1
            if retry_cnt == 3:
                print("[ERR] You entered wrong input over 3 times.")
                print("Let play with random initial configuration.")
                break;

    return initGameConfig

# Initialize piles
def initializePiles(gameConfig):
    # Initialize the piles with random number of stick. STICK_NUM_INDEX
    return [random.randint(1, gameConfig[STICK_NUM_INDEX]) for _ in range(gameConfig[PILE_NUM_INDEX])]

# Print the current state of the piles.
def printPiles(piles):
    print("Current piles:")
    for i, sticks in enumerate(piles):

        # print(f"Pile {i+1}: {sticks} stones")  # For debugging
        print(f"Pile {i+1}:",end="")
        for j in range(sticks):
            print("*",end="")

        # New line
        print()

# Allow the player to make a move.
def playerMove(piles):
    while True:
        printPiles(piles)
        pile = int(input("Select a pile (1, 2, 3, etc.Max=%d): "%(len(piles)))) - 1
        if 0 <= pile < len(piles):
            if piles[pile] == 0:
                print("[ERR] No stick in this pile. Please choose anothers!")
                continue

            sticks_to_remove = int(input("How many sticks do you want to remove(Max=%d)? "%(piles[pile])))
            if 1 <= sticks_to_remove <= piles[pile]:
                piles[pile] -= sticks_to_remove
                break
            else:
                print("[ERR] Invalid number of sticks!")
        else:
            print("[ERR] Invalid pile number!")

# computer's move
def computerMove(piles):

    pile = 0
    # if piles empty
    while piles[pile] == 0:
        pile = random.randint(0, len(piles) - 1)

    sticks_to_remove = random.randint(1, piles[pile])
    print(f"Computer removes {sticks_to_remove} sticks from pile {pile+1}")
    piles[pile] -= sticks_to_remove

# Check if the game is over.
def gameOver(piles):
    # if all of sticks in piles are removed, return true
    return all(sticks == 0 for sticks in piles)

# Main function
def main():
    print("Welcome to the game of Nim!")

    # Main loop
    while True:  
        # Initialize game configuration
        g_GameConfig = initializeGameConfig()

        # Initialize files
        piles = initializePiles(g_GameConfig)

        # Main processing
        while not gameOver(piles):
            playerMove(piles)
            if gameOver(piles):
                print("Congratulations! You win!")
                break
            computerMove(piles)
            if gameOver(piles):
                print("Sorry, the computer wins!")
                break
        
        usrInput = input("Do you want play more (Y/N):")
        usrInput = usrInput.lower()
        if usrInput == 'n':
            print("Thanks, see you again.")
            break

if __name__ == "__main__":
    main()