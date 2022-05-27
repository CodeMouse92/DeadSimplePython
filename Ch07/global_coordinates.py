from dis import dis
import math


class GlobalCoordinates:

    def __init__(self, *, latitude, longitude):
        self._lat_deg = latitude[0]
        self._lat_min = latitude[1]
        self._lat_sec = latitude[2]
        self._lat_dir = latitude[3]

        self._lon_deg = longitude[0]
        self._lon_min = longitude[1]
        self._lon_sec = longitude[2]
        self._lon_dir = longitude[3]

    @staticmethod
    def degrees_from_decimal(dec, *, lat):
        if lat:
            direction = "S" if dec < 0 else "N"
        else:
            direction = "W" if dec < 0 else "E"
        dec = abs(dec)
        degrees = int(dec)
        dec -= degrees
        minutes = int(dec * 60)
        dec -= minutes / 60
        seconds = round(dec * 3600, 1)
        return (degrees, minutes, seconds, direction)

    @staticmethod
    def decimal_from_degrees(degrees, minutes, seconds, direction):
        dec = degrees + minutes / 60 + seconds / 3600
        if direction == "S" or direction == "W":
            dec = -dec
        return round(dec, 6)

    @property
    def latitude(self):
        return self.decimal_from_degrees(
            self._lat_deg, self._lat_min, self._lat_sec, self._lat_dir
        )

    @property
    def longitude(self):
        return self.decimal_from_degrees(
            self._lon_deg, self._lon_min, self._lon_sec, self._lon_dir
        )

    def __repr__(self):
        return (
            f"<GlobalCoordinates "
            f"lat={self._lat_deg}°{self._lat_min}'"
            f"{self._lat_sec}\"{self._lat_dir} "
            f"lon={self._lon_deg}°{self._lon_min}'"
            f"{self._lon_sec}\"{self._lon_dir}>"
        )

    def __str__(self):
        return (
            f"{self._lat_deg}°{self._lat_min}'"
            f"{self._lat_sec}\"{self._lat_dir} "
            f"{self._lon_deg}°{self._lon_min}'"
            f"{self._lon_sec}\"{self._lon_dir}>"
        )

    def __hash__(self):
        return hash((
            self._lat_deg, self._lat_min, self._lat_sec, self._lat_dir,
            self._lon_deg, self._lon_min, self._lon_sec, self._lon_dir
        ))

    def __eq__(self, other):
        if not isinstance(other, GlobalCoordinates):
            return NotImplemented

        return (
            self._lat_deg == other._lat_deg
            and self._lat_min == other._lat_min
            and self._lat_sec == other._lat_sec
            and self._lat_dir == other._lat_dir
            and self._lon_deg == other._lon_deg
            and self._lon_min == other._lon_min
            and self._lon_sec == other._lon_sec
            and self._lon_dir == other._lon_dir
        )

    def __sub__(self, other):
        if not isinstance(other, GlobalCoordinates):
            return NotImplemented

        lat_diff = self.latitude - other.latitude
        lon_diff = self.longitude - other.longitude
        return (lat_diff, lon_diff)

    def __invert__(self):
        return GlobalCoordinates(
            latitude=self.degrees_from_decimal(-self.latitude, lat=True),
            longitude=self.degrees_from_decimal(-self.longitude, lat=False)
        )

    def __call__(self, other):
        EARTH_RADIUS_KM = 6371

        distance_lat = math.radians(other.latitude - self.latitude)
        distance_lon = math.radians(other.longitude - self.longitude)
        lat = math.radians(self.latitude)
        lon = math.radians(self.longitude)
        a = (
            math.sin(distance_lat / 2)
            * math.sin(distance_lat / 2)
            + math.sin(distance_lon)
            * math.sin(distance_lon / 2)
            * math.cos(lat)
            * math.cos(lon)
        )
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

        return c * EARTH_RADIUS_KM
