import json

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


with open('nearby.json', 'w') as jsonfile:
    json.dump(nearby_properties, jsonfile)
