"""Do the timing-variation systems carry Gaia's astrometric binary flag?

Gaia DR3's non_single_star is a bit mask: 1 astrometric, 2 spectroscopic, 4 eclipsing.
For every accepted system with a review gaia.json in this repository, the Gaia row nearest
the accepted position (within 3 arcsec) gives RUWE and non_single_star; the table is written
to gaia-ruwe-r-systems.csv. A short inner orbit (days) moves the photocentre by microarcseconds,
so an astrometric flag on these systems points to a wider companion: a tertiary.
Compared: the systems timed in three or more sectors (etv-summary.csv) and the timing-variation
candidates among them (etv-candidates.csv), with a one-sided Fisher test.
Run from the repository root: python3 reviews/duet-findings/timing/astrometric_flag.py
"""
import csv, glob, json, math, os, re
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
acc = {}
for r in csv.DictReader(open('accepted-systems.csv')):
    acc.setdefault(r['tic'], r)
rec = {}
for f in sorted(glob.glob('reviews/**/gaia.json', recursive=True)):
    m = re.search(r'/(\d{4,11})/(?:[a-z-]+/)?gaia\.json$', f)
    if not m or m.group(1) not in acc or m.group(1) in rec:
        continue
    try:
        src = json.load(open(f)).get('src') or []
    except (ValueError, AttributeError, OSError):
        continue
    a = acc[m.group(1)]
    ra0, de0 = float(a['ra_deg']), float(a['dec_deg'])
    best = None
    for s in src:
        try:
            sep = math.hypot((float(s['ra']) - ra0) * math.cos(math.radians(de0)), float(s['dec']) - de0) * 3600
        except (KeyError, ValueError, TypeError):
            continue
        if best is None or sep < best[0]:
            best = (sep, s)
    if best and best[0] < 3 and best[1].get('ruwe') not in (None, ''):
        s = best[1]
        rec[m.group(1)] = dict(review_id=a['review_id'], tic=m.group(1), tier=a['tier'], source_id=s['source_id'],
                               sep_arcsec=round(best[0], 2), ruwe=float(s['ruwe']), non_single_star=s.get('non_single_star', ''),
                               phot_g_mean_mag=s.get('phot_g_mean_mag', ''), parallax=s.get('parallax', ''), source_file=f)
rows = sorted(rec.values(), key=lambda r: (r['review_id'][0], int(re.sub(r'\D', '', r['review_id']) or 0)))
with open(os.path.join(HERE, 'gaia-ruwe-r-systems.csv'), 'w', newline='') as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows[0]), lineterminator='\n')
    w.writeheader(); w.writerows(rows)
astro = lambda r: (int(r['non_single_star'] or 0) & 1) == 1
print(f"accepted systems with a Gaia row in a review gaia.json: {len(rec)}; astrometric flag on {sum(astro(r) for r in rec.values())}; "
      f"RUWE median {np.median([r['ruwe'] for r in rec.values()]):.2f}, > 1.4 in {np.mean([r['ruwe'] > 1.4 for r in rec.values()]):.0%}")
summ = {r['tic']: r for r in csv.DictReader(open(os.path.join(HERE, 'etv-summary.csv')))}
cand = {r['tic']: r['review_id'] for r in csv.DictReader(open(os.path.join(HERE, 'etv-candidates.csv')))}
timed = [t for t in summ if t in rec and int(summ[t]['n_sectors']) >= 3]
N = len(timed); K = sum(astro(rec[t]) for t in timed)
n = sum(t in cand for t in timed); k = sum(astro(rec[t]) and t in cand for t in timed)
p = sum(math.comb(K, i) * math.comb(N - K, n - i) for i in range(k, min(K, n) + 1)) / math.comb(N, n)
print(f"timed in >= 3 sectors: {N}, astrometric flag on {K}; timing-variation candidates {n}, flagged {k}; one-sided Fisher p = {p:.1e}")
print("candidates:", ", ".join(f"{rec[t]['review_id']} (RUWE {rec[t]['ruwe']:.2f}, flag {rec[t]['non_single_star']})" for t in cand if t in rec))
print("every accepted system with the astrometric flag:")
for r in rows:
    if astro(r):
        s = summ.get(r['tic'])
        tl = (f"{s['n_sectors']} sectors timed, linear reduced chi2 {float(s['chi2r_lin']):.1f}, sector O-C range {float(s['sector_oc_range_min']):.1f} min, P {float(s['P_d']):.4f} d"
              if s else "not timed")
        print(f"  {r['review_id']:5s} RUWE {r['ruwe']:.2f}  G {float(r['phot_g_mean_mag']):.2f}  parallax {float(r['parallax']):.2f} mas  | {tl}"
              + ("  [timing-variation candidate]" if r['tic'] in cand else ""))
