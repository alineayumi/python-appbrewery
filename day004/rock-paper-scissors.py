import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

lst = [rock, paper, scissors]
my_choice = int(input('What do you choose? Type 0 for rock, 1 for paper or 2 for scissors.\n'))
comp_choice = random.randint(0,2)

if my_choice >= 3 or my_choice < 0: 
  print("You typed an invalid number, you lose!") 
else:
	print('your choice:')
	print(lst[my_choice])
	print('comp choice:')
	print(lst[comp_choice])

	if my_choice == comp_choice:
		print('It\'s a draw')
	elif my_choice == 0:
		if comp_choice == 1:
			print('You lose')
		else:
			print('You win')
	elif my_choice == 1:
		if comp_choice == 2:
			print('You lose')
		else:
			print('You win')
	elif my_choice == 2:
		if comp_choice == 0:
			print('You lose')
		else:
			print('You win')					


