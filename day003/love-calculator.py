# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
true = "true"
love = "love"
d = 0
u = 0
for letter in true:
  d += name1.lower().count(letter)
  d += name2.lower().count(letter)
for letter in love:
  u += name1.lower().count(letter)
  u += name2.lower().count(letter)
score = 10 * d + u

if score < 10 or score > 90:
  print(f"Your score is {score}, you go together like coke and mentos.")
elif score > 40 and score < 50:
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")