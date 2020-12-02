from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

turn_off = False
coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

while not turn_off:
    user_input = input(f"What would you like? ({menu.get_items()}): ")
    if user_input == "off":
        turn_off = True
    elif user_input == "report":
        coffee_machine.report()
        money_machine.report()
    else:
        order = menu.find_drink(user_input)
        if coffee_machine.is_resource_sufficient(order) and money_machine.make_payment(order.cost):
            coffee_machine.make_coffee(order)
