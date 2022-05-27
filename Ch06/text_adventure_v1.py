import random

health = 10
xp = 10


def attempt(action, min_roll, outcome):
    global health, xp
    roll = random.randint(1, 20)
    if roll >= min_roll:
        print(f"{action} SUCCEEDED.")
        result = True
    else:
        print(f"{action} FAILED.")
        result = False

    scores = outcome(result)
    health = health + scores[0]
    print(f"Health is now {health}")
    xp = xp + scores[1]
    print(f"Experience is now {xp}")

    return result


# def eat_bread(success):
#     if success:
#         return (1, 0)
#     return (-1, 0)


# def fight_ice_weasel(success):
#     if success:
#         return (0, 10)
#     return (-10, 10)

# attempt("Eating bread", 5, eat_bread)
# attempt("Fighting ice weasel", 15, fight_ice_weasel)

attempt("Eating bread", 5,
        lambda success: (1, 0) if success else (-1, 0))
attempt("Fighting ice weasel", 15,
        lambda success: (0, 10) if success else (-10, 10))
