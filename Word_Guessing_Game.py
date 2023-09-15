
#1: Word Guessing Game
import random

Guess = 0
def word_Guessing_Game(words):

    RandomWords = random.choice(words)
    Fletter = RandomWords[0]
    Lletter = RandomWords[-1]
    Guess = input(f"Guess the {len(RandomWords)} letter word starting with '{Fletter}' and ending with '{Lletter}': ")

    if Guess == RandomWords:
            print("Congratulations you've guessed correctly :) !")

    else:
            print(f"Wrong! the correct word was '{RandomWords}'")


WORDS = ["boat", "apple", "boy", "girl", "palace", "crown", "book", "sleep", "smart", "chair", "zoo", "house", "car",
         "cat", "dog", "home", "travel", "water", "country", "land", "actor", "sad", "mat", "pot", "pan", "kitchen",
         "bed", "road", "floor", "teacher", "soft", "life", "mother", "father", "vase", "rat", "part", "school",
         "friend", "laptop", "phone", "big", "insect", "campaign", "interest", "dictionary", "key", "python", "remote",
         "bug", "brother" "young", "pen", "egg", "black", "panther", "purple", "small", "code" "exit", "ground", "jug",
         "jungle", "king", "nurse", "orange", "queen", "winter", "xylophone", "ferrari", "clay", "random", "little", ]

word_Guessing_Game(WORDS)



