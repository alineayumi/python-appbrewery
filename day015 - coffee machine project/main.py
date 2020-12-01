MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


# Checks if there is enough ingredients to make the drink
# It returns true if there is or false if there is not
def check_resources(drink):
    drink_ingredients = MENU[drink]['ingredients']
    resources_sufficient = True
    for ingredient in drink_ingredients:
        if resources[ingredient] < drink_ingredients[ingredient]:
            resources_sufficient = False
            print(f"Sorry there is not enough {ingredient}.")
    return resources_sufficient


def update_resources(drink, drink_price):
    drink_ingredients = MENU[drink]['ingredients']
    resources['money'] += drink_price
    for ingredient in drink_ingredients:
        resources[ingredient] -= drink_ingredients[ingredient]


# Asks for the user to insert the coins and checks if the amount given is enough to pay the drink
# Returns true if there is enough money and false if there is not
def process_coins(drink):
    print("Please insert coins:")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    total_received = 0.25 * quarters + 0.10 * dimes + 0.05 * nickles + 0.01 * pennies
    drink_price = MENU[drink]['cost']
    if total_received >= drink_price:
        update_resources(drink, drink_price)
        change = round(total_received - drink_price, 2)
        if change > 0:
            print(f"Here is ${change} in change.")
        print(f"Here is your {drink} ☕️ Enjoy!")
    else:
        print("Sorry that is not enough money. Money refunded.")


def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}ml")
    print(f"Money: ${resources['money']}")


def coffee_machine():
    turn_off = False

    while not turn_off:
        # TODO: 1. Prompt user by asking “ What would you like? (espresso/latte/cappuccino): ”
        user_input = input("What would you like? (espresso/latte/cappuccino): ")

        # TODO: 2. Turn off the Coffee Machine by entering “ off ” to the prompt.
        if user_input == "off":
            turn_off = True
        elif user_input == "report":
            # TODO: 3. Print report
            print_report()
        elif user_input in MENU:
            # TODO: 4. Check resources sufficient?
            if check_resources(user_input):
                # TODO: 5. Process coins.
                # TODO: 6. Check transaction successful?
                # TODO: 7. Make Coffee.
                process_coins(user_input)
        else:
            print("Invalid input, please write again.")


coffee_machine()
