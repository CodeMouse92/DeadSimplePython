import random
from tracemalloc import start


def start_turn(limit, dice=5, sides=6):
    def roll():
        nonlocal limit
        if limit < 1:
            return None
        limit -= 1
        return tuple(random.randint(1, sides) for _ in range(dice))

    return roll


turn1 = start_turn(limit=3)
while toss := turn1():
    print(toss)

turn2 = start_turn(limit=3)
while toss := turn2():
    print(toss)
