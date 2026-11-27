"""AstroSpectroSB1 orbits: appoint.py sets omega = 0, and Gaia gives omega through the Thiele-Innes C and H.

Gaia DR3 publishes no arg_periastron for AstroSpectroSB1 solutions; omega is in the Thiele-Innes constants
(C = a sin(omega) sin(i), H = a cos(omega) sin(i), so omega = atan2(C, H)). appoint.py flags these rows
circular_assumed_omega0 and builds the windows with omega = 0 and Gaia's eccentricity.

1. The fresh-band windows of the flagged targets against conjunctions computed with omega = 0, and their spread
   against a Monte Carlo of T_p, P and e with omega held at 0 (the model used for the half-widths below).
2. R756 (TIC 200743349): the main-search window centre (Earthshine's find time less its phase offset) and its
   fitted eclipse times (period-free review) against the omega = 0 and the C, H conjunctions.
3. The main-search AstroSpectroSB1 targets whose Thiele-Innes row is in this repository: the distance from each
   omega = 0 window to the nearest true conjunction, against the window half-width min(max(3 sigma, 0.25 d), 7 d).

Run from the repository root: python3 reviews/duet-findings/gaia-errors/astrospectro_omega.py
Needs numpy and pandas. Writes astrospectro-omega-output.txt here.
"""
import glob, json, os, subprocess, sys
sys.dont_write_bytecode = True
import numpy as np, pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
ROWS = 'reviews/2026-11-26-fable51-main-search-gaia/main-search-gaia-rows.csv'
AUD = 'reviews/duet-findings/yield/periodfree-cut-audit.csv'
NUL = 'reviews/duet-findings/yield/null-vetoes-earthshine.csv'
NU = {'A': np.pi/2, 'B': 1.5*np.pi}


def mean_anom(nu, e):
    E = 2*np.arctan2(np.sqrt(1 - e)*np.sin(nu/2), np.sqrt(1 + e)*np.cos(nu/2))
    return (E - e*np.sin(E)) % (2*np.pi)


def wrap(d, P):
    return (d/P + 0.5) % 1*P - P/2


def conj(P, e, w, tp):
    return {k: tp + mean_anom(nu - w, e)/(2*np.pi)*P for k, nu in NU.items()}


def sig_w0(P, Pe, e, ee, tp, tpe, t, kind, rng, n=20000):
    """Spread of the omega = 0 conjunction at time t from independent draws of T_p, P and e."""
    c0 = conj(P, e, 0.0, tp)[kind]; cyc = np.round((t - c0)/P)
    Pd, ed, td = rng.normal(P, Pe, n), np.clip(rng.normal(e, ee, n), 0, 0.99), rng.normal(tp, tpe, n)
    return np.std(td + mean_anom(NU[kind], ed)/(2*np.pi)*Pd + cyc*Pd)


def thiele_innes_rows():
    files = [f for f in subprocess.run(['git', 'ls-files'], capture_output=True, text=True).stdout.split('\n')
             if f.endswith('.csv') and 'nss' in f.lower()]
    out = []
    for f in files:
        try: d = pd.read_csv(f, dtype={'source_id': str}, low_memory=False)
        except Exception: continue
        if {'source_id', 'c_thiele_innes', 'h_thiele_innes', 'nss_solution_type'} <= set(d.columns):
            out.append(d[d.nss_solution_type == 'AstroSpectroSB1'])
    return pd.concat(out).drop_duplicates('source_id').set_index('source_id')


def main():
    rng = np.random.default_rng(20261127)
    out = open(os.path.join(HERE, 'astrospectro-omega-output.txt'), 'w')
    P_ = lambda *a: print(*a, file=out)

    P_('1. Fresh-band targets flagged circular_assumed_omega0: windows against omega = 0 conjunctions')
    seen = set(); res, ratio = [], []
    for pop in sorted(glob.glob('reviews/**/fresh-band*/population.json', recursive=True)):
        if 'stage1' in pop: continue
        T = json.load(open(pop))['targets']; rd = os.path.join(os.path.dirname(pop), 'appointment-results')
        for tic, v in T.items():
            f = os.path.join(rd, f'{tic}.json')
            if tic in seen or not os.path.exists(f): continue
            seen.add(tic); d = json.load(open(f))
            if not d.get('circular_assumed_omega0'): continue
            g = v['gaia']; P, Pe, e, ee, tp, tpe = (float(g[k]) for k in ('period', 'period_error', 'eccentricity', 'eccentricity_error', 't_periastron', 't_periastron_error'))
            tp += 389
            for x in d.get('windows') or []:
                c = conj(P, e, 0.0, tp)[x['kind']]
                res.append(abs(wrap(x['tc'] - c, P)))
                ratio.append(x['sig']/sig_w0(P, Pe, e, ee, tp, tpe, x['tc'], x['kind'], rng, 4000))
            P_(f'   TIC {tic:>10} {g["nss_solution_type"]}: P {P:6.2f} d, e {e:.3f}, {len(d.get("windows") or [])} windows')
    P_(f'   {len(res)} windows: |centre - omega=0 conjunction| median {np.median(res):.3f} d, max {np.max(res):.3f} d; '
       f'window sigma / Monte Carlo sigma median {np.median(ratio):.2f} ({np.percentile(ratio, 10):.2f}-{np.percentile(ratio, 90):.2f})')

    TI = thiele_innes_rows()
    G = pd.read_csv(ROWS, dtype={'tic': str, 'source_id': str}).drop_duplicates('tic')
    asb = G[G.nss_solution_type == 'AstroSpectroSB1']
    P_(f'\nMain search: {len(asb)} AstroSpectroSB1 targets (' + ', '.join(f'{b} {n}' for b, n in asb.band.value_counts().sort_index().items())
       + f'); eccentricity median {asb.eccentricity.median():.2f}, quartiles {asb.eccentricity.quantile(.25):.2f}-{asb.eccentricity.quantile(.75):.2f}; '
       f'Thiele-Innes rows in this repository for {int(asb.source_id.isin(TI.index).sum())}')

    A = pd.read_csv(AUD, dtype={'tic': str}); E = pd.read_csv(NUL, dtype={'tic': str}).merge(A[['review_id', 'dphase']])
    r = E[E.review_id == 'R756'].iloc[0]; g = G[G.tic == r.tic].iloc[0]; ti = TI.loc[g.source_id]
    P, e, tp = g.period, g.eccentricity, g.t_periastron + 389
    w = np.arctan2(ti.c_thiele_innes, ti.h_thiele_innes)
    c0, c1 = conj(P, e, 0.0, tp), conj(P, e, w, tp)
    tc = r.find_t - r.dphase*P
    P_(f'\n2. R756 (TIC {r.tic}): P {P:.4f} d, e {e:.3f}, omega from C, H {np.degrees(w) % 360:.1f} deg')
    P_(f'   main-search window centre - omega=0 conjunction A: {wrap(tc - c0["A"], P):.2f} d; '
       f'half-width on the omega = 0 model {min(max(3*sig_w0(P, g.period_error, e, g.eccentricity_error, tp, g.t_periastron_error, tc, "A", rng), 0.25), 7):.2f} d')
    f = glob.glob(f'reviews/2026-11-05-period-free/**/{r.tic}/lead-numeric.json', recursive=True)[0]
    P_('   fitted eclipses: sector, BTJD, depth; offset from the omega=0 conjunctions; offset from the C, H conjunctions (d)')
    for x in json.load(open(f))['events']:
        if not x.get('fit_mid_btjd'): continue
        t = x['fit_mid_btjd']
        a = {k: wrap(t - v, P) for k, v in c0.items()}; b = {k: wrap(t - v, P) for k, v in c1.items()}
        P_(f'   s{x["sector"]:<3} {t:10.3f} {x["fit_depth_ppt"]:6.1f} ppt | A {a["A"]:6.2f} B {a["B"]:6.2f} | A {b["A"]:6.2f} B {b["B"]:6.2f}')

    P_('\n3. Other main-search AstroSpectroSB1 targets with Thiele-Innes rows here: omega = 0 windows against the true conjunctions (BTJD 2500)')
    miss = 0; m = asb[asb.source_id.isin(TI.index) & (asb.tic != r.tic)]
    for g in m.itertuples():
        ti = TI.loc[g.source_id]; P, e, tp = g.period, g.eccentricity, g.t_periastron + 389
        w = np.arctan2(ti.c_thiele_innes, ti.h_thiele_innes)
        c0, c1 = conj(P, e, 0.0, tp), conj(P, e, w, tp)
        line, both = [], True
        for k in 'AB':
            hw = min(max(3*sig_w0(P, g.period_error, e, g.eccentricity_error, tp, g.t_periastron_error, 2500., k, rng), 0.25), 7)
            dmin = min(abs(wrap(c0[k] - x, P)) for x in c1.values())
            both &= dmin > hw
            line.append(f'{k} {dmin:5.2f} d (hw {hw:4.2f})')
        miss += both
        P_(f'   TIC {g.tic:>10}: P {P:6.2f}, e {e:.2f}, omega {np.degrees(w) % 360:5.1f} deg; window to nearest true conjunction: ' + ', '.join(line)
           + ('; both miss' if both else ''))
    P_(f'   both windows miss both true conjunctions for {miss} of {len(m)}')
    fr = []
    for g in asb.itertuples():
        P, e, tp = g.period, g.eccentricity, g.t_periastron + 389
        hw = {k: min(max(3*sig_w0(P, g.period_error, e, g.eccentricity_error, tp, g.t_periastron_error, 2500., k, rng, 4000), 0.25), 7) for k in 'AB'}
        c0 = conj(P, e, 0.0, tp); ws = np.radians(np.arange(0, 360, 2.0)); hit = 0
        for w in ws:
            c1 = conj(P, e, w, tp)
            hit += any(abs(wrap(c0[k] - x, P)) <= hw[k] for k in 'AB' for x in c1.values())
        fr.append(1 - hit/len(ws))
    P_(f'   all {len(asb)} main-search AstroSpectroSB1 targets, omega uniform: both windows miss both conjunctions for {np.mean(fr):.2f} of orientations '
       f'(median target {np.median(fr):.2f})')
    out.close()


if __name__ == '__main__':
    main()
