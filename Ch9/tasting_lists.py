from itertools import product

samples = ['Costa Rica', 'Kenya', 'Vietnam', 'Brazil']
guests = ['Denis', 'William', 'Todd', 'Daniel', 'Glen']

# for sample in samples:
#     for guest in guests:
#         print(f"Give sample of {sample} coffee to {guest}.")

for sample, guest in product(samples, guests):
    print(f"Give sample of {sample} coffee to {guest}.")
