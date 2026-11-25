"""Exploratory sky-first search on signed flux, including weak target apertures."""
import argparse
import csv
import json
from pathlib import Path
import warnings

from astropy.io import fits
import numpy as np
from numpy.lib.stride_tricks import sliding_window_view
import pandas as pd

HERE = Path(__file__).resolve().parent


def screen(raw):
    names = ("TIME", "SAP_FLUX", "SAP_BKG")
    t, sap, sky = (raw[name].astype(float) for name in names)
    use = (raw["QUALITY"] == 0) & np.isfinite(t) & np.isfinite(sap) & np.isfinite(sky)
    minutes = 10 / 1440
    start = np.nanmin(t)
    bins = np.floor((t[use]-start)/minutes).astype(int)
    data = pd.DataFrame(dict(bin=bins, sap=sap[use], sky=sky[use])).groupby("bin")
    table = data.median().where(data.size() >= 3).reindex(range(bins.max()+1))
    # Padded or missing data stay missing; the 27-bin patterns have two
    # six-bin shoulders and a three-bin core, with gaps between them.
    windows = sliding_window_view(table.to_numpy(), 27, axis=0)
    left, right, core = windows[:, :, :6], windows[:, :, -6:], windows[:, :, 12:15]
    covered = ((np.isfinite(left[:, 0]).sum(axis=1) >= 5) &
               (np.isfinite(right[:, 0]).sum(axis=1) >= 5) &
               np.isfinite(core[:, 0]).all(axis=1))
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", RuntimeWarning)
        lmed, rmed, cmed = (np.nanmedian(x, axis=2) for x in (left, right, core))
        residual = np.concatenate((left-lmed[:,:,None], right-rmed[:,:,None]), axis=2)
        scatter = 1.4826 * np.nanmedian(abs(residual), axis=2)
    sky_gain = cmed[:,1] - np.maximum(lmed[:,1], rmed[:,1])
    sap_loss = np.minimum(lmed[:,0], rmed[:,0]) - cmed[:,0]
    sky_ratio = sky_gain / np.maximum(25., 8*scatter[:,1])
    flux_ratio = sap_loss / np.maximum(10., 4*scatter[:,0])
    score = np.minimum(sky_ratio, flux_ratio)
    centers = start + (np.arange(len(score))+13.5)*minutes
    selected = []
    passing = np.flatnonzero(covered & (score >= 1))
    for idx in passing[np.argsort(-score[passing], kind="stable")]:
        if any(abs(centers[idx] - item["btjd"]) < 4/24 for item in selected):
            continue
        selected.append(dict(btjd=centers[idx], rank_score=score[idx],
                             sap_loss_e_s=sap_loss[idx], sky_gain_e_s=sky_gain[idx],
                             sap_baseline_e_s=(lmed[idx,0]+rmed[idx,0])/2))
    return selected, int(covered.sum())


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("cache", type=Path)
    args = parser.parse_args()
    products = json.loads((HERE/"photometry/pilot-coverage.json").read_bytes())
    products += json.loads((HERE/"photometry/controls-coverage.json").read_bytes())
    controls = {113655666, 356752132, 187261476}
    events, coverage = [], []
    for row in products:
        tic, sector = int(row["tic"]), int(row["sector"])
        if "error" in row:
            coverage.append(dict(tic=tic, sector=sector, status=row["error"]))
            continue
        with fits.open(args.cache/row["filename"]) as h:
            assert (h[0].header["TICID"], h[0].header["SECTOR"]) == (tic, sector)
            group, usable = screen(h[1].data)
        meta = dict(tic=tic, sector=sector, control=tic in controls)
        coverage.append(dict(**meta, usable_ten_minute_centers=usable, triggers=len(group)))
        events.extend(dict(**meta, **entry, tpf_url=row["tpf_url"]) for entry in group)
    (HERE/"sky-seed-coverage.json").write_text(json.dumps(coverage, indent=2) + "\n", encoding="utf8")
    keys = ["tic","sector","control","btjd","rank_score","sap_loss_e_s","sky_gain_e_s",
            "sap_baseline_e_s","tpf_url"]
    with (HERE/"sky-seeds.csv").open("w", encoding="utf8", newline="") as f:
        w = csv.DictWriter(f, keys, lineterminator="\n")
        w.writeheader()
        w.writerows(sorted(events, key=lambda r: -r["rank_score"]))
