"""Which published ephemerides carry the un-barycentred sector 101+ eclipse times, and what
does that do to predictions?

For every row of the release's review tables (period_days, period_error_days,
primary_epoch_btjd) and of CHECKCARD.csv, find the target's measurements.json. Where its
timed events include sector 101+ or sectors 14-15, check that the published period is the measurements.json
one, then refit the linear ephemeris with the s101+ events corrected by time_offsets.correction_min
(s101: 3.5 min offset; s102+: Roemer delay). Report the shift of the epoch and of the predicted primary at
BTJD 5000 (2028 Aug 25, TESS's next pass for much of the sky), in minutes and in units of
the published prediction error (epoch and period errors combined).
Writes timing/published-ephemeris-shifts.csv.
usage (from the repo root): python3 reviews/duet-findings/timing/published_ephemerides.py
"""
import json, os, subprocess, sys
import numpy as np, pandas as pd
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from time_offsets import correction_min, positions  # noqa: E402

pos, _ = positions()

D = 'reviews/duet-findings/timing/'
TREF = 5000.0
tables = ['appointments-review.csv', 'bright-followup-review.csv', 'bright73-review.csv', 'faint-band-review.csv',
          'gap-review.csv', 'magnitude-review.csv', 'period-free-review.csv', 'remaining-screened-review.csv']
rows = []
for f in tables:
    t = pd.read_csv(f)
    for r in t.itertuples():
        rows.append(dict(table=f, review_id=getattr(r, 'review_id', ''), tic=str(r.tic), P=r.period_days,
                         eP=r.period_error_days, T0=r.primary_epoch_btjd))
pub = pd.DataFrame(rows).dropna(subset=['P', 'T0'])

meas = {}
for f in subprocess.run(['git', 'ls-files', '*measurements.json'], capture_output=True, text=True).stdout.split():
    try:
        d = json.load(open(f))
    except Exception:
        continue
    if isinstance(d, dict) and isinstance(d.get('events'), list):
        meas.setdefault(str(d.get('tic')), []).append((f, d))


def fit(tt, er, E):
    A = np.vstack([np.ones_like(E), E]).T; W = 1 / er ** 2
    C = np.linalg.inv(A.T @ (A * W[:, None])); c = C @ (A.T @ (W * tt))
    r = tt - A @ c; s2 = max(np.sum(W * r ** 2) / max(len(tt) - 2, 1), 1)
    return c, C * s2


out = []
for r in pub.itertuples():
    for f, d in meas.get(r.tic, []):
        P = d.get('period_days')
        if not P or abs(P - r.P) > 1e-9 * P:
            continue
        e = [x for x in d['events'] if isinstance(x, dict) and x.get('timing_usable', True) and x.get('mid_btjd') and x.get('sector') is not None]
        n101 = sum(x['sector'] >= 101 for x in e)
        n1415 = sum(x['sector'] in (14, 15) for x in e)
        if not (n101 or n1415) or r.tic not in pos or len(e) < 3:
            continue
        tt = np.array([x['mid_btjd'] for x in e]); er = np.array([x.get('timing_error_days') or 0.005 for x in e])
        E = np.round((tt - r.T0) / r.P)
        corr = correction_min([x['sector'] for x in e], tt, *pos[r.tic]) / 1440
        c0, C0 = fit(tt, er, E); c1, C1 = fit(tt - corr, er, E)
        n = np.round((TREF - r.T0) / r.P)
        sig_pub = np.hypot(0.0, n * (r.eP if np.isfinite(r.eP) else np.sqrt(C0[1, 1])))
        sig_fit = np.sqrt(C0[0, 0] + 2 * n * C0[0, 1] + n * n * C0[1, 1])
        d_ref = ((c1[0] + c1[1] * n) - (c0[0] + c0[1] * n)) * 1440
        out.append(dict(table=r.table, review_id=r.review_id, tic=r.tic, n_events=len(e), n_s101plus=n101, n_s14_15=n1415,
                        epoch_in_s101plus=bool(r.T0 >= 4100.0), dT0_min=round((c1[0] - c0[0]) * 1440, 2),
                        dP_s=round((c1[1] - c0[1]) * 86400, 3), dP_over_eP=round((c1[1] - c0[1]) / r.eP, 2) if r.eP > 0 else np.nan,
                        shift_2028_min=round(d_ref, 1), pub_sigma_2028_min=round(sig_pub * 1440, 1),
                        fit_sigma_2028_min=round(sig_fit * 1440, 1), shift_over_sigma=round(d_ref / (sig_fit * 1440), 2), file=f))
        break
o = pd.DataFrame(out).drop_duplicates('tic')
o = o.reindex(o.shift_over_sigma.abs().sort_values(ascending=False).index)
o.to_csv(D + 'published-ephemeris-shifts.csv', index=False)
for name, q in (('sector 101+', o[o.n_s101plus > 0]), ('sectors 14-15 (and no s101+)', o[(o.n_s14_15 > 0) & (o.n_s101plus == 0)])):
    print(f'{len(pub)} published rows; {len(q)} use {name} events through their measurements.json (period identical)')
    print(f'   epoch itself inside s101+: {int(q.epoch_in_s101plus.sum())}')
    print(f'   period shift > 1 published sigma: {int((q.dP_over_eP.abs() > 1).sum())}, > 3: {int((q.dP_over_eP.abs() > 3).sum())}')
    a = q.shift_2028_min.abs()
    print(f'   predicted primary at BTJD {TREF:.0f}: median |shift| {a.median():.1f} min, > 10 min in {int((a > 10).sum())}, > 30 min in {int((a > 30).sum())}')
    print(f"   shift beyond the fit's own 1-sigma prediction error in {int((q.shift_over_sigma.abs() > 1).sum())}, beyond 2 sigma in {int((q.shift_over_sigma.abs() > 2).sum())}")
print(o.head(12)[['review_id', 'tic', 'n_events', 'n_s101plus', 'n_s14_15', 'dT0_min', 'dP_over_eP', 'shift_2028_min', 'fit_sigma_2028_min', 'shift_over_sigma']].to_string(index=False))

cc = pd.read_csv('CHECKCARD.csv'); cc['TIC'] = cc.TIC.astype(str)
print(f'\nCHECKCARD.csv: {len(cc)} rows; epochs at BTJD >= 4100: {int((cc.T0_primary_BTJD >= 4100).sum())}; TICs among the s101+ ephemerides: {int(cc.TIC.isin(o.tic).sum())}')

# Calibration: predict each measurements.json ephemeris's last sector from its other sectors,
# with and without the clock correction, in units of the error the fit itself quotes
# (per-event timing errors, covariance inflated when reduced chi2 > 1, as measurements.json does).
print('\nCalibration of the quoted errors: last sector predicted from the others (measurements.json, >= 3 sectors)')
cal = []
for t, lst in meas.items():
    f, d = lst[0]
    P = d.get('period_days'); T0 = d.get('primary_epoch_btjd')
    if t not in pos or not P or not T0:
        continue
    e = [x for x in d['events'] if isinstance(x, dict) and x.get('timing_usable', True) and x.get('mid_btjd') and x.get('sector') is not None and x.get('timing_error_days')]
    s = np.array([x['sector'] for x in e])
    if len(set(s)) < 3:
        continue
    tt = np.array([x['mid_btjd'] for x in e]); er = np.array([x['timing_error_days'] for x in e]); E = np.round((tt - T0) / P)
    for cc in (False, True):
        tc = tt - (correction_min(s, tt, *pos[t]) / 1440 if cc else 0)
        m = s == s.max(); c, C = fit(tc[~m], er[~m], E[~m])
        Am = np.vstack([np.ones(m.sum()), E[m]]).T; pe = np.sqrt(np.einsum('ij,jk,ik->i', Am, C, Am)).mean()
        ww = 1 / er[m] ** 2
        cal.append(dict(tic=t, corrected=cc, last=s.max(), z=np.average(tc[m] - Am @ c, weights=ww) / np.hypot(pe, ww.sum() ** -0.5)))
cal = pd.DataFrame(cal)
mad = lambda x: 1.4826 * np.median(np.abs(x - np.median(x)))
for cc, g in cal.groupby('corrected'):
    a, b = g[g['last'] >= 101], g[g['last'] < 101]
    print(f"   {'corrected' if cc else 'as given '}: {len(g)} ephemerides; robust sigma of the miss in quoted errors {mad(g.z):.2f}, beyond 3 in {int((g.z.abs() > 3).sum())}; "
          f"last sector s101+: {mad(a.z):.2f} over {len(a)} (beyond 3 in {int((a.z.abs() > 3).sum())}); earlier: {mad(b.z):.2f} over {len(b)}")
