"""Run 13c: R729 (TIC 236223193) at Gaia's own epoch, with Fable 5.1's seven QLP event times.
Run from the repository root:
  python3 reviews/2026-11-24-duet-research-runs-1-4/run13-a-sample-gaia-epoch/r729_epoch.py
Event times: Fable 5.1, 2026-11-25 (house file r729-events.csv; reproduced here as r729-events-fable51.csv).
"""
import sys, os, math, csv
import numpy as np
D = 'reviews/2026-11-24-duet-research-runs-1-4/'
sys.path.insert(0, D); sys.path.insert(0, D + 'run13-a-sample-gaia-epoch')
import window_covariance as W
from a_epoch_test import orbit           # SB2 corr_vec order P, gamma, K1, K2, e, omega, Tp
HERE = os.path.dirname(os.path.abspath(__file__))
n = next(r for r in csv.DictReader(open('reviews/2026-11-05-claim-adjudication/proof/binary-next40-2026-11-05-gaia_nss.csv'))
         if r['source_id'] == '1869679326451426816')
v, err, corr = orbit(n)
print(f"Gaia {n['nss_solution_type']}: P {v[0]:.4f} +- {err[0]:.4f}, e {v[1]:.3f} +- {err[1]:.3f}, omega {math.degrees(v[2]):.1f} +- {math.degrees(err[2]):.1f} deg")
ev = [dict(family=r['family'], t=float(r['btjd'])) for r in csv.DictReader(open(os.path.join(HERE, 'r729-events-fable51.csv')))]
tA, tB = W.conj(v, 0), W.conj(v, 1)
sepG = ((tB - tA) / v[0]) % 1
print(f'Gaia conjunctions at its epoch: A {tA:.3f}, B {tB:.3f} BTJD; B - A = {sepG:.3f} in phase')
for fam in ('deep', 'other'):
    t = np.array([e['t'] for e in ev if e['family'] == fam]); t.sort()
    k = np.round((t - t[0]) / 35.237)
    A = np.vstack([np.ones_like(k), k]).T
    (T0, P), res, *_ = np.linalg.lstsq(A, t, rcond=None)
    r = t - (T0 + P * k); s = max(np.std(r, ddof=2) if len(t) > 2 else 0.04, 0.04)
    cov = s ** 2 * np.linalg.inv(A.T @ A); eP = math.sqrt(cov[1, 1])
    print(f'{fam}: {len(t)} events, P {P:.4f} +- {eP:.4f} d (residual rms {np.std(r)*24:.1f} h); z vs Gaia {(v[0]-P)/math.hypot(err[0], eP):+.1f}')
    for kk, tg in (('A', tA), ('B', tB)):
        nb = round((tg - T0) / P); o = T0 + nb * P - tg
        sf, si = W.sigmas(v, err, corr, 0 if kk == 'A' else 1, 0)
        sb = abs(nb) * eP
        print(f'   carried back {nb} cycles to Gaia conj {kk}: offset {o:+.2f} d = {o/v[0]:+.3f} phase'
              f' (sigma: Gaia {sf:.2f} d, eclipse ephemeris {sb:.2f} d)')
# joint fit: one period, two families with their own zero points
fam = np.array([0 if e['family'] == 'deep' else 1 for e in ev]); t = np.array([e['t'] for e in ev])
ref = t[fam == 0].min(); k = np.round((t - ref - 0.892 * 35.237 * fam) / 35.237)
A = np.vstack([1 - fam, fam, k]).T
(Td, To, P), *_ = np.linalg.lstsq(A, t, rcond=None)
r = t - A @ np.array([Td, To, P]); s = math.sqrt(np.sum(r ** 2) / (len(t) - 3)); cov = s ** 2 * np.linalg.inv(A.T @ A)
eP = math.sqrt(cov[2, 2]); sepJ = ((To - Td) / P) % 1; esep = math.sqrt(cov[0, 0] + cov[1, 1] - 2 * cov[0, 1]) / P
print(f'joint fit: P {P:.4f} +- {eP:.4f} d, rms {s*24:.1f} h; other - deep = {sepJ:.4f} +- {esep:.4f} in phase'
      f' (the other family precedes the deep one by {(1-sepJ)%1:.4f})')
for lab, T0, kk in (('deep -> A', Td, 0), ('other -> B', To, 1)):
    tg = W.conj(v, kk); nb = round((tg - T0) / P); o = T0 + nb * P - tg
    sf, _ = W.sigmas(v, err, corr, kk, 0)
    print(f'   {lab}: {nb} cycles back, offset {o:+.2f} d = {o/v[0]:+.4f} phase; sigma Gaia {sf:.2f} d, ephemeris {abs(nb)*eP:.2f} d;'
          f' z {o/math.hypot(sf, abs(nb)*eP):+.1f}')
# Gaia's predicted separation B - A, with its covariance (Monte Carlo over e, omega, Tp, P)
rng = np.random.default_rng(13)
Cov = corr * np.outer(err, err)
dr = rng.multivariate_normal(v, Cov, 20000)
seps = np.array([((W.conj(x, 1) - W.conj(x, 0)) / x[0]) % 1 for x in dr if 0 <= x[1] < 1])
print(f'Gaia separation of B before A: {1 - np.median(seps):.4f} +- {np.std(seps):.4f}; eclipses: {(1-sepJ)%1:.4f} +- {esep:.4f};'
      f' z {((1-sepJ)%1 - (1 - np.median(seps)))/math.hypot(np.std(seps), esep):+.1f}')
# which omega, at Gaia's e, would give the eclipses' separation? and the smallest e that can give it at all
def sep_B_before_A(e, w):
    x = np.array([0.0, e, w, 0.0]); return (1 - ((W.conj(np.r_[1.0, x[1:]], 1) - W.conj(np.r_[1.0, x[1:]], 0)) % 1)) % 1
target = (1 - sepJ) % 1
ws = np.radians(np.arange(0, 360, 0.05))
for e in (v[1], 0.6, 0.5, 0.45, 0.42, 0.4, 0.3):
    sp = np.array([sep_B_before_A(e, w) for w in ws])
    hit = ws[np.abs(sp - target) < 0.002]
    sols = sorted({round(math.degrees(h)) for h in hit})
    print(f'  e = {e:.3f}: omega giving B {target:.3f} before A: {sols[:6] if sols else "none"}')
emin = next(e for e in np.arange(0.40, 0.80, 0.005)
            if np.min(np.abs(np.array([sep_B_before_A(e, w) for w in ws[::4]]) - target)) < 0.002)
print(f'smallest e that gives the eclipses\' separation: {emin:.3f} (Gaia {v[1]:.3f} +- {err[1]:.3f})')
