"""Table 4's contradicted Gaia orbits once Gaia's quoted errors are scaled to the measured ones.

Table 4 counts an orbit as contradicted when its period or e cos w differs from the eclipse
value by 3 sigma of Gaia's quoted error under every treatment of the covariance.  Here:
  e cos w: Gaia's eccentricity errors are k = 1.37 +- 0.12 times too small (eccentricity_errors.py,
           31 circular binaries at P < 3 d).  Each failure's smallest quoted discrepancy is divided
           by k, and the number of chance 3-sigma failures expected among the 184 compared
           orbits is 184 * 2 * Phi(-3/k).
  period:  the A sample's period pulls have a robust width of 1.16 (a-epoch-test.csv), so
           chance 3-sigma failures number 184 * 2 * Phi(-3/1.16); the excess is real.
The discrepancies are read from Table 4 in paper.html (the smallest value of each e cos w entry).
Usage: python3 reviews/duet-findings/gaia-errors/table4_scaled.py
"""
import re, html, math
import numpy as np, pandas as pd

Phi = lambda x: 0.5 * math.erfc(-x / math.sqrt(2))
raw = open('paper.html', encoding='utf-8').read()
i = raw.find('orbit solutions contradicted by the eclipses:')
t4 = re.sub(r'\s+', ' ', html.unescape(re.sub('<[^>]+>', ' ', raw[i:raw.find('Catalogue corrections: the eleven', i)])))

# label: (smallest quoted e cos w discrepancy, the text it comes from in Table 4)
ECOSW = {'A21': (3.7, '3.7σ (RUWE 35)'), 'A28': (5.7, '5.7–6.1σ'), 'A30': (5.3, '5.3–5.6σ'),
         'A63': (3.8, '3.8σ (4.1–4.3σ'), 'A65': (4.0, '4.0–5.0σ'), 'A145': (4.5, '4.5σ away'),
         'A159': (3.3, '3.3σ without'), 'A202': (3.5, '3.5σ in e')}
for k_, (_, txt) in ECOSW.items():
    assert txt.replace(' ', '') in t4.replace(' ', ''), (k_, txt)

g = pd.read_csv('reviews/duet-findings/gaia-geometry/gaia-vs-eclipse.csv')
for c in ['eclipse_period_days', 'gaia_ecc', 'gaia_ecc_err']:
    g[c] = pd.to_numeric(g[c].astype(str).str.split('|').str[0], errors='coerce')
s = g[(g['class'] == 'harmonic 1') & g.nss_type.isin(['SB1', 'SB2']) & g.gaia_ecc_err.notna() & (g.eclipse_period_days < 3)]
k = math.sqrt(np.mean((s.gaia_ecc / s.gaia_ecc_err) ** 2) / 2); ke = k / math.sqrt(4 * len(s))

N = 184
print(f'e cos w: error scale k = {k:.2f} +- {ke:.2f} ({len(s)} binaries at P < 3 d)')
for kk in (1.0, k - ke, k, k + ke):
    print(f'  chance 3-sigma failures among {N} at k = {kk:.2f}: {N*2*Phi(-3/kk):.1f}')
print('  Table 4 e cos w failures, quoted and scaled (p = chance of one this large among 184):')
for lab, (z, _) in ECOSW.items():
    zs = z / k; p = 1 - (1 - 2 * Phi(-zs)) ** N
    print(f'    {lab:5s} {z:4.1f} sigma -> {zs:4.2f}   p = {p:.3f}', '  survives' if zs >= 3 else '')

a = pd.read_csv('reviews/duet-findings/gaia-errors/a-epoch-test.csv')
z = a.z_period.dropna(); w = 1.4826 * np.median(np.abs(z - np.median(z)))
print(f'period: A-sample robust width {w:.2f} over {len(z)}; |z| >= 3 in {(abs(z) >= 3).sum()},'
      f' chance at that width {N*2*Phi(-3/w):.1f}')
