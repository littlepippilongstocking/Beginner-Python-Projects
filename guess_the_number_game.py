"""
Dilyana Koleva, July 2022
Beginner's "Guess the number" game for Pyton
The user plays against the computer
"""

import random


def guess(x):
    random_number = random.randint(1, x)
    guess_num = 0
    while guess_num != random_number:
        guess_num = int(input(f"Guess a number between 1 and {x}: "))

        if guess_num < random_number:
            print("Sorry, guess again. The number you have chosen is too low.")
        elif guess_num > random_number:
            print("Sorry, guess again. The number you have chosen is too high.")

    print(f"Congratulations. You have just guessed my number {random_number} correctly!")
    response = input(f"Do you want to continue playing? Yes (Y) or No(N)".lower())

    if response == "y":
        guess(int(input("Please, choose an upper bound number: ")))
    elif response == "n":
        print("Thank you for playing. Goodbye!")


guess(int(input("Welcome to Guess the Number. My name is Compy. \n"
                "I will be playing with you. The rules are simple. \n"
                "You have to guess the number I have chosen. \n"
                "Now, please, choose an upper bound number: ")))
