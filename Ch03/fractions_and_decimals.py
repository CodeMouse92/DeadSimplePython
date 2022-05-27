from decimal import Decimal
from fractions import Fraction

third_fraction = Fraction(1, 3)
third_fixed = Decimal("0.333")
third_float = 1 / 3

print(third_fraction)  # 1/3
print(third_fixed)     # 0.333
print(third_float)     # 0.3333333333333333

third_float = float(third_fraction)
print(third_float)     # 0.3333333333333333

third_float = float(third_fixed)
print(third_float)     # 0.333
