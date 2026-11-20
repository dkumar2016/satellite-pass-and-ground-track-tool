# satellite-pass-and-ground-track-tool

[![tests](https://github.com/dkumar2016/satellite-pass-and-ground-track-tool/actions/workflows/tests.yml/badge.svg)](https://github.com/dkumar2016/satellite-pass-and-ground-track-tool/actions/workflows/tests.yml)

Satellite pass prediction, ground tracks and eclipse detection from real TLEs: when a satellite is visible from a ground station, where it is over the Earth, and when it is in Earth's shadow. Results are validated against Skyfield.

> **Status: in progress.** Week 4 of a 12-week flight dynamics and operations plan (Nov 23–27, 2026). The structure, input data and setup checks are in place; the analysis code and results arrive during the week. Nothing below is a result yet.

## What it will do

| Question an operator asks | What this tool will produce |
| --- | --- |
| When can my ground station talk to the satellite? | Every pass above a 10° elevation mask: AOS, TCA, LOS, maximum elevation |
| Where is the satellite over the Earth? | Sub-satellite latitude and longitude (ground track) |
| When is the satellite in Earth's shadow? | Eclipse entry and exit times and duration per orbit, cylindrical and conical (umbra / penumbra) models |
| How does eclipse change over the year? | Eclipse duration against beta angle, including why dawn-dusk sun-synchronous orbits barely see eclipses |
| What does eclipse do to the power system? | A simple battery state-of-charge model through each eclipse |
| How does SGP4 compare with numerical propagation? | Position difference over a day between SGP4 and [numerical-orbit-propagator](https://github.com/dkumar2016/numerical-orbit-propagator) from the same starting state |

## Planned case study

Three satellites over three ground stations for 72 hours, using the latest TLEs from CelesTrak.

| Satellite | NORAD ID | Why |
| --- | --- | --- |
| ISS (ZARYA) | 25544 | 51.6° inclination, low LEO |
| AQUA | 27424 | Sun-synchronous, polar |
| IRIDIUM 176 | 43923 | 86.6° inclination, constellation member |

| Station | Latitude | Longitude |
| --- | --- | --- |
| San Francisco | 37.77° N | 122.42° W |
| Azores (Ponta Delgada) | 37.74° N | 25.68° W |
| Punta Arenas | 53.16° S | 70.92° W |

Station altitudes are taken as sea level for now.

## How it will be validated

- Every pass above 10° listed in time order, with times cross-checked against Skyfield.
- Ground tracks that look physical: the ISS stays within ±51.6° latitude.
- Eclipse entry and exit times compared with Skyfield's `is_sunlit()`, with the timing difference reported in seconds and a stated tolerance.
- A hand-decoded TLE that matches what `sgp4` reads from the same lines.

## Roadmap

- [x] Repo structure, input data (satellites and stations), constants, setup tests and CI
- [ ] TLE decoding by hand and with `sgp4`; fetching the latest TLE from CelesTrak
- [ ] SGP4 vs numerical propagation over one day
- [ ] Time scales and frames: UTC / TT / UT1, TEME → ECEF → latitude, longitude, altitude
- [ ] Sun position and beta angle
- [ ] Ground tracks and pass prediction (AOS / TCA / LOS) with a Skyfield cross-check
- [ ] Eclipse detection: cylindrical, then conical; cross-check with Skyfield
- [ ] 72-hour multi-station pass table and ground-track figures
- [ ] Eclipse duration over a year vs beta angle; battery state of charge through eclipse
- [ ] Results, figures and validation numbers in this README

## Structure

    passtool/
        constants.py   μ, Earth radius and flattening, Earth rotation, Sun constants, 10° mask, paths
        sites.py       read the stations and satellites (in place)
        tle.py         fetch, decode and propagate TLEs with SGP4 (planned)
        frames.py      time scales; TEME → ECEF → geodetic; azimuth / elevation from a station (planned)
        sun.py         Sun position and beta angle (planned)
        passes.py      ground tracks; AOS / TCA / LOS (planned)
        eclipse.py     cylindrical and conical shadow models; eclipse intervals (planned)
        battery.py     battery state of charge through eclipse (planned)
    data/              satellites.csv (name, NORAD ID), stations.csv (lat, lon, alt)
    examples/          scripts that produce the pass table, ground tracks and eclipse analysis
    validation/        cross-checks against Skyfield
    tests/             pytest checks (setup checks now, physics tests as code lands)
    figures/, output/  results

## Install and run

    python -m pip install -r requirements.txt
    python -m pytest -v

## Conventions

Units are in variable names (`_km`, `_s`, `_deg`). Times are UTC unless stated. SGP4 states are in TEME; ground tracks and station geometry use ECEF on the WGS-84 ellipsoid.

## Related repos

- [numerical-orbit-propagator](https://github.com/dkumar2016/numerical-orbit-propagator): numerical propagation with plug-in forces (two-body, J2), used for the SGP4 comparison
- [orbit-state-vector-toolkit](https://github.com/dkumar2016/orbit-state-vector-toolkit): orbital elements ↔ state vectors, Kepler's equation
