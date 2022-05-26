nearby_properties = {
    "N. Anywhere Ave.":
    {
        123: 156_852,
        124: 157_923,
        126: 163_812,
        127: 144_121,
        128: 166_356,
    },
    "N. Everywhere St.":
    {
        4567: 175_753,
        4568: 166_212,
        4569: 185_123,
    }
}

for street, properties in nearby_properties.items():
    for address, value in properties.items():
        # print(f"{street}\t{address}\t${value:,}")
        print(street, address, f"${value:,}", sep='\t')
