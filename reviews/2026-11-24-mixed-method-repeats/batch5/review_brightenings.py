"""Inspect batch 5 SAP brightenings against QLP correction, background and Gaia timing."""
import argparse
import json
import sys
from pathlib import Path

from astropy.io import fits
from astropy.time import Time
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage import gaussian_filter1d
from scipy.signal import find_peaks, peak_widths

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "batch2"))
from review import csv_read, csv_write, load_curve, measure, predicted, short_periods


def ancillary(path):
    with fits.open(path) as hdu:
        data = hdu[1].data
        fields = ["TIME", "SAP_BKG", "SAP_X", "SAP_Y"]
        return tuple(np.asarray(data[name], dtype=float) if name in data.names
                     else np.full(len(data), np.nan) for name in fields)


def panel(ax, curve, auxiliary, center, width, title):
    m, traces = measure(curve, center, width)
    t, _, _, good, known = curve
    dx = t - center
    extent = max(2.6 * width, 0.16)
    close = (abs(dx) < extent) & good
    for signal, color in zip(traces, ("#254e87", "#df7b1f")):
        ax.plot(dx[close & ~known], signal[close & ~known], ".", c=color, ms=2)
        ax.plot(dx[close & known], signal[close & known], "x", c="red", ms=4)
    aux_time, bkg, x, y = auxiliary
    ax2 = ax.twinx()
    for label, signal, color in zip(("bkg", "x", "y"), (bkg, x, y), ("#478154", "#a179b6", "#a49540")):
        dt = aux_time - center
        local = (abs(dt) < extent) & np.isfinite(signal)
        if local.sum() < 3:
            m[f"{label}_core_wing_z"] = ""
            continue
        minimum, maximum = np.quantile(signal[local], [.005, .995])
        if maximum > minimum:
            ax2.plot(dt[local], (signal[local]-minimum)/(maximum-minimum), ".", c=color, alpha=.4, ms=1)
        wing = local & (abs(dt) >= .5*width) & (abs(dt) <= 1.5*width)
        core = local & (abs(dt) < .5*width)
        value = ""
        if wing.sum() >= 3 and core.sum() >= 3:
            level = np.median(signal[wing])
            scatter = 1.4826*np.median(abs(signal[wing]-level))
            if scatter > 0:
                value = round((np.median(signal[core])-level)/scatter, 3)
        m[f"{label}_core_wing_z"] = value
    ax2.set(ylim=(-.1, 1.1), yticks=[])
    ax.set(xlim=(-extent, extent), title=title)
    ax.title.set_fontsize(8)
    ax.tick_params(labelsize=7)
    ax.axhline(0, c="gray", lw=.5)
    ax.axvspan(-width/2, width/2, color="gray", alpha=.12)
    return m


def grid(count):
    figure, axes = plt.subplots((count+3)//4, 4, figsize=(13.5, 2.1*((count+3)//4)), squeeze=False)
    return figure, iter(axes.flat)


def save(figure, axes, path, title):
    for ax in axes:
        ax.set_visible(False)
    figure.suptitle(title + " | SAP blue, corrected orange, background green, X/Y purple/gold")
    figure.tight_layout()
    figure.savefig(path, dpi=110)
    plt.close(figure)


def pulse_train(curves, cameras, plot_dir):
    rows = []
    figure, panels = plt.subplots(len(curves), 1, figsize=(11, 8), squeeze=False)
    for ax, (sector, (t, raw, corrected, good, known)) in zip(panels.flat, curves.items()):
        use = good & ~known
        rejected = ~use
        rejected_flux = 1000 * (raw[rejected] / np.median(raw[use]) - 1)
        ax.plot(t[rejected], rejected_flux, ".", c=".70", ms=2, label="Excluded SAP")
        t, raw, corrected = t[use], raw[use], corrected[use]
        raw = 1000 * (raw / np.median(raw) - 1)
        corrected = 1000 * (corrected / np.median(corrected) - 1)
        cadence = np.median(np.diff(t))
        smooth = gaussian_filter1d(raw, .045 / cadence)
        peaks, props = find_peaks(smooth, prominence=4, height=5, distance=1/cadence)
        _, _, left, right = peak_widths(smooth, peaks, rel_height=.5)
        ax.plot(t, raw, ".", c="#254e87", ms=2, label="SAP")
        ax.plot(t, corrected, ".", c="#df7b1f", ms=1.4, label="QLP corrected")
        ax.plot(t[peaks], smooth[peaks], "+", c="#333333", label="Measured peaks")
        ax.set(ylim=(-3, 12), ylabel=f"S{sector} (ppt)")
        for i, peak in enumerate(peaks):
            center = t[peak]
            use_core = abs(t-center) < .15
            gap = max(np.diff(np.r_[center-.15, t[use_core], center+.15]))
            samples = np.arange(len(t))
            fwhm = np.interp(right[i], samples, t) - np.interp(left[i], samples, t)
            rows.append(dict(sector=sector, camera=cameras[sector], peak_btjd=center,
                             smoothed_peak_ppt=props["peak_heights"][i],
                             prominence_ppt=props["prominences"][i], width_d=fwhm,
                             central_gap_d=gap, used_in_fit=gap <= max(.04, 1.6*cadence)))
    times = np.array([row["peak_btjd"] for row in rows])
    cycles = np.rint((times-times[0])/5.3053).astype(int)
    use = np.array([row["used_in_fit"] for row in rows])
    period, epoch = np.polyfit(cycles[use], times[use], 1)
    train = use & np.array([row["sector"] < 82 for row in rows])
    early_period, early_epoch = np.polyfit(cycles[train], times[train], 1)
    width = float(np.median([r["width_d"] for r in rows if r["used_in_fit"]]))
    for row, cycle in zip(rows, cycles):
        sector = row["sector"]
        row.update(cycle=cycle, fitted_oc_d=row["peak_btjd"]-epoch-cycle*period,
                   early_fit_oc_d=row["peak_btjd"]-early_epoch-cycle*early_period)
    for ax, (sector, curve) in zip(panels.flat, curves.items()):
        for _, center, _ in predicted({sector: curve}, epoch, period, width):
            ax.axvline(center, c=".55", lw=.7)
    panels[0, 0].legend(loc="upper right")
    panels[-1, 0].set_xlabel("BTJD")
    figure.suptitle(f"TIC 287857379 pulse train at {period:.8f} d")
    figure.tight_layout()
    figure.savefig(plot_dir/"287857379-pulse-train.png", dpi=120)
    plt.close(figure)
    csv_write(HERE/"287857379-pulses.csv", rows)
    return period, epoch, width


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=HERE.parents[2] if (HERE.parents[2]/"sky/data/qlp-sb-p20-60").is_dir() else HERE.parent/"inputs/workspace")
    args = parser.parse_args()
    data = args.root / "sky/data/qlp-sb-p20-60"
    scans = args.root / "Astra/made/binary-exploration-2026-11-04/bulk-results"
    flags = {}
    for row in csv_read(args.root / "sky/mixed-fold-2026-11-24/cadence-controls/flagged-exposures.csv"):
        flags.setdefault((int(row["sector"]), int(row["camera"])), []).append(int(row["cadenceno"]))
    gaia = {row["source_id"]: row for row in csv_read(data / "nss.csv")}
    event_rows, forecast_rows, gaia_rows, short_rows = [], [], [], []
    plot_dir = HERE / "plots"
    plot_dir.mkdir(exist_ok=True)
    aliases = csv_read(HERE / "hypotheses.csv")
    for target in csv_read(HERE / "batch.csv"):
        tic = target["tic"]
        report = json.loads((scans/f"{tic}.json").read_text(encoding="utf-8"))
        paths = {f["sector"]: data/f"{tic}_s{f['sector']:03d}.fits" for f in report["files"]}
        cameras = {f["sector"]: f["camera"] for f in report["files"]}
        curves = {s: load_curve(path, flags) for s, path in paths.items()}
        aux = {s: ancillary(path) for s, path in paths.items()}
        short_rows.extend(short_periods(tic, curves, plot_dir))
        anchor = float(target["best_window_btjd"])
        width = float(target["best_window_duration_days"])
        orbit = gaia[target["gaia_dr3"]]
        period = float(orbit["period"])
        at = Time(anchor+2457000, format="jd", scale="tdb").tcb.jd
        ref = Time(2016, format="jyear", scale="tcb").jd
        periastron_ref = ref + float(orbit["t_periastron"])
        orbit_number = round((at-periastron_ref)/period)
        peri = Time(periastron_ref+orbit_number*period, format="jd", scale="tcb").tdb.jd - 2457000
        period_tdb = Time(periastron_ref+(orbit_number+1)*period, format="jd", scale="tcb").tdb.jd - 2457000 - peri
        gaia_rows.append(dict(tic=tic, period_d=period, eccentricity=orbit["eccentricity"],
                              eccentricity_error=orbit["eccentricity_error"], nominal_periastron_btjd=peri,
                              anchor_minus_periastron_d=anchor-peri,
                              independent_formal_timing_scale_d=np.hypot(orbit_number*float(orbit["period_error"]),
                                                                         float(orbit["t_periastron_error"]))))
        selected = [(f["sector"], w) for f in report["files"] for w in f.get("windows", [])
                    if (w["kind"] == "brightening" and w["flag"]) or w["time"] == anchor]
        figure, axes = grid(len(selected))
        for s, w in selected:
            center = w["time"]
            dt = (center-peri+period/2)%period-period/2
            mr = panel(next(axes), curves[s], aux[s], center, w["duration"],
                       f"S{s} C{cameras[s]} | {center:.4f} | {w['kind']}")
            event_rows.append(dict(tic=tic, sector=s, camera=cameras[s], kind=w["kind"], btjd=center,
                                   width_d=w["duration"], scan_excess_ppt=-1000*w["depth"],
                                   gaia_periastron_oc_d=dt, anchor=center == anchor, **mr))
        save(figure, axes, plot_dir/f"{tic}-events.png", f"TIC {tic} scan windows")
        ephemerides = [("Gaia_anchor", anchor, period_tdb, width), ("Gaia_periastron", peri, period_tdb, width)]
        ephemerides += [(a["name"], float(a["epoch_btjd"]), float(a["period_d"]), float(a["width_d"]))
                       for a in aliases if a["tic"] == tic]
        if tic == "287857379":
            pulse_period, pulse_epoch, pulse_width = pulse_train(curves, cameras, plot_dir)
            ephemerides.extend([("photometric_pulse", pulse_epoch, pulse_period, pulse_width),
                                ("photometric_half_period", pulse_epoch, pulse_period/2, pulse_width)])
        for name, epoch, test_p, test_w in ephemerides:
            windows = list(predicted(curves, epoch, test_p, test_w))
            observed = [(k, t, s) for k, t, s in windows if s is not None]
            if not observed:
                continue
            figure, axes = grid(len(observed))
            fresh = {}
            for k, t, s in observed:
                m = panel(next(axes), curves[s], aux[s], t, test_w,
                          f"S{s} C{cameras[s]} | {t:.4f} | cycle {k}")
                well_covered = (min(m["core_fraction"], m["left_fraction"], m["right_fraction"]) >= .65
                                and m["core_max_spacing_d"] <= max(.025, .15*test_w))
                fresh[k, s] = ("covered" if well_covered else "partial", m)
            empty = {key: "" for key in next(iter(fresh.values()))[1]}
            for k, t, s in windows:
                coverage, values = fresh.get((k, s), ("between_sectors", empty))
                forecast_rows.append(dict(tic=tic, hypothesis=name, period_d=test_p, epoch_btjd=epoch,
                                          cycle=k, predicted_btjd=t, sector=s or "", coverage=coverage,
                                          width_d=test_w, **values))
            save(figure, axes, plot_dir/f"{tic}-{name}.png", f"TIC {tic} {name} at {test_p:.6f} d")
    csv_write(HERE/"event-evidence.csv", event_rows)
    csv_write(HERE/"predicted-windows.csv", forecast_rows)
    csv_write(HERE/"gaia-periastron.csv", gaia_rows)
    csv_write(HERE/"short-periods.csv", short_rows)


if __name__ == "__main__":
    main()
