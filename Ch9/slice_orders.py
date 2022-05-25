orders = [
    "caramel macchiato",
    "drip",
    "pumpkin spice latte",
    "drip",
    "cappuccino",
    "mocha latte",
]

three_four_five = orders[3:6]
print(three_four_five)   # prints ['drip', 'cappuccino', 'americano']

after_third = orders[4:]
print(after_third)       # print ['cappuccino', 'americano', 'mocha latte']

next_two = orders[:2]
print(next_two)          # prints ['caramel macchiato', 'drip']

print(orders[-1])        # prints 'mocha latte'

last_three = orders[-3:]
print(last_three)        # prints ['cappuccino', 'americano', 'mocha latte']

last_two_but_one = orders[-3:-1]
print(last_two_but_one)  # prints ['cappuccino', 'americano']

every_other = orders[1::2]
print(every_other)       # prints ['drip', 'drip', 'americano']

reverse = orders[::-1]

every_other_reverse = orders[-2::-2]
print(every_other_reverse)  # prints['americano', 'drip', 'drip']

# three_to_five_reverse = orders[3:6:-1]  # WRONG! Returns empty list.
# print(three_to_five_reverse)            # prints []
three_to_five_reverse = orders[5:2:-1]
print(three_to_five_reverse)  # prints ['americano', 'cappuccino', 'drip']

order_copy = orders[:]
