specials = ["pumpkin spice latte", "caramel macchiato", "mocha cappuccino"]
print(specials[1])               # prints "caramel macchiato"

drink = specials.pop()           # return and remove last item
print(drink)                     # prints "mocha cappuccino"
print(specials)                  # prints ['pumpkin spice latte', 'caramel macchiato']

drink = specials.pop(1)          # return and remove item [1]
print(drink)                     # prints "caramel macchiato"
print(specials)                  # prints ['pumpkin spice latte']

specials.append("cold brew")     # inserts item at end
print(specials)                  # prints ['pumpkin spice latte', 'cold brew']

specials.insert(1, "americano")  # inserts as item [1]
print(specials)                  # prints ['pumpkin spice latte', 'americano', 'cold brew']
