from multiprocessing.sharedctypes import Value


class AverageCalculator:

    def __init__(self):
        self.total = 0
        self.count = 0

    def __call__(self, *values):
        if values:
            for value in values:
                self.total +=  float(value)
                self.count += 1
        return self.total / self.count


average = AverageCalculator()
values = input("Enter scores, separated by spaces:\n    ").split()
try:
    print(f"Aviage is {average(*values)}")
except ZeroDivisionError:
    print("ERROR: No values provided.")
except (ValueError, UnicodeError):
    print("ERROR: All inputs should be numeric.")
