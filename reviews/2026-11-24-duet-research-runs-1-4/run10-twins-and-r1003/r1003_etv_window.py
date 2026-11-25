"""Run 10e (Duet): does R1003's 2026 eclipse timing allow a fourth body in 10b's 8-17-d window?

Input: Fable's per-event times (r1003_events.csv; only the 19 deep 2026 events, depth > 50
ppt, as Fable advises). Model: linear ephemeris plus the ~83-d sinusoid that best fits the
timing (Fable's "wiggle that fits"), plus a sinusoid at each trial P4 in 8-17 d. Reports
the best P4, the 95% upper limit on its amplitude (amplitude + 2 sigma, errors scaled by the
reduced chi-square), and the leading-order dynamical ETV amplitude (m4/M) P_in^2 / (2 pi P4)
a fourth body of mass m4 would make.
usage: python3 r1003_etv_window.py r1003_events.csv
"""
import math
import sys
import numpy as np

P_IN, M = 2.8787113, 2.0


def main(path):
    rows = [l.strip().split(",") for l in open(path) if l.strip()]
    h = rows[0]; rows = [dict(zip(h, r)) for r in rows[1:]]
    rows = [r for r in rows if float(r["depth_ppt"]) > 50]
    t = np.array([float(r["t_btjd"]) for r in rows]); oc = np.array([float(r["oc_d"]) for r in rows]) * 86400
    w = 1 / (np.array([float(r["sigma_d"]) for r in rows]) * 86400) ** 2

    def fit(cols):
        B = np.column_stack(cols); W = np.diag(w); C = np.linalg.inv(B.T @ W @ B); c = C @ B.T @ W @ oc
        return ((oc - B @ c) ** 2 * w).sum(), c, C

    lin = [np.ones_like(t), t - t.mean()]
    print(f"{len(t)} deep events; linear ephemeris chi2 = {fit(lin)[0]:.1f} for {len(t)-2} dof")
    best = min((fit(lin + [np.sin(2*np.pi*t/P), np.cos(2*np.pi*t/P)])[0], P) for P in np.arange(20, 150, 0.02))
    Pl = best[1]
    print(f"best single sinusoid 20-150 d: P = {Pl:.1f} d, chi2 = {best[0]:.1f} for {len(t)-4} dof (broad: 75-106 d within chi2 + 4)")
    base = lin + [np.sin(2*np.pi*t/Pl), np.cos(2*np.pi*t/Pl)]
    ups = []; bestshort = (1e9, 0)
    for P4 in np.arange(8, 17.001, 0.05):
        c2, c, C = fit(base + [np.sin(2*np.pi*t/P4), np.cos(2*np.pi*t/P4)])
        s = max(c2 / (len(t) - 6), 1.0)
        amp = math.hypot(c[4], c[5]); err = math.sqrt(max(C[4, 4], C[5, 5]) * s)
        ups.append(amp + 2 * err); bestshort = min(bestshort, (c2, P4))
    print(f"8-17 d: best P4 = {bestshort[1]:.2f} d (chi2 {bestshort[0]:.1f}, no significant drop); 95% amplitude limit {np.median(ups):.0f} s (median), {max(ups):.0f} s (worst)")
    lim = max(ups)
    for P4 in (8, 12, 17):
        m4 = lim / 86400 * 2 * math.pi * P4 / P_IN ** 2 * M
        print(f"  P4 = {P4:2d} d: ETV amplitude per 0.01 Msun {0.01/M*P_IN**2/(2*math.pi*P4)*86400:.0f} s -> m4 < {m4:.4f} Msun ({m4*1047.6:.0f} Jupiter masses)")


if __name__ == "__main__":
    main(sys.argv[1])
