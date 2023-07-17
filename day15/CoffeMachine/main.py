
MENU = {
    'espresso': {
        'ingredients': {
            'water': 50,
            'coffee': 18
        },
        'cost': 1.5,
    },
    'latte': {
        'ingredients': {
            'water': 200,
            'milk': 150,
            'coffee': 24
        },
        'cost': 2.5,
    },
    'capuccino': {
        'ingredients': {
            'water': 250,
            'milk': 100,
            'coffee': 24
        },
        'cost': 3.0
    }

}

resources = {
    'machineMoney': 0,
    'water': 300,
    'milk': 200,
    'coffee': 100
}
# TODO: 1. Print the report of all coffee machine resources



# HANDLING VARIABLES



# EXPRESSO QTY OF ITEMS REQUIRED
espressoWaterQty = MENU['espresso']['ingredients']['water']
espressoCoffeeQty = MENU['espresso']['ingredients']['coffee']
espressoCost = MENU['espresso']['cost']

# LATTE QTY OF ITEMS REQUIRED
latteWaterQty = MENU['latte']['ingredients']['water']
latteCoffeeQty = MENU['latte']['ingredients']['coffee']
latteMilkQty = MENU['latte']['ingredients']['milk']
latteCost = MENU['latte']['cost']


# EXPRESSO QTY OF ITEMS REQUIRED
capuccinoWaterQty = MENU['capuccino']['ingredients']['water']
capuccinoCoffeeQty = MENU['capuccino']['ingredients']['coffee']
capuccinoMilkQty = MENU['capuccino']['ingredients']['milk']
capuccinoCost = MENU['capuccino']['cost']


def menu():
    money = 0
    change = 0

    option = input('What would you like? (espresso/latte/capuccino): \n')
    if option == 'report':
        print(f'Water : {resources["water"]} ml')
        print(f'Coffe : {resources["coffee"]} g')
        print(f'Milk : {resources["milk"]} ml')
        print(f'Money : {resources["machineMoney"]} $')

    elif option == 'off':
        print('GoodBye')
        exit()

    # Espresso option
    elif option == 'espresso':
        if (resources['water'] > espressoWaterQty) and (resources['coffee'] > espressoCoffeeQty ):
            try:
                quarters = int(input('Please, insert the quarters'))
                if quarters > 0:
                    money += quarters*.25
                elif quarters < 0:
                    print('That`s not possible')

                dimes = int(input('Please, insert the dimes'))
                if dimes > 0:
                    money += dimes * .25
                elif dimes < 0:
                    print('That`s not possible')

                nickles = int(input('Please, insert the nickles'))
                if nickles > 0:
                    money += nickles * .25
                elif nickles < 0:
                    print('That`s not possible')

                pennies = int(input('Please, insert the pennies'))
                if pennies > 0:
                    money += pennies*.25
                elif pennies < 0:
                    print('That`s not possible')
            except ValueError:
                print('You must to enter a valid values ')

            if money >= espressoCost:
                change = money-espressoCost
                resources['water'] -= espressoWaterQty
                resources['coffee'] -= espressoCoffeeQty
                # Add the money to machineMoney Field
                resources['machineMoney'] += espressoCost
                print(f"Take your coffee, your change is {change}")
            else:
                print('You need more money')
        else:
            print('Sorry, its not enough ingredients')

    # Latte option
    elif option == 'latte':
        if (resources['water'] > latteWaterQty) and\
            (resources['coffee'] > latteCoffeeQty) and \
                (resources['milk'] > latteMilkQty):
            try:
                quarters = int(input('Please, insert the quarters'))
                if quarters > 0:
                    money += quarters * .25
                elif quarters < 0:
                    print('That`s not possible')

                dimes = int(input('Please, insert the dimes'))
                if dimes > 0:
                    money += dimes * .25
                elif dimes < 0:
                    print('That`s not possible')

                nickles = int(input('Please, insert the nickles'))
                if nickles > 0:
                    money += nickles * .25
                elif nickles < 0:
                    print('That`s not possible')

                pennies = int(input('Please, insert the pennies'))
                if pennies > 0:
                    money += pennies * .25
                elif pennies < 0:
                    print('That`s not possible')
            except ValueError:
                print('You must to enter a valid values ')

            if money >= latteCost:
                change = money - latteCost
                resources['water'] -= latteWaterQty
                resources['coffee'] -= latteCoffeeQty
                resources['milk'] -= latteMilkQty
                # Add the money to machineMoney Field
                resources['machineMoney'] += latteCost
                print(f"Take your coffee, your change is {change}")

            else:
                print(f'You need more money, take your founds {change}')
        else:
            print('Sorry, its not enough ingredients')

    # Capuccino option
    elif option == 'capuccino':
        if (resources['water'] > capuccinoWaterQty) and \
                (resources['coffee'] > capuccinoCoffeeQty) and \
                (resources['milk'] > capuccinoMilkQty):
            try:
                quarters = int(input('Please, insert the quarters'))
                if quarters > 0:
                    money += quarters * .25
                elif quarters < 0:
                    print('That`s not possible')

                dimes = int(input('Please, insert the dimes'))
                if dimes > 0:
                    money += dimes * .1
                elif dimes < 0:
                    print('That`s not possible')

                nickles = int(input('Please, insert the nickles'))
                if nickles > 0:
                    money += nickles * .05
                elif nickles < 0:
                    print('That`s not possible')

                pennies = int(input('Please, insert the pennies'))
                if pennies > 0:
                    money += pennies * .01
                elif pennies < 0:
                    print('That`s not possible')
            except ValueError:
                print('You must to enter a valid values ')

            if money >= capuccinoCost:
                change = money - capuccinoCost
                resources['water'] -= capuccinoWaterQty
                resources['coffee'] -= capuccinoCoffeeQty
                resources['milk'] -= capuccinoMilkQty
                # Add the money to machineMoney Field
                resources['machineMoney'] += capuccinoCost
                print(f"Take your coffee, your change is {change}")
            else:
                print('You need more money')
                exit()
        else:
            print('Sorry, its not enough ingredients')

    else:
        print("Enter a valid option")


while True:
    print("Hello, this is a coffe machine")
    menu()
    print(resources)





# TODO: 2. Check resources sufficent to make drink order
# TODO: 3. Process coins
# TODO: 4. Check transaction succesfully
# TODO: 5. Make a coffeefe










'''if __name__ == '__main__':
    print_hi('PyCharm')'''

