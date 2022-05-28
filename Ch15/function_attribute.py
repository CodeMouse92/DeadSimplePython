def multiplier(n):
    if not hasattr(multiplier, 'factor'):
        multiplier.factor = 0
    print(n * multiplier.factor)


multiplier(2)               # prints 0
print(multiplier.__dict__)  # prints {}
multiplier.factor = 3
print(multiplier.__dict__)  # prints {'factor': 3}
multiplier(2)               # prints 6
