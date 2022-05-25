order = ['venti', 'no whip', 'mocha latte', 'for here']

match order:
    case ('tall', *drink, 'for here'):
        drink = ' '.join(drink)
        print(f"Filling ceramic mug with {drink}.")
    case ['grande', *drink, 'to go']:
        drink = ' '.join(drink)
        print(f"Filling large paper cup with {drink}.")
    case ('venti', *drink, 'for here'):
        drink = ' '.join(drink)
        print(f"Filling extra large tumbler with {drink}.")
