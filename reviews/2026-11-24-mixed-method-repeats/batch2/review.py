"""Reproduce the batch-2 event and ephemeris evidence from local QLP files."""
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
from scipy.optimize import least_squares
from scipy.signal import find_peaks


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


def fit_eclipses(curves):
    guesses = {17: 1774.87, 56: 2837.13, 76: 3381.09, 83: 3562.45, 84: 3588.35}
    fits_rows = []
    for sector, guess in guesses.items():
        t, raw, _, good, flagged = curves[sector]
        nearby = good & ~flagged & (abs(t - guess) < 1.4)
        x = t[nearby] - guess
        z = 1000 * (raw[nearby] / np.median(raw[nearby]) - 1)

        def residual(parameters):
            const, slope, depth, offset, sigma = parameters
            return const + slope*x - depth*np.exp(-.5*((x-offset)/sigma)**2) - z

        fit = least_squares(residual, [1, 1, 10, 0, .4],
                            bounds=([-20, -20, 0, -.45, .1], [20, 20, 30, .45, 1]),
                            loss="soft_l1", f_scale=1)
        _, _, depth, offset, sigma = fit.x
        fits_rows.append(dict(sector=sector, fitted_btjd=guess+offset, fitted_peak_ppt=depth,
                              fitted_fwhm_d=2*np.sqrt(2*np.log(2))*sigma))
    centers = np.array([row["fitted_btjd"] for row in fits_rows])
    cycle = np.rint((centers - centers[0]) / 25.898712655).astype(int)
    period, epoch = np.polyfit(cycle, centers, 1)
    for row, number, oc in zip(fits_rows, cycle, centers - (epoch + period*cycle)):
        row.update(cycle=number, photometric_oc_d=oc)
    return fits_rows, period, epoch


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


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=HERE.parents[2] if (HERE.parents[2]/"sky/data/qlp-sb-p20-60").is_dir() else HERE.parent/"inputs/workspace")
    args = parser.parse_args()
    data = args.root / "sky/data/qlp-sb-p20-60"
    scans = args.root / "Astra/made/binary-exploration-2026-11-04/bulk-results"
    controls = args.root / "sky/mixed-fold-2026-11-24/cadence-controls/flagged-exposures.csv"
    flags = {}
    for row in csv_read(controls):
        key = int(row["sector"]), int(row["camera"])
        flags.setdefault(key, []).append(int(row["cadenceno"]))
    event_rows, predict_rows, alias_rows, short_rows = [], [], [], []
    hypotheses = csv_read(HERE / "hypotheses.csv")
    fits_dir = HERE / "plots"
    fits_dir.mkdir(exist_ok=True)
    for target in csv_read(HERE / "batch.csv"):
        tic = target["tic"]
        report = json.loads((scans / f"{tic}.json").read_text(encoding="utf-8"))
        curves = {int(file["sector"]): load_curve(data / f"{tic}_s{file['sector']:03d}.fits", flags)
                  for file in report["files"]}
        short_rows.extend(short_periods(tic, curves, fits_dir))
        short_fold_periods = {"63637170": .3974, "175252465": .3843, "451227585": .285,
                              "144522712": 2.27, "368198987": 1.495}
        if tic in short_fold_periods:
            short_folds(tic, curves, fits_dir, short_fold_periods[tic])
        sector_info = {int(f["sector"]): f for f in report["files"]}
        epoch = float(target["best_window_btjd"])
        period = float(target["gaia_period_days"])
        width = float(target["best_window_duration_days"])
        events = [(int(file["sector"]), w) for file in report["files"] for w in file.get("windows", [])
                  if w["kind"] == "dip" and (w["flag"] or w["time"] == epoch)]
        cols = min(4, len(events))
        nrows = (len(events) + cols - 1) // cols
        fig, panels = plt.subplots(nrows, cols, figsize=(cols * 3.35, nrows * 2.1), squeeze=False)
        for ax, (sector, w) in zip(panels.flat, events):
            label = f"S{sector} {w['time']:.4f} ± {w['duration']/2:.2f} d"
            result = add_panel(ax, curves[sector], w["time"], w["duration"], label)
            oc = (w["time"] - epoch + period/2) % period - period/2
            event_rows.append(dict(tic=tic, sector=sector, camera=sector_info[sector]["camera"],
                                   center_btjd=w["time"], width_d=w["duration"], gaia_oc_d=round(oc, 5),
                                   scan_depth_ppt=round(1000*w["depth"], 4), **result))
        for ax in list(panels.flat)[len(events):]:
            ax.set_visible(False)
        fig.suptitle(f"TIC {tic} • scan windows • raw blue, corrected orange • local residuals (ppt)")
        fig.tight_layout()
        fig.savefig(fits_dir / f"{tic}-events.png", dpi=110)
        plt.close(fig)
        # Cross-sector pairwise spacings and periods obtained by rounding to the Gaia cycle count.
        for i, (s1, w1) in enumerate(events):
            for s2, w2 in events[i + 1:]:
                if s1 == s2:
                    continue
                delta = abs(w2["time"] - w1["time"])
                cycles = round(delta / period)
                if cycles:
                    alias_rows.append(dict(tic=tic, first_sector=s1, second_sector=s2,
                                           first_btjd=w1["time"], second_btjd=w2["time"],
                                           delta_d=round(delta, 6), cycles_near_gaia=cycles,
                                           period_near_gaia_d=round(delta/cycles, 9),
                                           gaia_time_mismatch_d=round(delta-cycles*period, 6)))
        eph = [("Gaia_from_scan", epoch, period, width)]
        eph += [(h["name"], float(h["epoch_btjd"]), float(h["period_d"]), float(h["width_d"]))
                for h in hypotheses if h["tic"] == tic]
        if tic == "405590521":
            fit_rows, fit_period, fit_epoch = fit_eclipses(curves)
            csv_write(HERE / "405590521-centers.csv", fit_rows)
            eph.extend([("photometric", fit_epoch, fit_period, 1.03),
                        ("photometric-half-period", fit_epoch, fit_period/2, 1.03)])
        for name, center_epoch, test_period, test_width in eph:
            windows = list(predicted(curves, center_epoch, test_period, test_width))
            plot_windows = [(i, center, sector) for i, center, sector in windows if sector is not None]
            nrows = (len(plot_windows) + 3) // 4
            fig, panels = plt.subplots(nrows, 4, figsize=(13.4, nrows * 2.1), squeeze=False)
            plot_axes = iter(panels.flat)
            empty = {key: "" for key in measure(next(iter(curves.values())), epoch, width)[0]}
            for cycle, center, sector in windows:
                if sector is None:
                    result = empty
                    coverage = "between_sectors"
                else:
                    result = add_panel(next(plot_axes), curves[sector], center, test_width,
                                       f"S{sector} {center:.4f} • cycle {cycle}")
                    enough_points = min(result["core_fraction"], result["left_fraction"],
                                        result["right_fraction"]) >= .65
                    small_gap = result["core_max_spacing_d"] <= max(.025, .15*test_width)
                    coverage = "covered" if enough_points and small_gap else "partial"
                predict_rows.append(dict(tic=tic, hypothesis=name, period_d=test_period, cycle=cycle,
                                         predicted_btjd=round(center, 7), sector=sector or "",
                                         coverage=coverage, width_d=test_width, **result))
            for ax in plot_axes:
                ax.set_visible(False)
            fig.suptitle(f"TIC {tic} • {name} • P = {test_period:.8f} d • raw blue, corrected orange")
            fig.tight_layout()
            fig.savefig(fits_dir / f"{tic}-{name}.png", dpi=110)
            plt.close(fig)
    csv_write(HERE / "event-evidence.csv", event_rows)
    csv_write(HERE / "predicted-windows.csv", predict_rows)
    csv_write(HERE / "pair-spacings.csv", alias_rows)
    csv_write(HERE / "short-periods.csv", short_rows)


if __name__ == "__main__":
    main()
