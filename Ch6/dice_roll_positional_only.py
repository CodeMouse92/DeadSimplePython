import random

import random


def roll_dice(dice=1, /, sides=6):
    return tuple(random.randint(1, sides) for _ in range(dice))


roll_dice(4, 20)             # OK; dice=4, sides=20
roll_dice(4)                 # OK; dice=4, sides=6
roll_dice(sides=20)          # OK; dice=1, sides=20
roll_dice(4, sides=20)       # OK; dice=4, sides 20

roll_dice(dice=4)            # TypeError
roll_dice(dice=4, sides=20)  # TypeError
