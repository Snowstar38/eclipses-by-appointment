"""Run 7b (Duet): R1003 (TIC 436693263), the binary whose eclipses switched on between 2023 and 2026.

Reads Fable 5's per-sector depths and event times (fable-r1003/, measured on the house's cached
TESS light curves) and the November 23 host table, then
  1. compares the host-table row with what the light curves show;
  2. tests whether the Gaia DR3 206.6-d orbit can be the third body, using order-of-magnitude
     hierarchical-triple scalings (nodal precession, Kozai-Lidov, light-travel time and the
     dynamical eclipse-timing term) over a range of masses and mutual inclinations.
Standard library only.  Run from the repository root:
    python3 reviews/2026-11-24-duet-research-runs-1-4/run7-temperature-and-r1003/r1003_triple.py
The scalings are textbook leading-order forms (e.g. Borkovits et al. 2016, MNRAS 455, 4136;
Soderhjelm 1975; Kiseleva, Eggleton & Mikkola 1998).  Factors of order unity that depend on
e_out, omega and the mutual inclination are dropped, so read the outputs to a factor of ~2."""
import csv, math, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = sys.argv[1] if len(sys.argv) > 1 else os.path.normpath(os.path.join(HERE, '../../..'))
host = {x['review_id']: x for x in csv.DictReader(open(
    os.path.join(REPO, 'reviews/2026-11-23-pipeline-and-survey-review/host-stars.csv')))}['R1003']
dep = list(csv.DictReader(open(os.path.join(HERE, 'fable-r1003/r1003_depths.csv'))))
ev = [e for e in csv.DictReader(open(os.path.join(HERE, 'fable-r1003/r1003_events.csv'))) if e.get('epoch')]

print('1. Host-table row against the light curves')
print('   table: P = %s d, epoch BTJD %s, depth %s ppt, secondary %s ppt at phase %s, %s events in %s sectors' % (
    host['adopted_period_days'], host['adopted_epoch_btjd'], host['depth_ppt'], host['secondary_depth_ppt'],
    host['secondary_phase'], host['n_events_prim'], host['n_sectors']))
for d in sorted(dep, key=lambda d: int(d['sector'])):
    print('   s%-4s %-4s primary %7.1f +- %4.1f ppt   secondary %6.1f +- %4.1f ppt' % (
        d['sector'], d['src'], float(d['prim_ppt']), float(d['prim_sig']), float(d['sec_ppt']), float(d['sec_sig'])))
T0 = float(host['adopted_epoch_btjd']); P_tab = float(host['adopted_period_days'])
e0 = [e for e in ev if int(e['epoch']) == 0][0]
print('   the table epoch %.3f falls in s%s; Fable measures %.1f ppt in that very window' % (T0, e0['sector'], float(e0['depth_ppt'])))
deep = sorted([e for e in ev if float(e['depth_ppt']) > 50], key=lambda e: float(e['t_btjd']))
# 2026-only linear ephemeris from the deep events
n = len(deep); E = [int(e['epoch']) for e in deep]; t = [float(e['t_btjd']) for e in deep]
w = [1 / float(e['sigma_d']) ** 2 for e in deep]
S, Sx, Sy, Sxx, Sxy = sum(w), sum(a * b for a, b in zip(w, E)), sum(a * b for a, b in zip(w, t)), \
    sum(a * b * b for a, b in zip(w, E)), sum(a * b * c for a, b, c in zip(w, E, t))
P26 = (S * Sxy - Sx * Sy) / (S * Sxx - Sx * Sx); T26 = (Sy - P26 * Sx) / S
print('   2026 deep events: %d, cycles %d-%d; weighted linear P = %.7f d (Fable: 2.8787113 +- 0.0000066)' % (n, min(E), max(E), P26))
gap = min(E)
print('   linking 2026 back to the table epoch needs %d unseen cycles; the two periods differ by %.1e d,' % (gap, P26 - P_tab))
print('   i.e. %.1f h at the table epoch, so the tabled period is a cycle count across an eclipse-free gap' % ((P26 - P_tab) * gap * 24))
dmean = sum(float(e['depth_ppt']) for e in deep) / n
print('   mean depth of the deep events %.0f ppt (QLP and SPOC mixed) against the table\'s %s ppt' % (dmean, host['depth_ppt']))
print('   Gaia neighbour in the attribution field: %s' % host['attribution'].split('UNRESOLVED')[-1].strip())
print('   If 2.94 is the neighbour\'s G-band offset, it gives %.1f%% of the target\'s flux and can make at most' % (100 * 10 ** (-0.4 * 2.94)))
print('   ~%.0f ppt in a crowding-corrected light curve, short of the 92-144 ppt now measured' % (1000 * 10 ** (-0.4 * 2.94) / (1 + 10 ** (-0.4 * 2.94)) / 0.9))

print('\n2. Can the Gaia 206.6-d orbit be the third body?')
P_in = P26; e_in_min = abs(math.pi / 2 * (float(host['secondary_phase']) - 0.5))
G = 2.959122e-4; AU_S = 499.005; DAY = 86400.0
print('   inner: P = %.4f d, e >= |e cos w| = %.2f' % (P_in, e_in_min))
print('   %-9s %-9s %-7s %10s %10s %9s %9s %9s' % ('P_out(d)', 'm12,m3', 'aout AU', 'Kozai(yr)', 'node(yr)', 'LTT(s)', 'dyn(s)', 'peri a/R'))
for P_out in (206.587, 103.3, 82.6):
    for m12, m3 in ((2.0, 0.5), (2.0, 1.0), (2.6, 1.3)):
        mt = m12 + m3
        a_out = (G * mt * P_out ** 2 / (4 * math.pi ** 2)) ** (1 / 3)
        tauK = (2 / (3 * math.pi)) * (mt / m3) * P_out ** 2 / P_in / 365.25          # Kozai-Lidov timescale
        tnode = (4 / 3) * (mt / m3) * P_out ** 2 / P_in / 365.25                        # nodal period, i_mut ~ 0
        ltt = a_out * m3 / mt * AU_S                                                    # x sin i_out
        dyn = (1 / (2 * math.pi)) * (m3 / mt) * P_in ** 2 / P_out * DAY                 # physical delay
        a_in = (G * m12 * P_in ** 2 / (4 * math.pi ** 2)) ** (1 / 3) * 215.032
        print('   %-9.1f %-9s %-7.2f %10.1f %10.0f %9.0f %9.0f %9.1f' % (
            P_out, '%.1f,%.1f' % (m12, m3), a_out, tauK, tnode, ltt, dyn, a_in * (1 - e_in_min) / 1.0))
print('   (peri a/R: periastron distance over a 1-Rsun primary, for the inner pair)')
print('   Turn-on: from no eclipse (b > 1 + k) to a 144-ppt eclipse needs the inner inclination to move by')
print('   roughly (R1+R2)/a ~ 0.25 rad / 3 ~ 2-5 degrees, done in <= 2.7 yr (s65 May 2023 -> s99 Feb 2026).')
for P_out in (206.587, 82.6):
    tnode = (4 / 3) * 3 * P_out ** 2 / P_in / 365.25
    for imut in (10, 20, 40):
        rate = 360 / tnode * math.sin(math.radians(imut)) * math.cos(math.radians(imut))   # deg/yr, ~ max di/dt
        print('   P_out %.1f d, i_mut %2d deg: nodal period ~%4.0f yr, max di/dt ~%.2f deg/yr, %.1f deg in 2.7 yr' % (
            P_out, imut, tnode / math.cos(math.radians(imut)), rate, 2.7 * rate))
