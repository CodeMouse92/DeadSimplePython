class Food:
    def __init__(self, name):
        self.name = name


class Pizza(Food):
    def __init__(self, toppings, name="Pizza", **kwargs):
        super().__init__(name=name, **kwargs)
        self.toppings = toppings


class Sandwich(Food):
    def __init__(self, bread, fillings, name="Sandwich", **kwargs):
        super().__init__(name=name, **kwargs)
        self.bread = bread
        self.fillings = fillings


class Calzone(Pizza, Sandwich):
    def __init__(self, toppings):
        super().__init__(
            toppings=toppings,
            bread='pizza crust',
            fillings=toppings,
            name='Calzone'
        )


# The usage...
pizza = Pizza(toppings="pepperoni")
sandwich = Sandwich(bread="rye", fillings="swiss")
calzone = Calzone("sausage")
