def calculate_age(birth_year, current_year):
    return (current_year - birth_year)


def calculate_third_age_year(current_age, current_year):
    return int(current_year - (current_age / 3))


birth_year = "1985"    # get from user, assume data validation
birth_year = int(birth_year)

current_year = "2010"  # get from system
current_year = int(current_year)

current_age = calculate_age(birth_year, current_year)
third_age_year = calculate_third_age_year(current_age, current_year)
print(third_age_year)
