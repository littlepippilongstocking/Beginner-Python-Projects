#Dilyana Koleva, July 2022
#A simple Python game for playing rock, paper, scissors

import random

def play():
	user = input("Choose your weapon: 'r' for rock, 'p' for paper, 's' for scissors\n")
	computer = random.choice(['r', 'p','s'])
	
	if user == computer:
		return "Oh, it is a tie!"
	if is_win(user, computer):
		return "Congratulations! You won!"

	return "Sorry! You lost!"

def is_win(player, opponent):
	if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
		return True

print(play())