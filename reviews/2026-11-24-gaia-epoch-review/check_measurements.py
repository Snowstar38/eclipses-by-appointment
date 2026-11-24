"""Check catalogue joins and timing fits. Optionally rerun the nine TESS box searches."""
import argparse
import csv
import hashlib
import math
import statistics
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent


def table(filename):
    with (HERE / filename).open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def refit_times(star, rows):
    events = [r for r in rows if r["tic"] == star["tic"] and r["accepted"] == "True"]
    cycles = [int(r["cycle"]) for r in events]
    centers = [float(r["center_btjd"]) for r in events]
    x = statistics.mean(cycles)
    y = statistics.mean(centers)
    period = sum((a-x)*(b-y) for a,b in zip(cycles,centers)) / sum((a-x)**2 for a in cycles)
    assert len(cycles) == len(set(cycles))
    assert math.isclose(period, float(star["adopted_period_days"]), abs_tol=6e-8), star["tic"]
    assert len(events) == int(star["n_events_prim"])
    assert len({r["sector"] for r in events}) == int(star["n_sectors"])
    epoch = float(star["adopted_epoch_btjd"])
    cycle = round((epoch - y)/period + x)
    assert abs(epoch - (y + (cycle-x)*period)) < 6e-6, star["tic"]


def remeasure_boxes(directory):
    import numpy as np
    from astropy.io import fits
    from astropy.timeseries import BoxLeastSquares
    from scipy.ndimage import median_filter

    products = table("tess-photometry.csv")
    for expected in table("wider-window-box-fits.csv"):
        times = []
        fluxes = []
        for prod in products:
            if prod["tic"] != expected["tic"]:
                continue
            path = directory / prod["file"]
            if not path.is_file():
                path = directory / prod["gaia_dr3"] / prod["file"]
            with path.open("rb") as f:
                assert hashlib.file_digest(f, "sha256").hexdigest() == prod["sha256"], path
            with fits.open(path) as hdus:
                d = hdus[1].data
                t = d["TIME"].astype(float)
                key = "PDCSAP_FLUX" if "PDCSAP_FLUX" in d.names else "SAP_FLUX"
                flux = d[key].astype(float)
                good = (d["QUALITY"] == 0) & np.isfinite(t) & np.isfinite(flux) & (flux > 0)
            t, flux = t[good], flux[good]
            for idx in np.split(np.arange(len(t)), np.flatnonzero(np.diff(t) > 0.4) + 1):
                if len(idx) < 12:
                    continue
                width = min(len(idx)//2*2-1, 2*int(1/np.median(np.diff(t[idx])))+1)
                detrended = flux[idx] / median_filter(flux[idx], size=width, mode="nearest")
                bins = np.floor(t[idx]*72).astype(int)
                bins -= bins.min()
                count = np.bincount(bins)
                occupied = count > 0
                for values, output in ((t[idx], times), (detrended, fluxes)):
                    output.extend(np.bincount(bins, weights=values)[occupied] / count[occupied])
        p = float(expected["period_gaia"])
        error = float(expected["period_err"])
        steps = min(1501, max(61, int(12*error*np.ptp(times)/(p*p)/0.003)))
        grid = np.linspace(p-6*error, p+6*error, steps)
        result = BoxLeastSquares(np.array(times), np.array(fluxes)).power(
            grid, np.array([0.012, 0.025, 0.045, 0.075])*p, oversample=10)
        best = np.argmax(result.power)
        assert abs(result.period[best] - float(expected["searched_best_d"])) < 6e-8
        assert abs(result.depth[best]*1000 - float(expected["stack_depth_ppt"])) < 0.001
        print(f"TIC {expected['tic']}  {result.period[best]:.7f} d  {1000*result.depth[best]:.3f} ppt")


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--fits-dir", type=Path, help="Directory holding the nine wider-window targets' FITS products")
    args = p.parse_args()
    hosts = table("host-stars.csv")
    reviewed = table("reviewed-stars.csv")
    assert len(reviewed) == len({r["tic"] for r in reviewed}) == len({r["gaia_dr3"] for r in reviewed}) == 24
    assert Counter(r["outcome"] for r in reviewed) == {"confirmed":14, "probable":3, "recovery":7}
    assert len(hosts) == 17
    accepted = {r["tic"]:r for r in reviewed if r["release_id"]}
    times = table("first-sample-timings.csv")
    for star in hosts:
        r = accepted[star["tic"]]
        assert (star["review_id"], star["gaia_dr3"], star["physical_tier"]) == (r["release_id"], r["gaia_dr3"], r["outcome"])
        assert float(star["adopted_period_days"]) == float(r["period_days"])
        if r["selection"] == "Gaia epoch search":
            refit_times(star, times)
    assert {r["tic"] for r in reviewed} == {r["tic"] for r in table("tess-photometry.csv")}
    print("Verified 24 decisions, 17 accepted hosts, and 13 accepted first-sample timing fits.")
    if args.fits_dir:
        remeasure_boxes(args.fits_dir)


if __name__ == "__main__":
    main()
