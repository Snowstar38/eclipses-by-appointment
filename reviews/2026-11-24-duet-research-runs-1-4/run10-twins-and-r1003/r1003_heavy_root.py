"""Run 10c (Duet): Gaia's R1003 photocentre orbit has a second, bright-tertiary solution.

Run 9b solved a0 = a * (m3/(M12 + m3) - beta) for m3 on the rising branch only
(beta = L3/(L12 + L3), L ~ m^4). A main-sequence tertiary's photocentre motion rises,
peaks and falls again as the tertiary gets bright, so the same a0 is also reached on
the falling branch. This script finds both roots, with the Thiele-Innes errors, for
the house's inner pair (1.1 + 0.9 Msun) and two others. NumPy only.
usage: python3 r1003_heavy_root.py nss.csv
"""
import csv
import math
import sys
import numpy as np

SID = "5861580639046056832"   # R1003


def a0_mas(A, B, F, G):
    u = (A * A + B * B + F * F + G * G) / 2
    v = A * G - B * F
    return math.sqrt(u + math.sqrt(u * u - v * v))


def photocentre(m3, M12, L12, P_yr):
    a = ((M12 + m3) * P_yr ** 2) ** (1 / 3)
    return a * (m3 / (M12 + m3) - m3 ** 4 / (L12 + m3 ** 4))


def bisect(f, lo, hi, n=80):
    flo = f(lo)
    if flo * f(hi) > 0:
        return float("nan")
    for _ in range(n):
        mid = 0.5 * (lo + hi)
        if f(mid) * flo > 0:
            lo, flo = mid, f(mid)
        else:
            hi = mid
    return 0.5 * (lo + hi)


def roots(a0_AU, M12, L12, P):
    g = np.linspace(0.01, 2.0, 4000)
    y = np.array([photocentre(m, M12, L12, P) for m in g])
    pk = g[np.argmax(y)]
    f = lambda m: photocentre(m, M12, L12, P) - a0_AU
    return bisect(f, 0.01, pk), bisect(f, pk, 2.0), pk


def main(path):
    r = {x["source_id"]: x for x in csv.DictReader(open(path))}[SID]
    A, B, F, G = (float(r[k + "_thiele_innes"]) for k in "abfg")
    eA, eB, eF, eG = (float(r[k + "_thiele_innes_error"]) for k in "abfg")
    plx = float(r["parallax"])
    P = float(r["period"]) / 365.25
    a0 = a0_mas(A, B, F, G) / plx
    rng = np.random.default_rng(1)
    s = [a0_mas(*(rng.normal(x, e) for x, e in zip((A, B, F, G), (eA, eB, eF, eG)))) / plx
         for _ in range(4000)]
    lo, hi = np.percentile(s, [16, 84])
    print(f"R1003: a0 = {a0:.4f} AU (68%: {lo:.4f}-{hi:.4f}), P_out = {P * 365.25:.2f} d")
    for m1, m2 in ((1.1, 0.9), (1.0, 0.8), (1.2, 1.0)):
        M12, L12 = m1 + m2, m1 ** 4 + m2 ** 4
        res = [roots(x, M12, L12, P) for x in (lo, a0, hi)]
        light, heavy, pk = res[1]
        beta = heavy ** 4 / (L12 + heavy ** 4)
        print(f"  inner {m1}+{m2}: light root m3 = {light:.3f} (68%: {res[2][0]:.3f}-{res[0][0]:.3f}); "
              f"heavy root m3 = {heavy:.3f} (68%: {res[0][1]:.3f}-{res[2][1]:.3f}); peak at {pk:.2f}; "
              f"heavy tertiary's share of the light {beta:.2f}")


if __name__ == "__main__":
    main(sys.argv[1])
