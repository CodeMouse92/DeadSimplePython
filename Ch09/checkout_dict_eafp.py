menu = {'drip': 1.95, 'cappuccino': 2.95, 'americano': 2.49}


def checkout(order):
    try:
        print(f"Your total is {menu[order]}")
    except KeyError:
        print("That item is not on the menu.")


checkout("drip")  # prints "Your total is 1.95"
checkout("tea")   # prints "That item is not on the menu."
