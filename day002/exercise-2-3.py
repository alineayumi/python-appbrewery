# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#First *fork* your copy. Then copy-paste your code below this line 👇
#Finally click "Run" to execute the tests
age_as_int = int(age)
left_years = 90 - age_as_int
left_months = left_years * 12
left_weeks = left_years * 52
left_days = left_years * 365

print(f'You have {left_days} days, {left_weeks} weeks, and {left_months} months left.')