"""Does a tertiary's moving systemic velocity show in Gaia DR3's spectroscopic fit quality?

Gaia DR3 fits each SB1/SB2 with a constant centre-of-mass velocity over about 2014.6-2017.4.
A third body on an orbit of years moves that velocity by km/s, which the fit cannot absorb,
so its goodness_of_fit (F2, about N(0,1) for a good fit) should run high.
For every accepted system with a review gaia.json, the Gaia NSS row of the source nearest
the accepted position (within 3 arcsec) gives the solution type, period and F2.
Compared, among systems timed in three or more sectors (timing/etv-summary.csv) with an
SB1 at the eclipse period: the light-travel systems (R623, R630, R423), the other
timing-variation candidates, and the rest.
Run from the repository root: python3 reviews/duet-findings/triples/sb1_fit_quality.py
"""
import csv, glob, json, math, os, re
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
T = os.path.join(HERE, '..', 'timing')
acc = {}
for r in csv.DictReader(open('accepted-systems.csv')):
    acc.setdefault(r['tic'], r)
rec = {}
for f in sorted(glob.glob('reviews/**/gaia.json', recursive=True)):
    m = re.search(r'/(\d{4,11})/(?:[a-z-]+/)?gaia\.json$', f)
    if not m or m.group(1) not in acc or m.group(1) in rec:
        continue
    try:
        g = json.load(open(f))
    except (ValueError, OSError):
        continue
    a = acc[m.group(1)]
    ra0, de0 = float(a['ra_deg']), float(a['dec_deg'])
    best = None
    for s in g.get('src') or []:
        try:
            sep = math.hypot((float(s['ra']) - ra0) * math.cos(math.radians(de0)), float(s['dec']) - de0) * 3600
        except (KeyError, ValueError, TypeError):
            continue
        if best is None or sep < best[0]:
            best = (sep, s)
    if not best or best[0] > 3:
        continue
    sid = best[1]['source_id']
    for n in g.get('nss') or []:
        if n.get('source_id') == sid and n.get('nss_solution_type', '').startswith('SB') and n.get('goodness_of_fit'):
            rec[m.group(1)] = dict(rid=a['review_id'], tic=m.group(1), typ=n['nss_solution_type'],
                                   P=float(n['period']), F2=float(n['goodness_of_fit']),
                                   nrv=int(n.get('rv_n_good_obs_primary') or 0), K1=float(n.get('semi_amplitude_primary') or 'nan'),
                                   G=float(best[1].get('phot_g_mean_mag') or 'nan'),
                                   ruwe=float(best[1].get('ruwe') or 'nan'), nss=best[1].get('non_single_star', ''))
            break
summ = {r['tic']: r for r in csv.DictReader(open(os.path.join(T, 'etv-summary.csv')))}
cand = {r['tic']: r['review_id'] for r in csv.DictReader(open(os.path.join(T, 'etv-candidates.csv')))}
LTTE = {'R623', 'R630', 'R423'}
NOISE = {'R526', 'R365', 'R617', 'R675'}        # measurement problems (Timing)
rows = []
for tic, r in rec.items():
    if tic not in summ or int(summ[tic]['n_sectors']) < 3 or not r['typ'].startswith('SB1'):
        continue
    Pe = float(summ[tic]['P_d'])
    if min(abs(r['P'] / Pe - k) for k in (1,)) > 0.01:
        continue
    r['group'] = 'ltte' if r['rid'] in LTTE else ('cand' if tic in cand and r['rid'] not in NOISE else ('noise' if r['rid'] in NOISE else 'rest'))
    rows.append(r)
with open(os.path.join(HERE, 'sb1-fit-quality.csv'), 'w', newline='') as fh:
    w = csv.DictWriter(fh, fieldnames=['rid', 'tic', 'group', 'typ', 'P', 'F2', 'nrv', 'K1', 'G', 'ruwe', 'nss'], lineterminator='\n', extrasaction='ignore')
    w.writeheader(); w.writerows(sorted(rows, key=lambda r: -r['F2']))
F = np.array([r['F2'] for r in rows]); rest = np.array([r['F2'] for r in rows if r['group'] == 'rest'])
print(f"timed (>= 3 sectors) systems with a Gaia SB1 at the eclipse period: {len(rows)}; F2 median {np.median(F):.2f}, "
      f"robust sd {1.4826*np.median(abs(F-np.median(F))):.2f}, > 3 in {np.mean(F > 3):.0%}")
for grp in ('ltte', 'cand', 'noise'):
    for r in sorted([r for r in rows if r['group'] == grp], key=lambda r: -r['F2']):
        pct = np.mean(rest < r['F2']) * 100
        print(f"  {grp:5s} {r['rid']:5s} P {r['P']:8.3f}  F2 {r['F2']:6.2f}  ({pct:4.0f}th pct of rest)  N_RV {r['nrv']:2d}  K1 {r['K1']:5.1f}  G {r['G']:.1f}  RUWE {r['ruwe']:.2f}")
# rank-sum: are the candidates (ltte + cand) above the rest?
def ranksum_p(x, y, nsim=200000, seed=1):
    rng = np.random.default_rng(seed); allv = np.concatenate([x, y]); n = len(x)
    obs = np.mean(x); sims = np.array([np.mean(rng.permutation(allv)[:n]) for _ in range(nsim // 100)])
    ranks = lambda v: np.argsort(np.argsort(v))
    r = ranks(allv); obs = r[:n].mean()
    sims = np.array([r[rng.permutation(len(allv))[:n]].mean() for _ in range(nsim)])
    return np.mean(sims >= obs)
x3 = np.array([r['F2'] for r in rows if r['group'] == 'ltte'])
xc = np.array([r['F2'] for r in rows if r['group'] in ('ltte', 'cand')])
print(f"one-sided rank test, light-travel three vs rest: p = {ranksum_p(x3, rest):.4f}")
print(f"one-sided rank test, all candidates vs rest:   p = {ranksum_p(xc, rest):.4f}")
print("highest F2 among the rest:", ', '.join(f"{r['rid']} {r['F2']:.1f}" for r in sorted([r for r in rows if r['group']=='rest'], key=lambda r: -r['F2'])[:8]))
