# divis_by_three = (n for n in range(100) if n % 3 == 0)
divis_by_three = (n if n % 3 == 0 else "redacted" for n in range(100))
