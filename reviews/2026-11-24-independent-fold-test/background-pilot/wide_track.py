"""Measure the new sky-seeded track in a wider sector 108 image, before orbit matching."""
import argparse
import csv
from io import BytesIO
from pathlib import Path
from zipfile import ZipFile

from astropy.io import fits
from astropy.time import Time
from astropy.wcs import WCS
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import requests
from scipy.optimize import least_squares

HERE = Path(__file__).resolve().parent
CENTER = 4312.172652
QUERY = dict(ra=25.8484570867833, dec=-1.83298325057801, x=35, y=35, sector=108)


def centroid(image):
    py, px = np.unravel_index(np.nanargmax(image), image.shape)
    assert 3 <= px < image.shape[1]-3 and 3 <= py < image.shape[0]-3
    patch = image[py-3:py+4, px-3:px+4]
    yy, xx = np.indices(patch.shape)

    def residual(v):
        a, x, y, width, floor = v
        model = a*np.exp(-((xx-x)**2+(yy-y)**2)/(2*width**2)) + floor
        return (model-patch)[np.isfinite(patch)]

    fit = least_squares(residual, [float(image[py,px]), 3, 3, .8, 0],
                        bounds=([0,1,1,.3,-np.inf],[np.inf,5,5,3,np.inf]))
    return px-3+fit.x[1], py-3+fit.x[2], fit.x[0]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("cache", type=Path)
    args = parser.parse_args()
    args.cache.mkdir(parents=True, exist_ok=True)
    path = args.cache / "wide-630314437.fits"
    if not path.exists():
        r = requests.get("https://mast.stsci.edu/tesscut/api/v0.1/astrocut", params=QUERY, timeout=100)
        r.raise_for_status()
        with ZipFile(BytesIO(r.content)) as z:
            name, = [f for f in z.namelist() if f.endswith(".fits")]
            path.write_bytes(z.read(name))
    with fits.open(path) as h:
        assert h[0].header["SECTOR"] == 108
        d = h[1].data
        t = d["TIME"]
        valid = np.isfinite(t) & (d["QUALITY"] == 0)
        dt = abs(t-CENTER)
        base = np.nanmedian(d["FLUX"][valid & (dt>.35) & (dt<.65)], axis=0)
        wcs = WCS(h[2].header)
        rows, images = [], []
        for off in [-1, -.5, 0, .5, 1]:
            i = np.argmin(np.where(valid, abs(t-CENTER-off/24), np.inf))
            assert abs(t[i]-CENTER-off/24) < .012
            img = d["FLUX"][i] - base
            x,y,a = centroid(img)
            ra,dec = wcs.pixel_to_world_values(x,y)
            reception = Time(t[i]-d["TIMECORR"][i]+h[1].header["BJDREFI"]+h[1].header["BJDREFF"],
                             format="jd",scale="tdb").utc
            rows.append(dict(tic=630314437, sector=108, utc=reception.isot, jd_utc=reception.jd,
                             ra_deg=float(ra), dec_deg=float(dec), x=x, y=y,
                             amplitude_e_s=a, ffi=d["FFI_FILE"][i]))
            images.append(img)
    with (HERE/"wide-track.csv").open("w", encoding="utf8", newline="") as f:
        w=csv.DictWriter(f,rows[0],lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    fig, axes = plt.subplots(1,5, figsize=(12,3), layout="constrained")
    for ax,img,row in zip(axes,images,rows):
        ax.imshow(img,origin="lower",cmap="magma",vmin=0,vmax=max(r["amplitude_e_s"] for r in rows))
        ax.scatter(row["x"],row["y"],s=110,edgecolors="#06cadd",facecolors="none")
        ax.set_title(row["utc"][11:19]+" UTC",fontsize=10)
        ax.set_xticks([]); ax.set_yticks([])
    fig.suptitle(f"TIC 630314437   ·   stationary background removed   ·   {rows[2]['utc'][:10]}")
    fig.savefig(HERE/"wide-track.png",dpi=160)
