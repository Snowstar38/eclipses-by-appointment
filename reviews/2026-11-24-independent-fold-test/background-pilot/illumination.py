"""Test whether the moving light reaches actual background pixels around the deep dip."""
import argparse
import csv
from pathlib import Path

from astropy.io import fits
from astropy.time import Time
from astropy.wcs import WCS
import numpy as np

HERE = Path(__file__).resolve().parent
CENTER = 4312.172652


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("tpf", type=Path)
    args = parser.parse_args()
    records = []
    with fits.open(args.tpf) as hdus:
        assert (hdus[0].header["TICID"], hdus[0].header["SECTOR"]) == (630314437, 108)
        d = hdus[1].data
        t = d["TIME"]
        good = np.isfinite(t) & (d["QUALITY"] == 0)
        times = Time(t[good]-d["TIMECORR"][good]+2457000, format="jd",scale="tdb").utc.jd
        detector = d["FLUX"][good] + d["FLUX_BKG"][good]
        dt = abs(t[good]-CENTER)
        quiet = np.nanmedian(detector[(dt>.35)&(dt<.65)], axis=0)
        wcs = WCS(hdus["APERTURE"].header)
        mask = hdus["APERTURE"].data
        by,bx = np.where((mask & 4) != 0)
        ay,ax = np.where((mask & 2) != 0)
        for row in csv.DictReader((HERE/"wide-track.csv").read_text().splitlines()):
            x,y = wcs.world_to_pixel_values(float(row["ra_deg"]),float(row["dec_deg"]))
            img = np.nanmedian(detector[abs(times-float(row["jd_utc"])) < 4/1440],axis=0)-quiet
            dist = np.hypot(bx-x, by-y)
            groups = np.array_split(np.argsort(dist), 4)
            levels = [float(np.nanmedian(img[by[g],bx[g]])) for g in groups]
            records.append(dict(utc=row["utc"], background_pixels=len(bx), stellar_pixels=len(ax),
                                nearest_background_center_px=float(min(dist)),
                                nearest_stellar_center_px=float(min(np.hypot(ax-x,ay-y))),
                                nearest_quartile_excess_e_s_per_px=levels[0],
                                farthest_quartile_excess_e_s_per_px=levels[-1]))
    with (HERE/"illumination.csv").open("w", newline="", encoding="utf8") as f:
        w = csv.DictWriter(f, records[0], lineterminator="\n")
        w.writeheader()
        w.writerows(records)
