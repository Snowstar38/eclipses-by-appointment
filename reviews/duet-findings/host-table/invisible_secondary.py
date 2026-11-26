"""Can the shorter period hold an invisible secondary?

For every row of Earthshine's pop-results-855.csv, assume the adopted (fold)
period P is the orbital period with one eclipse per orbit and a faint
main-sequence companion. The primary depth sets the smallest companion
radius (R2 >= R1*sqrt(depth/f), f = 1.3 limb-darkening allowance, which
makes the bound conservative); a main-sequence R->Teff relation gives that
companion's temperature; the TESS-band surface-brightness ratio then gives
the smallest occultation depth that companion must produce. Grazing
geometry, third light and a larger companion all make the predicted
secondary deeper, so the prediction is a lower bound.

The bound is compared with what the light curve allows: an occultation
error from the per-point rms and the number of points expected inside a
flat-bottomed window of half the fitted duration, inflated x2 for red
noise. Rows where P is already fixed by a measured secondary are the
calibration: there the lower bound must not exceed the observed depth.

usage: python3 invisible_secondary.py pop-results-855.csv vet-2p-855.csv
"""
import sys
import numpy as np
import pandas as pd

F_LD = 1.3        # central-eclipse limb-darkening allowance (conservative)
RED = 2.0         # red-noise inflation of the white-noise occultation error
FLOOR = 0.3       # ppt, systematics floor on the occultation limit
R_BD = 0.13       # Rsun: below this a brown dwarf / late M could be dark

# Main-sequence dwarfs, Pecaut & Mamajek (2013, updated table), rounded:
# radius (Rsun) -> Teff (K)
MS = np.array([
    (0.10, 2400), (0.12, 2650), (0.14, 2850), (0.20, 3060), (0.26, 3210),
    (0.39, 3410), (0.45, 3560), (0.50, 3680), (0.58, 3850), (0.63, 4050),
    (0.70, 4440), (0.76, 4830), (0.86, 5270), (0.90, 5490), (0.92, 5660),
    (1.00, 5770), (1.10, 5920), (1.18, 6100), (1.40, 6510), (1.50, 6810),
    (1.70, 7220), (1.80, 8180), (2.20, 9700), (3.0, 12000)])


def teff_ms(r):
    return np.interp(r, MS[:, 0], MS[:, 1])


_lam = np.linspace(600e-9, 1000e-9, 200)  # TESS band, flat response


def surf(t):
    h, c, k = 6.626e-34, 2.998e8, 1.381e-23
    x = h * c / (_lam * k * t)
    return np.trapezoid(1.0 / (_lam ** 5 * np.expm1(x)), _lam)


def bound(row):
    d = row.depth_fit_ppt / 1e3
    r1, t1 = row.rad, row.teff
    if not (np.isfinite(d) and np.isfinite(r1) and np.isfinite(t1)) or d <= 0:
        return np.nan, np.nan, "no host"
    k = np.sqrt(min(d / F_LD, 1.0))
    r2 = k * r1
    if r2 < R_BD:
        return r2, 0.0, "companion could be substellar"
    t2 = min(teff_ms(r2), t1)          # a smaller companion is not hotter
    ratio = surf(t2) / surf(t1)
    ds = (d / F_LD) * ratio * 1e3        # ppt; occultation of the companion
    return r2, ds, ""


def limit(row):
    frac = 0.5 * row.T14_fit_h / 24.0 / row.P_d
    n_in = row.n_pts * frac
    if not (np.isfinite(n_in) and n_in > 0 and np.isfinite(row.rms_ppt)):
        return np.nan
    return max(3 * RED * row.rms_ppt / np.sqrt(n_in), FLOOR)


def main(pop, vet):
    p = pd.read_csv(pop)
    v = pd.read_csv(vet)[["review_id", "frac_diff_pct", "sigma", "verdict"]]
    out = p.apply(lambda r: pd.Series(bound(r), index=["R2_min", "sec_pred_ppt", "flag"]), axis=1)
    p = pd.concat([p, out], axis=1)
    p["sec_limit_ppt"] = p.apply(limit, axis=1)
    p = p.merge(v, on="review_id", how="left")

    # calibration: rows whose period is fixed by a measured secondary
    cal = p[p.period_check.str.startswith("P:") & (p.sec_real == True)
            & np.isfinite(p.sec_pred_ppt) & (p.sec_pred_ppt > 0)].copy()
    cal["obs_over_pred"] = cal.sec_depth_ppt / cal.sec_pred_ppt
    print(f"calibration rows (secondary fixes P): {len(cal)}")
    q = np.percentile(cal.obs_over_pred, [2.5, 5, 16, 50, 84])
    print("  observed/predicted secondary depth, percentiles 2.5,5,16,50,84:",
          np.round(q, 2))
    bad = cal[cal.obs_over_pred < 1 / 1.5]
    print(f"  rows where the lower bound overshoots the observed depth by >1.5x: {len(bad)}")
    print(bad[["review_id", "P_d", "rad", "teff", "depth_fit_ppt", "sec_depth_ppt",
               "sec_pred_ppt", "obs_over_pred", "reading"]].round(2).to_string())

    # the test proper: rows with no secondary at P
    o = p[p.period_check == "open"].copy()
    o["excl_ratio"] = o.sec_pred_ppt / o.sec_limit_ppt
    o["P_excluded"] = o.excl_ratio > 1.5
    o["short"] = o.P_d < 3.0
    print(f"\nopen rows: {len(o)}; with host data and a bound: {np.isfinite(o.excl_ratio).sum()}")
    print("  companion could be substellar:", (o.flag == "companion could be substellar").sum())
    print("  P excluded (pred > 1.5 x limit):", o.P_excluded.sum(),
          " of which P < 3 d:", (o.P_excluded & o.short).sum())
    two = o[o.verdict == "2P"]
    print(f"  Earthshine 2P rows in open: {len(two)}, excluded at P by this test: {two.P_excluded.sum()}")
    print(two[["review_id", "P_d", "depth_fit_ppt", "sec_pred_ppt", "sec_limit_ppt",
               "excl_ratio", "frac_diff_pct"]].round(2).to_string())
    cols = ["review_id", "tic", "P_d", "rad", "teff", "depth_fit_ppt", "R2_min",
            "sec_pred_ppt", "sec_limit_ppt", "excl_ratio", "P_excluded", "reading",
            "verdict", "frac_diff_pct", "flag"]
    o[cols].sort_values("excl_ratio", ascending=False).round(3).to_csv(
        "invisible-secondary-test.csv", index=False)
    cal[["review_id", "P_d", "rad", "teff", "depth_fit_ppt", "sec_depth_ppt",
         "sec_pred_ppt", "obs_over_pred"]].round(3).to_csv(
        "invisible-secondary-calibration.csv", index=False)
    return p, o, cal


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])


def equal_dips_table(pop, vet, hosts):
    """The headline set: rows whose host-table text reads "P: no secondary
    found, alternate dips equal" (R946 left out: its text and column already
    disagree, run 5). Run at the default and the strictest settings."""
    global F_LD, RED, R_BD
    import contextlib, io
    h = pd.read_csv(hosts)
    head = h.period_resolution.fillna("").str.split("|").str[0]
    ids = set(h.review_id[head.str.startswith("P: no secondary found")]) - {"R946"}
    res = {}
    for name, (f, r, bd) in {"default": (1.3, 2.0, 0.13), "strict": (1.5, 3.0, 0.22)}.items():
        F_LD, RED, R_BD = f, r, bd
        with contextlib.redirect_stdout(io.StringIO()):
            _, o, _ = main(pop, vet)
        res[name] = o[o.review_id.isin(ids)].set_index("review_id")
    d, s = res["default"], res["strict"]
    t = d[["tic", "P_d", "rad", "teff", "depth_fit_ppt", "R2_min", "sec_pred_ppt",
           "sec_limit_ppt", "excl_ratio", "reading", "verdict", "frac_diff_pct", "flag"]].copy()
    t["P_excluded_default"] = d.P_excluded
    t["P_excluded_strict"] = s.P_excluded.reindex(t.index)
    h["sb2_text_prefers_2P"] = h.period_resolution.fillna("").str.contains("twin solution 2P")
    t = t.join(h.set_index("review_id")[["physical_tier", "adopted_period_days", "sb2_text_prefers_2P"]])
    t["implied_period_d"] = np.where(t.P_excluded_default, 2 * t.P_d, np.nan)
    t = t.sort_values("excl_ratio", ascending=False)
    t.round(4).to_csv("equal-dips-2P-test.csv")
    F_LD, RED, R_BD = 1.3, 2.0, 0.13
    print(f"equal-dips rows: {len(t)}, testable: {t.excl_ratio.notna().sum()}")
    print(f"  P excluded, default: {int(t.P_excluded_default.sum())} "
          f"(ratio > 5: {int((t.excl_ratio > 5).sum())}); strict: {int(t.P_excluded_strict.sum())}; "
          f"default and P < 3 d: {int((t.P_excluded_default & (t.P_d < 3)).sum())}")
    print(pd.crosstab(t.physical_tier, t.P_excluded_default))
    print(pd.crosstab(t.verdict.fillna("untested"), t.P_excluded_default))
    print(f"  SB2 text prefers 2P: {int(t.sb2_text_prefers_2P.sum())}; also excluded here: "
          f"{int((t.sb2_text_prefers_2P & t.P_excluded_default).sum())}; P excluded either way: "
          f"{int((t.sb2_text_prefers_2P | t.P_excluded_default).sum())}")
    return t


if __name__ == "__main__" and len(sys.argv) > 3:
    equal_dips_table(sys.argv[1], sys.argv[2], sys.argv[3])
