import math

import math


def average_string(number_string):
    try:
        numbers = [float(n) for n in number_string.split()]
    except ValueError:
        total = math.nan
        values = 1
    else:
        total = sum(numbers)
        values = len(numbers)

    try:
        average = total / values
    except ZeroDivisionError:
        average = math.inf

    return average

while True:
    number_string = input("Enter space-delimited list of numbers:\n    ")
    print(average_string(number_string))
