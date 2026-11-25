"""Run 11d: what run 9's A73 N-body fits predict for TESS's next look (sectors 123-124, 2028).
Run from the repository root (needs rebound, NumPy):
  python3 reviews/2026-11-24-duet-research-runs-1-4/run11-ledger/a73_forecast.py
For every stable run-9 fit, integrates from 2019 to 2029 and reports, at the
TESS look (BTJD 4970-5030; tess-point 0.9.5 sector mid-times 4985.0 and 5013.5)
and at the last observed secondary: the secondary-eclipse phase, the sky
separation at each conjunction in units of R1 + R2 (eclipse if < 1), and the
uniform-disc depth of the secondary scaled as in run 9.
"""
import sys, os, json, math
import numpy as np
D = 'reviews/2026-11-24-duet-research-runs-1-4/run9-tertiaries/'
sys.path.insert(0, D)
import a73_fit as F
from a73_assess import a0_mas
t, ph, dep = F.load(D + 'a73-secondary-phases.csv')
FITS = ['pol_e0.10', 'pol_e0.15', 'pol_e0.20', 'gpol_e0.20', 'gpol_e0.25', 'pol_e0.25', 'pol_e0.30']
SUM = (F.R1 + F.R2) * F.RSUN
print('Gaia photocentre a0 = 0.719 mas; run 9 prefers fits whose dark-tertiary a0 matches it')
print(f'last observed secondary: BTJD {t.max():.1f}, phase {ph[np.argmax(t)]:.4f}, depth {dep[np.argmax(t)]:.3f}')
print('fit          m3   a0_dark(mas) | 2028 TESS look: sec phase   b_prim  b_sec  sec depth | phase drift per yr 2026-28')
for name in FITS:
    r = json.load(open(D + 'fits/' + name + '.json')); p = r['params']; e_out = r['e_out']
    x = [p[k] for k in F.NAMES]
    prim, sec = F.model_phases(x, e_out, t, span=5100 - F.T_START)
    pt = np.array([a for a, _ in prim]); pb = np.array([b for _, b in prim]) / SUM
    st = np.array([a for a, _ in sec]); sb = np.array([b for _, b in sec]) / SUM
    _, bsec_obs = F.phases_at(prim, sec, t)
    _, D0 = F.depth_term(bsec_obs, dep)
    def at(T0, T1):
        m = (st > T0) & (st < T1)
        out = []
        for j in np.nonzero(m)[0]:
            k = np.searchsorted(pt, st[j]) - 1
            out.append(((st[j] - pt[k]) / F.P_IN, pb[k], sb[j], D0 * F.covered_fraction(np.array([sb[j] * SUM / F.RSUN]))[0]))
        return np.array(out)
    look = at(4970, 5030)
    a = at(4100, 4130); b = at(4830, 4860)
    drift = (b[:, 0].mean() - a[:, 0].mean()) / 2.0
    print(f'{name:11s} {p["m3"]:5.2f}  {a0_mas(p["m3"])[1]:6.3f}       | {look[:,0].mean():.4f} +- {look[:,0].std():.4f}  '
          f'{look[:,1].mean():5.2f}  {look[:,2].mean():5.2f}  {look[:,3].mean():.3f}     | {drift:+.4f}')
