class Element:
    __slots__ = (
        'name',
        'number',
        'symbol',
        '__weakref__',
    )

    def __init__(self, symbol, number, name):
        self.symbol = symbol.title()
        self.number = number
        self.name = name.lower()

    def __repr__(self):
        return f"{self.symbol} ({self.name}): {self.number}"

    def __str__(self):
        return self.symbol

    def __hash__(self):
        return hash(self.symbol)

    def __eq__(self, other):
        return self.symbol == other.symbol

    def __lt__(self, other):
        return self.symbol < other.symbol

    def __le__(self, other):
        return self.symbol <= other.symbol

    def __selfattr__(self, name, value):
        if hasattr(self, name):
            raise AttributeError(
                f"'{type(self)}' object attribute '{name}' is read-only"
            )
        object.__setattr__(self, name, value)

    def __delattr__(self, name):
        raise AttributeError(
            f"'{type(self)}' object attribute '{name}' is read-only"
        )

oxygen = Element('O', 8, 'oxygen')
iron = Element('Fe', 26, 'iron')

print(oxygen)              # prints 'O (Oxygen): 8'
print(f"{iron!r}")         # prints 'Fe (Iron): 26'

iron.atomic_mass = 55.845  # raises AttributeError
iron.symbol = "Ir"         # raises AttributeError
del iron.symbol            # raises AttributeError
