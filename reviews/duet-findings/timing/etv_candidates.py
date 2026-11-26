"""Eclipse timing variations that survive the clock model.

For every target in etv-events.csv with three or more sectors, correct the times with
time_offsets.correction_min, fit a linear ephemeris, average the residuals per sector and
compute a sector-level reduced chi-square with a 0.5 min floor per sector (the scatter of
well-behaved sectors). Compares the counts with and without the correction and lists the
targets whose sector means still disagree. A sector that moves alone by tens of minutes is
marked as a probable measurement problem (one event, a wrong cycle count or a blend), not a
timing variation, and so is a jump of more than 5 min between sectors three or fewer apart. Writes etv-candidates.csv.
usage (from the repo root): python3 reviews/duet-findings/timing/etv_candidates.py
"""
import os, sys
import numpy as np, pandas as pd
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from time_offsets import correction_min, positions  # noqa: E402

D = os.path.dirname(os.path.abspath(__file__)) + '/'
pos, rid = positions()
ev = pd.read_csv(D + 'etv-events.csv'); ev['tic'] = ev.tic.astype(str); ev = ev[ev.tic.isin(pos)]


def survey(correct):
    out = []
    for tic, g in ev.groupby('tic'):
        if g.sector.nunique() < 3:
            continue
        t = g.t_mid.values - (correction_min(g.sector.values, g.t_mid.values, *pos[tic]) / 1440 if correct else 0)
        w = 1 / g.err_d.values ** 2; A = np.vstack([np.ones(len(g)), g.cycle]).T
        c = np.linalg.solve(A.T @ (A * w[:, None]), A.T @ (w * t)); r = (t - A @ c) * 1440
        q = pd.DataFrame(dict(s=g.sector.values, r=r, w=w / 1440 ** 2, cad=g.cadence_min.values))
        sec = q.groupby('s').apply(lambda x: pd.Series(dict(m=np.average(x.r, weights=x.w), e=np.hypot(x.w.sum() ** -0.5, 0.5),
                                                              n=len(x), cad=x.cad.iloc[0])), include_groups=False)
        chi = np.sum((sec.m / sec.e) ** 2) / (len(sec) - 2)
        dev = sec.m.abs()
        lone = bool((dev.max() > 10) and (dev.sort_values().iloc[-2] < 0.3 * dev.max()))
        ss = sec.index.values; mm = sec.m.values
        adj = bool(any(ss[i + 1] - ss[i] <= 3 and abs(mm[i + 1] - mm[i]) > 5 for i in range(len(ss) - 1)))
        out.append(dict(review_id=rid.get(tic, ''), tic=tic, n_events=len(g), n_sectors=len(sec), span_yr=round(np.ptp(g.t_mid) / 365.25, 1),
                        sector_chi2_red=round(chi, 1), max_sector_dev_min=round(dev.max(), 1), lone_jump=lone, adjacent_jump=adj,
                        sector_means_min=' '.join(f'{int(s)}:{m:+.1f}' for s, m in zip(sec.index, sec.m))))
    return pd.DataFrame(out).sort_values('sector_chi2_red', ascending=False)


raw, cor = survey(False), survey(True)
for name, d in (('as given', raw), ('clock-corrected', cor)):
    print(f'{name:16s}: {len(d)} targets; sector-level reduced chi2 > 5 in {int((d.sector_chi2_red > 5).sum())}, > 20 in {int((d.sector_chi2_red > 20).sum())}')
cand = cor[cor.sector_chi2_red > 20]
cand.to_csv(D + 'etv-candidates.csv', index=False)
print(f'\nclock-corrected targets with sector-level reduced chi2 > 20 ({len(cand)}); lone_jump: one sector off by > 10 min;')
print('adjacent_jump: sectors <= 3 apart differ by > 5 min, faster than a third body on a multi-year orbit can move them')
ok = cand[~cand.lone_jump & ~cand.adjacent_jump]
print(f'left as timing-variation candidates: {len(ok)}: ' + ', '.join(ok.review_id))
pd.set_option('display.width', 250); pd.set_option('display.max_colwidth', 90)
print(cand[['review_id', 'n_sectors', 'span_yr', 'sector_chi2_red', 'max_sector_dev_min', 'lone_jump', 'adjacent_jump', 'sector_means_min']].to_string(index=False))
