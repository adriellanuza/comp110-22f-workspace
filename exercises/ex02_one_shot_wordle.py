"""Wordle Program!!!"""

__author__ = "730511180"

secret_word: str = "python"
player_guess: str = input("What is your 6-letter guess? ")
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
word_index: int = player_guess[0]

while len(player_guess) != 6:
    player_guess = input("That was not 6 letters! Try again: ")

if player_guess != secret_word:
    print("Not quite. Play again soon!")
else:
    print("Woo! You got it!")
    

    
        






    
