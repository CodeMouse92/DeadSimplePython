THICKNESS = 0.125  # must be a positive number
assert THICKNESS > 0, "Vinyl must have a positive thickness!"


def fit_records(width, shelves):
    records_per_shelf = width / THICKNESS
    records = records_per_shelf * shelves
    return int(records)


def get_number(prompt):
    while True:
        value = input(prompt)
        try:
            value = int(value)
        except ValueError:
            print("You must enter a whole number.")
            continue

        if value <= 0:
            print("You must enter a positive number.")
            continue

        return value


def main():
    width = get_number("What is the bookcase shelf width (in inches)? ")
    print("How many shelves are...")
    shelves_lp = get_number("    12+ inches high? ")
    shelves_78 = get_number("    10-11.5 inches high? ")
    shelves_single = get_number("    7-9.5 inches high? ")

    records_lp = fit_records(width, shelves_lp)
    records_single = fit_records(width, shelves_single)
    records_78 = fit_records(width, shelves_78)

    print(f"You can fit {records_lp}, "
          f"{records_single} singles, and "
          f"{records_78} 78s.")


if __name__ == "__main__":
    main()
