import random

def initialize_piles():
    """
    Initialize the piles with random number of stones.
    """
    return [random.randint(1, 10) for _ in range(random.randint(2, 5))]

def print_piles(piles):
    """
    Print the current state of the piles.
    """
    print("Current piles:")
    for i, stones in enumerate(piles):
        print(f"Pile {i+1}: {stones} stones")

def player_move(piles):
    """
    Allow the player to make a move.
    """
    while True:
        print_piles(piles)
        pile = int(input("Select a pile (1, 2, 3, etc.): ")) - 1
        if 0 <= pile < len(piles):
            stones_to_remove = int(input("How many stones do you want to remove? "))
            if 1 <= stones_to_remove <= piles[pile]:
                piles[pile] -= stones_to_remove
                break
            else:
                print("Invalid number of stones!")
        else:
            print("Invalid pile number!")

def computer_move(piles):
    """
    Implement the computer's move.
    """
    pile = random.randint(0, len(piles) - 1)
    stones_to_remove = random.randint(1, piles[pile])
    print(f"Computer removes {stones_to_remove} stones from pile {pile+1}")
    piles[pile] -= stones_to_remove

def game_over(piles):
    """
    Check if the game is over.
    """
    return all(stones == 0 for stones in piles)

def main():
    print("Welcome to the game of Nim!")
    piles = initialize_piles()
    while not game_over(piles):
        player_move(piles)
        if game_over(piles):
            print("Congratulations! You win!")
            break
        computer_move(piles)
        if game_over(piles):
            print("Sorry, the computer wins!")
            break

if __name__ == "__main__":
    main()