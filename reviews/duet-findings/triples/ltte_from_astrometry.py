"""Light-travel-time amplitude of an eclipsing pair from the Gaia DR3 astrometric orbit of the same star.
The photocentre orbit gives a lower bound on the pair's barycentric orbit (a luminous tertiary only enlarges it):
semi-amplitude = (a0 / parallax) sin i sqrt(1 - e^2 cos^2 w) / c (Irwin 1952). A95 checks it against the paper's
measured 3.4 +- 0.3 min; A119 is the prediction. Inputs: Fable 5.1's NSS export. Run from the repository root."""
import csv, math
import numpy as np
rows = {(r['review_id'], r['nss_solution_type']): r for r in csv.DictReader(open('reviews/duet-findings/gaia-errors/fable51-nss-appointments.csv'))}
C_AU_S = 499.004784
rng = np.random.default_rng(3)

def elements(A, B, F, G):
    u = (A*A + B*B + F*F + G*G) / 2; v = A*G - B*F; a0 = math.sqrt(u + math.sqrt((u + v) * (u - v)))
    i = math.acos(v / a0**2)
    wpO = math.atan2(B - F, A + G); wmO = math.atan2(-B - F, A - G)
    return a0, i, (wpO + wmO) / 2

def amp(r, A, B, F, G, plx, e):
    a0, i, w = elements(A, B, F, G)
    return a0 / plx * math.sin(i) * math.sqrt(1 - (e * math.cos(w))**2) * C_AU_S / 60

for lab in ('A95', 'A119'):
    r = rows[(lab, 'Orbital')]
    TI = [float(r[k + '_thiele_innes']) for k in 'abfg']; TE = [float(r[k + '_thiele_innes_error']) for k in 'abfg']
    plx, pe = float(r['parallax']), float(r['parallax_error']); e, ee = float(r['eccentricity']), float(r['eccentricity_error'])
    a0, i, w = elements(*TI)
    best = amp(r, *TI, plx, e)
    mc = [amp(r, *rng.normal(TI, TE), rng.normal(plx, pe), min(0.95, abs(rng.normal(e, ee)))) for _ in range(20000)]
    lo, hi = np.percentile(mc, [16, 84])
    print(f'{lab}: P_out = {float(r["period"]):.1f} d, e = {e:.3f}, i = {math.degrees(i):.1f} deg, a0 = {a0:.3f} mas, parallax {plx:.3f} mas'
          f' -> photocentre {a0/plx:.3f} AU; LTTE semi-amplitude >= {best:.2f} min (68%: {lo:.2f}-{hi:.2f})')
print('A95 measured in the paper: 3.4 +- 0.3 min on the 541-d period')
