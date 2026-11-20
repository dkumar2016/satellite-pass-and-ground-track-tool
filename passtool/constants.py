"""Physical constants, defaults and project paths. Units are in the names: km, s, deg."""
from pathlib import Path

# Earth (WGS-84)
MU_KM3_S2 = 398600.4418                  # Earth's gravitational parameter
R_EARTH_KM = 6378.137                    # equatorial radius
FLATTENING = 1 / 298.257223563           # WGS-84 flattening
OMEGA_EARTH_RAD_S = 7.2921150e-5         # Earth's rotation rate

# Sun (for eclipse detection)
AU_KM = 149_597_870.7                    # astronomical unit
R_SUN_KM = 695_700.0                     # nominal solar radius

# Pass prediction defaults
ELEVATION_MASK_DEG = 10.0                # a pass counts only above this elevation
DAY_S = 86400.0

# Paths
REPO_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = REPO_DIR / "data"
OUTPUT_DIR = REPO_DIR / "output"
FIGURES_DIR = REPO_DIR / "figures"
