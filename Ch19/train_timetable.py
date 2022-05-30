from datetime import time


def get_timetable(train):
    # Pretend this gets data from a server.
    return [
        {"station": "target_field", "arrives": time(hour=16, minute=27)},
        {"station": "fridley", "arrives": time(hour=16, minute=41)},
        {"station": "coon_rapids_fridley", "arrives": time(hour=16, minute=50)},
        {"station": "anoka", "arrives": time(hour=16, minute=54)},
        {"station": "ramsey", "arrives": time(hour=16, minute=59)},
        {"station": "elk_river", "arrives": time(hour=17, minute=4)},
        {"station": "big_lake", "arrives": time(hour=17, minute=17)},
    ]


def next_station(now, timetable):
    """Return the name of the next station."""
    station = None
    for stop in timetable:
        if stop['arrives'] > now:
            station = stop
            break
    station['station'] = station['station'].replace('_', ' ').title()
    return station


def arrives_at(station, timetable):
    for stop in timetable:
        if station == stop['station']:
            return stop


timetable = get_timetable('nstar_northbound')

station = next_station(time(hour=16, minute=43), timetable)
print(f"Next station is {station['station']}.")

stop = arrives_at('coon_rapids_fridley', timetable)
print(f"Arrives at {stop['arrives']}.")
