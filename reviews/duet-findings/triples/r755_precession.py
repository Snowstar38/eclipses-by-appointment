"""R755: is nodal precession fast enough to switch its eclipses on between TESS sectors 62 and 89?
Inputs, all in the repository: Gaia DR3 5523899796082005376's two solutions (24.68-d SB1 and 300.8-d astrometric
Orbital) in reviews/2026-11-05-catalogue-recovery/catalogues/gaia_nss-pending.csv; the TIC record (masses/tic-records.csv);
the sector coverage and the s89 eclipse in the period-free review's lead-numeric.json and REPORT.md.
Orders of magnitude: the nodal period uses the quadrupole formula, the eclipse band uses R1 + R2 over the inner
separation. NumPy and pandas. Run from the repository root."""
import csv, json, math
import numpy as np
csv.field_size_limit(10**8)
SID = '5523899796082005376'
rows = [r for r in csv.DictReader(open('reviews/2026-11-05-catalogue-recovery/catalogues/gaia_nss-pending.csv')) if r['source_id'] == SID]
sb1 = next(r for r in rows if r['nss_solution_type'] == 'SB1'); orb = next(r for r in rows if r['nss_solution_type'] == 'Orbital')
tic = next(r for r in csv.DictReader(open('reviews/duet-findings/masses/tic-records.csv')) if r['ID'] == '271053559')
f = lambda r, k: float(r[k])

def incl(A, B, F, G):
    u = (A*A + B*B + F*F + G*G) / 2; v = A*G - B*F
    a0 = math.sqrt(u + math.sqrt((u + v) * (u - v)))
    return math.degrees(math.acos(v / a0**2)), a0

TI = [f(orb, k + '_thiele_innes') for k in 'abfg']; TIe = [f(orb, k + '_thiele_innes_error') for k in 'abfg']
i_out, a0 = incl(*TI)
rng = np.random.default_rng(1)
mc = np.array([incl(*(rng.normal(TI, TIe))) for _ in range(20000)])
i_lo, i_hi = np.percentile(mc[:, 0], [2.5, 97.5])
print(f'outer orbit: P = {f(orb,"period"):.1f} d, e = {f(orb,"eccentricity"):.3f}, i = {i_out:.1f} deg (95%: {i_lo:.1f}-{i_hi:.1f}, independent TI errors), a0 = {a0:.3f} mas')

# inner pair: m1 from TIC, m2 from the SB1 mass function at i = 90
P_in, K, e_in = f(sb1, 'period'), f(sb1, 'semi_amplitude_primary'), f(sb1, 'eccentricity')
fm = 1.0361e-7 * (1 - e_in**2)**1.5 * K**3 * P_in
m1, R1 = float(tic['mass']), float(tic['rad'])
m2 = 0.1
for _ in range(100): m2 = (fm * (m1 + m2)**2)**(1/3)
m12 = m1 + m2
a_in = (m12 * (P_in / 365.25)**2)**(1/3) * 215.03
R2 = m2**0.9
theta = math.degrees(math.asin((R1 + R2) / a_in))
print(f'inner pair: P = {P_in:.3f} d, f(M) = {fm:.4f}, m1 = {m1:.2f} (TIC), m2 >= {m2:.2f} Msun, a = {a_in:.1f} Rsun, eclipse band |90 - i| < {theta:.1f} deg')

# tertiary mass from the photocentre orbit, tertiary dark (a luminous tertiary would need more mass)
plx, P_out, e_out = f(orb, 'parallax'), f(orb, 'period'), f(orb, 'eccentricity')
a_phot = a0 / plx
for m3 in np.arange(0.05, 3, 0.001):
    a_out = ((m12 + m3) * (P_out / 365.25)**2)**(1/3)
    if a_out * m3 / (m12 + m3) >= a_phot: break
print(f'tertiary (dark): m3 >= {m3:.2f} Msun, a_out = {a_out:.2f} AU, photocentre {a_phot:.3f} AU')

j_min = max(0.0, abs(90 - i_out) - theta)
print(f'mutual inclination >= {j_min:.1f} deg (sky-plane difference {abs(90-i_out):.1f} less the eclipse band); >= {max(0,90-i_hi-theta):.1f} deg at the 95% edge of i_out')
# switch-on: no deep eclipse at covered s62 conjunctions, a 313 ppt eclipse at BTJD 3735.6 (s89)
cov = {c['sector']: (c['start_btjd'], c['end_btjd']) for c in json.load(open('reviews/2026-11-05-period-free/binary-priority100-2026-11-05/batch09/271053559/lead-numeric.json'))['coverage']}
dt_yr = (3735.576 - cov[62][1]) / 365.25
dI_need = math.degrees(R2 / a_in)        # at least the companion's own angular size to go from no eclipse to a deep one
print(f'switch-on between s62 (ends BTJD {cov[62][1]:.0f}) and s89: {dt_yr:.2f} yr; the inner orbit had to tilt by >= {dI_need:.1f} deg, so >= {dI_need/dt_yr:.1f} deg/yr')
print(' i_out  j(deg)  m3   P_node(yr)  di/dt at the eclipse crossing (deg/yr)  eclipse epoch (yr)')
for io, js in ((i_out, (25, 30, 40, 60)), (i_hi, (8, 12, 20, 40))):
  A = math.radians(io)
  for m3x in (m3, 1.0):
    for j in js:
      J = math.radians(j)
      T = 4/3 * (m12 + m3x) / m3x * P_out**2 / P_in * (1 - e_out**2)**1.5 / abs(math.cos(J)) / 365.25
      c = -math.cos(A) * math.cos(J) / (math.sin(A) * math.sin(J))
      if abs(c) > 1: continue
      rate = math.sin(A) * math.sin(J) * math.sqrt(1 - c * c) * 360 / T
      print(f' {io:5.1f}  {j:3d}  {m3x:.2f}   {T:6.0f}       {rate:5.2f}                                 {2*theta/rate:5.1f}')
