"""
Dilyana Koleva, July 2022
Beginner's "Rock, Paper, Scissors" game for Pyton
"""
import random


def play():
    user = input("Welcome to Rock, Paper, Scissors. My name is Rick. \n"
                 "The rules are simple and I am sure you know them. Now let's play. \n"
                 "Choose your weapon: 'r' for rock, 'p' for paper, 's' for scissors\n")

    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        print(f"Oh, it is a tie! We both chose {computer}.")
        continue_playing()

    if is_win(user, computer):
        print(f"Congratulations! You won! I chose {computer} and your {user} won against me.")
        continue_playing()

    print(f"Sorry! You lost! I chose {computer} and your {user} lost against me.")
    continue_playing()


def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (
            player == 'p' and opponent == 'r'):
        return True


def continue_playing():
    response = input(f"Do you want to continue playing? Yes (Y) or No(N)".lower())
    if response == "y":
        print(input("Choose your weapon: 'r' for rock, 'p' for paper, 's' for scissors "))
    elif response == "n":
        print("Thank you for playing. Goodbye!")


play()
