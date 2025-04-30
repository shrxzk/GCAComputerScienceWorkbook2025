#Libarys
import random
from time import sleep

#SuperDefs

currentGuess: int = 0

#Functions
def generate_numbers(amount: int) -> int:
    generatedNumber: str = ""
    for i in range(amount):
        generatedNumber += str(random.randrange(0,9))
    return generatedNumber

def make_guess(guess: str) -> str:
    guessCount = 0
    for letter in guess:
        if letter in Numbers:
            if guess[guess.index(letter)] == Numbers[guess.index(letter)]:
                guessCount += 1
    print(f"{guessCount} numbers are correct!")
    return 1
    
def eval_performance(currentguess: int, lastguess: str) -> int:
    if Numbers == lastguess:
        print(f"Guessed number [{Numbers}] in [{currentguess}] attempts!")
        sleep(10)
        exit() 
    else:
        return 1
#Declarations

Numbers: str = generate_numbers(4)

#Runtime
while True:
    print("\nNew guess!\n")
    lastguess: str = input("Guess the numbers: ")
    if lastguess == "nums":
        print(Numbers)
    currentGuess += make_guess(lastguess)
    eval_performance(currentGuess, lastguess)
        
#Debug and testing standard
#Use command "nums" to print numbers
#Id reccomend making use of print statments in the functions to test this
