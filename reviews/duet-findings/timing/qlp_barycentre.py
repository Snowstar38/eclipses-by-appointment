"""Are the house's sector 101+ eclipse times barycentric?

1. Per-sector test. For each target in timing/etv-events.csv, fit a linear ephemeris to
   sectors <= 100 only, then average its residuals per sector. Across targets, regress each
   sector's mean residual on the Roemer delay (Sun-geocentre vector dotted with the star's
   direction, in minutes) a time that skipped the barycentric correction would carry. A
   corrected sector gives k ~ 0, an uncorrected one k ~ 1.
2. Jump test. For targets seen in both s90-100 and s101+, the step in mean residual against
   the Roemer delay of the s101+ events (s90-100 being corrected).
3. Ephemeris bias. For every measurements.json with sector 101+ events, refit the period
   after removing the Roemer delay from those events; write timing/qlp-barycentre-periods.csv.
usage (from the repo root): python3 reviews/duet-findings/timing/qlp_barycentre.py
"""
import json
import subprocess
import numpy as np
import pandas as pd

D = 'reviews/duet-findings/timing/'


def roemer_min(btjd, ra, dec):
    n = np.asarray(btjd) + 2457000 - 2451545.0
    L = np.radians(280.460 + 0.9856474 * n); g = np.radians(357.528 + 0.9856003 * n)
    lam = L + np.radians(1.915) * np.sin(g) + np.radians(0.020) * np.sin(2 * g)
    R = 1.00014 - 0.01671 * np.cos(g) - 0.00014 * np.cos(2 * g); eps = np.radians(23.439 - 4e-7 * n)
    s = R * np.array([np.cos(lam), np.cos(eps) * np.sin(lam), np.sin(eps) * np.sin(lam)])
    a, d = np.radians(ra), np.radians(dec)
    nv = np.array([np.cos(d) * np.cos(a), np.cos(d) * np.sin(a), np.sin(d)])
    return 8.3167 * np.tensordot(nv, s, 1)


pos, rid = {}, {}
for f in ('overview/systems.csv', 'scientific-review-register.csv', 'accepted-systems.csv'):
    t = pd.read_csv(f)
    t['tic'] = t.tic.astype(str)
    if 'ra_deg' in t:
        pos.update({k: (r, d) for k, r, d in zip(t.tic, t.ra_deg, t.dec_deg) if np.isfinite(r)})
    rid.update(dict(zip(t.tic, t.review_id)))

ev = pd.read_csv(D + 'etv-events.csv'); ev['tic'] = ev.tic.astype(str)
ev = ev[ev.tic.isin(pos)]
rows = []
for tic, g in ev.groupby('tic'):
    ref = g[g.sector <= 100]
    if len(ref) < 4 or ref.sector.nunique() < 2:
        continue
    w = 1 / ref.err_d ** 2
    A = np.vstack([np.ones(len(ref)), ref.cycle]).T
    c = np.linalg.solve(A.T @ (A * w.values[:, None]), A.T @ (w * ref.t_mid))
    res = (g.t_mid - (c[0] + c[1] * g.cycle)) * 1440
    rm = roemer_min(g.t_mid.values, *pos[tic])
    for s, gg in g.assign(res=res, rm=rm, e=g.err_d * 1440).groupby('sector'):
        ww = 1 / gg.e ** 2
        rows.append(dict(tic=tic, sector=s, res=np.average(gg.res, weights=ww), err=ww.sum() ** -0.5, rm=gg.rm.mean()))
ps = pd.DataFrame(rows)

print('1. Per-sector slope k of mean residual on the Roemer delay (residuals from a <= s100 ephemeris)')
print('   sector  targets   k      +-')
for s in sorted(ps.sector.unique()):
    q = ps[(ps.sector == s)]
    if s < 85 or len(q) < 8:
        continue
    w = 1 / (q.err ** 2 + 0.3 ** 2)
    A = np.vstack([np.ones(len(q)), q.rm]).T
    C = np.linalg.inv(A.T @ (A * w.values[:, None])); cc = C @ (A.T @ (w * q.res))
    print(f'   {s:5d}  {len(q):6d}  {cc[1]:6.2f}  {np.sqrt(C[1,1]):5.2f}')

print('\n2. Jump from s90-100 to s101+ in the same targets, against the s101+ Roemer delay')
jr = []
for tic, q in ps.groupby('tic'):
    a, b = q[(q.sector >= 90) & (q.sector <= 100)], q[q.sector >= 101]
    if len(a) and len(b):
        wa, wb = 1 / a.err ** 2, 1 / b.err ** 2
        J = np.average(b.res, weights=wb) - np.average(a.res, weights=wa)
        Je = np.hypot(wa.sum() ** -0.5, wb.sum() ** -0.5)
        jr.append(dict(tic=tic, J=J, Je=Je, pred=np.average(b.rm, weights=wb)))
jr = pd.DataFrame(jr)
w = 1 / (jr.Je ** 2 + 0.3 ** 2)
k = (w * jr.J * jr.pred).sum() / (w * jr.pred ** 2).sum(); ke = (w * jr.pred ** 2).sum() ** -0.5
print(f'   {len(jr)} targets; slope of jump on predicted step {k:.2f} +- {ke:.2f}')
print(f'   jump has the predicted sign in {int((np.sign(jr.J) == np.sign(jr.pred)).sum())} of {len(jr)}')
print(f'   median |predicted step| {jr.pred.abs().median():.1f} min; median residual after removing it {np.median(jr.J - jr.pred):+.2f} min')

print('\n3. Ephemeris bias in measurements.json files with sector 101+ events')
fs = subprocess.run(['git', 'ls-files', '*measurements.json'], capture_output=True, text=True).stdout.split()
out, seen, skipped = [], set(), 0
for f in fs:
    try:
        d = json.load(open(f))
    except Exception:
        continue
    if not isinstance(d, dict) or not isinstance(d.get('events'), list):
        continue
    t = str(d.get('tic'))
    e = [x for x in d['events'] if isinstance(x, dict) and x.get('timing_usable', True) and x.get('mid_btjd') and x.get('sector') is not None]
    if not any(x['sector'] >= 101 for x in e) or t in seen:
        continue
    seen.add(t)
    P = d.get('period_days') or d.get('period_d'); T0 = d.get('primary_epoch_btjd') or d.get('epoch_btjd')
    if t not in pos or len(e) < 3 or not P or not T0:
        skipped += 1; continue
    tt = np.array([x['mid_btjd'] for x in e]); er = np.array([x.get('timing_error_days') or 0.005 for x in e])
    E = np.round((tt - T0) / P)
    corr = np.array([roemer_min(x['mid_btjd'], *pos[t]) / 1440 if x['sector'] >= 101 else 0 for x in e])
    A = np.vstack([np.ones_like(E), E]).T; W = 1 / er ** 2
    C = np.linalg.inv(A.T @ (A * W[:, None]))
    c0 = C @ (A.T @ (W * tt)); c1 = C @ (A.T @ (W * (tt - corr)))
    out.append(dict(tic=t, review_id=rid.get(t, ''), n_events=len(e), n_s101plus=int(sum(x['sector'] >= 101 for x in e)),
                    max_shift_min=round(1440 * np.abs(corr).max(), 2), period_d=P,
                    dP_s=round((c1[1] - c0[1]) * 86400, 3), P_err_s=round(np.sqrt(C[1, 1]) * 86400, 3),
                    dP_over_err=round((c1[1] - c0[1]) / np.sqrt(C[1, 1]), 2), file=f))
o = pd.DataFrame(out).sort_values('dP_over_err', key=abs, ascending=False)
o.to_csv(D + 'qlp-barycentre-periods.csv', index=False)
print(f'   {len(o)} targets ({skipped} skipped: no position, period or < 3 events)')
print(f'   period shift > 3 sigma in {int((o.dP_over_err.abs() > 3).sum())}, > 1 sigma in {int((o.dP_over_err.abs() > 1).sum())}; median |shift| {o.dP_over_err.abs().median():.2f} sigma')
print('   largest:', ', '.join(f"{r.review_id or r.tic} {r.dP_over_err:+.1f}" for r in o.head(10).itertuples()))

print('\n4. 30-min era (s1-26) against an ephemeris from s27-100')
off = []
for tic, g in ev.groupby('tic'):
    ref = g[(g.sector >= 27) & (g.sector <= 100)]; old = g[g.sector <= 26]
    if len(old) < 2 or len(ref) < 4 or ref.sector.nunique() < 2:
        continue
    w = 1 / ref.err_d ** 2
    A = np.vstack([np.ones(len(ref)), ref.cycle]).T
    C = np.linalg.inv(A.T @ (A * w.values[:, None])); c = C @ (A.T @ (w * ref.t_mid))
    r = (old.t_mid - (c[0] + c[1] * old.cycle)) * 1440
    pe = np.sqrt(np.einsum('ij,jk,ik->i', np.vstack([np.ones(len(old)), old.cycle]).T, C, np.vstack([np.ones(len(old)), old.cycle]).T)) * 1440
    wo = 1 / ((old.err_d * 1440) ** 2)
    off.append(dict(tic=tic, off=np.average(r, weights=wo), err=np.hypot(wo.sum() ** -0.5, np.median(pe))))
off = pd.DataFrame(off)
print(f'   {len(off)} targets; median offset {off.off.median():+.2f} min; negative in {int((off.off < 0).sum())}')
w = 1 / off.err ** 2
print(f'   weighted mean {np.average(off.off, weights=w):+.2f} +- {w.sum() ** -0.5:.2f} min (formal); sign test p = {__import__("math").erfc(abs((off.off < 0).sum() - len(off) / 2) / (len(off) ** 0.5 / 2) / 2 ** 0.5):.3f}')

print('\n5. Sign of ETV curvature (quadratic term, > 3 sigma) before and after removing the s101+ delay')
for corr in (False, True):
    neg = pos_ = 0
    for tic, g in ev.groupby('tic'):
        if g.sector.nunique() < 3 or len(g) < 6:
            continue
        t = g.t_mid.values.copy()
        if corr:
            m = (g.sector >= 101).values
            t[m] -= roemer_min(t[m], *pos[tic]) / 1440
        x = g.cycle.values.astype(float); x = (x - x.mean()) / (np.ptp(x) or 1)
        A = np.vstack([np.ones_like(x), x, x ** 2]).T; w = 1 / g.err_d.values ** 2
        C = np.linalg.inv(A.T @ (A * w[:, None])); c = C @ (A.T @ (w * t))
        r = t - A @ c; s2 = max(np.sum(w * r ** 2) / max(len(t) - 3, 1), 1)
        z = c[2] / np.sqrt(C[2, 2] * s2)
        neg += z < -3; pos_ += z > 3
    print(f'   {"after " if corr else "before"}: {neg} negative, {pos_} positive')

print("\n6. R1003's 2026 ephemeris (Fable 5's deep events, s99-101) with the s101 delay removed")
r3 = pd.read_csv('reviews/duet-findings/triples/fable-r1003/r1003_events.csv')
r3 = r3[r3.depth_ppt > 50]
P_tab = 2.878458
for corr in (False, True):
    t = r3.t_btjd.values.copy()
    if corr:
        m = (r3.sector >= 101).values
        t[m] -= roemer_min(t[m], 193.786609, -65.53488) / 1440
    E = r3.epoch.values.astype(float); w = 1 / r3.sigma_d.values ** 2
    A = np.vstack([np.ones_like(E), E]).T; C = np.linalg.inv(A.T @ (A * w[:, None])); c = C @ (A.T @ (w * t))
    r = t - A @ c; chi = np.sum(w * r ** 2); dof = len(t) - 2; sp = np.sqrt(C[1, 1])
    per = {s: round(np.average(r[r3.sector.values == s], weights=w[r3.sector.values == s]) * 86400) for s in (99, 100, 101)}
    print(f'   {"corrected" if corr else "as given "}: P = {c[1]:.7f} +- {sp:.7f} d, chi2 {chi:.1f}/{dof}; tabled P off by {(c[1]-P_tab)/sp:.0f} sigma '
          f'({(c[1]-P_tab)/(sp*np.sqrt(chi/dof)):.0f} with errors scaled); sector mean O-C (s) {per}')
