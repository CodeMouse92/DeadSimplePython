from functools import singledispatchmethod


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

    @singledispatchmethod
    def __eq__(self, other):
        return self.symbol == other.symbol

    @__eq__.register
    def _(self, other: str):
        return self.symbol == other

    @__eq__.register
    def _(self, other: float):
        return self.number == other
    
    @__eq__.register
    def _(self, other: int):
        return self.number == other

    @singledispatchmethod
    def __lt__(self, other):
        return self.symbol < other.symbol

    @__lt__.register(str)
    def _(self, other):
        return self.symbol < other

    @__lt__.register(int)
    @__lt__.register(float)
    def _(self, other):
        return self.number < other

    @singledispatchmethod
    def __le__(self, other):
        return self.symbol <= other.symbol

    __le__.register(str, lambda self, other: self.symbol <= other)

    __le__.register(int, lambda self, other: self.number <= other)
    __le__.register(float, lambda self, other: self.number <= other)

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


class Compound:

    def __init__(self, name):
        self.name = name.title()
        self.components = {}

    def add_element(self, element, count):
        try:
            self.components[element] += count
        except KeyError:
            self.components[element] = count

    def __str__(self):
        s = ""
        formula = self.components.copy()
        # Hill system
        if 'C' in formula.keys():
            s += f"C{formula['C']}"
            del formula['C']
            if 'H' in formula.keys():
                s += f"H{formula['H']}"
                del formula['H']
        for element, count in sorted(formula.items()):
            s += f"{element.symbol}{count if count > 1 else ''}"
        # substitute subscript digits for normal digits
        s = s.translate(str.maketrans("0123456789","₀₁₂₃₄₅₆₇₈₉"))
        return s

    def __repr__(self):
        return f"{self.name}: {self}"


hydrogen = Element('H', 1, 'hydrogen')
carbon = Element('C', 6, 'carbon')
oxygen = Element('O', 8, 'oxygen')
iron = Element('Fe', 26, 'iron')

rust = Compound("iron oxide")
rust.add_element(oxygen, count=3)
rust.add_element(iron, count=2)
print(f"{rust!r}")    # prints 'Iron Oxide: Fe₂O₃'

aspirin = Compound("acetylsalicylic acid")
aspirin.add_element(hydrogen, 8)
aspirin.add_element(oxygen, 4)
aspirin.add_element(carbon, 9)
print(f"{aspirin!r}")  # prints 'Acetylsalicylic Acid: C₉H₈O₄'

water = Compound("water")
water.add_element(hydrogen, 2)
water.add_element(oxygen, 1)
print(f"{water!r}")    # prints 'Water: H₂O'
