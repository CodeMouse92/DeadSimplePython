Food = type('Food', (), {})


def __init__(obj, toppings):
    obj.toppings = toppings


Pizza = type('Pizza', (Food,), {'name': 'pizza', '__init__': __init__})

print(Pizza.name)                     # 'name' is a class attribute
pizza = Pizza(['sausage', 'garlic'])  # instantiate like normal
print(pizza.toppings)                 # prints "['sausage', 'garlic']"
