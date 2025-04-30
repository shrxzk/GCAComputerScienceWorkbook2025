# Library
import random  # Import the random module to generate random choices for the computer

# Variables
YourGuess: str = None  # Stores the player's choice
ComputerGuess: str = None  # Stores the computer's choice

YourScore: int = 0  # Tracks the player's score
CScore: int = 0  # Tracks the computer's score

# Dictionary containing possible choices
Options = {
    1: "Rock",
    2: "Paper",
    3: "Scissors"
}

# Function to generate the computer's random choice
def computer_Guess():
    return Options[random.randint(1, 3)]  # Picks a random value from the dictionary using a random key (1-3)

# Game starts
print("Welcome to Rock Paper Scissors")

# Variables for round tracking
CurrentRound: int = 0
RoundsToPlay: int = 0

# Get a valid number of rounds from the player
while True:
    RoundsToPlay = int(input("Amount of rounds to play: "))  # Ask for the number of rounds
    CurrentRound = 0  # Reset current round

    if RoundsToPlay < 1 or RoundsToPlay > 10:  # Ensures rounds are between 1 and 10
        print("Enter between 1 and 10 rounds!\n")
    else:
        break  # Exit the loop if input is valid

# Main game loop
while True:

    # Player's turn to input a choice
    while True:
        YourGuess = input("Your turn: ")  # Player inputs their choice
        ComputerGuess = computer_Guess()  # Computer generates its random choice

        # Validate input - must be Rock, Paper, or Scissors
        if YourGuess.capitalize() in ["Rock", "Paper", "Scissors"]:
            break  # Exit loop if valid
        else:
            print("\nInvalid option\n")  # Prompt user to enter a valid choice

    CurrentRound += 1  # Increment the round counter

    # Show choices
    print(f"\nComputer chose: {ComputerGuess}")

    # Determine the winner
    if YourGuess == ComputerGuess:
        print("\nDraw")  # If both choices are the same
    elif YourGuess == "Rock" and ComputerGuess == "Scissors":
        print("\nYou win!")  # Rock beats Scissors
        YourScore += 1
    elif YourGuess == "Paper" and ComputerGuess == "Rock":
        print("\nYou win!")  # Paper beats Rock
        YourScore += 1
    elif YourGuess == "Scissors" and ComputerGuess == "Paper":
        print("\nYou win!")  # Scissors beats Paper
        YourScore += 1
    else:
        print("\nComputer wins!")  # If none of the above conditions are met, the computer wins
        CScore += 1

    # Check if the game is over
    if CurrentRound == RoundsToPlay:
        # Final results
        if YourScore > CScore:
            print(f"\nYou win the game! Final score: {YourScore} - {CScore}")
        elif CScore > YourScore:
            print(f"\nYou lose the game! Final score: {YourScore} - {CScore}")
        else:
            print("\nIt's a tie!")  # If scores are equal
        break  # Exit the game loop
    else:
        print(f"\nRound number {CurrentRound + 1} starting...\n")  # Start next round
        
#I hated this logic so much