import csv
import json
from collections import defaultdict

import numpy as np
from scipy.signal import find_peaks

from archive import HERE, CACHE, load_batch

SCALES_H = np.array([0.075, 0.13, 0.23, 0.40, 0.70, 1.20, 2.0, 3.4, 5.8, 9.9, 16.8])
MIN_DEPTH = 10.


def mad(y):
    return 1.4826 * np.median(abs(y - np.median(y)))


def runs(mask):
    edges = np.flatnonzero(np.diff(np.r_[False, mask, False]))
    return zip(edges[::2], edges[1::2])


def measure(y, center, half):
    # Skip a transition band around the core, then require real, adjacent
    # cadences on both shoulders inside a segment with no missing data.
    wing = max(4, half)
    inner = max(half+1, round(1.65*half))
    outer = inner + wing
    if center < outer or center + outer >= len(y):
        return None
    left = y[center-outer:center-inner]
    right = y[center+inner+1:center+outer+1]
    lmed, rmed = np.median(left), np.median(right)
    noise = max(.01, mad(np.r_[left-lmed, right-rmed]))
    core = y[center-half:center+half+1]
    # Use the lower shoulder and require three individual cadences over
    # the same threshold. This also rejects most monotonic jumps.
    base = min(lmed, rmed)
    depth = base - np.median(core)
    threshold = max(MIN_DEPTH, 5*noise)
    n = max((b-a for a,b in runs(base-core > threshold)), default=0)
    if depth <= threshold or n < 3:
        return None
    excursion = max(np.ptp(np.percentile(side, [10,90])) for side in (left, right))
    stable = bool(excursion < .7*depth and abs(lmed-rmed) < .8*depth)
    return dict(depth=round(float(depth), 3), scatter=round(float(noise), 3),
                consecutive=int(n), stable=stable, shoulder_excursion=round(float(excursion), 3),
                shoulder_difference=round(float(abs(lmed-rmed)), 3))


def scan(t, a, b):
    valid = np.isfinite(a) & np.isfinite(b) & (a>0) & (b>0)
    cadence = np.nanmedian(np.diff(t))
    splits = np.flatnonzero(np.r_[True, (np.diff(t) > 1.5*cadence) | ~valid[1:] | ~valid[:-1], True])
    events = []
    for first, last in zip(splits[:-1], splits[1:]):
        if last-first < 13:
            continue
        x = t[first:last]
        sap, pdc = (1000*(f[first:last]/np.median(f[first:last])-1) for f in (a,b))
        candidates = []
        widths = np.unique(np.maximum(1, np.rint(SCALES_H/(48*cadence)).astype(int)))
        sums = [np.r_[0, np.cumsum(f)] for f in (sap,pdc)]
        for half in widths:
            wing = max(4, half)
            inner = max(half+1, round(1.65*half))
            outer = inner + wing
            if 2*outer+3 > len(x):
                continue
            c = np.arange(outer, len(x)-outer)
            depression = []
            for ps in sums:
                left = (ps[c-inner]-ps[c-outer])/wing
                right = (ps[c+outer+1]-ps[c+inner+1])/wing
                core = (ps[c+half+1]-ps[c-half])/(2*half+1)
                depression.append(np.minimum(left,right)-core)
            joint = np.maximum(*depression)
            # Permissive trigger. Robust endpoint is evaluated on raw points.
            peaks = find_peaks(np.r_[0,joint,0], height=4, distance=max(1,half//2))[0]-1
            for i in c[peaks]:
                sa, pd = measure(sap, i, half), measure(pdc, i, half)
                if sa is None and pd is None:
                    continue
                # Keep the other channel's continuous measurements even if it
                # falls below the formal independent threshold.
                candidates.append(dict(i=int(i), half=int(half), btjd=round(float(x[i]), 7),
                                       core_h=round(float((2*half+1)*cadence*24), 4),
                                       sap=sa, pdc=pd))
        candidates.sort(key=lambda v: (sum(s is not None and s["stable"] for s in (v["sap"],v["pdc"])),
                                       sum(s is not None for s in (v["sap"],v["pdc"])),
                                       max(s["depth"] for s in (v["sap"],v["pdc"]) if s)), reverse=True)
        kept = []
        for ev in candidates:
            if any(abs(ev["i"]-k["i"]) <= max(2, ev["half"]+k["half"]) for k in kept):
                continue
            kept.append(ev)
        events.extend(sorted(kept, key=lambda e:e["btjd"]))
    return events


def main():
    records = json.loads((HERE/"archive.json").read_text(encoding="utf8"))
    grouped = defaultdict(list)
    for p in records:
        if "error" not in p:
            with np.load(CACHE / f'{p["tic"]}-{p["sector"]}.npz') as arr:
                p["events"] = scan(arr["t"], arr["sap"], arr["pdc"])
        grouped[p["tic"]].append(p)
        print(p["tic"], p["sector"], len(p.get("events", [])), flush=True)
    (HERE/"dips.json").write_text(json.dumps(grouped, indent=2), encoding="utf8")
    with (HERE/"dips.csv").open("w", newline="", encoding="utf8") as output:
        writer = csv.writer(output)
        writer.writerow(["tic","sector","btjd","core_h",
                         "sap_depth_ppt","sap_scatter_ppt","sap_consecutive","sap_stable",
                         "pdc_depth_ppt","pdc_scatter_ppt","pdc_consecutive","pdc_stable"])
        for tic, products in grouped.items():
            for p in products:
                for e in p.get("events", []):
                    row = [tic,p["sector"],e["btjd"],e["core_h"]]
                    for channel in ("sap","pdc"):
                        ev = e[channel] or {}
                        row.extend(ev.get(k) for k in ("depth","scatter","consecutive","stable"))
                    writer.writerow(row)


if __name__ == "__main__":
    main()
