"""R750 (TIC 33065877): where Gaia's SB2 orbit puts the secondary eclipse, against where it is.

The period-free review measured nine eclipses of two kinds (lead-numeric.json, fitted mid-times and depths).
This folds them on Gaia's elements (main-search Gaia rows), measures each one's offset from Gaia's two
conjunctions, and compares the measured A-to-B phase with Gaia's, varying e and omega within their errors,
then with the errors scaled by the solution's fit quality as the Gaia-errors entries calibrate for SB2s
(sqrt(chi2/nu) from F2; nu = 20, 40 and 80 bracket the unknown RV count).

Run from the repository root: python3 reviews/duet-findings/gaia-errors/r750_secondary.py
Needs numpy and pandas. Writes r750-secondary-output.txt here.
"""
import json, os, sys
sys.dont_write_bytecode = True
import numpy as np, pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
EV = 'reviews/2026-11-05-period-free/binary-priority100-2026-11-05/batch08/33065877/lead-numeric.json'
ROWS = 'reviews/2026-11-26-fable51-main-search-gaia/main-search-gaia-rows.csv'
HW = 'reviews/duet-findings/gaia-errors/fable51-window-halfwidths.csv'


def mean_anom(nu, e):
    E = 2*np.arctan2(np.sqrt(1 - e)*np.sin(nu/2), np.sqrt(1 + e)*np.cos(nu/2))
    return (E - e*np.sin(E)) % (2*np.pi)


def main():
    out = open(os.path.join(HERE, 'r750-secondary-output.txt'), 'w')
    P_ = lambda *a: print(*a, file=out)
    g = pd.read_csv(ROWS, dtype={'tic': str, 'source_id': str}).drop_duplicates('tic').set_index('tic').loc['33065877']
    hw = pd.read_csv(HW, dtype={'source_id': str}); hw = hw[hw.source_id == g.source_id].set_index('conjunction').halfwidth_independent_d
    P, e, w = g.period, g.eccentricity, np.radians(g.arg_periastron)
    tp = g.t_periastron + 389                      # Gaia's T_p is days from J2016.0 = BTJD 389
    cA = tp + mean_anom(np.pi/2 - w, e)/(2*np.pi)*P
    cB = tp + mean_anom(1.5*np.pi - w, e)/(2*np.pi)*P
    P_(f'Gaia DR3 {g.source_id} ({g.nss_solution_type}): P {P:.4f} d, e {e:.4f} +- {g.eccentricity_error:.4f}, '
       f'omega {g.arg_periastron:.2f} +- {g.arg_periastron_error:.2f} deg, goodness of fit {g.goodness_of_fit:.2f}')
    P_(f'window half-widths (independent errors, mid-mission): A {hw["A"]:.2f} d, B {hw["B"]:.2f} d')
    P_('\nmeasured eclipses (period-free review) against Gaia\'s conjunctions:')
    P_(f'  {"sector":>6s} {"BTJD":>10s} {"depth ppt":>9s} {"from A (d)":>10s} {"from B (d)":>10s} {"in window":>9s}')
    ev = json.load(open(EV))['events']; sA = []; sB = []
    for x in sorted(ev, key=lambda x: x['fit_mid_btjd']):
        t = x['fit_mid_btjd']
        dA = ((t - cA)/P + 0.5) % 1*P - P/2; dB = ((t - cB)/P + 0.5) % 1*P - P/2
        k = 'A' if abs(dA) < abs(dB) else 'B'
        (sA if k == 'A' else sB).append(t)
        inw = abs(dA) <= hw['A'] if k == 'A' else abs(dB) <= hw['B']
        P_(f'  {x["sector"]:6d} {t:10.3f} {x["fit_depth_ppt"]:9.0f} {dA:10.2f} {dB:10.2f} {k + (" yes" if inw else " no"):>9s}')
    phA = np.array(sA) % P; phB = np.array(sB) % P
    sep = ((np.median(phB) - np.median(phA)) % P)/P
    rng = np.random.default_rng(1); n = 200000
    ee = e + g.eccentricity_error*rng.standard_normal(n); ww = np.radians(g.arg_periastron + g.arg_periastron_error*rng.standard_normal(n))
    gs = ((mean_anom(1.5*np.pi - ww, ee) - mean_anom(np.pi/2 - ww, ee)) % (2*np.pi))/(2*np.pi)
    ns = abs(gs.mean() - sep)/gs.std()
    P_(f'\nA-to-B phase: measured {sep:.4f} ({sep*P:.2f} d); Gaia {gs.mean():.4f} +- {gs.std():.4f} ({gs.mean()*P:.2f} d); {ns:.1f} sigma')
    F2 = g.goodness_of_fit
    for nu in (20, 40, 80):
        s = max(np.clip(F2/np.sqrt(9*nu/2) + 1 - 2/(9*nu), 0.1, None)**1.5, 1)
        P_(f'  errors scaled by sqrt(chi2/nu) = {s:.2f} (nu = {nu}): {ns/s:.1f} sigma')
    out.close()
    fn = os.path.join(HERE, 'r750-secondary-output.txt'); print(open(fn).read())


if __name__ == '__main__':
    main()
