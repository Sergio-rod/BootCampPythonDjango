"""

from prettytable import PrettyTable

table = PrettyTable()
table.add_column('Pokemon name', ['Pikachu', 'Squirtle', 'Charmander'])
table.add_column('Type', ['Electric', 'Water', 'Fire'])
table.align = 'l'

print(table)


"""
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


# Objects Calling
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()


is_on = True

# Execution


while is_on:
    options = menu.get_items()
    choice = input(f'Choose your coffee {options}:' )

    if choice == 'off':
        is_on = False
    elif choice == 'report':
        coffee_maker.report()
        money_machine.report()

    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)





" Prompt user by asking “What would you like? (espresso/latte/cappuccino):”"
