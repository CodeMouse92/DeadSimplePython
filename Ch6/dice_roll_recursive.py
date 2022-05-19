import random


def roll_dice(sides, dice):
    if dice < 1:
        return ()
    roll = random.randint(1, sides)
    return (roll, ) + roll_dice(sides, dice-1)


dice_cup = roll_dice(6, 5)
print(dice_cup)
