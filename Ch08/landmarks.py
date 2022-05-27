from cgitb import lookup


cities = {
    "SEATTLE": "WASHINGTON, USA",
    "PORTLAND": "OREGON, USA",
    "BOSTON": "MASSACHUSETTS, USA",
}

landmarks = {
    "SPACE NEEDLE": "SEATTLE",
    "LIBERTY SHIP MEMORIAL": "PORTLAND",
    "ALAMO": "SAN ANTONIO",
}


def lookup_landmark(landmark):
    landmark = landmark.upper()
    try:
        city = landmarks[landmark]
        state = cities[city]
    except KeyError as e:
        raise KeyError("Landmark not found.") from e
    print(f"{landmark} is in {city}, {state}")


lookup_landmark("space needle")
lookup_landmark("alamo")
lookup_landmark("golden gate bridge")
