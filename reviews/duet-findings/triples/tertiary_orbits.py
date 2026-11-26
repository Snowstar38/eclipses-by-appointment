"""Accepted eclipsing systems whose Gaia DR3 orbit is much longer than the eclipse
period, read as a possible tertiary.  For each: period ratio, a Mardling & Aarseth (2001)
stability check, and the expected eclipse-timing amplitudes (light-travel time and the
'physical' dynamical delay), which set how wide an eclipse prediction for that star must be.
Standard library only.  Run from the repository root:
    python3 reviews/duet-findings/triples/tertiary_orbits.py
Masses are not known: m_inner = 2.0 and m3 = 0.5-1.0 Msun are assumed, so amplitudes are good
to a factor of ~2.  Timing scalings as in r1003_triple.py.  The Gaia orbits are read from the
repository's own copies of the NSS table (any reviews/**/*nss*.csv)."""
import csv, glob, math, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = sys.argv[1] if len(sys.argv) > 1 else os.path.normpath(os.path.join(HERE, '../../..'))
os.chdir(REPO)
G = 2.959122e-4; AU_S = 499.005; DAY = 86400.0

nss = {}
for f in sorted(glob.glob('reviews/**/*nss*.csv', recursive=True)):
    for r in csv.DictReader(open(f, newline='')):
        if r.get('source_id') and r.get('period'):
            nss.setdefault(r['source_id'], {})[(r.get('nss_solution_type') or '?', round(float(r['period']), 3))] = r

targets = []
for x in csv.DictReader(open('reviews/2026-11-23-pipeline-and-survey-review/host-stars.csv')):
    m = re.search(r'Gaia DR3 NSS (\w+) orbit P=([0-9.]+) d does not match P', x['reason'])
    if m and float(m.group(2)) > 3 * float(x['adopted_period_days']):
        targets.append((x['review_id'], x['tic'], x['gaia_dr3'], float(x['adopted_period_days']), m.group(1), float(m.group(2))))
# R755 (TIC 271053559): eclipses at Gaia's own 24.68-d SB1 period, plus a 300.8-d astrometric orbit
targets.append(('R755', '271053559', '5523899796082005376', 24.6548, 'Orbital', 300.8052))

def a0_mas(r):
    """Photocentre semi-major axis from the Thiele-Innes constants (mas)."""
    A, B, F, Gt = (float(r[k]) for k in ('a_thiele_innes', 'b_thiele_innes', 'f_thiele_innes', 'g_thiele_innes'))
    u = (A * A + B * B + F * F + Gt * Gt) / 2; v = A * Gt - B * F
    return math.sqrt(u + math.sqrt(max(u * u - v * v, 0)))

def ma_critical(e_out, q_out, i_mut_deg=0.0):
    """Mardling & Aarseth (2001): minimum a_out/a_in for long-term stability."""
    return 2.8 * (1 + q_out) ** 0.4 * (1 + e_out) ** 0.4 * (1 - e_out) ** -1.2 * (1 - 0.3 * i_mut_deg / 180)

print('%-6s %-10s %9s %9s %-15s %6s %5s %6s %8s %9s %9s %10s' % (
    'row', 'TIC', 'P_ecl', 'P_gaia', 'Gaia type', 'ratio', 'e_out', 'stable', 'a0 (AU)', 'LTT (s)', 'dyn (s)', 'node (yr)'))
for rid, tic, gid, Pin, typ, Pout in targets:
    sol = nss.get(gid, {}).get((typ, round(Pout, 3)))
    e_out = float(sol['eccentricity']) if sol and sol.get('eccentricity') else None
    a0 = None
    if sol and sol.get('a_thiele_innes') and sol.get('parallax'):
        a0 = a0_mas(sol) / float(sol['parallax'])
    m_in, m3 = 2.0, 0.75; mt = m_in + m3
    a_in = (G * m_in * Pin ** 2 / (4 * math.pi ** 2)) ** (1 / 3); a_out = (G * mt * Pout ** 2 / (4 * math.pi ** 2)) ** (1 / 3)
    crit = ma_critical(e_out if e_out is not None else 0.0, m3 / m_in)
    stable = 'yes' if a_out / a_in > crit else 'NO'
    ef = (1 - (e_out or 0) ** 2) ** -1.5
    ltt = (G * (m_in + 1.0) * Pout ** 2 / (4 * math.pi ** 2)) ** (1 / 3) * 1.0 / (m_in + 1.0) * AU_S   # m3 = 1
    ltt_lo = (G * (m_in + 0.5) * Pout ** 2 / (4 * math.pi ** 2)) ** (1 / 3) * 0.5 / (m_in + 0.5) * AU_S
    dyn = [(1 / (2 * math.pi)) * (m / (m_in + m)) * Pin ** 2 / Pout * ef * DAY for m in (0.5, 1.0)]
    node = (4 / 3) * (mt / m3) * Pout ** 2 / Pin * (1 - (e_out or 0) ** 2) ** 1.5 / 365.25
    print('%-6s %-10s %9.4f %9.2f %-15s %6.1f %5s %6s %8s %4.0f-%-4.0f %4.0f-%-4.0f %10.0f' % (
        rid, tic, Pin, Pout, typ, Pout / Pin, '%.2f' % e_out if e_out is not None else '-', stable,
        '%.3f' % a0 if a0 else '-', ltt_lo, ltt, dyn[0], dyn[1], node))
print('\nLTT: half-amplitude of the light-travel-time delay x sin(i_out), for m3 = 0.5-1 Msun.')
print('dyn: leading-order physical (dynamical) delay; it grows as P_ecl^2 / P_gaia and dominates for wide inner pairs.')
print('a0: Gaia photocentre semi-major axis in AU (Orbital solutions only); the photocentre orbit is a lower')
print('    bound on the inner pair\'s barycentric orbit when the tertiary is fainter, so a0 x 499 s bounds LTT from below.')
