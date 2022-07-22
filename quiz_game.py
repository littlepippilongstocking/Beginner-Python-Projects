"""
Dilyana Koleva, July 2022
Beginner's Python Project - Quiz Game
"""
def play():
    print("Welcome to this computer quiz!")
    playing = input("Do you want to begin playing? ").lower()
    if playing == "yes":
        print("Let's begin! ")
        score = 0
        level1(score)
    else:
        print("Sorry to see you go. See you soon! ")
        quit()


def level1(score):
    print("Level 1 has 4 questions. For each question you get correct you receive one (1) point.")
    print("Let's play!")

    question1 = input("Q1: What does CPU stand for? ").lower()
    if question1 == "central processing unit":
        print("Your answer is correct!")
        score += 1
    else:
        print("Sorry. The correct answer is Central Processing Unit.")

    question2 = input("Q2: What does GPU stand for? ").lower()
    if question2 == "graphics processing unit":
        print("Your answer is correct!")
        score += 1
    else:
        print("Sorry. The correct answer is Graphics Processing Unit.")

    question3 = input("Q3: What does RAM stand for? ").lower()
    if question3 == "random access memory":
        print("Your answer is correct!")
        score += 1
    else:
        print("Sorry. The correct answer is Random Access Memory.")

    question4 = input("Q4: What does UoS stand for? ").lower()
    if question4 == "university of southampton":
        print("Your answer is correct!")
        score += 1
    else:
        print("Sorry. The correct answer is University of Southampton.")

    if score == 1:
        print(f"You got {score} question correct! Awesome game! See you soon.")
    elif score > 1:
        print(f"You got {score} questions correct! Awesome game! See you soon.")
    elif score == 0:
        print(f" Oh, you got {score} questions correct. Try again later!")


play()
