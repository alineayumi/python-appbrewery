from art import logo, vs
from game_data import data
from os import system, name

import random

def clear(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

def pronoun(person):
	if person['description'][0].lower() in "aeiou":
		return 'an'
	return 'a'

def biggest(a, b):
	if a['follower_count'] > b['follower_count']:
		return 'a'
	else:
		return 'b'

def person_details(a):
	return f"{a['name']}, {pronoun(a)} {a['description']}, from {a['country']}."

def check_answer(a, b, score):
	print(f"Compare A: {person_details(a)}")
	print(vs)
	print(f"Against B: {person_details(b)}")
	answer = input("Who has more followers? Type 'A' or 'B': ").lower()
	while answer != 'a' and answer != 'b':
		print('Answer not valid.')
		answer = input("Who has more followers? Type 'A' or 'B': ").lower()
	most_popular = biggest(a,b)
	if most_popular == answer:
		return 1		
	return 0

def game():
	should_continue = True
	score = 0
	a = random.choice(data)

	while should_continue:
		clear()
		print(logo)
		b = random.choice(data)
		while (b == a):
			b = random.choice(data)
		if score > 0:
			print(f"You're right! Current score: {score}")
		if check_answer(a, b, score):
			score += 1
			a = b
		else:
			should_continue = False
			clear()
			print(logo)
			print(f"Sorry! That is wrong! Final score: {score}")

game()