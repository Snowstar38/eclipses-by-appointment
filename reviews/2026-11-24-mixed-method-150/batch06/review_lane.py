"""Generate raw/detrended QLP event panels and period tests for batches 06–10."""
import argparse
import json
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from astropy.io import fits
from scipy.optimize import least_squares

HERE = Path(__file__).resolve().parent
HOUSE = HERE.parents[2]
DEFAULT_ROOT = HOUSE if (HOUSE/"sky/data/qlp-sb-p20-60").is_dir() else HERE.parent/"inputs/workspace"
shared = HOUSE/"sky/mixed-repeats-2026-11-24/batch2"
if not (shared/"review.py").exists():
    shared = HERE.parents[1]/"2026-11-24-mixed-method-repeats/batch2"
sys.path.insert(0, str(shared))
from review import add_panel, csv_read, csv_write, load_curve, measure, predicted, short_folds, short_periods

SHORT_FOLDS = {
    "214689049": .13835, "121999831": .798202, "240799649": .456000,
    "276194285": 5.43, "268732110": .64, "321813701": .375,
    "70889777": 1.405, "383529972": .3818, "260406489": .13735,
    "290665111": .683, "248408609": 1.437, "302200827": 5.735405,
    "248646032": .9408, "281709735": 3.44,
}
LOCAL_FITS = {
    "341293943": (38.868627, [(13, 1657.452), (27, 2046.43), (101, 4106.176), (102, 4145.055), (104, 4184.205)]),
    "128781401": (15.91406, [(56, 2831.417), (56, 2847.355), (83, 3579.383)]),
    "235594109": (21.0351207, [(25, 1985.742), (25, 2006.263), (53, 2764.652),
                                 (74, 3332.263), (79, 3458.888), (80, 3500.881)]),
}


def render_events(tic, tests, curves, out, label):
    cols = min(4, len(tests))
    rows = (len(tests)+cols-1)//cols
    fig, axes = plt.subplots(rows, cols, figsize=(max(8.0, cols*3.15), rows*1.8), squeeze=False)
    results = []
    for ax, (sector, center, width, title) in zip(axes.flat, tests):
        result = add_panel(ax, curves[sector], center, width, title)
        results.append(result)
    for ax in list(axes.flat)[len(tests):]:
        ax.set_visible(False)
    fig.suptitle(f"TIC {tic}, {label} | SAP blue / corrected orange | ppt and days")
    fig.tight_layout()
    fig.savefig(out, dpi=105)
    plt.close(fig)
    return results


def peg_control(data, output, flags):
    """Join SAP/background by spacecraft cadence despite target-dependent BTJD."""
    records = []
    fig, axes = plt.subplots(2, 1, figsize=(11, 5), squeeze=False)
    for sector, ax in zip((56, 83), axes.flat):
        tic_list = (128781401, 287857379)
        archive = []
        for tic in tic_list:
            with fits.open(data/f"{tic}_s{sector:03d}.fits") as hdus:
                table = hdus[1].data
                header = hdus[0].header
                archive.append((header["CAMERA"], header["CCD"], np.array(table["CADENCENO"]),
                                np.array(table["TIME"]), np.array(table["SAP_FLUX"]),
                                np.array(table["SAP_BKG"]), np.array(table["QUALITY"])))
        (c_a, d_a, i_a, t_a, a, g_a, q_a), (c_b, d_b, i_b, t_b, b, g_b, q_b) = archive
        ids, ia, ib = np.intersect1d(i_a, i_b, return_indices=True)
        good = ((q_a[ia] == 0) & (q_b[ib] == 0) & np.isfinite(a[ia]) & np.isfinite(b[ib])
                & ~np.isin(ids, flags.get((sector, c_a), [])))
        ta, tb = t_a[ia][good], t_b[ib][good]
        ra = 1000*(a[ia][good]/np.median(a[ia][good])-1)
        rb = 1000*(b[ib][good]/np.median(b[ib][good])-1)
        ax.plot(tb, ra, ".", ms=2, label="128781401 (CCD 4)")
        ax.plot(tb, rb, ".", ms=2, label="14 Peg (CCD 3)")
        ax.set(ylabel=f"S{sector} SAP (ppt)")
        for cycle, peak, _ in predicted({sector:(tb,)}, 1712.14069136, 5.3046858321, .6):
            ax.axvline(peak, c=".55", lw=.75)
            nearest = int(np.argmin(abs(tb-peak)))
            core = abs(tb-peak) < .25
            if core.sum() < 2:
                continue
            records.append(dict(sector=sector, cycle=cycle, predicted_14peg_btjd=peak,
                                cadence=int(ids[good][nearest]), t14peg_btjd=tb[nearest], target_btjd=ta[nearest],
                                target_camera=c_a, target_ccd=d_a, peg_camera=c_b, peg_ccd=d_b,
                                target_median_ppt=float(np.median(ra[core])),
                                peg_median_ppt=float(np.median(rb[core])),
                                target_bkg_median=float(np.nanmedian(g_a[ia][good][core])),
                                peg_bkg_median=float(np.nanmedian(g_b[ib][good][core]))))
    axes[0, 0].legend()
    axes[-1, 0].set_xlabel("14 Peg BTJD, both targets joined by spacecraft cadence")
    fig.tight_layout()
    fig.savefig(output/"plots/128781401-14peg-control.png", dpi=110)
    plt.close(fig)
    csv_write(output/"128781401-14peg-control.csv", records)


def anchor_for_period(events, period, nominal_width):
    """Find a phase among scan times supported by the most distinct sectors."""
    def support(event):
        _, t, width, amplitude = event
        nearby = {sector for sector, center, other_width, _ in events
                  if abs((center-t+period/2)%period-period/2) < max(.05, min(.65, (width+other_width)/3))}
        return len(nearby), -abs(np.log(width/nominal_width)), amplitude
    _, center, width, _ = max(events, key=support)
    return center, width


def fit_local_centers(curves, period, guesses):
    rows = []
    for sector, guess in guesses:
        t, raw, _, good, flagged = curves[sector]
        use = good & ~flagged & (abs(t-guess) < 1.4)
        x = t[use]-guess
        z = 1000*(raw[use]/np.median(raw[use])-1)

        def residual(parameters):
            level, slope, depth, offset, sigma = parameters
            return level+slope*x-depth*np.exp(-.5*((x-offset)/sigma)**2)-z

        fit = least_squares(residual, [1, 1, 4, 0, .4], loss="soft_l1", f_scale=1,
                            bounds=([-40, -40, 0, -.7, .1], [40, 40, 50, .7, 1]))
        _, _, depth, offset, sigma = fit.x
        rows.append(dict(sector=sector, guess_btjd=guess, fit_btjd=guess+offset,
                         peak_depth_ppt=depth, fwhm_d=2.355*sigma))
    centers = np.array([row["fit_btjd"] for row in rows])
    cycles = np.rint((centers-centers[0])/period).astype(int)
    fitted_period, epoch = np.polyfit(cycles, centers, 1)
    for row, cycle, oc in zip(rows, cycles, centers-epoch-cycles*fitted_period):
        row.update(cycle=cycle, period_d=fitted_period, epoch_btjd=epoch, oc_d=oc)
    return rows


def short_eclipse_clock(curves, folder):
    seed_period, seed_epoch = .456027, 3600.98275
    rows = []
    for sector, (t, _, corrected, good, known) in curves.items():
        use = good & ~known
        dt = (t[use]-seed_epoch+seed_period/2)%seed_period-seed_period/2
        flux = corrected[use]/np.median(corrected[use])
        bins = np.arange(-.12, .12, .003)
        medians = [np.median(flux[(dt >= left) & (dt < left+.003)]) for left in bins]
        trough = bins[np.argmin(medians)]
        near = abs(dt-trough) < .012
        a, b, _ = np.polyfit(dt[near], flux[near], 2)
        cycle = int(np.median(np.rint((t[use]-seed_epoch)/seed_period)))
        rows.append(dict(sector=sector, cycle=cycle, seed_oc_d=-b/(2*a)))
    cycles = [row["cycle"] for row in rows]
    offset, constant = np.polyfit(cycles, [row["seed_oc_d"] for row in rows], 1)
    period, epoch = seed_period+offset, seed_epoch+constant
    for row in rows:
        row.update(period_d=period, epoch_btjd=epoch,
                   oc_d=row["seed_oc_d"]-constant-offset*row["cycle"])
    csv_write(folder/"240799649-clock.csv", rows)
    fig, axes = plt.subplots(2, 1, figsize=(8, 5), sharex=True)
    edges = np.linspace(-.5, .5, 101)
    for sector, (t, raw, corrected, good, known) in curves.items():
        use = good & ~known
        phase = ((t[use]-epoch)/period+.5)%1-.5
        for ax, signal in zip(axes, (raw, corrected)):
            flux = 1000*(signal[use]/np.median(signal[use])-1)
            groups = [(phase >= a) & (phase < b) for a, b in zip(edges, edges[1:])]
            medians = [np.median(flux[g]) if g.any() else np.nan for g in groups]
            ax.plot((edges[:-1]+edges[1:])/2, medians, label=f"S{sector}")
    axes[0].set_ylabel("SAP (ppt)")
    axes[1].set_ylabel("Corrected (ppt)")
    axes[0].legend(ncols=4, fontsize=8)
    axes[1].set_xlabel("Phase relative to primary minimum")
    fig.suptitle(f"TIC 240799649 | globally folded at {period:.8f} d")
    fig.tight_layout()
    fig.savefig(folder/"plots/240799649-global-fold.png", dpi=110)
    plt.close(fig)


def common_windows(base):
    batches = [base/f"batch{number:02d}" for number in range(6,11)]
    source = {folder: csv_read(folder/"event-evidence.csv") for folder in batches}
    rows = [row for values in source.values() for row in values]
    for folder, values in source.items():
        matches = []
        for row in values:
            center = float(row["center_btjd"])
            for other in rows:
                if row["tic"] == other["tic"] or row["sector"] != other["sector"]:
                    continue
                dt = float(other["center_btjd"]) - center
                if abs(dt) <= .35:
                    matches.append(dict(tic=row["tic"], sector=row["sector"], camera=row["camera"],
                                        center_btjd=center, peer_tic=other["tic"], peer_camera=other["camera"],
                                        peer_center_btjd=other["center_btjd"], peer_minus_target_d=dt))
        csv_write(folder/"common-windows.csv", matches)


def review_batch(folder, root):
    data = root/"sky/data/qlp-sb-p20-60"
    scans = root/"Astra/made/binary-exploration-2026-11-04/bulk-results"
    flags = {}
    for row in csv_read(root/"sky/mixed-fold-2026-11-24/cadence-controls/flagged-exposures.csv"):
        flags.setdefault((int(row["sector"]), int(row["camera"])), []).append(int(row["cadenceno"]))
    plots = folder/"plots"
    plots.mkdir(exist_ok=True)
    alternate = folder/"hypotheses.csv"
    hypotheses = csv_read(alternate) if alternate.exists() else []
    evidence, predictions, spectra = [], [], []
    for target in csv_read(folder/"batch.csv"):
        tic = target["tic"]
        scan = json.loads((scans/f"{tic}.json").read_text(encoding="utf-8"))
        sectors = scan["files"]
        curves = {f["sector"]: load_curve(data/f"{tic}_s{f['sector']:03d}.fits", flags) for f in sectors}
        cameras = {f["sector"]:f["camera"] for f in sectors}
        epoch, width = float(target["best_window_btjd"]), float(target["best_window_duration_days"])
        events = [(f["sector"], w["time"], w["duration"], 1000*w["depth"])
                  for f in sectors for w in f.get("windows", [])
                  if (w["flag"] and w["kind"] == "dip") or w["time"] == epoch]
        panels = [(s, t, w, f"S{s} C{cameras[s]}  {t:.4f}  w={w:.2f} d") for s,t,w,_ in events]
        results = render_events(tic, panels, curves, plots/f"{tic}-events.png", "archived windows")
        for (sector, t, w, amplitude), result in zip(events, results):
            evidence.append(dict(tic=tic, sector=sector, camera=cameras[sector], center_btjd=t,
                                 width_d=w, scan_depth_ppt=amplitude, **result))
        periods = [(key, float(target[key])) for key in ("gaia_period_days","pilot_period_d","fold_screening_period_days")
                   if target[key]]
        clocks = [(label, p, *anchor_for_period(events, p, width)) for label,p in periods]
        clocks.extend([(h["name"], float(h["period_d"]), float(h["epoch_btjd"]), float(h["width_d"]))
                       for h in hypotheses if h["tic"] == tic])
        for label, period, center, window_width in clocks:
            windows = list(predicted(curves, center, period, window_width))
            samples = [(sector,t,window_width,f"S{sector} C{cameras[sector]}  {t:.4f}  cycle {cycle}")
                       for cycle,t,sector in windows if sector is not None]
            results = iter(render_events(tic, samples, curves, plots/f"{tic}-{label}.png", f"{label} P={period:.7f} d"))
            empty = {key:"" for key in measure(next(iter(curves.values())), epoch, width)[0]}
            for cycle, t, sector in windows:
                result = next(results) if sector is not None else empty
                coverage = "between_sectors"
                if sector is not None:
                    dense = min(result["core_fraction"],result["left_fraction"],result["right_fraction"]) >= .65
                    connected = result["core_max_spacing_d"] <= max(.025, .15*window_width)
                    coverage = "covered" if dense and connected else "partial"
                predictions.append(dict(tic=tic, hypothesis=label, period_d=period, epoch_btjd=center,
                                        cycle=cycle, predicted_btjd=t, sector=sector or "", coverage=coverage,
                                        width_d=window_width, **result))
        spectra.extend(short_periods(tic, curves, plots))
        if tic in SHORT_FOLDS:
            short_folds(tic, curves, plots, SHORT_FOLDS[tic])
        if tic in LOCAL_FITS:
            csv_write(folder/f"{tic}-local-centers.csv", fit_local_centers(curves, *LOCAL_FITS[tic]))
        if tic == "240799649":
            short_eclipse_clock(curves, folder)
        if tic == "128781401":
            peg_control(data, folder, flags)
    csv_write(folder/"event-evidence.csv", evidence)
    csv_write(folder/"predicted-windows.csv", predictions)
    csv_write(folder/"short-periods.csv", spectra)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("batches", nargs="*", type=int, default=list(range(6,11)))
    parser.add_argument("--root", type=Path, default=DEFAULT_ROOT)
    args = parser.parse_args()
    for number in args.batches:
        if number not in range(6,11):
            parser.error("This lane covers batches 06–10")
        review_batch(HERE.parent/f"batch{number:02d}", args.root)
    base = HERE.parent
    if all((base/f"batch{number:02d}"/"event-evidence.csv").exists() for number in range(6,11)):
        common_windows(base)


if __name__ == "__main__":
    main()
