customers = [
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
]

for customer, drink in customers:
    print(f"Making {drink}...")
    print(f"Order for {customer}!")

for _, drink in sorted(customers, key=lambda x: x[1]):
    print(f"{drink}")

for number, (customer, drink) in enumerate(customers, start=1):
    print(f"#{number}. {customer}: {drink}")
