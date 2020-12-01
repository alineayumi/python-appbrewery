import random
from os import system, name 
# import sleep to show output for some time period 
from time import sleep 
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
  
# define our clear function 
def clear(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

def check_answer(guess, number, n_attempts):
	if guess == number:
		print(f'You are correct! Congrats!! The answer was {number}!')
	else:
		if guess > number:
			print('Too high.')
		elif guess < number:
			print('Too low.')
		if n_attempts > 1:
			print('Guess again')
		else:
			print('You\'ve run out guesses, you lose')

def set_difficult():
	difficulty = input('Choose a difficulty. Type "easy" or "hard": ')
	if difficulty == 'easy':
		return EASY_LEVEL_TURNS
	else:
		return HARD_LEVEL_TURNS

def guess_game():
	clear()
	print(logo)
	print('Welcome to the Number Guessing Game!')
	print('I am thinking of a number between 1 and 100')

	nbr = random.randint(1, 101)
	n_attempts = set_difficult()

	guess = 0
	while n_attempts > 0 and guess != nbr:
		print(f'You have {n_attempts} remaining to guess the number')
		guess = int(input('Make a guess: '))
		check_answer(guess, nbr, n_attempts)
		n_attempts -= 1

guess_game()
