"""TLEs: fetch from CelesTrak, decode by hand, propagate with SGP4.

Planned (Week 4, Mon-Tue):
    fetch_tle(norad_id)        -> latest TLE lines from the CelesTrak API
    decode_tle(line1, line2)   -> epoch, i, RAAN, e, argp, mean anomaly, mean motion, BSTAR
    sgp4_states(tle, times)    -> TEME position and velocity at each time
"""
