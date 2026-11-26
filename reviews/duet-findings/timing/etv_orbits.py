"""Light-travel-time orbits for the four timing-variation candidates with extra sectors.

Input: timing/etv4-times.csv (Fable 5's primary-eclipse times for R371, R423, R630 and R660
from MAST QLP, every file checked with the cadence-curvature clock test; R660's s102-103
times already carry the +BC(t) repair) with R630's two scrambled-clock s15 times replaced
by their TESS-SPOC re-times from timing/s1415-tspoc-times.csv. For each target, fit
  linear:     T0 + P E
  quadratic:  + c E^2                (a steady period change)
  LTTE:       + light-travel term of an outer orbit (period P3, semi-amplitude A,
                eccentricity e, argument w, periastron time tp; Irwin 1952)
with per-event errors inflated by a jitter term chosen so the best model has reduced
chi2 = 1 (the same jitter is used for every model of a target). Reports chi2, BIC, the
outer mass function f(m3) = (A c)^3 / (G P3^2) and the minimum tertiary mass for the TIC
primary mass plus a companion from the inner orbit (assumed m2 = 0.6 m1 unless given).
A grid over P3 from 1.5 to 20 yr (log-spaced) with local least squares at each step; the
P3 range within delta-chi2 < 4 of the best is quoted.
usage (from the repo root): python3 reviews/duet-findings/timing/etv_orbits.py   (SciPy)
"""
import os
import numpy as np, pandas as pd
from scipy.optimize import least_squares, brentq

D = os.path.dirname(os.path.abspath(__file__)) + '/'
M1 = {'R371': 2.05, 'R423': 0.929, 'R630': 1.06, 'R660': 1.2}   # TIC masses (R660 giant: no TIC mass; 1.2 assumed)
C_AU_S = 499.005  # light seconds per au

f = pd.read_csv(D + 'etv4-times.csv'); f['tic'] = f.tic.astype(str)
sp = pd.read_csv(D + 's1415-tspoc-times.csv'); sp['tic'] = sp.tic.astype(str); sp = sp[sp.flag == 'ok']
for i, r in f[(f.rid == 'R630') & (f.sector == 15)].iterrows():
    m = sp[(sp.tic == r.tic) & (sp.sector == 15) & (abs(sp.t_mid_listed - r.t_mid_btjd) < 0.01)]
    f.loc[i, ['t_mid_btjd', 'err_s', 'clock']] = [m.t_mid_tspoc.iloc[0], m.err_s.iloc[0], 'tess-spoc']


def kepler_E(M, e):
    E = M.copy()
    for _ in range(30):
        E = E - (E - e * np.sin(E) - M) / (1 - e * np.cos(E))
    return E


def ltte(t, P3, A, e, w, tp):
    M = 2 * np.pi * (t - tp) / P3
    E = kepler_E(np.mod(M, 2 * np.pi), e)
    nu = 2 * np.arctan2(np.sqrt(1 + e) * np.sin(E / 2), np.sqrt(1 - e) * np.cos(E / 2))
    return A / np.sqrt(1 - e ** 2 * np.cos(w) ** 2) * ((1 - e ** 2) / (1 + e * np.cos(nu)) * np.sin(nu + w) + e * np.sin(w))


def design(t, x, P3, e, tp, quad=False):
    """columns: 1, E (, E^2) and, if P3, the two LTTE columns linear in K cos w and K sin w"""
    cols = [np.ones_like(x), x] + ([x ** 2] if quad else [])
    if P3:
        M = np.mod(2 * np.pi * (t - tp) / P3, 2 * np.pi)
        Ea = kepler_E(M, e)
        nu = 2 * np.arctan2(np.sqrt(1 + e) * np.sin(Ea / 2), np.sqrt(1 - e) * np.cos(Ea / 2))
        r = (1 - e ** 2) / (1 + e * np.cos(nu))
        cols += [r * np.sin(nu), r * np.cos(nu) + e]
    return np.vstack(cols).T


def wls(A, t, s):
    W = 1 / s ** 2
    c = np.linalg.lstsq(A * np.sqrt(W)[:, None], t * np.sqrt(W), rcond=None)[0]
    r = t - A @ c
    return np.sum(W * r * r), c, r


P3_GRID = np.exp(np.linspace(np.log(400), np.log(7300), 160))
E_GRID = {'circular': [0.0], 'eccentric': [0.0, 0.15, 0.3, 0.45, 0.6, 0.75]}


def scan(t, x, s, eccs):
    best = {}
    for P3 in P3_GRID:
        for e in eccs:
            for tp in t.min() + P3 * np.arange(0, 1, 1 / (1 if e == 0 else 24)):
                c2, c, r = wls(design(t, x, P3, e, tp), t, s)
                if P3 not in best or c2 < best[P3][0]:
                    best[P3] = (c2, c, e, tp)
    return best


def fit_target(g, model):
    t = g.t_mid_btjd.values; E = g.cycle.values.astype(float); err0 = g.err_s.values / 86400
    x = E - E.mean(); npar = 5 if model == 'circular' else 7
    jit = 0.0
    for _ in range(8):
        s = np.hypot(err0, jit)
        best = scan(t, x, s, E_GRID[model])
        P3b = min(best, key=lambda k: best[k][0]); c2 = best[P3b][0]
        red = c2 / (len(t) - npar)
        if red <= 1.02:
            break
        jit = np.sqrt(jit ** 2 + (red - 1) * np.median(s) ** 2)
    c2l, cl, rl = wls(design(t, x, 0, 0, 0), t, s); c2q, cq, rq = wls(design(t, x, 0, 0, 0, quad=True), t, s)
    c2, c, e, tp = best[P3b]
    K = np.hypot(c[2], c[3]); w = np.arctan2(c[3], c[2])
    A = K * np.sqrt(1 - e ** 2 * np.cos(w) ** 2)
    ok = np.array([P for P in best if best[P][0] < c2 + 4])
    n = len(t)
    return dict(n=n, sectors=g.sector.nunique(), span_yr=np.ptp(t) / 365.25, jitter_s=jit * 86400,
                chi2_lin=c2l, chi2_quad=c2q, chi2_ltte=c2, bic_lin=c2l + 2 * np.log(n), bic_quad=c2q + 3 * np.log(n),
                bic_ltte=c2 + npar * np.log(n), P3_d=P3b, P3_lo=ok.min(), P3_hi=ok.max(), A_s=A * 86400, K_s=K * 86400, e3=e,
                w3=np.degrees(w) % 360, tp=tp, c=c, rms_lin_s=np.sqrt(np.mean(rl ** 2)) * 86400, t=t, x=x, sec=g.sector.values,
                E=E, dE=E.mean())


def m3_min(fm, M12):
    return brentq(lambda m: m ** 3 / (M12 + m) ** 2 - fm, 1e-4, 1e4)


def clumps(t, gap=60.0):
    t = np.sort(t)
    return 1 + int(np.sum(np.diff(t) > gap))


for rid, g in f.groupby('rid'):
    g = g.sort_values('t_mid_btjd')
    oc = fit_target(g, 'circular'); oe = fit_target(g, 'eccentric')
    nc = clumps(g.t_mid_btjd.values)
    a_au = oc['K_s'] / C_AU_S; fm = a_au ** 3 / (oc['P3_d'] / 365.25) ** 2; M12 = M1[rid] * 1.6
    n = oc['n']
    print(f"{rid}: {n} events in {oc['sectors']} sectors ({nc} groups more than 60 d apart) over {oc['span_yr']:.1f} yr; "
          f"jitter {oc['jitter_s']:.0f} s (set so the circular LTTE has reduced chi2 1)")
    print(f"   chi2 linear {oc['chi2_lin']:.1f} ({n - 2} dof), quadratic {oc['chi2_quad']:.1f} ({n - 3}), circular LTTE {oc['chi2_ltte']:.1f} ({n - 5}); "
          f"BIC {oc['bic_lin']:.1f} / {oc['bic_quad']:.1f} / {oc['bic_ltte']:.1f}; linear rms {oc['rms_lin_s']:.0f} s")
    print(f"   circular LTTE: P3 = {oc['P3_d']:.0f} d ({oc['P3_d'] / 365.25:.1f} yr; dchi2 < 4: {oc['P3_lo']:.0f}-{oc['P3_hi']:.0f} d), "
          f"semi-amplitude {oc['A_s']:.0f} s; a12 sin i = {a_au:.2f} au, f(m3) = {fm:.3g} Msun, m3 >= {m3_min(fm, M12):.2f} Msun (M12 = {M12:.2f})")
    print(f"   eccentric LTTE (e up to 0.75, at the same jitter): chi2 {oe['chi2_ltte']:.1f} at P3 = {oe['P3_d']:.0f} d, e = {oe['e3']:.2f} (unconstrained)")
    tl = oc['t'] - (oc['c'][0] + oc['c'][1] * oc['x'])
    Al = design(oc['t'], oc['x'], oc['P3_d'], oc['e3'], oc['tp'])[:, 2:] @ oc['c'][2:]
    print('   sector O-C / circular model (s): ' + '  '.join(f"s{s_}:{np.mean(tl[oc['sec'] == s_]) * 86400:+.0f}/{np.mean(Al[oc['sec'] == s_]) * 86400:+.0f}" for s_ in np.unique(oc['sec'])))
    # forward predictions: circular LTTE versus quadratic, both against the same events
    t = oc['t']; x = oc['x']; s_ = np.hypot(g.err_s.values / 86400, oc['jitter_s'] / 86400)
    _, cq, _ = wls(design(t, x, 0, 0, 0, quad=True), t, s_)
    _, cc, _ = wls(design(t, x, oc['P3_d'], 0.0, oc['tp']), t, s_)
    P = cq[1]
    print(f"   quadratic: dP/dt = {2 * cq[2] / P * 365.25 * 86400:+.2f} s per year")
    line = '   predicted primary, circular LTTE minus quadratic (s):'
    for tq in (4300.0, 4500.0, 4700.0, 5000.0):
        xq = np.array([np.round((tq - cq[0]) / P)])
        tqq = np.array([cq[0] + P * xq[0]])
        d = (design(tqq, xq, oc['P3_d'], 0.0, oc['tp']) @ cc - design(tqq, xq, 0, 0, 0, quad=True) @ cq)[0]
        line += f'  BTJD {tq:.0f}: {d * 86400:+.0f}'
    print(line)
