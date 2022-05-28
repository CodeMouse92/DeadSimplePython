class Element:
    __slots__ = (
        'name',
        'number',
        'symbol',
        'family',
        'iupac_num',
        '__dict__',
        '__weakref__'
    )

    def __init__(self, symbol, number, name, family, numeration):
        self.symbol = symbol.title()
        self.number = number
        self.name = name.lower()
        self.family = family.lower()
        self.iupac_num = numeration

    def __str__(self):
        return f"{self.symbol} ({self.name}): {self.number}"


oxygen = Element('O', 8, 'oxygen', 'non-metals', 16)
iron = Element('Fe', 26, 'iron', 'transition metal', 8)

print(oxygen)  # prints 'O (Oxygen): 8'
print(iron)    # prints 'Fe (Iron): 26'

iron.atomic_mass = 55.845
