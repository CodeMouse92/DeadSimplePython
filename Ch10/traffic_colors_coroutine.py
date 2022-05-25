from random import choice


def color_counter(color):
    matches = 0
    while True:
        vehicle = yield matches
        if color in vehicle:
            matches += 1


colors = ['red', 'green', 'blue', 'silver', 'white', 'black']
vehicles = ['car', 'truck', 'semi', 'motorcycle']


def traffic():
    while True:
        vehicle = choice(vehicles)
        color = choice(colors)
        yield f"{color} {vehicle}"


counter = color_counter('red')
# counter.send(None)  # prime the coroutine
next(counter)  # prime the coroutine

matches = 0
for count, vehicle in enumerate(traffic(), start=1):
    if count < 100:
        matches = counter.send(vehicle)
    else:
        counter.close()
        break

print(f"There were {matches} matches.")
