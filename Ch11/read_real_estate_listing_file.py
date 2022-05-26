real_estate_listing = open("213AnywhereAve.txt")
real_estate_listing.__enter__()
try:
    print(real_estate_listing.read())
finally:
    real_estate_listing.__exit__()

# with open("213AnywhereAve.txt") as real_estate_listing:
#     print(real_estate_listing.read())
