# #HINT: You can call clear() to clear the output in the console.
import art

print(art.logo)
print("Welcome to the secret aution program.")
continue_asking = True
bids = {}

while continue_asking:
  name = input('What is your name? ')
  bid = int(input('What is your bid? $'))
  continue_asking = (input("Are there any other bidders? Type 'yes' or 'no'.").lower() == 'yes')
  bids[name] = bid
max = 0
name = ''
for key in bids:
  value = bids[key]
  if value > max:
    max = value
    name  = key
print(f"{name} won with a bid of ${max}")
