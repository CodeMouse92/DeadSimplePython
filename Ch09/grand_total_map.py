from operator import add

cost = [5.95, 4.95, 5.45, 3.45, 2.95]
tip = [0.25, 1.00, 2.00, 0.15, 0.00]

for total in map(add, cost, tip):
    print(f"{total:.02f}")
