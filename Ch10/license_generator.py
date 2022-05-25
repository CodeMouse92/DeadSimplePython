from itertools import product
from string import ascii_uppercase as alphabet


def gen_license_plates():
    for letters in product(alphabet, repeat=3):
        letters = "".join(letters)
        if letters == 'GOV':
            continue

        for numbers in range(1000):
            yield f'{letters} {numbers:03}'


license_plates = gen_license_plates()

# for plate in license_plates:
#     print(plate)

registrations = {}


def new_registration(owner):
    if owner not in registrations:
        plate = next(license_plates)
        registrations[owner] = plate
        return plate
    return None


# Fast-forward through several results for testing purposes.
for _ in range(4441888):
    next(license_plates)

name = "Jason C. McDonald"
my_plate = new_registration(name)
print(my_plate)
print(registrations[name])
