def average(number_string):
    total = 0
    skip = 0
    values = 0
    for n in number_string.split():
        values += 1
        try:
            total += float(n)
        except ValueError:
            skip += 1
    if skip == values:
        raise ValueError("No valid numbers provided.")
    elif skip:
        print(f"<!> Skipped {skip} invalid values.")

    return total / values


while True:
    try:
        line = input("Enter numbers (space delimiated):\n    ")
        avg = average(line)
        print(avg)
    except ValueError:
        print("No valid numbers provided.")
