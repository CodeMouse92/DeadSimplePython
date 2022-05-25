from random import choice, randint

colors = ['red', 'green', 'blue', 'silver', 'white', 'black']
vehicles = ['car', 'truck', 'semi', 'motorcycle', None]


def biker_gang():
    for _ in range(randint(2, 10)):
        color = choice(colors)
        yield f"{color} motorcycle"


def traffic():
    while True:
        if randint(1, 50) == 50:
            yield from biker_gang()
            continue

        vehicle = choice(vehicles)
        color = choice(colors)
        yield f"{color} {vehicle}"


count = 0
for count, vehicle in enumerate(traffic()):
    print(f"{vehicle}")
    if count == 100:
        break
