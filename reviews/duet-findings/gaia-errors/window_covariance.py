"""Finding 4: appointment-window widths with and without Gaia's correlations.

Uses only files already in this repository and numpy.
1. Every Gaia DR3 SB1 solution with corr_vec in reviews/**/*nss*.csv
   (corr_vec order as in the team's geometry.py: P, gamma, K, e, omega, Tp).
2. Conjunction time near BTJD 2500 for both conjunctions, linear propagation,
   once with independent errors and once with the full covariance.
3. Calibration: accepted systems with a Gaia SB1 orbit and a measured eclipse
   epoch whose period is within 2% of Gaia's; z = (O - C) / sigma against the
   nearer predicted conjunction.
Run from the repository root:  python3 reviews/duet-findings/gaia-errors/window_covariance.py
"""
import csv, glob, json, math, os
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
REF_BTJD = 2500.0
GAIA_OFFSET = 389.0  # t_c = Tp + 389.0 + M P / 2pi (BTJD), Section 2.2


def load_sb1():
    out = {}
    for f in sorted(glob.glob('reviews/**/*nss*.csv', recursive=True)):
        with open(f, newline='') as fh:
            r = csv.DictReader(fh)
            if not r.fieldnames or 'corr_vec' not in r.fieldnames:
                continue
            for x in r:
                if x.get('nss_solution_type') == 'SB1' and x.get('corr_vec'):
                    out[x['source_id']] = x
    return out


def orbit(n):
    v = np.array([float(n['period']), float(n['eccentricity']),
                  math.radians(float(n['arg_periastron'])),
                  float(n['t_periastron']) + GAIA_OFFSET])
    err = np.array([float(n['period_error']), float(n['eccentricity_error']),
                    math.radians(float(n['arg_periastron_error'])),
                    float(n['t_periastron_error'])])
    C = np.eye(6)
    vals = [float(x) for x in n['corr_vec'].strip('{}[]()').split(',')]
    z = 0
    for i in range(1, 6):
        for j in range(i):
            C[i, j] = C[j, i] = vals[z]
            z += 1
    sub = C[np.ix_([0, 3, 4, 5], [0, 3, 4, 5])]  # P, e, omega, Tp
    return v, err, sub


def conj(v, k):
    p, e, w, tp = v
    nu = (math.pi / 2 if k == 0 else 3 * math.pi / 2) - w
    E = 2 * math.atan2(math.sqrt(1 - e) * math.sin(nu / 2), math.sqrt(1 + e) * math.cos(nu / 2))
    return tp + (E - e * math.sin(E)) % (2 * math.pi) / (2 * math.pi) * p


def t_at(v, k, cyc):
    return conj(v, k) + cyc * v[0]


def sigmas(v, err, corr, k, cyc):
    d = []
    for j in range(4):
        step = max(err[j] * 1e-4, 1e-8)
        a = v.copy(); b = v.copy(); a[j] += step; b[j] -= step
        if j == 1:
            b[j] = max(b[j], 0.0)
        d.append((t_at(a, k, cyc) - t_at(b, k, cyc)) / (a[j] - b[j]))
    d = np.array(d) * err
    s_ind = float(np.sqrt(np.sum(d ** 2)))
    s_full = float(np.sqrt(max(d @ corr @ d, 0.0)))
    return s_full, s_ind


def halfwidth(s):
    return min(max(3 * s, 0.25), 7.0)


def robust_sd(x):
    x = np.asarray(x)
    return float(1.4826 * np.median(np.abs(x - np.median(x))))


def gaia_by_tic():
    m = {}
    for f in ['accepted-systems.csv', 'reviews/2026-11-23-pipeline-and-survey-review/host-stars.csv',
              'claim-adjudication.csv']:
        for r in csv.DictReader(open(f, newline='')):
            g = (r.get('gaia_dr3') or '').strip()
            if g and r.get('tic'):
                m.setdefault(r['tic'].strip(), g)
    for f in glob.glob('reviews/**/targets-selected.json', recursive=True):
        try:
            d = json.load(open(f))
        except Exception:
            continue
        items = d.items() if isinstance(d, dict) else []
        for tic, t in items:
            g = t.get('gaia', {}).get('source_id') if isinstance(t, dict) and isinstance(t.get('gaia'), dict) else None
            if g:
                m.setdefault(str(tic), str(g))
    return m


def measured_epochs():
    ep = {}
    for f in glob.glob('reviews/**/measurements.json', recursive=True):
        try:
            d = json.load(open(f))
        except Exception:
            continue
        if isinstance(d, dict) and d.get('tic') and d.get('primary_epoch_btjd') and d.get('period_days'):
            ep.setdefault(str(d['tic']), (float(d['period_days']), float(d['primary_epoch_btjd'])))
    for r in csv.DictReader(open('reviews/2026-11-23-pipeline-and-survey-review/host-stars.csv', newline='')):
        try:
            ep.setdefault(r['tic'], (float(r['adopted_period_days']), float(r['adopted_epoch_btjd'])))
        except ValueError:
            pass
    return ep


def main():
    sb1 = load_sb1()
    pop = []
    for sid, n in sb1.items():
        try:
            v, err, corr = orbit(n)
        except (ValueError, KeyError):
            continue
        if not (0 <= v[1] < 1) or not np.all(np.isfinite(err)):
            continue
        for k in (0, 1):
            cyc = round((REF_BTJD - conj(v, k)) / v[0])
            sf, si = sigmas(v, err, corr, k, cyc)
            pop.append(dict(source_id=sid, P=v[0], e=v[1], kind=k, sig_full=sf, sig_ind=si))
    print(f'SB1 solutions with corr_vec: {len(sb1)}; conjunction rows: {len(pop)}')
    band = [r for r in pop if 20 <= r['P'] < 60 and r['sig_full'] > 0]
    ratio = np.array([r['sig_ind'] / r['sig_full'] for r in band])
    print(f'20 <= P < 60 d: {len(band)} conjunction rows')
    print('  sigma_ind / sigma_full: median %.2f, p75 %.2f, p90 %.2f' % tuple(np.percentile(ratio, [50, 75, 90])))
    for lo, hi in [(0, .05), (.05, .15), (.15, .4), (.4, 1)]:
        rr = [r['sig_ind'] / r['sig_full'] for r in band if lo <= r['e'] < hi]
        if rr:
            print(f'  e {lo:.2f}-{hi:.2f}: n={len(rr)}, median ratio {np.median(rr):.2f}')
    hw_i = np.array([halfwidth(r['sig_ind']) for r in band])
    hw_f = np.array([halfwidth(r['sig_full']) for r in band])
    print('  windows at the 7-d cap: independent %.0f%%, full %.0f%%' % (100 * np.mean(hw_i >= 7), 100 * np.mean(hw_f >= 7)))
    print('  median half-width: independent %.1f d, full %.1f d' % (np.median(hw_i), np.median(hw_f)))

    accepted = {r['tic'].strip(): r['review_id'] for r in csv.DictReader(open('accepted-systems.csv', newline=''))}
    g = gaia_by_tic()
    ep = measured_epochs()
    out = []
    for tic, rid in accepted.items():
        sid = g.get(tic)
        if not sid or sid not in sb1 or tic not in ep:
            continue
        n = sb1[sid]
        v, err, corr = orbit(n)
        Pecl, T0 = ep[tic]
        if abs(Pecl / v[0] - 1) > 0.02:
            continue
        best = None
        for k in (0, 1):
            cyc = round((T0 - conj(v, k)) / v[0])
            oc = T0 - t_at(v, k, cyc)
            sf, si = sigmas(v, err, corr, k, cyc)
            if best is None or abs(oc) < abs(best[1]):
                best = (k, oc, sf, si)
        k, oc, sf, si = best
        if sf <= 0 or si <= 0:
            continue
        out.append(dict(review_id=rid, tic=tic, gaia_dr3=sid, P_gaia=round(v[0], 6), e=round(v[1], 4), kind=k,
                        oc_d=round(oc, 5), sig_full_d=round(sf, 5), sig_ind_d=round(si, 5),
                        z_full=round(oc / sf, 3), z_ind=round(oc / si, 3)))
    zf = np.array([r['z_full'] for r in out]); zi = np.array([r['z_ind'] for r in out])
    print(f'Calibration against measured eclipse epochs: N = {len(out)}')
    for name, z in [('full covariance', zf), ('independent errors', zi)]:
        print(f'  {name}: robust sd {robust_sd(z):.2f}; within 1/2/3 sigma: '
              f'{100*np.mean(abs(z)<1):.0f}% / {100*np.mean(abs(z)<2):.0f}% / {100*np.mean(abs(z)<3):.0f}%; beyond 3 sigma: {int(np.sum(abs(z)>3))}')
    sub = [r for r in out if 20 <= r['P_gaia'] < 60]
    if sub:
        print(f'  20 <= P < 60 d (N = {len(sub)}): robust sd full {robust_sd([r["z_full"] for r in sub]):.2f}, '
              f'independent {robust_sd([r["z_ind"] for r in sub]):.2f}')
    with open(os.path.join(HERE, 'window-covariance-oc.csv'), 'w', newline='') as fh:
        w = csv.DictWriter(fh, fieldnames=list(out[0]))
        w.writeheader(); w.writerows(sorted(out, key=lambda r: r['review_id']))


if __name__ == '__main__':
    main()
