from collections import deque

customers = deque([
    ('Newman', 'tea'),
    ('Daniel', 'lemongrass tea'),
    ('Simon', 'chai latte'),
    ('James', 'medium roast drip, milk, 2 sugar substitutes'),
    ('William', 'french press'),
    ('Kyle', 'mocha cappuccino'),
    ('Jason', 'pumpkin spice latte'),
    ('Devin', 'double-shot espresso'),
    ('Todd', 'dark roast drip'),
    ('Glen', 'americano, no sugar, heavy cream'),
    ('Denis', 'cold brew')
])

# for customer, drink in customers.copy():
#     print(f"Making {drink}...")
#     print(f"Order for {customer}!")
#     customers.popleft()

# print(customers)  # prints deque([])

while customers:
    customer, drink = customers.popleft()
    print(f"Making {drink}")
    print(f"Order for {customer}!")
