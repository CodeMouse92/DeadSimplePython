import random


def roll_dice(*dice):
    # return tuple(random.randint(1, d) for d in dice)
    if dice:
        roll = random.randint(1, dice[0])
        return (roll,) + roll_dice(*dice[1:])
    return ()


dice_cup = roll_dice(6, 6, 6, 6, 6)
print(dice_cup)

bunch_o_dice = roll_dice(20, 6, 8, 4)
print(bunch_o_dice)
