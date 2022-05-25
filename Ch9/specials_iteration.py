specials = ["pumpkin spice latte", "caramel macchiato", "mocha cappuccino"]

# first_iterator = specials.__iter__()
first_iterator = iter(specials)
# second_iterator = specials.__iter__()
second_iterator = iter(specials)
print(type(first_iterator))  # prints <class 'list_iterator'>

# item = first_iterator.__next__()
item = next(first_iterator)
print(item)                  # prints 'pumpkin spice latte'

# item = first_iterator.__next__()
item = next(first_iterator)
print(item)                  # prints 'caramel macchiato'

# item = second_iterator.__next__()
item = next(second_iterator)
print(item)                  # prints 'pumpkin spice latte'

# item = first_iterator.__next__()
item = next(first_iterator)
print(item)                  # prints 'mocha cappuccino'

item = next(first_iterator)  # raises StopIteration
