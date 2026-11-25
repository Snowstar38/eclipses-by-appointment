"""Measure brightest excess pixels at fixed time offsets, with UTC spacecraft times."""
import csv
import hashlib
import io
import json
from pathlib import Path

import numpy as np
import requests
from astropy.io import fits
from astropy.time import Time
from astropy.wcs import WCS

here = Path(__file__).resolve().parent
rows = []
for tic in ["113655666", "356752132"]:
    folder = here.parent / f"single-{tic}"
    if tic == "113655666":
        record = json.loads((folder / "receipt.json").read_bytes())
        center, shoulders = record["t0_btjd"], record["baseline_offsets_d"]
    else:
        prior = json.loads((folder / "evidence.json").read_bytes())
        record = prior["files"]["target-tpf.fits"]
        center, shoulders = prior["measurement_center_btjd"], prior["shoulder_abs_limits_d"]
    file = folder / "target-tpf.fits"
    if file.exists():
        content = file.read_bytes()
    else:
        response = requests.get(record["url"], timeout=45)
        response.raise_for_status()
        content = response.content
    assert hashlib.sha256(content).hexdigest() == record["sha256"]
    with fits.open(io.BytesIO(content)) as h:
        d = h[1].data
        t = d["TIME"]
        good = (d["QUALITY"] == 0) & np.isfinite(t)
        delta = abs(t - center)
        baseline = good & (delta > shoulders[0]) & (delta < shoulders[1])
        pixels = d["FLUX"] + d["FLUX_BKG"]
        quiet = np.nanmedian(pixels[baseline], axis=0)
        wcs = WCS(h[2].header)
        for hour in [-1, -.5, 0, .5, 1]:
            mask = good & (abs(24*(t - center) - hour) <= .07)
            excess = np.nanmedian(pixels[mask], axis=0) - quiet
            y, x = np.unravel_index(np.nanargmax(excess), excess.shape)
            ra, dec = wcs.pixel_to_world_values(x, y)
            jd = np.median(t[mask] - d["TIMECORR"][mask]) + h[1].header["BJDREFI"] + h[1].header["BJDREFF"]
            utc = Time(jd, format="jd", scale="tdb").utc
            rows.append(dict(tic=tic, offset_hours=hour, utc=utc.isot, jd_utc=utc.jd,
                             peak_x=x, peak_y=y, ra_deg=float(ra), dec_deg=float(dec),
                             excess_e_per_s=float(excess[y,x])))
with (here / "observed.csv").open("w", newline="", encoding="utf8") as f:
    writer = csv.DictWriter(f, rows[0], lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
