from itertools import islice

menu = {'drip': 1.95, 'cappuccino': 2.95, 'americano': 2.49}

menu = dict(islice(menu.items(), 0, 3, 2))  # same as [0:3:2]
print(menu)
