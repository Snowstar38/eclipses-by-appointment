"""Check the original features against additional indexed full-frame light curves."""
from concurrent.futures import ThreadPoolExecutor
import hashlib
import io
import json
from pathlib import Path

from astropy.io import fits
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import requests

HERE = Path(__file__).resolve().parent
CASES = [(187261476, 59), (187261476, 73), (187261476, 86),
         (356752132, 42), (356752132, 44)]


def read_product(case):
    tic, sector = case
    tag = f"{tic:016d}"
    parts = "/".join(tag[i:i + 4] for i in range(0, 16, 4))
    url = (f"https://archive.stsci.edu/hlsps/tess-spoc/s{sector:04d}/target/{parts}/"
           f"hlsp_tess-spoc_tess_phot_{tag}-s{sector:04d}_tess_v1_lc.fits")
    reply = requests.get(url, timeout=(10, 40))
    reply.raise_for_status()
    with fits.open(io.BytesIO(reply.content), memmap=False) as hd:
        assert (hd[0].header["TICID"], hd[0].header["SECTOR"]) == case
        data = hd[1].data
        good = data["QUALITY"] == 0
        for key in ("TIME", "SAP_FLUX", "PDCSAP_FLUX"):
            good &= np.isfinite(data[key])
        t, sap, pdc = [np.array(data[c][good], float) for c in ("TIME","SAP_FLUX","PDCSAP_FLUX")]
    meta = dict(tic=tic, sector=sector, url=url, sha256=hashlib.sha256(reply.content).hexdigest(),
                cadences=len(t), start_btjd=t.min(), end_btjd=t.max())
    return meta, t, sap/np.median(sap), pdc/np.median(pdc)


def deep_events(t, sap, pdc):
    """Flag sustained coincident losses of >15% relative to both sector medians."""
    ids = np.flatnonzero((sap < .85) & (pdc < .85))
    groups = np.split(ids, np.flatnonzero((np.diff(ids) > 1) | (np.diff(t[ids]) > .025)) + 1)
    events = []
    for g in groups:
        if len(g) < 3:
            continue
        lowest = g[np.argmin(pdc[g])]
        events.append(dict(start_btjd=t[g[0]], end_btjd=t[g[-1]], min_btjd=t[lowest],
                           core_cadences=len(g), min_pdc_rel=pdc[lowest], min_sap_rel=sap[lowest]))
    return events


def test_short_clock(t, sap, pdc):
    period, epoch = 1.178992420, 2912.2224825
    phase = ((t - epoch + period/2) % period) / period - .5
    edges = np.linspace(-.5, .5, 101)
    summary = []
    for flux in (sap, pdc):
        bins = np.array([np.median(flux[(phase >= a) & (phase < b)])
                         for a, b in zip(edges[:-1], edges[1:])])
        local = np.abs((edges[1:] + edges[:-1]) / 2) < .18
        index = np.flatnonzero(local)[np.argmin(bins[local])]
        center = (edges[index] + edges[index+1])/2
        core = abs(phase-center) < .02
        shoulder = (abs(phase-center) >= .08) & (abs(phase-center) < .14)
        summary.append(dict(min_phase_within_search=center,
                            depth_ppt=1000*(1-np.median(flux[core])/np.median(flux[shoulder]))))
    return dict(period_d=period, epoch_btjd=epoch, search_halfwidth_cycles=.18,
                bin_width_cycles=.01, sap=summary[0], pdc=summary[1])


def main():
    with ThreadPoolExecutor(5) as pool:
        products = list(pool.map(read_product, CASES))
    fig, axes = plt.subplots(len(products), 1, figsize=(11, 10), constrained_layout=True)
    records = []
    for ax, (meta, t, sap, pdc) in zip(axes, products):
        item = dict(**meta, deep_events=deep_events(t, sap, pdc))
        if meta["tic"] == 187261476:
            item["short_clock"] = test_short_clock(t, sap, pdc)
        records.append(item)
        ax.plot(t, sap, ".", ms=1, color="#a6b1b9", label="SAP")
        ax.plot(t, pdc, ".", ms=1, color="#24496a", label="PDCSAP")
        ax.set_title(f"TIC {meta['tic']}  ·  Sector {meta['sector']}", loc="left")
        ax.set_ylabel("Relative flux")
        ax.legend(loc="lower right", markerscale=4)
    axes[-1].set_xlabel("Time (BTJD)")
    fig.savefig(HERE/"sectors.png", dpi=130)
    (HERE/"evidence.json").write_text(json.dumps(records, indent=2) + "\n", encoding="utf8")


if __name__ == "__main__":
    main()
