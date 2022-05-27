class CoffeeOrder:

    def __init__(self, recipe, to_go=False):
        self.recipe = recipe
        self.to_go = to_go

    def brew(self):
        vessel = "in a paper cup" if self.to_go else "in a mug"
        print("Brewing", *self.recipe.parts, vessel)


class CoffeeRecipe:

    def __init__(self, parts):
        self.parts = parts


special = CoffeeRecipe(["double-shot", "grande", "no-whip", "mocha"])
order = CoffeeOrder(special, to_go=False)
order.brew()  # prints "Brewing double-shot grande no-whip mocha in a mug"


import functools
def auto_order(to_go):
    def decorator(cls):
        @functools.wraps(cls)
        def wrapper(*args, **kwargs):
            recipe = cls(*args, **kwargs)
            return (CoffeeOrder(recipe, to_go), recipe)
        return wrapper
    return decorator


@auto_order(to_go=True)
class CoffeeShackRecipe(CoffeeRecipe):
    pass


order, recipe = CoffeeShackRecipe(["tall", "decaf", "cappuccino"])
order.brew()  # prints "Brewing tall decaf cappuccino in a paper cup"
