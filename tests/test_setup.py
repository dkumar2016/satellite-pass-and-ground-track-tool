"""Checks on the project's constants and input data (the physics tests arrive with the code)."""
import math

import pytest

from passtool.constants import (ELEVATION_MASK_DEG, FLATTENING, MU_KM3_S2,
                                OMEGA_EARTH_RAD_S, R_EARTH_KM)
from passtool.sites import read_satellites, read_stations


def test_earth_constants_are_wgs84():
    assert MU_KM3_S2 == pytest.approx(398600.4418)
    assert R_EARTH_KM == pytest.approx(6378.137)
    assert 1 / FLATTENING == pytest.approx(298.257223563)


def test_earth_rotation_is_one_sidereal_day():
    sidereal_day_s = 2 * math.pi / OMEGA_EARTH_RAD_S
    assert sidereal_day_s == pytest.approx(86164.1, abs=0.1)


def test_elevation_mask_is_ten_degrees():
    assert ELEVATION_MASK_DEG == 10.0


def test_three_stations_with_valid_coordinates():
    stations = read_stations()
    assert [s["name"] for s in stations] == [
        "san_francisco", "azores_ponta_delgada", "punta_arenas"]
    for s in stations:
        assert -90 <= s["lat_deg"] <= 90 and -180 <= s["lon_deg"] <= 180


def test_three_satellites_with_unique_norad_ids():
    sats = read_satellites()
    ids = [s["norad_id"] for s in sats]
    assert ids == [25544, 27424, 43923]
    assert len(set(ids)) == len(ids)


def test_bad_latitude_is_rejected(tmp_path):
    bad = tmp_path / "stations.csv"
    bad.write_text("name,lat_deg,lon_deg,alt_m\nnowhere,95.0,0.0,0.0\n")
    with pytest.raises(ValueError, match="latitude"):
        read_stations(bad)
