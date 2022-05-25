from random import choice

colors = ['red', 'green', 'blue', 'silver', 'white', 'black']
vehicles = ['car', 'truck', 'semi', 'motorcycle', None]


# as an iterator class

# class Traffic:
#     def __iter__(self):
#         return self

#     def __next__(self):
#         vehicle = choice(vehicles)

#         if vehicle is None:
#             raise StopIteration

#         color = choice(colors)

#         return f"{color} {vehicle}"

# as a generator function

def traffic():
    while True:
        vehicle = choice(vehicles)

        if vehicle is None:
            return

        color = choice(colors)
        yield f"{color} {vehicle}"


# merge into traffic
count = 0
# for count, vehicle in enumerate(Traffic(), start=1):
for count, vehicle in enumerate(traffic(), start=1):
    print(f"Wait for {vehicle}...")

print(f"Merged after {count} vehicles!")
