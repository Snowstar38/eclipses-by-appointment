"""Test TESS-only timing predictions on source-position ZTF measurements without refitting."""
import argparse
from pathlib import Path

import astropy.units as u
from astropy.coordinates import EarthLocation, SkyCoord
from astropy.time import Time
from astropy.utils import iers
import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent
PALOMAR = EarthLocation.from_geodetic(-116.865, 33.3563, 1712 * u.m)
iers.conf.auto_download = False


def cycle_depth(phase, cycle, residual, halfwidth, offset):
    distance = (phase - offset + .5) % 1 - .5
    use = abs(distance) <= halfwidth
    nights = np.unique(cycle[use])
    if len(nights) < 3:
        return len(nights), None
    medians = [np.median(residual[use & (cycle == n)]) for n in nights]
    return len(nights), float(np.median(medians))


def analyze(row, cache):
    tic = str(row["tic"])
    path = cache / (tic + ".csv.gz")
    if not path.exists():
        return []
    d = pd.read_csv(path)
    if d.empty:
        return []
    for name in ("catflags", "mag", "magerr", "mjd", "exptime", "ra", "dec"):
        d[name] = pd.to_numeric(d[name], errors="coerce")
    d = d.dropna(subset=["mjd", "exptime", "ra", "dec", "mag", "magerr"])
    d = d[(d.catflags == 0) & np.isfinite(d.mag) & (d.magerr > 0) & (d.magerr < .2)]
    p, epoch = float(row["alternate_period_d"]), float(row["alternate_epoch_btjd"])
    width = min(.04, float(row["alternate_duration_h"]) / 24 / p * .36)
    target = SkyCoord(float(row["ra_deg"]), float(row["dec_deg"]), unit="deg")
    rows = []
    for (oid, band), g in d.groupby(["oid", "filtercode"]):
        if len(g) < 30:
            continue
        obj = SkyCoord(np.median(g.ra), np.median(g.dec), unit="deg")
        tm = Time(g.mjd.to_numpy() + g.exptime.to_numpy()/172800, format="mjd", scale="utc", location=PALOMAR)
        x = ((tm.tdb + tm.light_travel_time(obj)).jd - 2457000 - epoch) / p
        m = g.mag.to_numpy()
        centered = m - np.median(m)
        scatter = max(.005, np.median(g.magerr), 1.4826*np.median(abs(centered)))
        def depth_at(offset):
            return cycle_depth(x, np.floor(x-offset+.5), centered, width, offset)
        cycles, depth = depth_at(0)
        controls = [v for shift in np.arange(1,101)/101 if min(shift,1-shift)>2*width
                    for _,v in [depth_at(shift)] if v is not None]
        pct = sum(v < depth for v in controls)/len(controls) if depth is not None and controls else None
        support = cycles >= 4 and depth is not None and depth >= 3*scatter and len(controls)>=40 and pct>=.95
        rows.append(dict(tic=tic, clock_source=row["clock_source"], oid=str(oid), band=band, separation_arcsec=target.separation(obj).arcsec,
                         period_d=p, epoch_btjd=epoch, halfwidth_d=width*p, n_good=len(g),
                         cycles_in_core=cycles, depth_mag=depth, scatter_mag=scatter,
                         usable_shifted_phases=len(controls), fraction_shifted_shallower=pct,
                         supports_tess_prediction=bool(support)))
    return rows


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("cache", type=Path)
    args = parser.parse_args()
    stars = pd.read_csv(HERE.parent / "batch.csv").set_index("tic")
    timing = pd.read_csv(HERE.parent / "sol/outcome.csv", usecols=["tic", "alternate_period_d",
                         "alternate_epoch_btjd", "alternate_duration_h"]).set_index("tic")
    timing["clock_source"] = "Sol"
    fable = pd.read_csv(HERE / "fable-clocks.csv").set_index("tic")
    fable["clock_source"] = "Fable"
    targets = pd.concat([timing, fable]).join(stars[["ra_deg","dec_deg"]]).reset_index()
    rows = [entry for row in targets.to_dict("records") if np.isfinite(row.get("alternate_period_d", np.nan))
            for entry in analyze(row, args.cache)]
    pd.DataFrame(rows).to_csv(HERE / "phase-checks.csv", index=False)
