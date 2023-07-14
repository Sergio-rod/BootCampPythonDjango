
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
            'coffe': 24
        },
        'cost': 3.0
    }

}

resources = {
    'water': 300,
    'milk': 200,
    'coffee': 100
}
# TODO: 1. Print the report of all coffee machine resources


#handling variables
espressoWaterQty = MENU['espresso']['ingredients']['water']
espressoCoffeQty= MENU['espresso']['ingredients']['coffe']


def menu():
    money = 0
    option = input('What would you like? (espresso/latte/capuccino): \n')
    if option == 'report':
        print(resources)
    elif option == 'off':
        print('GoodBye')
        exit()
    elif option == 'espresso':
        if (resources['water'] > espressoWaterQty) and (resources['coffee'] > espressoCoffeQty ):
            try:
                quarters = int(input('Please, insert the quarters'))
                if quarters > 0:
                    money += quarters*.25
                elif quarters < 0:
                    print('That`s not possible')

                dimes = input('Please, insert the dimes')
                nickles = input('Please, insert the nickles')
                pennies = input('Please, insert the pennies')
            except ValueError:
                print('You must to enter a valid values ')

            
        else: 
            print('Sorry, its not enough ingredients')







# TODO: 2. Check resources sufficent to make drink order
# TODO: 3. Process coins
# TODO: 4. Check transaction succesfully
# TODO: 5. Make a coffe










'''if __name__ == '__main__':
    print_hi('PyCharm')'''

