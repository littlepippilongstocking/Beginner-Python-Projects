"""
Dilyana Koleva, July 2022
Beginner's "Guess the number" game for Pyton
The computer plays against the user
"""
import random


def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low

        feedback = input(f"Is {guess} too high(H), too low(L) or correct(C)?".lower())

        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1

    print(f"Wow. I have just guessed the number {guess} correctly!")
    response = input(f"Do you want to continue playing? Yes (Y) or No(N)".lower())

    if response == "y":
        computer_guess(int(input("Please, choose an upper bound number: ")))
    elif response == "n":
        print("Thank you for playing. Goodbye!")


computer_guess(int(input(" Welcome to Guess the Number. My name is Compy and"
                         "I will be playing with you today. \n Let's begin. "
                         "Please, choose an upper bound number: ")))
