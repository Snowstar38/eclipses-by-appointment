"""Review QLP SAP and corrected flux for lane 06?10 using fixed window trials.

The QLP helpers are adapted from the mixed-repeats batch 2 review.
"""
import argparse
import csv
import json
from pathlib import Path

from astropy.io import fits
from astropy.timeseries import LombScargle
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks
from scipy.optimize import least_squares

HERE = Path(__file__).resolve().parent


def csv_read(path):
    with path.open(newline="", encoding="utf-8") as stream:
        return list(csv.DictReader(stream))


def csv_write(path, rows):
    with path.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def load_curve(path, flagged):
    with fits.open(path) as hdu:
        data = hdu[1].data
        header = hdu[0].header
        sector, camera = header["SECTOR"], header["CAMERA"]
        t = np.array(data["TIME"])
        raw = np.array(data["SAP_FLUX"])
        column = "KSPSAP_FLUX" if "KSPSAP_FLUX" in data.names else "DET_FLUX"
        corrected = np.array(data[column])
        q = np.array(data["QUALITY"])
        cadence = np.array(data["CADENCENO"])
    known = np.isin(cadence, tuple(flagged.get((sector, camera), ())))
    valid = np.isfinite(t) & np.isfinite(raw) & np.isfinite(corrected)
    return t[valid], raw[valid], corrected[valid], q[valid] == 0, known[valid]


def measure(curve, center, width):
    t, raw, corrected, good, flagged = curve
    dt = t - center
    use = good & ~flagged
    core = use & (abs(dt) < width / 2)
    left = use & (dt >= -1.5 * width) & (dt <= -width / 2)
    right = use & (dt >= width / 2) & (dt <= 1.5 * width)
    step = float(np.median(np.diff(t)))
    result = dict(core_n=int(core.sum()), left_n=int(left.sum()), right_n=int(right.sum()),
                  core_fraction=round(min(1.0, core.sum() * step / width), 3),
                  left_fraction=round(min(1.0, left.sum() * step / width), 3),
                  right_fraction=round(min(1.0, right.sum() * step / width), 3),
                  core_max_spacing_d=round(float(np.max(np.diff(np.r_[-width/2, dt[core], width/2]))), 5),
                  control_hits=int(np.sum(flagged & (abs(dt) < width/2))))
    traces = []
    for name, flux in (("raw", raw), ("corrected", corrected)):
        depth = scatter = np.nan
        baseline = float(np.median(flux[use]))
        trend = np.full_like(t, baseline)
        if left.sum() >= 2 and right.sum() >= 2:
            x_left, x_right = np.median(dt[left]), np.median(dt[right])
            f_left, f_right = np.median(flux[left]), np.median(flux[right])
            baseline = float(np.interp(0, [x_left, x_right], [f_left, f_right]))
            trend = (f_right-f_left)/(x_right-x_left)*(dt-x_left)+f_left
        residual = 1000 * (flux - trend) / baseline
        if core.any() and left.sum() >= 2 and right.sum() >= 2:
            depth = -float(np.median(residual[core]))
            side = residual[left | right]
            scatter = 1.4826 * float(np.median(abs(side - np.median(side))))
        result[f"{name}_depth_ppt"] = round(depth, 4)
        result[f"{name}_wing_mad_ppt"] = round(scatter, 4)
        traces.append(residual)
    return result, traces


def add_panel(ax, curve, center, width, title):
    evidence, (raw, corrected) = measure(curve, center, width)
    t, _, _, good, flagged = curve
    dt = t - center
    near = abs(dt) < max(width * 2.7, 0.22)
    for y, color in ((raw, "#284e91"), (corrected, "#e07a20")):
        ax.plot(dt[near & good & ~flagged], y[near & good & ~flagged], ".", c=color, ms=2)
        ax.plot(dt[near & good & flagged], y[near & good & flagged], "x", c="red", ms=5)
    ax.axvspan(-width / 2, width / 2, color="#dadde1", alpha=.5, zorder=0)
    ax.axhline(0, color="gray", lw=.5)
    ax.set_xlim(-max(width * 2.7, 0.22), max(width * 2.7, 0.22))
    ax.set_title(title, fontsize=8)
    ax.tick_params(labelsize=7)
    return evidence


def predicted(curves, epoch, period, width):
    first = min(curve[0][0] for curve in curves.values())
    last = max(curve[0][-1] for curve in curves.values())
    k_min = int(np.floor((first - epoch) / period))
    k_max = int(np.ceil((last - epoch) / period))
    for cycle in range(k_min, k_max + 1):
        center = epoch + cycle * period
        if not first - width/2 <= center <= last + width/2:
            continue
        matches = [sector for sector, curve in curves.items()
                   if curve[0][0] <= center + width and curve[0][-1] >= center - width]
        if not matches:
            yield cycle, center, None
        for sector in matches:
            yield cycle, center, sector


def short_periods(tic, curves, plot_dir):
    rows = []
    fig, axes = plt.subplots(1, 2, figsize=(10, 3), sharex=True)
    for sector, (t, raw, corrected, good, flagged) in curves.items():
        use = good & ~flagged
        for ax, z, name in zip(axes, (raw, corrected), ("raw", "corrected")):
            ls = LombScargle(t[use], z[use])
            freq, power = ls.autopower(minimum_frequency=.07, maximum_frequency=8, samples_per_peak=8)
            peaks = find_peaks(power)[0]
            strongest = peaks[np.argsort(power[peaks])[-3:]][::-1]
            for rank, index in enumerate(strongest, 1):
                rows.append(dict(tic=tic, sector=sector, flux=name, rank=rank,
                                 period_d=round(1/freq[index], 7), power=round(power[index], 7)))
            ax.plot(1/freq, power, lw=.65, alpha=.8, label=str(sector))
            ax.set_xscale("log")
            ax.set(title=name, xlabel="Period (days)", ylabel="Lomb–Scargle power")
    axes[1].legend(title="Sector", fontsize="x-small", ncol=2)
    fig.suptitle(f"TIC {tic} • sector periodograms")
    fig.tight_layout()
    fig.savefig(plot_dir / f"{tic}-short-periods.png", dpi=110)
    plt.close(fig)
    return rows


def short_folds(tic, curves, plot_dir, period):
    fig, axes = plt.subplots(len(curves), 2, figsize=(9, 1.55*len(curves)), squeeze=False)
    for axs, (sector, (t, raw, corrected, good, flagged)) in zip(axes, curves.items()):
        use = good & ~flagged
        phase = ((t[use] - t[use][0]) / period) % 1
        bins = np.linspace(0, 1, 41)
        for ax, flux in zip(axs, (raw[use], corrected[use])):
            flux = 1000 * (flux / np.median(flux) - 1)
            medians = [np.median(flux[group]) if group.any() else np.nan
                       for group in ((phase >= x) & (phase < y) for x, y in zip(bins, bins[1:]))]
            ax.plot(phase, flux, ".", c="#6f8195", ms=1, alpha=.2)
            ax.plot((bins[:-1]+bins[1:])/2, medians, c="#08355b", lw=1)
            ax.set_ylabel(f"S{sector} (ppt)", fontsize=8)
            ax.tick_params(labelsize=7)
    axes[0, 0].set_title("SAP")
    axes[0, 1].set_title("QLP corrected")
    for ax in axes[-1]:
        ax.set_xlabel("Phase from first usable cadence in each sector")
    fig.suptitle(f"TIC {tic} • short-period comparison at {period:.4f} d")
    fig.tight_layout()
    fig.savefig(plot_dir / f"{tic}-short-fold.png", dpi=110)
    plt.close(fig)


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


def anchor_for_period(events, period, nominal_width):
    """Find a phase among scan times supported by the most distinct sectors."""
    def support(event):
        _, t, width, amplitude = event
        nearby = {sector for sector, center, other_width, _ in events
                  if abs((center-t+period/2)%period-period/2) < max(.05, min(.65, (width+other_width)/3))}
        return len(nearby), -abs(np.log(width/nominal_width)), amplitude
    _, center, width, _ = max(events, key=support)
    return center, width


def fit_clock(curves, trials):
    """Fit Gaussian timing profiles over a local linear SAP baseline."""
    rows = []
    period_seed = float(trials[0]["period_seed_d"])
    fit_radius = float(trials[0]["fit_radius_d"])
    for row in trials:
        sector, guess = int(row["sector"]), float(row["center_btjd"])
        t, raw, _, good, flagged = curves[sector]
        use = good & ~flagged & (abs(t-guess) < fit_radius)
        x = t[use]-guess
        z = 1000*(raw[use]/np.median(raw[use])-1)

        def residual(parameters):
            level, slope, depth, offset, sigma = parameters
            return level+slope*x-depth*np.exp(-.5*((x-offset)/sigma)**2)-z

        fit = least_squares(residual, [1, 1, 9, 0, .1], loss="soft_l1",
                            bounds=([-20, -20, 1, -.13, .035], [20, 20, 22, .13, .28]))
        _, _, depth, offset, sigma = fit.x
        rows.append(dict(sector=sector, guess_btjd=guess, fit_btjd=guess+offset,
                         peak_depth_ppt=depth, fwhm_d=2.355*sigma))
    t = np.array([row["fit_btjd"] for row in rows])
    cycles = np.rint((t-t[0])/period_seed).astype(int)
    period, epoch = np.polyfit(cycles, t, 1)
    width = float(np.median([row["fwhm_d"] for row in rows]))
    for row, k, oc in zip(rows, cycles, t-epoch-period*cycles):
        row.update(cycle=k, fit_oc_d=oc, period_d=period, epoch_btjd=epoch, width_d=width)
    return rows, (period, epoch, width)


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
        if matches:
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

    fold_path = folder/"short-fold-trials.csv"
    fold_trials = {row["tic"]:float(row["period_d"]) for row in csv_read(fold_path)} if fold_path.exists() else {}
    center_path = folder/"center-trials.csv"
    center_trials = csv_read(center_path) if center_path.exists() else []
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
                   if target.get(key)]
        clocks = [(label, p, *anchor_for_period(events, p, width)) for label,p in periods]
        clocks.extend([(h["name"], float(h["period_d"]), float(h["epoch_btjd"]), float(h["width_d"]))
                       for h in hypotheses if h["tic"] == tic])
        seeds = [r for r in center_trials if r["tic"] == tic]
        if seeds:
            fits_rows, (p, e, w) = fit_clock(curves, seeds)
            csv_write(folder/f"{tic}-centers.csv", fits_rows)
            clocks.extend([("photometric_clock",p,e,w), ("photometric_half_period",p/2,e,w)])
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
        if tic in fold_trials:
            short_folds(tic, curves, plots, fold_trials[tic])
    csv_write(folder/"event-evidence.csv", evidence)
    csv_write(folder/"predicted-windows.csv", predictions)
    csv_write(folder/"short-periods.csv", spectra)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("batches", nargs="*", type=int, default=list(range(6,11)))
    parser.add_argument("--root", type=Path, default=Path.cwd())
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
