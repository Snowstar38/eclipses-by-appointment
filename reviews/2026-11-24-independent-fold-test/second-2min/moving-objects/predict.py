"""Compare measured peak pixels to astrometric ICRF ephemerides as seen from TESS."""
import csv
import io
from pathlib import Path

import requests
from astropy import units as u
from astropy.coordinates import SkyCoord
from astropy.time import Time

here = Path(__file__).resolve().parent
observed = list(csv.DictReader((here / "observed.csv").read_text().splitlines()))
for row in observed:
    row["method"] = "brightest target-stamp pixel"
wide = list(csv.DictReader((here / "positions.csv").read_text().splitlines()))
for row in wide:
    row["jd_utc"] = str(Time(row["utc"], scale="utc").jd)
    row["method"] = "full-frame centroid"
observed.extend(wide)
matches = []
for tic, number, name in [("113655666", 25, "Phocaea"), ("356752132", 521, "Brixia")]:
    group = [row for row in observed if row["tic"] == tic]
    epochs = sorted({round(float(row["jd_utc"]), 8) for row in group})
    params = dict(format="json", COMMAND=f"'{number};'", CENTER="'500@-95'",
                  EPHEM_TYPE="OBSERVER", QUANTITIES="'1,3,9'", CSV_FORMAT="YES",
                  ANG_FORMAT="DEG", EXTRA_PREC="YES", CAL_FORMAT="BOTH", TIME_TYPE="UT",
                  TLIST="'"+",".join(map(str, epochs))+"'")
    resp = requests.get("https://ssd.jpl.nasa.gov/api/horizons.api", params=params, timeout=50)
    resp.raise_for_status()
    result = resp.json()["result"]
    if "$$SOE" not in result:
        raise ValueError(result[:1500])
    assert name in result and "TESS" in result
    text = result.split("$$SOE")[1].split("$$EOE")[0].strip()
    header = next(line for line in result.splitlines() if "Date__(UT)" in line and "R.A." in line)
    keys = [s.strip() for s in header.split(",")]
    (here / f"horizons-{number}.txt").write_bytes(result.encode())
    eph = [[s.strip() for s in row] for row in csv.reader(io.StringIO(text))]
    ra_idx = next(i for i,k in enumerate(keys) if k.startswith("R.A."))
    dec_idx = next(i for i,k in enumerate(keys) if k.startswith("DEC"))
    for row in group:
        values = min(eph, key=lambda v: abs(float(v[1])-float(row["jd_utc"])))
        ra, dec = float(values[ra_idx]), float(values[dec_idx])
        assert abs(float(values[1])-float(row["jd_utc"])) < 1e-6
        peak = SkyCoord(float(row["ra_deg"])*u.deg, float(row["dec_deg"])*u.deg)
        pred = SkyCoord(ra*u.deg, dec*u.deg)
        matches.append(dict(tic=tic, asteroid=f"({number}) {name}", utc=row["utc"], method=row["method"],
                            measured_ra_deg=peak.ra.deg, measured_dec_deg=peak.dec.deg,
                            predicted_ra_deg=ra, predicted_dec_deg=dec,
                            separation_arcsec=round(peak.separation(pred).arcsec, 2)))
    print(tic, name, [r["separation_arcsec"] for r in matches if r["tic"]==tic])
with (here / "matches.csv").open("w", newline="", encoding="utf8") as f:
    writer = csv.DictWriter(f, matches[0], lineterminator="\n")
    writer.writeheader()
    writer.writerows(matches)
