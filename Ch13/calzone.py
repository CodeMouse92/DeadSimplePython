class Food:
    def __str__(self):
        return "Yum, what is it?"


class Pizza(Food):
    def __str__(self):
        return "Piiiizzaaaaaa"


class Sandwich(Food):
    def __str__(self):
        return "Mmm, sammich."


class Calzone(Pizza, Sandwich):
    pass


calzone = Calzone()
print(calzone)  # what gets printed??


# class PizzaSandwich(Sandwich, Pizza):
class PizzaSandwich(Pizza, Sandwich):
    pass


class CalzonePizzaSandwich(Calzone, PizzaSandwich):
    def __str__(self):
        return Calzone.__str__(self)
