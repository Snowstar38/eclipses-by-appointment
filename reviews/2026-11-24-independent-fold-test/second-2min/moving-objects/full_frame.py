"""Remeasure the brightest moving source in a wider MAST cutout at three epochs."""
import csv
from io import BytesIO
from pathlib import Path
from zipfile import ZipFile

from astropy.io import fits
from astropy.time import Time
from astropy.wcs import WCS
import numpy as np
import requests
from scipy.optimize import least_squares

here = Path(__file__).resolve().parent
observations = list(csv.DictReader((here / "observed.csv").read_text().splitlines()))
fields = [("113655666", 24.8756, 20.4233, 43), ("356752132", 61.2126, 9.6046, 42)]
rows = []
for tic, ra, dec, sector in fields:
    r = requests.get("https://mast.stsci.edu/tesscut/api/v0.1/astrocut",
                     params=dict(ra=ra, dec=dec, x=35, y=35, sector=sector), timeout=120)
    r.raise_for_status()
    with ZipFile(BytesIO(r.content)) as z:
        filename, = [name for name in z.namelist() if name.endswith(".fits")]
        content = z.read(filename)
    with fits.open(BytesIO(content)) as h:
        assert h[0].header["SECTOR"] == sector
        d = h[1].data
        wcs = WCS(h[2].header)
        group = [row for row in observations if row["tic"] == tic]
        middle = float(group[2]["jd_utc"])
        jd = d["TIME"] - d["TIMECORR"] + h[1].header["BJDREFI"] + h[1].header["BJDREFF"]
        good = np.flatnonzero((d["QUALITY"] == 0) & np.isfinite(jd))
        utc = Time(jd[good], format="jd", scale="tdb").utc
        away = abs(utc.jd - middle)
        baseline = np.nanmedian(d["FLUX"][good[(away > .3) & (away < .7)]], axis=0)
        for row in group[::2]:
            j = np.argmin(abs(utc.jd - float(row["jd_utc"])))
            index = good[j]
            image = d["FLUX"][index] - baseline
            x, y = wcs.world_to_pixel_values(float(row["ra_deg"]), float(row["dec_deg"]))
            x0, y0 = int(np.rint(x)) - 3, int(np.rint(y)) - 3
            patch = image[y0:y0+7, x0:x0+7]
            yy, xx = np.indices(patch.shape)
            py, px = np.unravel_index(np.nanargmax(patch), patch.shape)

            def residual(v):
                amplitude, cx, cy, width, floor = v
                model = amplitude * np.exp(-((xx-cx)**2 + (yy-cy)**2)/(2*width**2)) + floor
                return np.nan_to_num(model - patch).ravel()

            fit = least_squares(residual, [float(patch[py,px]), px, py, .7, 0],
                                bounds=([0,-1,-1,.3,-np.inf],[np.inf,7,7,3,np.inf]))
            measured_ra, measured_dec = wcs.pixel_to_world_values(x0+fit.x[1], y0+fit.x[2])
            rows.append(dict(tic=tic, offset_h=row["offset_hours"], utc=utc[j].isot,
                             ra_deg=float(measured_ra), dec_deg=float(measured_dec),
                             x=x0+fit.x[1], y=y0+fit.x[2], ffi_filename=d["FFI_FILE"][index]))
with (here / "positions.csv").open("w", encoding="utf8", newline="") as f:
    writer = csv.DictWriter(f, rows[0], lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
