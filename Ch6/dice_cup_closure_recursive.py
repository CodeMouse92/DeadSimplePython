import random


def make_dice_cup(sides=6, dice=1):
    def roll(dice=dice):
        # nonlocal dice
        if dice < 1:
            return ()
        die = random.randint(1, sides)
        dice -= 1
        return (die, ) + roll(dice - 1)

    return roll


roll_for_damage = make_dice_cup(sides=8, dice=5)
damage = roll_for_damage()
print(damage)

damage = roll_for_damage()
print(damage)
