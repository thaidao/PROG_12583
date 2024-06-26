# PROG12583_Assignment 3rd
# Author: Dao Nam Thai - StudentID: 991739094
# Brief: Implementation of "The game of Nim"

import random

# Initial game config [stick,files,sticklose]
STICK_NUM_INDEX         = 0     # index of stick in configuration list
PILE_NUM_INDEX          = 1     # index of pile in configuration list
STICKLOSE_NUM_INDEX     = 2     # index of sticklose in configuration list
GAME_MODE               = 3     # single mode or multiplayers mode

STICK_NUM_DEFAULT       = 10    # default value of stick
PILE_NUM_DEFAULT        = 5     # default value of pile
STICKLOSE_NUM_DEFAULT   = 0     # default value of stick lose

STICK_NUM_MAX           = 20    # maximum number of stick in one file
PILE_NUM_MAX            = 20    # maximum number of file

GAME_MODE_SINGLE        = 0     # single player mode, with computer
GAME_MODE_MULIPLAYERS   = 1     # multiple players

MSG_PLAYER1             = 1     # congratulation message for player 1st
MSG_PLAYER2             = 2     # congratulation message for playe 2nd/computer

# Default Game configuration
g_GameConfig = [STICK_NUM_DEFAULT,PILE_NUM_DEFAULT,STICKLOSE_NUM_DEFAULT,GAME_MODE_SINGLE]

# Convert from string to positive integer and validate it
def convertStrToInt(in_str):
    if in_str.isdigit():
        resVal = int(in_str)
        if resVal >= 0:
            return resVal

    # Exception
    return -1

# Initialize general game configuration
def initializeGameConfig():
    # Initialize the piles with random number of sticks.
    initGameConfig = g_GameConfig
    retry_cnt = 0

    while True:
        # Setting game mode
        usrInput = input("Choose game mode(0:single player, 1:multiple players):")
        gameMode = convertStrToInt(usrInput)

        # User input
        usrInput = input("Choose number of pile(2~%d): "%(PILE_NUM_MAX))
        numPile = convertStrToInt(usrInput)
    
        usrInput = input("Choose maximum number of stick in one pile(1~%d): "%(STICK_NUM_MAX))
        numStick = convertStrToInt(usrInput)

        #usrInput = input("Choose number of last sticks lose: ")
        numStickLose = 0  #convertStrToInt(usrInput)

        if numStick in range(1,STICK_NUM_MAX+1) and\
            numPile in range(2,PILE_NUM_MAX+1) and\
            numStickLose >= 0 and\
            gameMode in range(0,2):

            initGameConfig[STICK_NUM_INDEX] = numStick
            initGameConfig[PILE_NUM_INDEX] = numPile
            initGameConfig[STICKLOSE_NUM_INDEX] = numStickLose
            initGameConfig[GAME_MODE] = gameMode
            break
        else:
            print("[ERR] Invalid input number!")
            retry_cnt += 1
            if retry_cnt == 3:
                print("[ERR] You entered wrong input over 3 times.")
                print("Let's play with a random initial configuration.")
                break;

    return initGameConfig

# Initialize piles
def initializePiles(gameConfig):
    # Initialize the piles with random number of stick. STICK_NUM_INDEX
    return [random.randint(1, gameConfig[STICK_NUM_INDEX]) for _ in range(gameConfig[PILE_NUM_INDEX])]

# Check if the game is over.
def gameOver(piles):
    
    for stick in piles:
        if stick != 0:
            return False
    
    # if all of sticks in piles are removed, return true
    return True

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

# print the congratation message
def printCongratMessage(msg_type):
    if msg_type == MSG_PLAYER1:
        print("Amazing, Player 1st won!")
    else:
        if g_GameConfig[GAME_MODE] == GAME_MODE_SINGLE:
            print("Sorry, the computer won!")
        elif g_GameConfig[GAME_MODE] == GAME_MODE_MULIPLAYERS:
            print("Congratulation, Player 2nd won!")

# Computer's move
def computerMove(piles):

    pile = 0
    # if piles empty
    while piles[pile] == 0:
        pile = random.randint(0, len(piles) - 1)

    sticks_to_remove = random.randint(1, piles[pile])
    print(f"Computer removed {sticks_to_remove} sticks from pile {pile+1}")
    piles[pile] -= sticks_to_remove

# Allow the player to make a move.
def playerMove(piles):
    while True:

        # Print the current piles
        #printPiles(piles)

        # Ask user selecting the pile
        usr_input = input("Select a pile (1, 2, 3, etc.Max=%d): "%(len(piles)))
        pile = convertStrToInt(usr_input)
        if pile == -1 or pile == 0:
            print("Invalid input number!")
            continue
        
        # pile = int(input("Select a pile (1, 2, 3, etc.Max=%d): "%(len(piles)))) - 1
        # pile >= 1
        pile = pile -1

        if 0 <= pile < len(piles):
            if piles[pile] == 0:
                print("[ERR] No stick in this pile. Please choose anothers!")
                continue

            #sticks_to_remove = int(input("How many sticks do you want to remove(Max=%d)? "%(piles[pile])))
            while True:
                usr_input = input("How many sticks do you want to remove(Max=%d)? "%(piles[pile]))
                sticks_to_remove = convertStrToInt(usr_input)
                if sticks_to_remove != -1:
                    break
                else:
                    print("Invalid input number!")
                    continue
            
            # Decrease the stick in piles
            if 1 <= sticks_to_remove <= piles[pile]:
                piles[pile] -= sticks_to_remove
                break
            else:
                print("[ERR] Invalid number of sticks!")
        else:
            print("[ERR] Invalid pile number!")

#==================MAIN PROGRAM================================================
# Main function
def main():
    print("=================================")
    print("|| Welcome to the game of Nim! ||")
    print("=================================")

    # Main loop
    while True:  
        # Initialize game configuration
        g_GameConfig = initializeGameConfig()

        # Initialize files
        piles = initializePiles(g_GameConfig)

        # Print the current piles
        printPiles(piles)

        # Main processing
        while not gameOver(piles):
            # Ask player move
            print("Player 1st turn")
            playerMove(piles)
            if gameOver(piles):
                #print("Amazing! You won!")
                printCongratMessage(MSG_PLAYER1)
                break

            print()
            printPiles(piles)
            if g_GameConfig[GAME_MODE] == GAME_MODE_SINGLE:
                # Computer move
                print("Computer turn.")
                computerMove(piles)
            elif g_GameConfig[GAME_MODE] == GAME_MODE_MULIPLAYERS:
                # Ask player 2nd move
                print("Player 2nd turn.")
                playerMove(piles)

            # Checking the game is over or not
            if gameOver(piles):
                #print("Sorry, the computer won!")
                printCongratMessage(MSG_PLAYER2)
                break

            printPiles(piles)
        
        usrInput = input("Do you want play more (Y/N):")
        usrInput = usrInput.lower()
        if usrInput == 'n':
            print("Thanks, see you again.")
            break

if __name__ == "__main__":
    main()