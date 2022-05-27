class Pizza:

    def __init__(self, topping, second_topping=None):
        self.first = topping
        self.second = second_topping


order = Pizza("pepperoni", "mushrooms")

match order:
    case Pizza(first='pepperoni', second='mushroom'):
        print("ANSI standard pizza")
    case Pizza(first='pineapple'):
        print("Is this even pizza?")
    case Pizza(first=first, second='cheese'):
        print(f"Very cheesy pizza with {first}.")
    case Pizza(first=first, second=second):
        print(f"Pizza with {first} and {second}.")
