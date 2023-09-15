# 1: Calculator
def multiplication(*rigs):
    answer = 1
    for Num in rigs:
        answer *= Num
    return answer


def subtract_numbers(*args):
    result = args[0]
    for num in args[1:]:
        result -= num
    return result



def addition(numbers):
    total = 0
    for number in numbers:
        total += int(number)
    return total


def division(*KW):
    var = KW[0]
    for quo in KW[1:]:
        var /= quo
    return var


Question = input("""
Select:
1 - Addition
2 - Subtraction
3 - Multiplication
4 - Division
""")


if Question == "1":
    numbers = input("Enter the numbers, separate with space: ")
    numbers = numbers.split(" ") # [2 4  7 4 5 7 4 6 7 4 6 3 5 67 8 4 3]
    over = addition(numbers)
    print("The sum is", over)


elif Question == "2":
    input_nums = input("Enter the numbers you want to subtract, separate by spaces: ")
    nums = [int(num) for num in input_nums.split()]
    result = subtract_numbers(*nums)
    print("The difference is:", result)


elif Question == "3":
    input_Num = input("Enter the numbers you want to multiply, separate by spaces: ")
    Nums = [int(Num) for Num in input_Num.split()]
    answer = multiplication(*Nums)
    print("The product is:", answer)



elif Question == "4":
    input_div = input("Enter the numbers you want to divide, separated by spaces: ")
    sums = [float(quo) for quo in input_div.split()]
    var = division(*sums)
    print("The quotient is:",var)
else:
    print("Error!")




#2: Word Guessing Game
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



