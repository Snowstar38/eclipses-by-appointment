"""Do Gaia's understated SB1 errors follow each solution's own goodness of fit?

If the period, conjunction and eccentricity errors are too small because each star's RV
errors are, the pulls should widen with F2, and dividing each pull by the solution's own
sqrt(chi2 / nu) (chi2 / nu from F2 with nu = N_RV - 6) should bring them to unit width.
Pulls: Gaia period against the eclipse period (gaia-period-pulls.csv, R and A); conjunction
at Gaia's epoch with the full covariance (gaia-epoch-test.csv for R, a-epoch-test.csv for A);
e cos w against the secondary phase (A systems, from eccentricity_errors.py's table if present).
SB1 only (the SB2 rows carry no usable N_RV).
nu is recovered from obj_func and F2, since some exports carry placeholder RV counts.
Run from the repository root: python3 reviews/duet-findings/gaia-errors/fit_quality_scaling.py
"""
import csv, glob, json, math, os
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
nss = {}
for f in glob.glob('reviews/**/gaia.json', recursive=True):
    try:
        g = json.load(open(f))
    except (ValueError, OSError):
        continue
    for n in g.get('nss') or []:
        if n.get('nss_solution_type') == 'SB1' and n.get('goodness_of_fit') and n.get('obj_func'):
            nss[n['source_id']] = n
for f in glob.glob('reviews/**/*nss*.csv', recursive=True):
    try:
        for n in csv.DictReader(open(f)):
            if n.get('nss_solution_type') == 'SB1' and n.get('goodness_of_fit') and n.get('obj_func') and n.get('source_id') not in nss:
                nss[n['source_id']] = n
    except (UnicodeDecodeError, csv.Error, OSError):
        continue
byrid = {r['review_id']: r['source_id'] for r in csv.DictReader(open(os.path.join(HERE, 'fable51-nss-appointments.csv')))}
for r in csv.DictReader(open(os.path.join(HERE, 'gaia-period-pulls.csv'))):
    byrid.setdefault(r['review_id'], r['sid'])
for r in csv.DictReader(open(os.path.join(HERE, '..', 'timing', 'gaia-ruwe-r-systems.csv'))):
    byrid.setdefault(r['review_id'], r['source_id'])


def F2_of(chi2, nu):
    return math.sqrt(9 * nu / 2) * ((chi2 / nu) ** (1 / 3) + 2 / (9 * nu) - 1)


def nu_of(n):
    """nu from obj_func and F2 (unique; reproduces N_RV - 6 on all 816 SB1 rows that list N)"""
    obj, F = float(n['obj_func']), float(n['goodness_of_fit'])
    return min(range(1, 400), key=lambda k: abs(F2_of(obj, k) - F))


def chi2nu(n):
    nu = nu_of(n)
    F = float(n['goodness_of_fit'])
    return (1 - 2 / (9 * nu) + F / math.sqrt(9 * nu / 2)) ** 3, F


def rw(z):
    z = np.asarray(z)
    return 1.4826 * np.median(np.abs(z - np.median(z)))


sets = []
pp = [(r['review_id'], float(r['z'])) for r in csv.DictReader(open(os.path.join(HERE, 'gaia-period-pulls.csv')))]
sets.append(('period (Gaia vs eclipse), R and A', pp))
ep = [(r['review_id'], float(r['z_gaia_epoch'])) for r in csv.DictReader(open(os.path.join(HERE, 'gaia-epoch-test.csv'))) if r['z_gaia_epoch']]
sets.append(('conjunction at Gaia epoch, R', ep))
ae = [(r['review_id'], float(r['z_full'])) for r in csv.DictReader(open(os.path.join(HERE, 'a-epoch-test.csv'))) if r['z_full'] and r['sol'] == 'SB1']
sets.append(('conjunction at Gaia epoch, A', ae))
rows_out = []
rng = np.random.default_rng(3)
for lab, data in sets:
    z, F, s = [], [], []
    for rid, zz in data:
        sid = byrid.get(rid)
        if not sid or sid not in nss or not math.isfinite(zz) or abs(zz) > 20:
            continue
        c, f2 = chi2nu(nss[sid])
        z.append(zz); F.append(f2); s.append(math.sqrt(c))
        rows_out.append(dict(test=lab, review_id=rid, source_id=sid, z=round(zz, 3), F2=round(f2, 3), sqrt_chi2nu=round(math.sqrt(c), 3)))
    z, F, s = map(np.array, (z, F, s))
    order = np.argsort(F); thirds = np.array_split(order, 3)
    rho = np.corrcoef(np.argsort(np.argsort(F)), np.argsort(np.argsort(np.abs(z))))[0, 1]
    perm = [np.corrcoef(rng.permutation(len(F)), np.argsort(np.argsort(np.abs(z))))[0, 1] for _ in range(20000)]
    print(f"{lab}: n {len(z)}, robust width {rw(z):.2f}; Spearman(|z|, F2) {rho:+.2f} (one-sided p {np.mean(np.array(perm) >= rho):.3f})")
    print("   by F2 tercile: " + "; ".join(f"F2 {F[t].min():+.1f} to {F[t].max():+.1f}: width {rw(z[t]):.2f}, |z|>=3 {np.sum(np.abs(z[t]) >= 3)}" for t in thirds))
    print(f"   divided by each solution's sqrt(chi2/nu) (median {np.median(s):.2f}): width {rw(z / s):.2f}, |z|>=3 {np.sum(np.abs(z / s) >= 3)} (was {np.sum(np.abs(z) >= 3)})")
with open(os.path.join(HERE, 'fit-quality-scaling.csv'), 'w', newline='') as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows_out[0]), lineterminator='\n'); w.writeheader(); w.writerows(rows_out)

# an empirical scale that grows with F2: errors x a * exp(b * F2), fitted to unit robust width
# per F2 tercile on the two conjunction sets together (Gaia's epoch), then applied to each set
import itertools
R = [r for r in rows_out if r['test'].startswith('conjunction')]
z = np.array([r['z'] for r in R]); F = np.array([r['F2'] for r in R])
best = None
for a, b in itertools.product(np.arange(0.8, 1.61, 0.02), np.arange(0.0, 0.61, 0.02)):
    zs = z / (a * np.exp(b * F))
    cost = sum((rw(zs[t]) - 1) ** 2 for t in np.array_split(np.argsort(F), 4))
    if best is None or cost < best[0]:
        best = (cost, a, b)
_, a, b = best
print(f"\nconjunctions (R and A, n {len(z)}): errors scale as {a:.2f} exp({b:.2f} F2), i.e. x{a*np.exp(-b):.2f} at F2 = -1, "
      f"x{a:.2f} at 0, x{a*np.exp(b):.2f} at 1, x{a*np.exp(2*b):.2f} at 2, x{a*np.exp(3*b):.2f} at 3")
# bootstrap the slope
bs = []
for _ in range(300):
    i = rng.integers(0, len(z), len(z)); zz, FF = z[i], F[i]; bb = None
    for aa, b2 in itertools.product(np.arange(0.8, 1.61, 0.04), np.arange(0.0, 0.61, 0.02)):
        zs = zz / (aa * np.exp(b2 * FF))
        cost = sum((rw(zs[t]) - 1) ** 2 for t in np.array_split(np.argsort(FF), 4))
        if bb is None or cost < bb[0]: bb = (cost, b2)
    bs.append(bb[1])
print(f"   slope b: 68% bootstrap {np.percentile(bs, 16):.2f}-{np.percentile(bs, 84):.2f}; b = 0 in {np.mean(np.array(bs) <= 0.001):.0%} of resamples")
for lab in ('conjunction at Gaia epoch, R', 'conjunction at Gaia epoch, A'):
    S = [r for r in rows_out if r['test'] == lab]
    zz = np.array([r['z'] for r in S]); FF = np.array([r['F2'] for r in S]); sc = a * np.exp(b * FF)
    print(f"   {lab}: |z|>=3 {np.sum(abs(zz) >= 3)} as published -> {np.sum(abs(zz / sc) >= 3)} with the F2 scale "
          f"(-> {np.sum(abs(zz / 1.4) >= 3)} with a flat 1.4); width {rw(zz):.2f} -> {rw(zz / sc):.2f}")
    for r in sorted(S, key=lambda r: -abs(r['z'])):
        if abs(r['z']) >= 3:
            print(f"      {r['review_id']:5s} z {r['z']:+6.2f}  F2 {r['F2']:+5.2f}  scaled {r['z'] / (a * np.exp(b * r['F2'])):+6.2f}")

# within confirmed systems only (a failed Gaia check was a reason to grade probable)
tier = {}
for r in csv.DictReader(open('accepted-systems.csv')):
    tier.setdefault(r['review_id'], r['tier'])
cm = np.array([tier.get(r['review_id']) == 'confirmed' for r in R])
zc_, Fc_ = z[cm], F[cm]
rho = np.corrcoef(np.argsort(np.argsort(Fc_)), np.argsort(np.argsort(np.abs(zc_))))[0, 1]
perm = np.array([np.corrcoef(rng.permutation(len(zc_)), np.argsort(np.argsort(np.abs(zc_))))[0, 1] for _ in range(20000)])
print(f"   confirmed systems only (n {cm.sum()}): Spearman(|z|, F2) {rho:+.2f} (p {np.mean(perm >= rho):.4f}); widths by F2 tercile "
      + ", ".join(f"{rw(zc_[t]):.2f}" for t in np.array_split(np.argsort(Fc_), 3)))

# against a flat scale with the same mean (same total window width)
sc = a * np.exp(b * F); flat = sc.mean()
q = np.array_split(np.argsort(F), 4)
print(f"\nsame mean scale ({flat:.2f}): robust width by F2 quartile, F2 scale | flat:")
for t in q:
    print(f"   F2 {F[t].min():+.1f} to {F[t].max():+.1f}: {rw(z[t] / sc[t]):.2f} | {rw(z[t] / flat):.2f}")
for k in (3, 4, 5):
    print(f"   windows at +-{k} sigma: misses {np.sum(abs(z / sc) >= k)} with the F2 scale, {np.sum(abs(z / flat) >= k)} flat (of {len(z)})")

# eccentricity: Gaia's e / sigma_e on circular short binaries (eccentricity_errors.py's test 1), by F2
gv = list(csv.DictReader(open(os.path.join(HERE, '..', 'gaia-geometry', 'gaia-vs-eclipse.csv'))))
E = []
for r in gv:
    try:
        P = float(r['eclipse_period_days'].split('|')[0]); e = float(r['gaia_ecc'].split('|')[0]); se = float(r['gaia_ecc_err'].split('|')[0])
    except (ValueError, KeyError):
        continue
    sid = byrid.get(r['review_id'])
    if r.get('class') != 'harmonic 1' or r.get('nss_type') != 'SB1' or P >= 3 or not sid or sid not in nss or not se > 0:
        continue
    E.append((r['review_id'], e / se, float(nss[sid]['goodness_of_fit'])))
ez = np.array([x[1] for x in E]); eF = np.array([x[2] for x in E])
kr = lambda v: math.sqrt(np.mean(np.asarray(v) ** 2) / 2)
lo, hi = eF <= np.median(eF), eF > np.median(eF)
sce = a * np.exp(b * eF)
print(f"\neccentricity on circular SB1s below 3 d (n {len(E)}): Rayleigh scale {kr(ez):.2f}; F2 below median {kr(ez[lo]):.2f} (n {lo.sum()}), "
      f"above {kr(ez[hi]):.2f} (n {hi.sum()}); with the conjunction F2 scale {kr(ez / sce):.2f} (low {kr(ez[lo] / sce[lo]):.2f}, high {kr(ez[hi] / sce[hi]):.2f})")

# Table 4's e cos w failures (table4_scaled.py's list, quoted sigma) under the F2 scale
T4 = {'A21': 3.7, 'A28': 5.7, 'A30': 5.3, 'A63': 3.8, 'A65': 4.0, 'A145': 4.5, 'A159': 3.3, 'A202': 3.5}
print("\nTable 4 e cos w failures under the F2 scale (quoted sigma -> scaled; flat 1.37 in brackets):")
for rid, zq in T4.items():
    sid = byrid.get(rid); n = nss.get(sid)
    if n is None:
        print(f"   {rid}: no SB1 row"); continue
    Fv = float(n['goodness_of_fit']); s_ = a * math.exp(b * Fv)
    print(f"   {rid:5s} F2 {Fv:+5.2f}: {zq:.1f} -> {zq / s_:.2f} [{zq / 1.37:.2f}]")

# SB2s (no F2 cut; N_RV not usable, nu recovered from obj_func and F2): pulls against sqrt(chi2/nu)
print("\nSB2 and SB2C solutions of the A sample (a-epoch-test.csv), pulls divided by each solution's sqrt(chi2/nu):")
N2 = {r['review_id']: r for r in csv.DictReader(open(os.path.join(HERE, 'fable51-nss-appointments.csv'))) if r['nss_solution_type'].startswith('SB2')}
S2 = [r for r in csv.DictReader(open(os.path.join(HERE, 'a-epoch-test.csv'))) if r['review_id'] in N2 and r['z_full']]
s2 = np.array([math.sqrt(chi2nu(N2[r['review_id']])[0]) for r in S2])
F2s = np.array([float(N2[r['review_id']]['goodness_of_fit']) for r in S2])
print(f"   n {len(S2)}; F2 median {np.median(F2s):.1f} (max {F2s.max():.1f}); sqrt(chi2/nu) median {np.median(s2):.2f} ({s2.min():.2f}-{s2.max():.2f})")
for lab, col in (('period', 'z_period'), ('conjunction at Gaia epoch', 'z_full')):
    zz = np.array([float(r[col]) for r in S2])
    rho = np.corrcoef(np.argsort(np.argsort(F2s)), np.argsort(np.argsort(np.abs(zz))))[0, 1]
    perm = np.array([np.corrcoef(rng.permutation(len(zz)), np.argsort(np.argsort(np.abs(zz))))[0, 1] for _ in range(20000)])
    print(f"   {lab}: width {rw(zz):.2f}, |z|>=3 {np.sum(abs(zz) >= 3)}; Spearman(|z|, F2) {rho:+.2f} (p {np.mean(perm >= rho):.3f}); "
          f"scaled: width {rw(zz / s2):.2f}, |z|>=3 {np.sum(abs(zz / s2) >= 3)}"
          + "".join(f"; {r['review_id']} {float(r[col]):+.1f} -> {float(r[col]) / x:+.1f}" for r, x in zip(S2, s2) if abs(float(r[col]) / x) >= 3))

# does F2 mark the conjunction-kind exceptions or the probable tier? (gaia-geometry/conjunction-kind.csv, clean timing)
tic2src = {r['tic']: r['source_id'] for r in csv.DictReader(open(os.path.join(HERE, '..', 'timing', 'gaia-ruwe-r-systems.csv')))}
ck = [r for r in csv.DictReader(open(os.path.join(HERE, '..', 'gaia-geometry', 'conjunction-kind.csv')))
      if r['tier'] in ('confirmed', 'probable') and float(r['z_other']) > 3 and float(r['z_closest']) < 3]
K = []
for r in ck:
    sid = tic2src.get(r['tic']) or byrid.get(r['review_id'])
    if sid in nss:
        K.append((int(r['kind']), float(nss[sid]['goodness_of_fit']), r['tier'] == 'probable'))
kk = np.array([x[0] for x in K]); kf = np.array([x[1] for x in K]); kp = np.array([x[2] for x in K])
print(f"\nconjunction kind (clean timing, SB1, n {len(K)}): kind-1 fraction by F2 <0 / 0-1 / 1-2 / 2-3: "
      + " / ".join(f"{kk[(kf >= lo) & (kf < hi)].mean():.2f}" for lo, hi in ((-9, 0), (0, 1), (1, 2), (2, 3)))
      + f"; median F2 probable {np.median(kf[kp]):.2f}, confirmed {np.median(kf[~kp]):.2f}")

# what goes with a high F2? accepted R systems with an SB1 (gaia-ruwe-r-systems.csv sources)
from scipy.stats import spearmanr   # SciPy for this last block only
srcrow = {}
for f in glob.glob('reviews/**/gaia.json', recursive=True):
    try:
        g = json.load(open(f))
    except (ValueError, OSError):
        continue
    if isinstance(g, dict):
        for s_ in g.get('src') or []:
            if isinstance(s_, dict):
                srcrow.setdefault(s_.get('source_id'), s_)
Q = []
for r in csv.DictReader(open(os.path.join(HERE, '..', 'timing', 'gaia-ruwe-r-systems.csv'))):
    sid = r['source_id']
    if sid in nss and sid in srcrow and nss[sid].get('rv_n_good_obs_primary'):
        n, s_ = nss[sid], srcrow[sid]
        g_ = lambda k: float(s_.get(k) or 'nan')
        Q.append(dict(F=float(n['goodness_of_fit']), G=g_('phot_g_mean_mag'), bp_rp=g_('bp_rp'), teff=g_('teff_gspphot'), ruwe=g_('ruwe'),
                      P=float(n['period']), K1=float(n['semi_amplitude_primary']), e=float(n['eccentricity'] or 0)))
QF = np.array([q['F'] for q in Q])
out = []
for k in ('teff', 'bp_rp', 'K1', 'G', 'ruwe', 'P', 'e'):
    x = np.array([q[k] for q in Q]); m = np.isfinite(x)
    rho, p = spearmanr(x[m], QF[m]); out.append(f"{k} {rho:+.2f} (p {p:.1g}, n {m.sum()})")
print("\nSpearman with F2, accepted R systems' SB1s: " + "; ".join(out))
