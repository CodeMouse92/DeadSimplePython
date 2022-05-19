from dbm import dumb
import random


def roll_dice(*, sides=6, dice=1):
    return tuple(random.randint(1, sides) for _ in range(dice))


dice_cup = roll_dice(sides=6, dice=5)
print(dice_cup)

dice_cup = roll_dice(6, 5)  # raises TypeError
print(dice_cup)
