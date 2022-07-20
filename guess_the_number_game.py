import random
def guess(x):
	random_number = random.randint(1,x)
	guess = 0
	while guess != random_number:
		guess = int(input(f"Guess a number between 1 and {x}: "))
		if guess < random_number:
			print("Sorry, guess again. The number you have chosen is too low.")
		elif guess > random_number:
			print("Sorry, guess again. The number you have chosen is too high.")
	print("Congratulations. You have just guessed the number correctly!")
guess(10)
