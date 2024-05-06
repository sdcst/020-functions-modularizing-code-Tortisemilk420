"""
Task 2:
Create a program to play a number guessing game
There should be a function:
title()
displays instructions and how to play

game()
plays the games

"""


def title():
    print("Guess a number between 1 and 100")

def game():
    guess = 0
    import random
    choice = random. randint(1, 100)
    while choice != guess: 
        guess = int(input("Pick a number between 1 and 100:"))
    else:
        print("You Guessed the corect number") 


title()
game()