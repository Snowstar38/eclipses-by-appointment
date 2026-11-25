"""Projected dynamical quantities implied by the published Gaia SB2 elements."""
import csv
import json
import math
from pathlib import Path

from astropy import constants as const
from astropy import units as u

HERE = Path(__file__).resolve().parent
with (HERE.parent / "gaia/gaia_nss.csv").open(encoding="utf-8-sig") as stream:
    row = next(csv.DictReader(stream))
period = float(row["period"]) * u.day
e = float(row["eccentricity"])
k1 = float(row["semi_amplitude_primary"]) * u.km / u.s
k2 = float(row["semi_amplitude_secondary"]) * u.km / u.s
omega = math.radians(float(row["arg_periastron"]))
projection = math.sqrt(1 - e**2)
a_sini = (period * (k1 + k2) * projection / (2 * math.pi)).to(u.R_sun)
total_min = (4 * math.pi**2 * a_sini**3 / (const.G * period**2)).to_value(u.M_sun)
m1_min = total_min * (k2 / (k1 + k2)).value
m2_min = total_min - m1_min
result = dict(
    interpretation="Conditional on the published orbit and association of its component velocities.",
    m1_sin3i_solar=m1_min, m2_sin3i_solar=m2_min, m2_over_m1=(k1/k2).value,
    a_sini_solar_radii=a_sini.value,
    example_i_degrees_for_m1_equal_to_one_solar_mass=math.degrees(math.asin(m1_min**(1/3))),
    max_line_separation_kms=(k1 + k2).value * (1 + abs(e * math.cos(omega))),
)
assert math.isclose(m2_min/m1_min, result["m2_over_m1"])
(HERE / "dynamics.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf8")
