"""Paired, fixed-time injections on the actual held-out TESS apertures."""
import argparse
import csv
import hashlib
import json
from pathlib import Path

from astropy.io import fits
import numpy as np

from photometry.screen import measure

HERE = Path(__file__).resolve().parent
DEPTHS = (0., .015, .05, .15)
HALF = .025  # 36 minutes to each side of the window center


def window(data):
    t = data["TIME"].astype(float)
    flux = np.stack([data[k] for k in ("SAP_FLUX", "SAP_BKG", "PDCSAP_FLUX")], axis=1).astype(float)
    valid = np.isfinite(t) & np.all(np.isfinite(flux), axis=1) & (data["QUALITY"] == 0)
    dt = np.nanmedian(np.diff(t))
    first = np.nanmin(t) + .32 * (np.nanmax(t) - np.nanmin(t))
    # Split on the time axis before inspecting brightness or any classification.
    indices = np.flatnonzero(valid)
    runs = np.split(indices, np.flatnonzero(np.diff(t[indices]) > 1.5*dt) + 1)
    pad = 3.2 * HALF + 6*dt
    for run in runs:
        if len(run) == 0:
            continue
        centers = run[(t[run] >= max(first, t[run[0]]+pad)) & (t[run] <= t[run[-1]]-pad)]
        for idx in centers:
            c = t[idx]
            use = run[abs(t[run]-c) <= pad]
            baseline = np.median(flux[use][abs(t[use]-c) > 1.6*HALF], axis=0)
            if min(baseline[0], baseline[2]) > 0:
                return t[use], flux[use], c, dt, baseline
    return None


def audit(row, folder):
    tic = row["tic"]
    sector = min(map(int, row["sectors"].split("|")))
    pattern = f"*-s{sector:04d}-{int(tic):016d}-*_lc.fits"
    files = sorted(folder.glob(pattern))
    base = dict(tic=tic, sector=sector)
    if len(files) != 1:
        return [dict(**base, status="ambiguous_or_missing_product")]
    with fits.open(files[0]) as hdus:
        assert int(hdus[0].header["TICID"]) == int(tic) and hdus[0].header["SECTOR"] == sector
        chosen = window(hdus[1].data)
    if chosen is None:
        return [dict(**base, status="no_valid_window")]
    t, original, center, dt, levels = chosen
    # Same underlying measurements and time stamps in every arm. Smooth raised
    # cosine with zero signal in the shoulders; the eclipse has a flat core.
    x = abs(t-center) / HALF
    spike = np.where(x < 1.4, (1+np.cos(np.pi*np.minimum(x/1.4, 1)))/2, 0)
    eclipse = np.clip((1.35-x)/.65, 0, 1)
    results = []
    for with_sky in (False, True):
        for depth in DEPTHS:
            y = original.copy()
            extra_sky = levels[0] * (.20 if with_sky else 0.) * spike
            y[:, 0] -= extra_sky + depth*levels[0]*eclipse
            y[:, 1] += extra_sky
            # PDCSAP provides context only; the decision uses SAP and SAP_BKG.
            y[:, 2] -= levels[2]*((.20 if with_sky else 0.)*spike + depth*eclipse)
            result = measure(t, y, center, HALF, dt)
            label = result["classification"] if result else "no_trigger"
            results.append(dict(**base, status="assessed", btjd=float(center),
                                injected_sky_percent=20 if with_sky else 0,
                                injected_stellar_percent=round(100*depth, 1),
                                classification=label,
                                restored_loss_ppt=None if result is None else result["restored_loss_ppt"]))
    return results


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("cache", type=Path, help="Directory holding the original SPOC light-curve FITS files")
    args = parser.parse_args()
    with (HERE/"batch.csv").open(newline="") as stream:
        rows = [entry for row in csv.DictReader(stream) for entry in audit(row, args.cache)]
    source = HERE/"photometry/screen.py"
    output = dict(classifier_sha256=hashlib.sha256(source.read_bytes()).hexdigest(), rows=rows)
    (HERE/"stress.json").write_text(json.dumps(output, indent=2) + "\n", encoding="utf8")
