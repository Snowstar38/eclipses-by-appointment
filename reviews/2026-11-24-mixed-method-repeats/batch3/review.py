"""Batch 3 independent QLP light-curve and recurrence review."""
import argparse
import csv
import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from astropy.io import fits

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2] if (HERE.parents[2]/"sky/data/qlp-sb-p20-60").is_dir() else HERE.parent/"inputs/workspace"


def read_csv(path):
    with path.open(newline="") as stream:
        return list(csv.DictReader(stream))


def write_csv(path, rows):
    if rows:
        with path.open("w", newline="") as stream:
            writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
            writer.writeheader()
            writer.writerows(rows)


def load(path, flagged):
    with fits.open(path) as hdus:
        h, data = hdus[0].header, hdus[1].data
        sector, camera = h["SECTOR"], h["CAMERA"]
        t = data["TIME"]
        corrected = "KSPSAP_FLUX" if "KSPSAP_FLUX" in data.names else "DET_FLUX"
        flux = np.column_stack([data[name] for name in ("SAP_FLUX", corrected)]).astype(float)
        good = (data["QUALITY"] == 0) & np.isfinite(t) & np.isfinite(flux).all(axis=1)
        good &= (flux > 0).all(axis=1)
        guard = np.isin(data["CADENCENO"], list(flagged.get((sector, camera), [])))
        order = np.argsort(t[good])
        t, flux, guard = t[good][order], flux[good][order], guard[good][order]
        flux = (flux / np.median(flux, axis=0) - 1) * 1000
        return sector, camera, t, flux, guard


def measure(t, flux, guard, center, width):
    cadence = np.median(np.diff(t))
    dt = t - center
    core = abs(dt) <= width / 2
    left = (dt >= -1.5 * width) & (dt < -width / 2) & ~guard
    right = (dt <= 1.5 * width) & (dt > width / 2) & ~guard
    safe = core & ~guard
    n, nl, nr = map(np.count_nonzero, (safe, left, right))
    out = dict(n=n, fraction=min(1, n * cadence / width), left_n=nl, right_n=nr,
               guarded=np.count_nonzero(core & guard),
               center_distance_d=np.min(abs(dt[~guard])) if np.any(~guard) else np.nan,
               max_gap_d=np.max(np.diff(np.r_[-width/2, dt[safe], width/2])),
               sap_ppt=np.nan, corrected_ppt=np.nan, sap_side_mad_ppt=np.nan,
               corrected_side_mad_ppt=np.nan, sap_guard_included_ppt=np.nan,
               corrected_guard_included_ppt=np.nan)
    if min(n, nl, nr) >= 2:
        medl, medr = (np.median(flux[side], axis=0) for side in (left, right))
        tl, tr = (np.median(dt[side]) for side in (left, right))
        residual = flux - (medl + (medr-medl) * ((dt[:, None]-tl)/(tr-tl)))
        out["sap_ppt"], out["corrected_ppt"] = -np.median(residual[safe], axis=0)
        out["sap_guard_included_ppt"], out["corrected_guard_included_ppt"] = -np.median(residual[core], axis=0)
        sides = residual[left | right]
        out["sap_side_mad_ppt"], out["corrected_side_mad_ppt"] = 1.4826 * np.median(
            abs(sides - np.median(sides, axis=0)), axis=0)
    return out


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()
    fits_dir = args.root / "sky/data/qlp-sb-p20-60"
    archive = args.root / "Astra/made/binary-exploration-2026-11-04/bulk-results"
    guard_file = args.root / "sky/mixed-fold-2026-11-24/cadence-controls/flagged-exposures.csv"
    flagged = {}
    for row in read_csv(guard_file):
        if row["screen_flag"] == "True":
            flagged.setdefault((int(row["sector"]), int(row["camera"])), set()).add(int(row["cadenceno"]))
    measurements, repeats, ranges = [], [], []
    manual = read_csv(HERE / "clocks.csv") if (HERE / "clocks.csv").exists() else []
    for target in read_csv(HERE / "batch.csv"):
        tic = target["tic"]
        sectors = dict((data[0], data) for data in
                       (load(path, flagged) for path in sorted(fits_dir.glob(f"{tic}_s*.fits"))))
        screens = json.loads((archive / f"{tic}.json").read_text())["files"]
        panels = []
        for file in screens:
            sector = file["sector"]
            _, camera, t, flux, guard = sectors[sector]
            gaps = np.diff(t)
            cadence = np.median(gaps)
            ranges.append(dict(tic=tic, sector=sector, camera=camera, start=t.min(),
                               stop=t.max(), cadence=cadence, n=t.size, guarded=guard.sum()))
            for window in file.get("windows", []):
                if window["kind"] != "dip":
                    continue
                center, width = window["time"], window["duration"]
                measurements.append(dict(tic=tic, sector=sector, camera=camera, center=center,
                                         width=width, archive_flag=window["flag"],
                                         archive_supported=window["supported"], **measure(t, flux, guard, center, width)))
                if window["flag"]:
                    panels.append((sector, center, width, "Archive"))
        center, width = (float(target[k]) for k in ("best_window_btjd", "best_window_duration_days"))
        gaia = float(target["gaia_period_days"])
        clocks = [(kind, gaia * factor, center, width) for kind, factor in
                  (("Gaia", 1), ("Gaia/2", .5), ("Gaia*2", 2))]
        clocks += [(r["name"], float(r["period_d"]), float(r["epoch_btjd"]), float(r["width_d"]))
                   for r in manual if r["tic"] == tic]
        for name, period, epoch, width in clocks:
            for sector, camera, t, flux, guard in sectors.values():
                lo = int(np.ceil((t.min() - epoch - width/2) / period))
                hi = int(np.floor((t.max() - epoch + width/2) / period))
                for cycle in range(lo, hi + 1):
                    predicted = epoch + period * cycle
                    row = measure(t, flux, guard, predicted, width)
                    repeats.append(dict(tic=tic, clock=name, period_d=period, epoch_btjd=epoch,
                                        sector=sector, camera=camera, cycle=cycle, center=predicted,
                                        width=width, **row))
                    if name not in ("Gaia", "Gaia/2", "Gaia*2") and not name.startswith("Short repeat"):
                        panels.append((sector, predicted, width, name))
        archive_panels = [panel for panel in panels if panel[3] == "Archive"]
        gaia_predictions = [r for r in repeats if r["tic"] == tic and r["clock"] == "Gaia"]
        event_count = len(panels)
        fig, axes = plt.subplots(max(1, (event_count + 2)//3), 3, figsize=(13.5, 2.7*max(1, (event_count+2)//3)),
                                 layout="constrained", squeeze=False)
        for ax in axes.flat:
            ax.set_visible(False)
        for ax, (sector, center, width, name) in zip(axes.flat, panels):
            ax.set_visible(True)
            _, _, t, flux, guard = sectors[sector]
            dt = t-center
            near = abs(dt) < 2.5*width
            f = flux - np.median(flux[near], axis=0) if np.any(near) else flux
            for col, color in ((0, "tab:blue"), (1, "black")):
                ax.scatter(dt[near & ~guard], f[near & ~guard, col], s=4, c=color, alpha=.5)
                if np.any(near & guard):
                    ax.scatter(dt[near & guard], f[near & guard, col], s=9, c="red")
            ax.set(xlim=(-2.5*width, 2.5*width), title=f"{name}  S{sector}  {center:.4f}",
                   xlabel="Days from center", ylabel="Local ppt")
            ax.axvspan(-width/2, width/2, color="orange", alpha=.15)
        fig.suptitle(f"TIC {tic}  |  blue SAP, black corrected, red guarded")
        fig.savefig(HERE/f"{tic}-events.png", dpi=100)
        plt.close(fig)
        fig, axes = plt.subplots(len(sectors), 1, figsize=(12, max(2, 1.8*len(sectors))),
                                 layout="constrained", squeeze=False)
        for ax, (sector, camera, t, flux, guard) in zip(axes.flat, sectors.values()):
            for col, color in ((0, "tab:blue"), (1, "black")):
                ax.scatter(t[~guard], flux[~guard, col], s=2, c=color, alpha=.3)
                ax.scatter(t[guard], flux[guard, col], s=3, c="red")
            for sec, c, w, _ in archive_panels:
                if sec == sector:
                    ax.axvspan(c-w/2, c+w/2, alpha=.15, color="orange")
            for prediction in gaia_predictions:
                if prediction["sector"] == sector:
                    ax.axvline(prediction["center"], color="tab:purple", alpha=.4, ls="--", lw=.8)
            ax.set(ylabel="ppt", title=f"S{sector} camera {camera}")
            lo, hi = np.percentile(flux, [.3, 99.7])
            ax.set_ylim(lo - (hi-lo)*.1, hi + (hi-lo)*.1)
        axes[-1, 0].set_xlabel("BTJD")
        fig.suptitle(f"TIC {tic}  |  blue SAP, black corrected, red guarded, dashed purple Gaia")
        fig.savefig(HERE/f"{tic}-sectors.png", dpi=100)
        plt.close(fig)
    write_csv(HERE / "archive-windows.csv", measurements)
    write_csv(HERE / "predicted-windows.csv", repeats)
    write_csv(HERE / "sector-coverage.csv", ranges)


if __name__ == "__main__":
    main()
