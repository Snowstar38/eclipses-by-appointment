"""Systemic-velocity curves that Gaia DR4's epoch RVs (2014-07-25 to 2020-01-20) should show
for the triples whose outer orbit is fixed by Gaia's astrometry and the eclipse timing.

The inner pair's line-of-sight velocity is v = c d tau / dt, with tau the light-travel delay
(numerical derivative of the same shape function the timing fits use).
  A95:  Gaia's 541-d astrometric orbit (P3, e, T_peri, w from the Thiele-Innes elements) with
        the amplitude and sign fitted to Fable 5's 66 eclipse times (a95_ltte.py: 3.48 +- 0.25
        min, sign -). Phase, shape, amplitude and sign are all predicted.
  A119: Gaia's 601-d astrometric orbit; the amplitude is the photocentre lower bound
        (ltte_from_astrometry.py, >= 3.38 min) and the sign is not known (TESS timing does not
        detect the wobble: Earthshine, -122 +- 96 s SAP, +109 +- 105 s PDCSAP at Gaia's orbit,
        against >= 227 s). Phase and shape are predicted, the size is a lower bound.
  R630, R423: circular light-travel orbits refitted to etv4-times.csv (timing/ruwe_wobble.py's fit,
        the same data and jitter as timing/etv_orbits.py) at every outer period within Delta chi2 < 4;
        the delay's sign is physical (later = farther), so the velocity's sign is predicted.
        The spread over the allowed periods is given at each date.
R623's two branches are in timing/r623_gaia_branches.py.
Run from the repository root: python3 reviews/duet-findings/triples/dr4_gamma_predictions.py
"""
import csv, math
import numpy as np

C_KMS = 299792.458
NSS = 'reviews/duet-findings/gaia-errors/fable51-nss-appointments.csv'
T1, T2 = 2456863.9 - 2457000, 2458868.5 - 2457000  # DR4 span, BTJD
YEARS = [2015.0, 2015.5, 2016.0, 2016.5, 2017.0, 2017.5, 2018.0, 2018.5, 2019.0, 2019.5, 2020.0]


def kepler(M, e):
    E = M.copy()
    for _ in range(50):
        E -= (E - e * np.sin(E) - M) / (1 - e * np.cos(E))
    return E


def elements(r):
    A, B, F, G = (float(r[k + '_thiele_innes']) for k in 'abfg')
    w = (math.atan2(B - F, A + G) + math.atan2(-B - F, A - G)) / 2
    return float(r['period']), float(r['eccentricity']), float(r['t_periastron']) + 389.0, w


def shape(t, P, e, tp, w):
    nu = 2 * np.arctan(np.sqrt((1 + e) / (1 - e)) * np.tan(kepler(np.mod(2 * np.pi * (t - tp) / P, 2 * np.pi), e) / 2))
    return (1 - e ** 2) / (1 + e * np.cos(nu)) * np.sin(nu + w) + e * np.sin(w)


def velocity(t, P, e, tp, w, K_days):
    h = 0.01
    return C_KMS * K_days * (shape(t + h, P, e, tp, w) - shape(t - h, P, e, tp, w)) / (2 * h)


def semi_amp_to_K(amp_min, e, w):
    """semi-amplitude of the delay (min) -> coefficient of the shape function (days)."""
    return amp_min / 1440 / math.sqrt(1 - (e * math.cos(w)) ** 2)


rows = {(r['review_id'], r['nss_solution_type']): r for r in csv.DictReader(open(NSS))}
tb = np.array([(y - 2016.0) * 365.25 + 389.0 for y in YEARS])
tt = np.linspace(T1, T2, 4000)
for lab, amp, sig, sign in (('A95', 3.48, 0.25, -1), ('A119', 3.38, None, None)):
    P, e, tp, w = elements(rows[(lab, 'Orbital')])
    Kd = semi_amp_to_K(amp, e, w)
    v = velocity(tt, P, e, tp, w, Kd * (sign or 1))
    vy = velocity(tb, P, e, tp, w, Kd * (sign or 1))
    k_rv = (v.max() - v.min()) / 2
    lead = f"{lab}: P3 {P:.1f} d, e {e:.3f}, T_peri BTJD {tp:.1f}; delay semi-amplitude {amp:.2f} min"
    lead += f" +- {sig:.2f}" if sig else " (lower bound)"
    print(lead + f" -> RV semi-amplitude {k_rv:.2f} km/s" + (f" +- {k_rv * sig / amp:.2f}" if sig else " or more")
          + f"; DR4-span swing {v.max() - v.min():.1f} km/s")
    tmax, tmin = tt[np.argmax(v)], tt[np.argmin(v)]
    yr = lambda x: 2016.0 + (x - 389.0) / 365.25
    if sign:
        print(f"   gamma highest at {yr(tmax):.2f}, lowest at {yr(tmin):.2f} (then every {P / 365.25:.2f} yr)")
    else:
        print(f"   gamma extremes at {yr(tmax):.2f} and {yr(tmin):.2f}, sign unknown (then every {P / 365.25:.2f} yr)")
    print("   gamma minus its DR4 mean (km/s; A119 up to an overall sign and a factor >= 1): "
          + " ".join(f"{y:.1f}:{x - v.mean():+.1f}" for y, x in zip(YEARS, vy)))


import os, sys
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'timing'))
from ruwe_wobble import circ_fits

for lab in ('R630', 'R423'):
    ok, best = circ_fits(lab)
    curves = []
    for P3, chi2, amp, tp in ok:
        K = 2 * np.pi * amp / (P3 * 86400) * C_KMS
        curves.append((P3, chi2, K, K * np.cos(2 * np.pi * (tb - tp) / P3), K * np.cos(2 * np.pi * (tt - tp) / P3)))
    b = min(curves, key=lambda x: x[1])
    v = np.array([c[3] - c[4].mean() for c in curves])
    swing = [c[4].max() - c[4].min() for c in curves]
    print(f"{lab}: circular P3 {ok[0][0]:.0f}-{ok[-1][0]:.0f} d (best {b[0]:.0f}); RV semi-amplitude {min(c[2] for c in curves):.1f}-"
          f"{max(c[2] for c in curves):.1f} km/s (best {b[2]:.1f}); DR4-span swing {min(swing):.1f}-{max(swing):.1f} km/s")
    print("   gamma minus its DR4 mean (km/s), best period [range over allowed periods]: "
          + " ".join(f"{y:.1f}:{x - b[4].mean():+.1f}[{lo:+.0f},{hi:+.0f}]" for y, x, lo, hi in zip(YEARS, b[3], v.min(0), v.max(0))))
