# def fibonacci_next(series=[1, 1]):
def fibonacci_next(series=None):
    if series is None:
        series = [1, 1]
    series.append(series[-1] + series[-2])
    return series


fib1 = fibonacci_next()
print(fib1)  # prints [1, 1, 2]
fib1 = fibonacci_next(fib1)
print(fib1)  # prints [1, 1, 2, 3]

fib2 = fibonacci_next()
print(fib2)  # should be [1, 1, 2] riiiiight?
