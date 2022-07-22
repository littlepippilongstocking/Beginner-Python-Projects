"""
Dilyana Koleva, July 2022
Beginner's Python Project - Choose your own adventure Game
"""


def play():
    print("Welcome to Choose your own adventure!")
    playing = input("Do you want to begin playing? ").lower()
    if playing == "yes":
        print("Let's begin! ")
        choice1()
    else:
        print("Sorry to see you go. See you soon! ")
        quit()


def choice1():
    c1 = input("Your adventure begins one early morning. \n"
               "You are travelling on the long dirty road when suddenly it comes to an end.\n"
               "You can go left or right. Which path do you choose? ").lower()
    if c1 == "left":
        choice2part1()
    elif c1 == "right":
        choice2part2()
    else:
        print("Not a valid option. You lose.")
        quit()


def choice2part1():
    c2 = input("You chose the left path which leads to the sea.\n"
               "There you find an abandoned castle. Do you enter it or do you pass it?\n"
               "Type ENTER or PASS. ").lower()
    if c2 == "enter":
        print("You entered the abandoned castle. There you find a dying beast.\n"
              "You decide to help him and suddenly he turns into a beautiful prince.\n"
              "You and the beast fall in love and live happily ever after.")
        quit()
    elif c2 == "pass":
        print("You decided to pass the castle and continue to the nearby village.\n"
              "There you open a shop and live a long and prosperous life.")
        quit()
    else:
        print("The option you typed is incorrect. Goodbye!")
        quit()


def choice2part2():
    c2 = input("You have reached a river.\n"
               "You can either swim across or try to find another way?\n"
               "Which way do you choose?\n"
               "Type WALK to find another way or SWIM to swim it. ").lower()

    if c2 == "walk":
        print("You have decided to find another way.\n"
              "Suddenly, you encounter a dragon. After a long and fierce fight\n"
              "you lose to the strong animal and fall to your death.")
        quit()
    elif c2 == "swim":
        print("While swimming you encounter a river monster.\n"
              "Just when you are about to lose the fight\n"
              "a dolphin comes and saves you. Your saviour brings you to safety.\n")
        quit()
    else:
        print("The option you typed is incorrect. Goodbye!")
        quit()

play()