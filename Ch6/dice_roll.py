import random
import typing

TupleInts = typing.Tuple[int, ...]


def roll_dice(sides: int = 6, dice: int = 1) -> TupleInts:
    # return random.randint(1, sides)
    return tuple(random.randint(1, sides) for _ in range(dice))


print("Roll for initiative...")
# player1 = roll_dice(20)
# player2 = roll_dice(20)
player1, player2 = roll_dice(20, 2)
if player1 >= player2:
    print(f"Player 1 goes first (rolled {player1}).")
else:
    print(f"Player 2 goes first (rolled {player2}).")

# dice_cup = roll_dice(6, 5)
# dice_cup = roll_dice(sides=6, dice=5)
# dice_cup = roll_dice(dice=5, sides=6)
# dice_cup = roll_dice(dice=5)
dice_cup = roll_dice(6, dice=5)
