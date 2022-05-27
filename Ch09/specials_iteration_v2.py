specials = ["pumpkin spice latte", "caramel macchiato", "mocha cappuccino"]
iterator = iter(specials)

while True:
    try:
        item = next(iterator)
    except StopIteration:
        break
    else:
        print(item)
