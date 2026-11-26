"""Are Gaia DR3's eccentricity errors right?  Two tests.

1. Short binaries are circular (circularisation/: no secondary below 2 d has |e cos w| > 0.031),
   so Gaia's free-eccentricity SB1/SB2 fits at P < 2.5 d and < 3 d should give e/sigma_e following
   a Rayleigh law of scale 1.  The maximum-likelihood scale k = sqrt(mean((e/sigma)^2)/2) measures
   how far the quoted errors are off.  Input: gaia-geometry/gaia-vs-eclipse.csv.
2. For A-sample systems whose secondary phase the paper states (Appendix A notes), compare
   |e cos w| from the phase, (pi/2)|phase - 0.5|, with Gaia's |e cos w| and its error
   (e and w errors, correlations ignored).  Inputs: paper.html, gaia-errors/fable51-nss-appointments.csv.
Usage: python3 reviews/duet-findings/gaia-errors/eccentricity_errors.py
"""
import re, html, math, numpy as np, pandas as pd

D = 'reviews/duet-findings/'
g = pd.read_csv(D + 'gaia-geometry/gaia-vs-eclipse.csv')
for c in ['eclipse_period_days', 'gaia_ecc', 'gaia_ecc_err']:
    g[c] = pd.to_numeric(g[c].astype(str).str.split('|').str[0], errors='coerce')
x = g[(g['class'] == 'harmonic 1') & g.nss_type.isin(['SB1', 'SB2']) & g.gaia_ecc_err.notna()]
print('1. Gaia e / sigma_e for short binaries (free-e SB1/SB2 at the eclipse period)')
for lim in (2.5, 3.0):
    s = x[x.eclipse_period_days < lim]; z = s.gaia_ecc / s.gaia_ecc_err
    k = math.sqrt(np.mean(z**2) / 2)
    print(f'  P < {lim} d: n = {len(s)}, median e/sigma {z.median():.2f} (Rayleigh 1.18), scale k = {k:.2f} +- {k/math.sqrt(4*len(s)):.2f};'
          f' above 3 sigma {int((z > 3).sum())} (expected {len(s)*math.exp(-4.5):.1f}): {s.review_id[z > 3].tolist()}')
for a, b in [(3, 5), (5, 8), (8, 20), (20, 100)]:
    s = x[(x.eclipse_period_days >= a) & (x.eclipse_period_days < b)]; z = s.gaia_ecc / s.gaia_ecc_err
    print(f'  P {a}-{b} d: n = {len(s)}, median e/sigma {z.median():.2f}, fraction above 3 sigma {np.mean(z > 3):.2f}')

raw = open('paper.html', encoding='utf-8').read()
i = raw.find('Appendix A. Ephemerides')
tab = re.findall(r'<table.*?</table>', raw[i:], flags=re.S)[3]
nss = pd.read_csv(D + 'gaia-errors/fable51-nss-appointments.csv').set_index('review_id')
print('2. A systems with a stated secondary phase: |e cos w| from the phase against Gaia')
print('  id    type  P(d)     phase    phot    Gaia    sigma   z')
zs = []
for r in re.findall(r'<tr>(.*?)</tr>', tab, flags=re.S)[1:]:
    c = [html.unescape(re.sub('<[^>]+>', '', t)).strip() for t in re.findall(r'<td[^>]*>(.*?)</td>', r, flags=re.S)]
    m = re.findall(r'(?:secondary|second eclipse|shallower)[^;]{0,80}?phase\s+([01]\.\d+)', ' '.join(c[1:]))
    if not m or c[0] not in nss.index: continue
    o = nss.loc[c[0]]; e = o.eccentricity; w = math.radians(o.arg_periastron)
    sw = math.radians(o.arg_periastron_error) if pd.notna(o.arg_periastron_error) else 0.0
    gc = abs(e * math.cos(w)); sg = math.hypot(math.cos(w) * o.eccentricity_error, e * math.sin(w) * sw)
    pc = math.pi / 2 * abs(float(m[0]) - 0.5); z = (gc - pc) / sg; zs.append((c[0], z))
    print(f'  {c[0]:5s} {o.nss_solution_type:4s} {o.period:7.3f}  {float(m[0]):.5f}  {pc:.4f}  {gc:.4f}  {sg:.4f}  {z:+.2f}')
z = np.array([t[1] for t in zs])
print(f'  n = {len(z)}: rms z {np.sqrt(np.mean(z**2)):.2f}; without A145 {np.sqrt(np.mean(np.array([t[1] for t in zs if t[0] != "A145"])**2)):.2f}')
