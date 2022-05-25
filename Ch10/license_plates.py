from itertools import product
from string import ascii_uppercase as alphabet

# def license_plates():
#     for num in range(1000):
#         yield f"ABC {num:03}"

# license_plates = (
#     f"ABC {number:03}"
#     for number in range(1000)
# )

license_plates = (
    f'{letters} {number:03}'
    for letters in (
        "".join(chars)
        for chars in product(alphabet, repeat=3)
    )
    if letters != 'GOV'
    for number in range(1000)
)

# for plate in license_plates():
# for plate in license_plates:
#     print(plate)

registrations = {}


def new_registration(owner):
    if owner not in registrations:
        plate = next(license_plates)
        registrations[owner] = plate
        return True
    return False


# Fast-forward through several results for testing purposes.
for _ in range(4441888):
    next(license_plates)

name = "Jason C. McDonald"
my_plate = new_registration(name)
print(registrations[name])
