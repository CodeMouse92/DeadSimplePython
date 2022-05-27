specials = ["pumpkin spice latte", "caramel macchiato", "mocha cappuccino"]
# print(specials[1])            # prints "caramel macchiato"
print(specials.__getitem__(1))  # prints "caramel macchiato"
# specials[1] = "drip"
specials.__setitem__(1, "drip")
# print(specials[1])            # prints "drip"
print(specials.__getitem__(1))  # prints "drip"
