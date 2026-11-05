r"""Conjunction attribution for TIC 402940895: is the dip where Gaia's SB1
orbit puts the companion in front of the primary (primary at superior
conjunction, nu = pi/2 - omega; gaia_orbit.py convention)?
Input: marg9-persec\402940895-gaia-nss.csv (Gaia DR3 nss_two_body_orbit,
fetched 2026-11-02). Observed dip ephemeris from persec402-out.txt (5b).
Monte Carlo over P, Tp, e, omega (Gaussian, Gaia errors).
Receipt: persec402_gaia-out.txt.
"""
import csv, os, sys
import numpy as np

sys.stdout.reconfigure(encoding="utf-8")
SB = os.path.dirname(os.path.abspath(__file__))
r = next(csv.DictReader(open(os.path.join(SB, "marg9-persec", "402940895-gaia-nss.csv"))))
P, eP = float(r["period"]), float(r["period_error"])
Tp, eTp = float(r["t_periastron"]), float(r["t_periastron_error"])
e, ee = float(r["eccentricity"]), float(r["eccentricity_error"])
w, ew = np.radians(float(r["arg_periastron"])), np.radians(float(r["arg_periastron_error"]))
K1 = float(r["semi_amplitude_primary"])
TP_BTJD = 2457389.0 + Tp - 2457000.0
P_FIT, T0_FIT = 16.43920, 1632.1758      # persec402-out.txt, local refit from 5 dips
DIPS = [1632.075, 1648.684, 2371.992, 3835.087, 3851.281]

def tconj(P, Tp, e, w, nu):
    E = 2 * np.arctan(np.sqrt((1 - e) / (1 + e)) * np.tan(nu / 2))
    M = E - e * np.sin(E)
    return Tp + M / (2 * np.pi) * P

print(f"Gaia DR3 NSS SB1: P {P:.5f}+-{eP:.5f}  Tp {TP_BTJD:.3f}+-{eTp:.3f} BTJD  e {e:.3f}+-{ee:.3f}  "
      f"omega {np.degrees(w):.1f}+-{np.degrees(ew):.1f}  K1 {K1:.2f} km/s  sig {r['significance']}")
fm = 1.0361e-7 * K1**3 * P * (1 - e**2) ** 1.5
print(f"mass function f(M) = {fm:.4f} Msun")
for M1 in (1.0, 1.3, 1.6):
    m2 = np.linspace(0.01, 2, 20000)
    m2min = m2[np.argmin(np.abs(m2**3 / (M1 + m2)**2 - fm))]
    a = ((M1 + m2min) * (P / 365.25) ** 2) ** (1 / 3) * 215.03
    print(f"  M1 {M1}: M2 (i=90) {m2min:.3f} Msun, a {a:.1f} Rsun, central-eclipse duration for R1 3.33 "
          f"+ R2~{m2min:.2f} Rsun: {P / np.pi * np.arcsin((3.33 + m2min) / a):.2f} d")

tc1 = tconj(P, TP_BTJD, e, w, np.pi / 2 - w)
tc2 = tconj(P, TP_BTJD, e, w, 3 * np.pi / 2 - w)
print(f"\nGaia nominal: primary-eclipsed conjunction {tc1:.3f} + n*P ; secondary-eclipsed {tc2:.3f} + n*P "
      f"(separation {((tc2 - tc1) / P) % 1:.3f} phase)")

rng = np.random.default_rng(1)
N = 200000
Ps = rng.normal(P, eP, N); Tps = rng.normal(TP_BTJD, eTp, N)
es = np.clip(rng.normal(e, ee, N), 0, 0.95); ws = rng.normal(w, ew, N)
tcs = tconj(Ps, Tps, es, ws, np.pi / 2 - ws)
print("\nobserved dips vs Gaia's primary-eclipsed conjunction (MC over Gaia errors):")
print("  dip BTJD    cycle from Gaia tc   phase offset (obs - Gaia)   Gaia 1-sigma   z")
for t in DIPS:
    n = np.round((t - tc1) / P)
    pred = tcs + n * Ps
    d = (t - pred) / P
    d = (d + 0.5) % 1 - 0.5
    med, sd = np.median(d), 1.4826 * np.median(np.abs(d - np.median(d)))
    print(f"  {t:9.3f}   {int(n):5d}               {med:+.3f}                     {sd:.3f}        {med / sd:+.2f}")
# the same against the secondary-eclipsed conjunction, for completeness
tcs2 = tconj(Ps, Tps, es, ws, 3 * np.pi / 2 - ws)
n = np.round((DIPS[2] - tc2) / P)
d2 = ((DIPS[2] - (tcs2 + n * Ps)) / P + 0.5) % 1 - 0.5
print(f"  (vs the OTHER conjunction, s039 dip: {np.median(d2):+.3f} +- {1.4826*np.median(np.abs(d2-np.median(d2))):.3f})")
print(f"\nlocal dip-train P {P_FIT:.5f} vs Gaia {P:.5f}+-{eP:.5f}: {(P_FIT - P) / eP:+.2f} sigma")
