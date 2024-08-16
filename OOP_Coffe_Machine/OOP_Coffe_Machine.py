from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
should_continue = True







while should_continue:
    options = menu.get_items()
    user_chice = input(f"What would you like? ({options}): ").lower()
    if user_chice == "off":
        should_continue = False
    elif user_chice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(user_chice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
    

