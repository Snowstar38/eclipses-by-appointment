"""Are the house's eclipse times barycentric? Tests of the clock model in time_offsets.py.

1. Per-sector test. For each target in timing/etv-events.csv, fit a linear ephemeris to
   sectors <= 99 only, then average its residuals per sector. Across targets, regress each
   sector's mean residual on the Roemer delay (Sun-geocentre vector dotted with the star's
   direction, in minutes) a time that skipped the barycentric correction would carry. A
   corrected sector gives k ~ 0, an uncorrected one k ~ 1.
1b. Leave-one-sector-out. For each sector, fit every target's ephemeris to its other sectors
   (corrected with time_offsets.correction_min), then fit that sector's mean residuals as
   a + k * Roemer delay. 102-104 come out not barycentric and 14-15 near 1.5 times the
   delay on average. For s100 and s101, compare residual = 0, residual = a fitted constant
   and the frozen correction (residual = roemer(t) - roemer(4069.5), no free parameter).
1c. After the correction: the median corrected residual per sector.
2. Jump test. For targets seen in both s90-99 and s102+, the step in mean residual against
   the Roemer delay of the s102+ events.
3. Ephemeris bias. For every measurements.json with sector 101+ events, refit the period
   after correcting the events with time_offsets.correction_min; write timing/qlp-barycentre-periods.csv.
4-6. The 30-min era offset, the sign of timing curvature, and R1003's 2026 ephemeris.
usage (from the repo root): python3 reviews/duet-findings/timing/qlp_barycentre.py
"""
import json
import os
import subprocess
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import pandas as pd

D = 'reviews/duet-findings/timing/'


from time_offsets import roemer_min, correction_min, extra_err_min, positions, FROZEN_BTJD

pos, rid = positions()
ev = pd.read_csv(D + 'etv-events.csv'); ev['tic'] = ev.tic.astype(str)
ev = ev[ev.tic.isin(pos)]
rows = []
for tic, g in ev.groupby('tic'):
    ref = g[g.sector <= 99]
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

print('1. Per-sector slope k of mean residual on the Roemer delay (residuals from a <= s99 ephemeris)')
print('   sector  targets   k      +-')
for s in sorted(ps.sector.unique()):
    q = ps[(ps.sector == s)]
    if s < 85 or len(q) < 8:
        continue
    w = 1 / (q.err ** 2 + 0.3 ** 2)
    A = np.vstack([np.ones(len(q)), q.rm]).T
    C = np.linalg.inv(A.T @ (A * w.values[:, None])); cc = C @ (A.T @ (w * q.res))
    print(f'   {s:5d}  {len(q):6d}  {cc[1]:6.2f}  {np.sqrt(C[1,1]):5.2f}')

print('\n1b. Leave-one-sector-out: each sector against ephemerides from the other (corrected) sectors')
print('   sectors with >= 5 targets; median res/rm is the robust slope (0: barycentric, 1: not)')
print('   sector  targets   a (min)        k            chi2/dof  median res/rm')
ev['rm'] = 0.0
for tic, g in ev.groupby('tic'):
    ev.loc[g.index, 'rm'] = roemer_min(g.t_mid.values, *pos[tic])
loso = {}
for S in range(1, 105):
    rows = []
    for tic, g in ev.groupby('tic'):
        m = (g.sector == S).values
        ref = ~m
        if not m.any() or ref.sum() < 3 or g[ref].sector.nunique() < 2:
            continue
        cor = correction_min(g.sector.values, g.t_mid.values, *pos[tic], tic=tic)
        t = g.t_mid.values - cor / 1440
        ee = np.hypot(g.err_d.values, extra_err_min(g.sector.values, tic=tic) / 1440)
        w = 1 / ee[ref] ** 2
        A = np.vstack([np.ones(ref.sum()), g.cycle.values[ref]]).T
        C = np.linalg.inv(A.T @ (A * w[:, None])); c = C @ (A.T @ (w * t[ref]))
        r = t[ref] - A @ c; C = C * max(np.sum(w * r * r) / max(ref.sum() - 2, 1), 1)
        Am = np.vstack([np.ones(m.sum()), g.cycle.values[m]]).T
        pe = np.sqrt(np.einsum('ij,jk,ik->i', Am, C, Am)) * 1440
        res = (g.t_mid.values[m] - Am @ c) * 1440; ww = 1 / np.hypot(g.err_d.values[m] * 1440, pe) ** 2
        rows.append(dict(tic=tic, res=np.average(res, weights=ww), err=ww.sum() ** -0.5, rm=np.average(g.rm.values[m], weights=ww),
                         cor=np.average(cor[m], weights=ww), rm0=roemer_min(FROZEN_BTJD, *pos[tic])))
    o = pd.DataFrame(rows)
    if len(o) == 0:
        continue
    o = o[o.err < 2]
    if len(o) < 5:
        continue
    w = 1 / (o.err ** 2 + 0.5 ** 2); A = np.vstack([np.ones(len(o)), o.rm]).T
    C = np.linalg.inv(A.T @ (A * w.values[:, None])); c = C @ (A.T @ (w * o.res)); r = o.res - A @ c
    loso[S] = o
    print(f'   {S:5d}  {len(o):6d}   {c[0]:+5.2f} +- {np.sqrt(C[0,0]):4.2f}   {c[1]:+5.2f} +- {np.sqrt(C[1,1]):4.2f}   {np.sum(w*r*r)/(len(o)-2):6.1f}   {np.median(o.res / o.rm):+5.2f}')
for S in (14, 15):
    o = loso[S]
    print(f'   s{S}: res/rm per target ' + ' '.join(f'{x:+.2f}' for x in sorted(o.res / o.rm)))
o = loso[101]; w = 1 / (o.err ** 2 + 0.5 ** 2)
for S in (100, 101):
    o = loso[S]; w = 1 / (o.err ** 2 + 0.5 ** 2)
    for name, pred, nfree in (('barycentric (residual = 0)', 0 * o.rm, 0), ('barycentric plus one fitted constant', 0 * o.rm, 1),
                              ('frozen at 4069.5 (residual = rm - rm(4069.5))', o.rm - o.rm0, 0)):
        d = o.res - pred; cst = np.average(d, weights=w) if nfree else 0.0
        print(f'   s{S} as {name}: mean left {np.average(d - cst, weights=w):+.2f} min, chi2 {np.sum(w * (d - cst) ** 2):.1f} for {len(o) - nfree} dof')
o = loso[101]; w = 1 / (o.err ** 2 + 0.5 ** 2)
for name, pred in (('uncorrected (residual = Roemer delay)', o.rm), ('barycentric (residual = 0)', 0 * o.rm)):
    d = o.res - pred; cst = np.average(d, weights=w)
    print(f'   s101 as {name}: best constant {cst:+.2f} +- {w.sum() ** -0.5:.2f} min, chi2 {np.sum(w * (d - cst) ** 2):.1f} for {len(o) - 1} dof')

print('\n1c. After the correction: median corrected residual per sector (targets with errors < 1 min, sectors with >= 6)')
meds = []
for S, o in loso.items():
    q = o[o.err < 1.0]
    if len(q) >= 6:
        meds.append((S, len(q), np.median(q.res - q.cor)))
print('   ' + '  '.join(f's{S}:{m:+.2f}({n})' for S, n, m in meds))
print(f'   {len(meds)} sectors; largest |median| {max(abs(m) for _, _, m in meds):.2f} min')

print('\n2. Jump from s90-99 to s102+ in the same targets, against the s102+ Roemer delay')
jr = []
for tic, q in ps.groupby('tic'):
    a, b = q[(q.sector >= 90) & (q.sector <= 99)], q[q.sector >= 102]
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
    corr = correction_min([x['sector'] for x in e], [x['mid_btjd'] for x in e], *pos[t], tic=t) / 1440
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

print('\n5. Sign of ETV curvature (quadratic term, > 3 sigma) before and after correcting s101+ times')
for corr in (False, True):
    neg = pos_ = 0
    for tic, g in ev.groupby('tic'):
        if g.sector.nunique() < 3 or len(g) < 6:
            continue
        t = g.t_mid.values.copy()
        if corr:
            t -= correction_min(g.sector.values, t, *pos[tic], tic=tic) / 1440
        x = g.cycle.values.astype(float); x = (x - x.mean()) / (np.ptp(x) or 1)
        A = np.vstack([np.ones_like(x), x, x ** 2]).T; w = 1 / g.err_d.values ** 2
        C = np.linalg.inv(A.T @ (A * w[:, None])); c = C @ (A.T @ (w * t))
        r = t - A @ c; s2 = max(np.sum(w * r ** 2) / max(len(t) - 3, 1), 1)
        z = c[2] / np.sqrt(C[2, 2] * s2)
        neg += z < -3; pos_ += z > 3
    print(f'   {"after " if corr else "before"}: {neg} negative, {pos_} positive')

print("\n6. R1003's 2026 ephemeris (Fable 5's deep events, s99-101) with the clock corrected (s101 QLP; s100 is SPOC)")
r3 = pd.read_csv('reviews/duet-findings/triples/fable-r1003/r1003_events.csv')
r3 = r3[r3.depth_ppt > 50]
P_tab = 2.878458
for corr in (False, True):
    t = r3.t_btjd.values.copy()
    if corr:
        t -= correction_min(r3.sector.values, t, 193.786609, -65.53488, spoc=r3.sector.values == 100) / 1440
    E = r3.epoch.values.astype(float); w = 1 / r3.sigma_d.values ** 2
    A = np.vstack([np.ones_like(E), E]).T; C = np.linalg.inv(A.T @ (A * w[:, None])); c = C @ (A.T @ (w * t))
    r = t - A @ c; chi = np.sum(w * r ** 2); dof = len(t) - 2; sp = np.sqrt(C[1, 1])
    per = {s: round(np.average(r[r3.sector.values == s], weights=w[r3.sector.values == s]) * 86400) for s in (99, 100, 101)}
    print(f'   {"corrected" if corr else "as given "}: P = {c[1]:.7f} +- {sp:.7f} d, chi2 {chi:.1f}/{dof}; tabled P off by {(c[1]-P_tab)/sp:.0f} sigma '
          f'({(c[1]-P_tab)/(sp*np.sqrt(chi/dof)):.0f} with errors scaled); sector mean O-C (s) {per}')
