orders = ['cold brew', 'lemongrass tea', 'chai latte', 'medium drip',
          'french press', 'mocha cappuccino', 'pumpkin spice latte',
          'double-shot espresso', 'dark roast drip', 'americano']


def brew(order):
    print(f"Making {order}...")
    return order


for order in map(brew, orders):
    print(f"One {order} is ready!")
