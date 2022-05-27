orders = ["pumpkin spice latte", "caramel macchiato", "mocha cappuccino"]

new_orders = orders[:]
for order in orders:
    # ... do whatever ...
    new_orders.append(order)
orders = new_orders

print(orders)
