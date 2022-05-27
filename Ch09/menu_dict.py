menu = {"drip": 1.95, "cappuccino": 2.95}
print(menu["drip"])  # prints 1.95
menu["americano"] = 2.49
print(menu)  # prints {'drip': 1.95, 'cappuccino': 2.95, 'americano': 2.49}
del menu["americano"]
print(menu)  # prints {'drip': 1.95, 'cappuccino': 2.95}
