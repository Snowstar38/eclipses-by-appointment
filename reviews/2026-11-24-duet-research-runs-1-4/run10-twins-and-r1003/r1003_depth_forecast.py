"""Run 10e (Duet): what R1003's 2026 eclipse depths say about the switch-on, and what to expect next.

Input: Fable's per-event and per-sector depths (run7-temperature-and-r1003/fable-r1003/
r1003_events.csv, r1003_depths.csv; house QLP s99/s101 and SPOC 2-min s100 cache).
Geometry: two uniform disks, R1 = 1.1, R2 = 0.9 Rsun (the house's 1.1 + 0.9 Msun pair,
R1 + R2 = 2.0 as in runs 7 and 9), surface-brightness ratio from the secondary/primary depth
ratio (|e cos w| = 0.49 from the secondary phase; with e sin w ~ 0 both eclipses share one
impact parameter b, in units of R1 + R2, and the overlap areas are equal, so the depth ratio
is S2/S1). SPOC's crowding-corrected depth is taken as true, with and without the heavy
Gaia root's ~21% third light (section 10b).

It prints (1) the depth trend inside each 2026 sector and between the two QLP sectors,
(2) the impact parameter now and how fast the primary depth changes with b, and (3) the
depth change per year a tertiary moving b at 0.038 or 0.106 per year would make, which
TESS's next sectors can check.
usage: python3 r1003_depth_forecast.py r1003_events.csv r1003_depths.csv
"""
import math
import sys
import numpy as np

R1, R2 = 1.1, 0.9


def overlap(d, r1=R1, r2=R2):
    if d >= r1 + r2:
        return 0.0
    if d <= abs(r1 - r2):
        return math.pi * min(r1, r2) ** 2
    a = r1 * r1 * math.acos((d * d + r1 * r1 - r2 * r2) / (2 * d * r1))
    b = r2 * r2 * math.acos((d * d + r2 * r2 - r1 * r1) / (2 * d * r2))
    c = 0.5 * math.sqrt((-d + r1 + r2) * (d + r1 - r2) * (d - r1 + r2) * (d + r1 + r2))
    return a + b - c


def depth(bb, s21, third=0.0):
    ltot = math.pi * (R1 ** 2 + s21 * R2 ** 2)
    return (1 - third) * overlap(bb * (R1 + R2)) / ltot


U1, U2 = 0.40, 0.25          # quadratic limb darkening, roughly a 5,500-6,000 K star in TESS's band


def ld_blocked(rs, ro, d, n=1201):
    """Fraction of a limb-darkened star's (radius rs) flux hidden by a dark disk of radius ro at d."""
    x = np.linspace(-rs, rs, n); X, Y = np.meshgrid(x, x); r = np.hypot(X, Y); inside = r < rs
    mu = np.sqrt(np.clip(1 - (r / rs) ** 2, 0, 1)); I = (1 - U1 * (1 - mu) - U2 * (1 - mu) ** 2) * inside
    return (I * (((X - d) ** 2 + Y ** 2) < ro * ro)).sum() / I.sum()


def ld_depths(bb, s21):
    d = bb * (R1 + R2); f1 = R1 ** 2; f2 = s21 * R2 ** 2
    return ld_blocked(R1, R2, d) * f1 / (f1 + f2), ld_blocked(R2, R1, d) * f2 / (f1 + f2)


def ld_solve(P, S):
    """b and S2/S1 that reproduce primary and secondary depths P, S (fractions)."""
    s21 = S / P
    for _ in range(6):
        lo, hi = 0.0, 1.0
        for _ in range(30):
            mid = (lo + hi) / 2
            if ld_depths(mid, s21)[0] > P: lo = mid
            else: hi = mid
        p, s = ld_depths(lo, s21); s21 *= (S / s) / (P / p)
    return lo, s21


def read(path):
    rows = [l.strip().split(",") for l in open(path) if l.strip()]
    h = rows[0]
    return [dict(zip(h, r)) for r in rows[1:]]


def main(ev_path, dp_path):
    ev = read(ev_path); dp = {r["sector"]: r for r in read(dp_path)}
    print("(1) Depth trends in 2026 (per-event depths, scatter-based errors)")
    means = {}
    for s in ("99", "100", "101"):
        t = np.array([float(r["t_btjd"]) for r in ev if r["sector"] == s])
        y = np.array([float(r["depth_ppt"]) for r in ev if r["sector"] == s])
        A = np.vstack([t - t.mean(), np.ones_like(t)]).T
        c = np.linalg.lstsq(A, y, rcond=None)[0]; res = y - A @ c
        cov = res.var(ddof=2) * np.linalg.inv(A.T @ A)
        means[s] = (y.mean(), res.std(ddof=2) / math.sqrt(len(y)), t.mean())
        print(f"  s{s} ({dp[s]['src']}): {len(y)} events, mean {y.mean():.1f} ppt, slope {c[0]*365.25:+.0f} +- {math.sqrt(cov[0,0])*365.25:.0f} ppt/yr over {t.max()-t.min():.0f} d")
    d = means["101"][0] - means["99"][0]; e = math.hypot(means["101"][1], means["99"][1]); dt = (means["101"][2] - means["99"][2]) / 365.25
    e2 = math.hypot(float(dp["99"]["prim_sig"]), float(dp["101"]["prim_sig"]))
    print(f"  QLP s99 -> s101 ({dt*365.25:.0f} d): {d:+.1f} ppt (+-{e:.1f} from event scatter, +-{e2:.1f} from Fable's red-noise-scaled sector fits)")
    for s in ("99", "100", "101"):
        p, ps, q, qs = (float(dp[s][k]) for k in ("prim_ppt", "prim_sig", "sec_ppt", "sec_sig"))
        print(f"  s{s} secondary/primary {q/p:.3f} +- {q/p*math.hypot(ps/p, qs/q):.3f}")
    s21 = float(dp["100"]["sec_ppt"]) / float(dp["100"]["prim_ppt"])
    D = float(dp["100"]["prim_ppt"]) / 1000
    print(f"\n(2) Geometry now (uniform disks, S2/S1 = {s21:.3f}, SPOC primary {D*1000:.1f} ppt)")
    rates = (0.038, 0.106)
    for third in (0.0, 0.21):
        lo, hi = 0.0, 1.0
        for _ in range(60):
            mid = (lo + hi) / 2
            if depth(mid, s21, third) > D: lo = mid
            else: hi = mid
        b = lo; h = 1e-4
        dDdb = (depth(b + h, s21, third) - depth(b - h, s21, third)) / (2 * h) * 1000
        dmax = depth(0.0, s21, third) * 1000
        print(f"  third light {third:.2f}: b = {b:.3f}, max depth (b = 0) {dmax:.0f} ppt, dDepth/db = {dDdb:.0f} ppt per unit b")
        for r in rates:
            print(f"     b moving {r:.3f}/yr: primary depth changes {abs(dDdb)*r:.0f} ppt/yr; eclipses gone in {(1-b)/r:.0f} yr if b grows, deepest in {b/r:.0f} yr if it shrinks")
    print("\n(3) Grazing check: s64/s65 (2023) limits are ~2-3 ppt; depth(b) reaches 3 ppt at")
    for third in (0.0, 0.21):
        bb = np.linspace(0.8, 1.0, 20001); dd = np.array([depth(x, s21, third) for x in bb]) * 1000
        print(f"  third light {third:.2f}: b = {bb[np.argmin(abs(dd-3))]:.3f}")

    print("\n(4) Limb-darkened disks (quadratic u = 0.40, 0.25), and what the switch-on needed vs what 2026 shows")
    gap = (float([r for r in ev if r["sector"] == "99"][0]["t_btjd"]) - float([r for r in ev if r["sector"] == "65"][-1]["t_btjd"])) / 365.25
    spoc_slope, spoc_err = -7.3, 17.0
    t = np.array([float(r["t_btjd"]) for r in ev if r["sector"] == "100"]); y = np.array([float(r["depth_ppt"]) for r in ev if r["sector"] == "100"])
    A = np.vstack([t - t.mean(), np.ones_like(t)]).T; c = np.linalg.lstsq(A, y, rcond=None)[0]; r_ = y - A @ c
    spoc_slope = c[0] * 365.25; spoc_err = math.sqrt(r_.var(ddof=2) * np.linalg.inv(A.T @ A)[0, 0]) * 365.25
    qscale = float(dp["100"]["prim_ppt"]) / ((float(dp["99"]["prim_ppt"]) + float(dp["101"]["prim_ppt"])) / 2)
    qlp_slope, qlp_err = d / dt * qscale, e2 / dt * qscale   # QLP depths are diluted relative to SPOC's
    print(f"  QLP depths scaled by {qscale:.2f} to SPOC's crowding-corrected scale for the rate below")
    print(f"  last eclipse-free event (s65) to first deep one (s99): {gap:.2f} yr")
    for third in (0.0, 0.21):
        P = float(dp["100"]["prim_ppt"]) / 1000 / (1 - third); S = float(dp["100"]["sec_ppt"]) / 1000 / (1 - third)
        b, s21 = ld_solve(P, S)
        dDdb = (ld_depths(b + 0.01, s21)[0] - ld_depths(b - 0.01, s21)[0]) / 0.02 * 1000 * (1 - third)
        bb = np.linspace(0.85, 1.0, 151); dd = np.array([ld_depths(x, s21)[0] for x in bb]) * 1000 * (1 - third)
        b3 = bb[np.argmin(abs(dd - 3.0))]
        need = (b3 - b) / gap
        v1 = spoc_slope / dDdb; e1 = spoc_err / abs(dDdb)
        v2 = qlp_slope / dDdb; e2_ = qlp_err / abs(dDdb)
        w = np.array([1 / e1 ** 2, 1 / e2_ ** 2]); vm = (w * np.array([v1, v2])).sum() / w.sum(); em = w.sum() ** -0.5
        print(f"  third light {third:.2f}: b now {b:.3f} (S2/S1 {s21:.3f}); depth 3 ppt at b = {b3:.3f}; dDepth/db = {dDdb:.0f} ppt")
        print(f"     switch-on needed db/dt <= {-need:.3f}/yr on average (May 2023 - Feb 2026); at that rate the primary deepens {need*abs(dDdb):.0f} ppt/yr now")
        print(f"     2026 depths give db/dt = {v1:+.3f} +- {e1:.3f} (SPOC s100), {v2:+.3f} +- {e2_:.3f} (QLP s99->s101, red-noise errors); combined {vm:+.3f} +- {em:.3f}/yr")
        print(f"     -> the 2026 rate differs from the switch-on's average by {(vm + need)/em:.1f} sigma")

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
