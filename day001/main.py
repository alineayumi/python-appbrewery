print('Hello world')

# exercise 1-1
print('\n--- exercise 1-1  ---\n')
print('Day 1 - Python Print Function')
print('The function is declared like this:')
print("print('what to print')")

print('\n--- exercise 1-2  ---\n')
# Fix the code below 👇
print("Day 1 - String Manipulation")
print("String Concatenation is done with the '+' sign.")
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")
# string concatenation
print('Hello ' + 'Aline!')

print('\n--- exercise 1-3  ---\n')
#Write your code below this line 👇
name = input("What's your name? ")
print(len(name))

print('\n--- exercise 1-4  ---\n')
# 🚨 Don't change the code below 👇
a = input("a: ")
b = input("b: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
tmp = a
a = b
b = tmp
#Write your code above this line 👆
####################################

# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)

print('\n--- band name generator  ---\n')
#1. Create a greeting for your program.
print('Hi there! Welcome to the band name generator!')
#2. Ask the user for the city that they grew up in.
city = input("Which city did you grow up in?\n")
#3. Ask the user for the name of a pet.
pet = input("Tell me the name of a pet:\n")
#4. Combine the name of their city and pet and show them their band name.
print('Your band name could be ' + city + ' ' + pet)
#5. Make sure the input cursor shows on a new line, see the example at:
#   https://band-name-generator-end.appbrewery.repl.run/