"""Run 13a: the Gaia-epoch test on the paper's own appointment (A) sample, with Gaia's full covariance.
For every A system with a Gaia DR3 SB1 or SB2 orbit in fable51-nss-appointments.csv and an eclipse ephemeris
in CHECKCARD.csv, carry the eclipse ephemeris back to Gaia's own epoch and compare with Gaia's predicted
conjunctions (both A and B; the nearer is kept), with the conjunction-time sigma propagated through corr_vec
and, for comparison, with independent errors. Also carries Gaia's ephemeris forward to the eclipse epoch.
Run from the repository root:
  python3 reviews/2026-11-24-duet-research-runs-1-4/run13-a-sample-gaia-epoch/a_epoch_test.py
"""
import sys, os, math, re, html
import numpy as np, pandas as pd
D = 'reviews/2026-11-24-duet-research-runs-1-4/'
sys.path.insert(0, D)
import window_covariance as W
HERE = os.path.dirname(os.path.abspath(__file__))

def orbit(n):
    # corr_vec order (Gaia nsstools): SB1 P, gamma, K1, e, omega, Tp; SB2 P, gamma, K1, K2, e, omega, Tp
    sb2 = n['nss_solution_type'] == 'SB2'
    npar, idx = (7, [0, 4, 5, 6]) if sb2 else (6, [0, 3, 4, 5])
    v = np.array([float(n['period']), float(n['eccentricity']), math.radians(float(n['arg_periastron'])),
                  float(n['t_periastron']) + W.GAIA_OFFSET])
    err = np.array([float(n['period_error']), float(n['eccentricity_error']),
                    math.radians(float(n['arg_periastron_error'])), float(n['t_periastron_error'])])
    vals = [float(x) for x in str(n['corr_vec']).strip('{}[]()"').split(',')]
    if len(vals) != npar * (npar - 1) // 2: raise ValueError('corr_vec length')
    C = np.eye(npar); z = 0
    for i in range(1, npar):
        for j in range(i):
            C[i, j] = C[j, i] = vals[z]; z += 1
    return v, err, C[np.ix_(idx, idx)]

def paper_ephemerides():
    """The paper's ephemeris table (paper.html): label, P +- err, T0 (BJD_TDB) [+- err]. BTJD = BJD - 2457000."""
    t = open('paper.html').read(); out = {}
    for r in re.findall(r'<tr[^>]*>(.*?)</tr>', t, re.S):
        c = [re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', '', x))).strip() for x in re.findall(r'<t[dh][^>]*>(.*?)</t[dh]>', r, re.S)]
        if len(c) >= 3 and re.fullmatch(r'A\d+', c[0]):
            m1 = re.match(r'([\d.]+) ± ([\d.]+)$', c[1]); m2 = re.match(r'(24\d+\.\d+)', c[2])
            if m1 and m2: out.setdefault(c[0], (float(m1.group(1)), float(m1.group(2)), float(m2.group(1)) - 2457000.0))
    return out

def paper_methods():
    """Discovery method of each A system from the paper's Table A1 (App = appointments search; Batch, Fold, MD, Ast)."""
    t = open('paper.html').read(); out = {}
    for r in re.findall(r'<tr[^>]*>(.*?)</tr>', t, re.S):
        c = [re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', '', x))).strip() for x in re.findall(r'<t[dh][^>]*>(.*?)</t[dh]>', r, re.S)]
        if len(c) >= 6 and re.fullmatch(r'A\d+', c[0]) and c[5] in ('confirmed', 'probable'): out.setdefault(c[0], c[4])
    return out


def main():
    nss = pd.read_csv(D + 'fable51-nss-appointments.csv', dtype=str)
    EPH = paper_ephemerides()
    METHOD = paper_methods()
    cc = pd.read_csv('CHECKCARD.csv', dtype=str)
    for _, c in cc.iterrows():
        try: EPH.setdefault(c.label, (float(c.P_days), float(c.eP_days) if c.eP_days == c.eP_days else float('nan'), float(c.T0_primary_BTJD)))
        except (TypeError, ValueError): pass
    rows = []
    for _, n in nss.iterrows():
        rid = n.review_id
        if n.nss_solution_type not in ('SB1', 'SB2') or rid not in EPH: continue
        P, eP, T0 = EPH[rid]
        v, err, corr = orbit(n)
        ratio = P / v[0]
        rel = 'same' if abs(ratio - 1) < 0.02 else f'x{ratio:.3f}'
        if rel != 'same':               # eclipse period is an alias or a different period; test at Gaia's period is meaningless
            rows.append(dict(review_id=rid, sol=n.nss_solution_type, P_ecl=P, P_gaia=v[0], P_ratio=round(ratio, 4), note='period differs >2%'))
            continue
        zP = (v[0] - P) / math.hypot(err[0], eP if eP == eP else 0)
        best = None
        for k in (0, 1):
            tg = W.conj(v, k)
            nb = round((tg - T0) / P)
            o0 = T0 + nb * P - tg
            sf, si = W.sigmas(v, err, corr, k, 0)
            sb = abs(nb) * (eP if eP == eP else 0)
            cyc = round((T0 - tg) / v[0])
            oT = T0 - W.t_at(v, k, cyc)
            sTf, sTi = W.sigmas(v, err, corr, k, cyc)
            d = dict(review_id=rid, sol=n.nss_solution_type, P_ecl=P, P_gaia=v[0], P_ratio=round(ratio, 6), z_period=round(zP, 2),
                     e=round(v[1], 3), e_err=round(err[1], 3), conj='A' if k == 0 else 'B',
                     offset_gaia_epoch_d=round(o0, 4), sig_full_d=round(math.hypot(sf, sb), 4), sig_ind_d=round(math.hypot(si, sb), 4),
                     z_full=round(o0 / math.hypot(sf, sb), 2), z_ind=round(o0 / math.hypot(si, sb), 2),
                     phase=round(o0 / v[0], 4), offset_tess_d=round(oT, 3), z_tess_full=round(oT / sTf, 2), z_tess_ind=round(oT / sTi, 2),
                     cycles=cyc, note='')
            if best is None or abs(o0) < abs(best['offset_gaia_epoch_d']): best = d
        rows.append(best)
    o = pd.DataFrame(rows)
    o.to_csv(os.path.join(HERE, 'a-epoch-test.csv'), index=False)
    t = o[o.note == '']
    print(f'A systems with SB1/SB2 orbit: {len(o)}; same period (within 2%): {len(t)}; others: {(o.note != "").sum()}')
    print(o[o.note != ''][['review_id', 'sol', 'P_ecl', 'P_gaia', 'P_ratio']].to_string(index=False))
    print('\nconjunction offset at Gaia epoch in sigma (nearer conjunction):')
    for lab, q in [('all', t), ('SB1', t[t.sol == 'SB1']), ('SB2', t[t.sol == 'SB2']), ('e<0.1', t[t.e < 0.1]), ('e>=0.1', t[t.e >= 0.1]),
                   ('|zP|<3', t[t.z_period.abs() < 3])]:
        print(f'  {lab:7s} n={len(q):3d} full: robust sd {W.robust_sd(q.z_full):.2f}, |z|>=3 {(q.z_full.abs()>=3).sum()};'
              f'  independent: robust sd {W.robust_sd(q.z_ind):.2f}, |z|>=3 {(q.z_ind.abs()>=3).sum()};  median |phase| {q.phase.abs().median():.4f}')
    print('  conjunction kinds:', t.conj.value_counts().to_dict())
    print('\n|z_full| >= 3 or |phase| >= 0.02 at Gaia epoch, or |z_period| >= 3:')
    cols = ['review_id', 'sol', 'P_ecl', 'z_period', 'e', 'conj', 'offset_gaia_epoch_d', 'sig_full_d', 'z_full', 'z_ind', 'phase', 'offset_tess_d', 'z_tess_full', 'z_tess_ind']
    print(t[(t.z_full.abs() >= 3) | (t.phase.abs() >= 0.02) | (t.z_period.abs() >= 3)].sort_values('z_full')[cols].to_string(index=False))
    print('\nthe paper\'s three uncounted conjunction offsets and its two Gaia-epoch cases:')
    print(t[t.review_id.isin(['A87', 'A89', 'A104', 'A147', 'A167', 'A202', 'A203'])][cols].to_string(index=False))

    print('\nat the eclipse epoch (Gaia ephemeris carried forward), same-period systems:')
    print(f'  robust sd of z: full {W.robust_sd(t.z_tess_full):.2f}, independent {W.robust_sd(t.z_tess_ind):.2f}')
    for lab, col in [('full covariance', 'z_tess_full'), ('independent', 'z_tess_ind')]:
        for k in (3, 4.5, 6):
            print(f'  {lab:15s}: eclipse outside +-{k} sigma: {(t[col].abs() > k).sum()} of {len(t)}')

    # 13b: would the found eclipses have been inside the search windows built each way?
    # half-width = min(max(k * sigma, 0.25 d), 7 d), sigma at the eclipse epoch (paper's T0); sigma = |offset| / |z|
    t = t.copy()
    t['method'] = t.review_id.map(METHOD)
    print('  methods of the tested systems:', t.method.value_counts().to_dict())
    t['sig_tess_full'] = (t.offset_tess_d / t.z_tess_full).abs()
    t['sig_tess_ind'] = (t.offset_tess_d / t.z_tess_ind).abs()
    print('\n13b: found eclipses outside the window min(max(k sigma, 0.25 d), 7 d) at the eclipse epoch:')
    for lab, col in [('independent (the search)', 'sig_tess_ind'), ('full covariance', 'sig_tess_full')]:
        for k in (3, 4.5):
            hw = np.clip(k * t[col], 0.25, 7.0)
            out = t[t.offset_tess_d.abs() > hw]
            print(f'  {lab:25s} k={k}: median half-width {hw.median():.2f} d; outside: {len(out)} {sorted(out.review_id, key=lambda s: int(s[1:]))}')
            for mm, q in (('App', t.method == 'App'), ('not App', t.method != 'App')):
                o2 = out[out.method.eq('App') == (mm == 'App')]
                print(f'      {mm:8s}: {len(o2)} of {int(q.sum())} outside {sorted(o2.review_id, key=lambda s: int(s[1:]))}')
    t[['review_id', 'method', 'P_ecl', 'z_period', 'offset_tess_d', 'sig_tess_full', 'sig_tess_ind', 'z_tess_full', 'z_tess_ind']].to_csv(os.path.join(HERE, 'a-window-coverage.csv'), index=False)


if __name__ == '__main__':
    main()

def calib():
    """Robust width of z by discovery method: systems not found through the windows are an unbiased test."""
    t = pd.read_csv(os.path.join(HERE, 'a-window-coverage.csv'))
    g = pd.read_csv(os.path.join(HERE, 'a-epoch-test.csv'))
    t = t.merge(g[['review_id', 'z_full', 'z_ind', 'sol']], on='review_id')
    print('\nrobust width of z (eclipse epoch | Gaia epoch), full covariance / independent:')
    for lab, q in (('App', t[t.method == 'App']), ('not App', t[t.method != 'App']), ('not App, SB1', t[(t.method != 'App') & (t.sol == 'SB1')])):
        print(f'  {lab:13s} n={len(q):3d}: eclipse epoch {W.robust_sd(q.z_tess_full):.2f} / {W.robust_sd(q.z_tess_ind):.2f};'
              f'  Gaia epoch {W.robust_sd(q.z_full):.2f} / {W.robust_sd(q.z_ind):.2f}')

if __name__ == '__main__':
    calib()
