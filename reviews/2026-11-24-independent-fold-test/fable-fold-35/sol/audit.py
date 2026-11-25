"""Independent eclipse-clock audit from SPOC cadence NPZ files."""
import argparse
import csv
from pathlib import Path

import numpy as np
from astropy.timeseries import BoxLeastSquares
from scipy.ndimage import percentile_filter, uniform_filter1d


HERE = Path(__file__).resolve().parent
DEFAULT_CACHE = HERE.parents[2] / "data" / "fable52-ffi-tce-2026-11-24" / "cadences"


def robust_sigma(values):
    return 1.4826 * np.median(np.abs(values - np.median(values)))


def load_cadences(cache, tic, channel="pdc"):
    chunks = []
    for path in sorted(cache.glob(f"{tic}-*.npz")):
        sector = int(path.stem.split("-")[-1])
        with np.load(path) as data:
            t, flux = data["t"], data[channel].astype(float)
        good = np.isfinite(t) & np.isfinite(flux) & (flux > 0)
        t, flux = t[good], flux[good]
        order = np.argsort(t)
        t, flux = t[order], flux[order]
        for block in np.split(np.arange(len(t)), np.flatnonzero(np.diff(t) > 0.35) + 1):
            if len(block) < 20:
                continue
            time, f = t[block], flux[block]
            cadence = np.median(np.diff(time))
            size = min(len(f) // 2 * 2 - 1, 2 * int(1.1 / cadence) + 1)
            baseline = uniform_filter1d(percentile_filter(f, 65, size=size, mode="nearest"), max(1, size // 4))
            y = 1000 * (f / baseline - 1)
            # Search on hourly medians so late high-cadence sectors do not dominate.
            index = np.floor((time - time[0]) * 24).astype(int)
            bins = np.split(np.arange(len(time)), np.flatnonzero(np.diff(index)) + 1)
            x = np.array([np.median(time[b]) for b in bins])
            v = np.array([np.median(y[b]) for b in bins])
            if len(v) >= 12:
                sigma = max(0.025, robust_sigma(v), robust_sigma(np.diff(v)) / np.sqrt(2))
                chunks.append((x, v, np.full(len(v), sigma), np.full(len(v), sector)))
    if not chunks:
        return None
    t, v, s, sectors = [np.concatenate(col) for col in zip(*chunks)]
    order = np.argsort(t)
    return t[order], v[order], s[order], sectors[order]


def event_windows(data, period, epoch, duration, details=None, reference_depth=None):
    t, y, error, sectors = data
    number = np.round((t - epoch) / period).astype(int)
    events = []
    gap_count = 0
    expected = sum(
        max(0, int(np.floor((t[sectors == sector].max() - epoch) / period))
            - int(np.ceil((t[sectors == sector].min() - epoch) / period)) + 1)
        for sector in np.unique(sectors)
    )
    radius = min(2.6 * duration, 0.43 * period)
    core = max(duration * 0.40, 0.040)
    for n in np.unique(number):
        center = epoch + n * period
        i, j = np.searchsorted(t, [center - radius, center + radius])
        dt = t[i:j] - center
        middle = np.abs(dt) <= core
        left = dt < -max(duration * 0.66, core)
        right = dt > max(duration * 0.66, core)
        if (sum(middle) < max(1, int(core * 24)) or sum(left) < 2 or sum(right) < 2
                or min(abs(dt[middle])) > 0.05):
            if t[0] <= center <= t[-1] and any(
                t[sectors == sector].min() <= center <= t[sectors == sector].max()
                for sector in np.unique(sectors[i:j])
            ):
                gap_count += 1
            continue
        window_y = y[i:j]
        baseline = (np.median(window_y[left]) + np.median(window_y[right])) / 2
        depth = baseline - np.median(window_y[middle])
        local_noise = max(np.median(error[i:j]), robust_sigma(window_y[left | right]))
        uncertainty = local_noise * np.sqrt(1 / sum(middle) + 1 / sum(left | right))
        events.append((n, center, int(sectors[i:j][middle][0]), depth, uncertainty))
    if not events:
        return dict(expected=expected, covered=0, gap=max(expected, gap_count), hits=0, empty=0,
                    sectors=0, depth=np.nan, snr=0, odd_even=np.nan, fraction=0)
    a = np.array(events)
    depth, uncertainty = a[:, 3], a[:, 4]
    hits = depth > 3 * uncertainty
    # Bootstrap-like robust comparison: use the median of individual ≥3 sigma hits.
    reference = np.median(depth[hits]) if hits.any() else np.median(depth)
    usable_reference = hits.any() or reference_depth is not None
    if reference_depth is not None:
        reference = reference_depth
    empty = (depth + 2 * uncertainty < 0.45 * reference) & ~hits & usable_reference
    if details is not None:
        for i, (n, center, sector, dep, unc) in enumerate(events):
            details.append(dict(cycle=n, center_btjd=center, sector=sector, depth_ppt=dep,
                                uncertainty_ppt=unc, hit=bool(hits[i]), empty=bool(empty[i])))
    weights = 1 / uncertainty ** 2
    combined_snr = np.sum(depth * weights) / np.sqrt(np.sum(weights))
    odd, even = (depth[(a[:, 0] % 2) == parity] for parity in (1, 0))
    odd_even = np.median(odd) - np.median(even) if len(odd) and len(even) else np.nan
    return dict(expected=expected, covered=len(a), gap=max(expected - len(a), gap_count, 0),
                hits=int(hits.sum()), empty=int(empty.sum()), sectors=len(np.unique(a[hits, 2])),
                depth=float(np.median(depth)), snr=float(combined_snr),
                odd_even=float(odd_even), fraction=float(hits.sum() / len(a)))


def phase_shape(data, period, epoch, duration):
    t, y, _, _ = data
    dt = (t - epoch + period / 2) % period - period / 2
    regions = [
        (np.abs(dt) < 0.25 * duration),
        (dt >= 0.25 * duration) & (dt < 0.55 * duration),
        (-dt >= 0.25 * duration) & (-dt < 0.55 * duration),
        (np.abs(dt) > 0.7 * duration) & (np.abs(dt) < 1.5 * duration),
        (np.abs(np.abs(dt) - period / 2) < 0.25 * duration),
    ]
    center, right, left, wing, secondary = [np.median(y[mask]) if np.any(mask) else np.nan for mask in regions]
    return dict(center_ppt=wing-center, ingress_ppt=wing-left, egress_ppt=wing-right,
                phase_half_ppt=wing-secondary)


def search_candidates(data):
    t, y, error, _ = data
    pivot = t.min()
    duration_grid = np.array([0.09, 0.17, 0.30, 0.52])
    search = BoxLeastSquares(t-pivot, np.clip(y, -100 * error, 4 * error), dy=error)
    # Frequency spacing broad enough for a 0.17 d eclipse across the available baseline.
    df = 0.12 / (np.ptp(t) * 18)
    short_frequencies = np.arange(1/18, 1/0.60 + df, df)
    long_frequencies = np.arange(1/40, 1/18, 0.45 * df)
    frequencies = np.concatenate((long_frequencies, short_frequencies))
    power = search.power(1 / frequencies, duration_grid, objective="snr", oversample=3)
    ordered = np.argsort(power.power)[::-1]
    picked = []
    candidates = []
    for i in ordered:
        frequency = frequencies[i]
        if any(abs(frequency - prev) < 2 * df for prev in picked):
            continue
        picked.append(frequency)
        period = float(power.period[i])
        epoch = float(power.transit_time[i] + pivot)
        duration = float(power.duration[i])
        metrics = event_windows(data, period, epoch, duration)
        # Rank by repeated clean windows instead of a single unusually deep event.
        score = (np.sqrt(metrics["hits"]) * metrics["fraction"] *
                 (1 + 0.15 * min(metrics["sectors"], 5)) /
                 (1 + metrics["empty"] / max(1, metrics["hits"])))
        candidates.append((score, period, epoch, duration, float(power.power[i]), metrics))
        if len(candidates) == 18:
            break
    return sorted(candidates, reverse=True)


def fixed_period(data, period, duration):
    t, y, error, _ = data
    bls = BoxLeastSquares(t-t[0], np.clip(y, -100 * error, 4 * error), dy=error)
    p = bls.power([period], [min(duration, 0.45 * period)], objective="snr", oversample=8)
    return float(p.transit_time[0] + t[0]), float(p.duration[0])


def relation(alternate, recorded, baseline, duration):
    ratio = alternate / recorded
    for harmonic in (1, 0.5, 2, 1/3, 3):
        if abs(1 / alternate - 1 / (recorded * harmonic)) * baseline < duration / alternate:
            return {1: "same", 0.5: "half", 2: "double", 1/3: "third", 3: "triple"}[harmonic]
    return "distinct"


def summarize(metrics):
    return f'{metrics["hits"]}/{metrics["covered"]} significant windows, {metrics["empty"]} sensitive empty, {metrics["sectors"]} sectors with hits'


def verdict(rec, alt, rel, segs):
    strong = alt["hits"] >= 3 and alt["sectors"] >= 2 and alt["fraction"] >= 0.65 and alt["empty"] <= 1
    repeat = rec["hits"] >= 3 and rec["sectors"] >= 2 and rec["fraction"] >= 0.65 and rec["empty"] <= 1
    if strong and rel != "same" and (not repeat or alt["empty"] < rec["empty"]):
        return "alternate-clock", f"Independent {rel} clock has {summarize(alt)}. Recorded clock has {summarize(rec)}."
    if repeat:
        return "recorded-clock-supported", f"Recorded clock has {summarize(rec)}. Independent clock ({rel}) has {summarize(alt)}."
    if strong and rel == "same":
        return "recorded-period-rephased", f"Independent epoch at the same period has {summarize(alt)}. Recorded epoch has {summarize(rec)}."
    if segs < 2 or rec["covered"] < 2:
        return "coverage-limited", f"Clock has {summarize(rec)} over {segs} sectors. Independent clock has {summarize(alt)}."
    if rec["empty"] >= 2:
        return "recorded-clock-inconsistent", f"Recorded clock has {summarize(rec)}. Independent clock has {summarize(alt)}."
    return "inconclusive", f"Recorded clock has {summarize(rec)}. Independent clock ({rel}) has {summarize(alt)}."


def prefix(name, values):
    return {f"{name}_{key}": value for key, value in values.items()}


def audit(row, cache):
    tic, group = row["tic"], int(row["group"])
    meta = dict(tic=tic, group=group)
    period, epoch, duration = (float(row[key]) for key in ("period_d", "t0_btjd", "duration_h"))
    duration /= 24
    data = load_cadences(cache, tic)
    if data is None:
        return dict(**meta, outcome="no-cache", why="No usable PDC windows"), []
    t, _, _, sectors = data
    baseline = np.ptp(t)
    segs = len(np.unique(sectors))
    recorded = event_windows(data, period, epoch, duration)
    shifted_epoch, shifted_duration = fixed_period(data, period, duration)
    shifted = event_windows(data, period, shifted_epoch, shifted_duration)
    candidates = search_candidates(data)
    _, ap, ae, ad, asnr, alternate = candidates[0]
    rel = relation(ap, period, baseline, ad)
    outcome, why = verdict(recorded, alternate, rel, segs)
    sap = load_cadences(cache, tic, "sap")
    output = dict(**meta, outcome=outcome, why=why, sectors=segs, baseline_d=baseline,
                  recorded_period_d=period, recorded_epoch_btjd=epoch,
                  recorded_duration_h=duration * 24, alternate_period_d=ap,
                  alternate_epoch_btjd=ae, alternate_duration_h=ad * 24,
                  alternate_relation=rel, alternate_bls_snr=asnr,
                  fixed_period_epoch_btjd=shifted_epoch,
                  **prefix("recorded", recorded), **prefix("fixed_period", shifted),
                  **prefix("alternate", alternate),
                  **prefix("recorded", phase_shape(data, period, epoch, duration)),
                  **prefix("alternate", phase_shape(data, ap, ae, ad)))
    for name, p in (("half", period/2), ("double", 2*period)):
        ep, dur = fixed_period(data, p, duration)
        output.update({f"{name}_epoch_btjd": ep, **prefix(name, event_windows(data, p, ep, dur))})
    if sap is not None:
        output.update(prefix("sap_alternate", event_windows(sap, ap, ae, ad)))
        output.update(prefix("sap_recorded", event_windows(sap, period, epoch, duration)))
    records = [dict(**meta, rank=i+1, rank_score=score, period_d=p, epoch_btjd=e,
                    duration_h=d*24, bls_snr=snr, relation=relation(p, period, baseline, d),
                    **metrics)
               for i, (score, p, e, d, snr, metrics) in enumerate(candidates)]
    return output, records


def write_csv(path, rows):
    keys = list(dict.fromkeys(key for row in rows for key in row))
    with path.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=keys)
        writer.writeheader()
        writer.writerows(rows)


def annotate(results, candidates, cache):
    all_events = []
    for row in results:
        if row["outcome"] == "no-cache":
            continue
        tic = row["tic"]
        data = load_cadences(cache, tic)
        sap = load_cadences(cache, tic, "sap")
        times = data[0]
        middle = (times.min() + times.max()) / 2
        ephemerides = {}
        for name in ("recorded", "alternate"):
            period, epoch, hours = (float(row[f"{name}_{column}"]) for column in
                                    ("period_d", "epoch_btjd", "duration_h"))
            ephemerides[name] = (period, epoch, hours / 24)
        metrics = {}
        for name, ephemeris in ephemerides.items():
            for channel_name, channel_data in (("pdc", data), ("sap", sap)):
                if channel_data is None:
                    continue
                events = []
                values = event_windows(channel_data, *ephemeris, details=events)
                all_events.extend(dict(tic=tic, group=row["group"], clock=name,
                                       flux_channel=channel_name, **event) for event in events)
                key = name if channel_name == "pdc" else f"sap_{name}"
                metrics[key] = values
                row.update(prefix(key, values))
                for split_name, early in (("early", True), ("late", False)):
                    subset = [event for event in events if (event["center_btjd"] < middle) == early]
                    row[f"{key}_{split_name}_covered"] = len(subset)
                    row[f"{key}_{split_name}_hits"] = sum(event["hit"] for event in subset)

        recorded, alternate = metrics["recorded"], metrics["alternate"]
        rec_period = ephemerides["recorded"][0]
        alt_period, alt_epoch, alt_duration = ephemerides["alternate"]
        reference = alternate["depth"] if alternate["hits"] >= 3 and alternate["depth"] > 0 else None
        interstitial = event_windows(data, alt_period, alt_epoch + alt_period / 2, alt_duration,
                                     reference_depth=reference)
        row.update(prefix("alternate_interstitial", interstitial))
        alternatives = [other for other in candidates if other["tic"] == tic]
        best_score = float(alternatives[0]["rank_score"])
        ambiguous = []
        for other in alternatives[1:]:
            p, e = float(other["period_d"]), float(other["epoch_btjd"])
            delta = abs(1/p - 1/alt_period) * np.ptp(times)
            phase_offset = abs((e - alt_epoch + alt_period/2) % alt_period - alt_period/2)
            same_clock = delta < alt_duration / alt_period and phase_offset < alt_duration
            if (not same_clock and int(other["hits"]) >= 3
                    and float(other["rank_score"]) >= 0.90 * best_score):
                ambiguous.append((p, float(other["rank_score"])))
        row["competitive_periods_d"] = " ".join(f"{p:.8f}" for p, _ in ambiguous)
        row["fixed_period_epoch_shift_h"] = 24 * (
            (float(row["fixed_period_epoch_btjd"]) - ephemerides["recorded"][1] + rec_period/2)
            % rec_period - rec_period/2)
        state, why = verdict(recorded, alternate, row["alternate_relation"], int(row["sectors"]))
        if state == "alternate-clock":
            support = metrics.get("sap_alternate")
            if support:
                why += f" SAP at the alternate clock has {summarize(support)}."
            if ambiguous:
                state = "alternate-clock-alias-ambiguous"
                why += " Another period scores within 10% in the sampled search."
            if row["alternate_early_hits"] == 0 or row["alternate_late_hits"] == 0:
                why += " Significant detections occur in one temporal half."
            if support is None or support["hits"] < 2:
                state = "alternate-clock-pdc-only"
                why += " SAP corroboration is weak or unavailable."
        if recorded["hits"] == 0 and recorded["covered"] >= 2:
            why += " No significant recorded-phase dip supplies a depth reference for sensitive empty windows."
        if recorded["gap"] or alternate["gap"]:
            why += f' Coverage gaps at {recorded["gap"]} recorded and {alternate["gap"]} alternate windows.'
        row.update(outcome=state, why=why)
    return all_events

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--batch", type=Path, default=HERE.parent / "batch.csv")
    parser.add_argument("--cache", type=Path, default=DEFAULT_CACHE)
    parser.add_argument("--group", type=int, choices=range(1, 5))
    parser.add_argument("--recheck", action="store_true", help="Recompute window annotations from saved search outputs")
    args = parser.parse_args()
    suffix = f"-{args.group}" if args.group else ""
    if args.recheck:
        results, candidates = [], []
        for name, rows in (("outcome", results), ("candidates", candidates)):
            with (HERE / f"{name}{suffix}.csv").open(newline="", encoding="utf-8") as stream:
                rows.extend(csv.DictReader(stream))
        events = annotate(results, candidates, args.cache)
        write_csv(HERE / f"outcome{suffix}.csv", results)
        write_csv(HERE / f"events{suffix}.csv", events)
        return
    with args.batch.open(newline="", encoding="utf-8-sig") as stream:
        rows = list(csv.DictReader(stream))
    results, candidates = [], []
    for row in rows:
        if args.group and int(row["group"]) != args.group:
            continue
        result, records = audit(row, args.cache)
        print(result["tic"], result["outcome"], result["why"], flush=True)
        results.append(result)
        candidates.extend(records)
    events = annotate(results, candidates, args.cache)
    write_csv(HERE / f"outcome{suffix}.csv", results)
    write_csv(HERE / f"candidates{suffix}.csv", candidates)
    write_csv(HERE / f"events{suffix}.csv", events)


if __name__ == "__main__":
    main()
