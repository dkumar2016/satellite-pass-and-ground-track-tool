"""Read the ground stations and satellites this project works with."""
import csv

from passtool.constants import DATA_DIR

STATION_FIELDS = ("name", "lat_deg", "lon_deg", "alt_m")


def read_stations(path=DATA_DIR / "stations.csv"):
    """Return a list of stations as dicts with numeric lat_deg, lon_deg, alt_m."""
    stations = []
    with open(path, newline="") as f:
        for row in csv.DictReader(f):
            station = {"name": row["name"]}
            for field in STATION_FIELDS[1:]:
                station[field] = float(row[field])
            if not -90.0 <= station["lat_deg"] <= 90.0:
                raise ValueError(f"{station['name']}: latitude out of range")
            if not -180.0 <= station["lon_deg"] <= 180.0:
                raise ValueError(f"{station['name']}: longitude out of range")
            stations.append(station)
    return stations


def read_satellites(path=DATA_DIR / "satellites.csv"):
    """Return a list of satellites as dicts with name and integer norad_id."""
    with open(path, newline="") as f:
        return [{"name": row["name"], "norad_id": int(row["norad_id"])}
                for row in csv.DictReader(f)]
