

import random

randomNumbers = random.randint(1,100)
Guess = 0
Chances = 5
while Guess != randomNumbers and Chances > 0:
    Guess = int(input(f"Guess the number you have {Chances} chances to guess. Good luck!"))
    if Guess > randomNumbers:
        print("Guess lower!")
    elif Guess < randomNumbers:
        print("Guess higher!")
    Chances -= 1
if Guess == randomNumbers:
        print(" you've guessed right :) !")
else:
        print(f"Sorry! the right number is {randomNumbers} better luck next time :( ")








