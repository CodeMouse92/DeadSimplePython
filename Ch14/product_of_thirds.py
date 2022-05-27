from collections.abc import Sequence
from numbers import Complex


def product_of_thirds(sequence):
    if not isinstance(sequence, Sequence):
        raise ValueError("Argument must be a sequence.")
    if not isinstance(sequence[0], Complex):
        raise TypeError("Sequence elements must support multiplication.")

    r = sequence[0]
    for i in sequence[1::3]:
        r *= i
    return r


print(product_of_thirds(range(1, 50)))  # prints '262134882788466688000'
print(product_of_thirds("Foobarbaz"))   # raises TypeError
