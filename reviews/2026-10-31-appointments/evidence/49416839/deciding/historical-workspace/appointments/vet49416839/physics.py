"""A ephemeris, e cos w from the A-B phase separation (exact Kepler solve at Gaia e), f(M), m2, a, separations and
central durations at each conjunction, a coarse two-sphere (quadratic LD primary, uniform companion) grid fitted to the
four observed numbers (depth/T14 of A and B), dilution table, next eclipses. python physics.py -> physics.txt"""
import json, numpy as np
E = json.load(open('ephem.json')); T0B, PB, CB = E['T0'], E['P'], np.array(E['cov'])
A = json.load(open('afit.json'))
ta = {}
for r in A:
    if r['src'] in ('TSPOC', 'TARS', 'QLP') and r['depth'] < 0.01: ta.setdefault(r['s'], []).append(r['t0'])
TA = np.array([np.mean(v) for k, v in sorted(ta.items())]); SA = np.array([max(np.std(v), 4 / 1440) for k, v in sorted(ta.items())])
n = np.round((TA - TA[0]) / PB); M = np.vstack([np.ones_like(n), n]).T; W = np.diag(1 / SA ** 2); C = np.linalg.inv(M.T @ W @ M); p = C @ M.T @ W @ TA
print(f'A times {np.round(TA,4)} (+- {np.round(SA*1440,1)} min), cycles {n}: T0 {p[0]:.4f} +- {np.sqrt(C[0,0])*1440:.1f} min, P {p[1]:.5f} +- {np.sqrt(C[1,1]):.5f} (B: {PB:.6f}); O-C min {np.round((TA-M@p)*1440,1)}')
ph = np.mean(((TA - T0B) / PB) % 1); print(f'A at phase {ph:.4f} after B -> B-A phase separation {1-ph:.4f} (Gaia MC 0.6614 +- 0.0121: {((1-ph)-0.6614)/0.0121:+.1f} sigma)')
P, K, e, w = 21.428467, 33.3617, 0.355762, np.radians(314.381)
def tconj(nu0, e, w):
    nu = nu0 - w; Ea = 2 * np.arctan2(np.sqrt(1 - e) * np.sin(nu / 2), np.sqrt(1 + e) * np.cos(nu / 2)); return ((Ea - e * np.sin(Ea)) / (2 * np.pi)) % 1
ws = np.radians(np.linspace(270, 360, 9001)); sep = np.array([(tconj(1.5 * np.pi, e, x) - tconj(0.5 * np.pi, e, x)) % 1 for x in ws])
wbest = ws[np.argmin(np.abs(sep - (1 - ph)))]
print(f'at Gaia e {e:.3f}: observed separation needs w = {np.degrees(wbest):.1f} deg (Gaia 314.4 +- 4.3) -> e cos w {e*np.cos(wbest):.3f} (Gaia 0.248 +- 0.020), e sin w {e*np.sin(wbest):.3f}')
fM = 1.0361e-7 * (1 - e ** 2) ** 1.5 * K ** 3 * P; print(f'f(M) = {fM:.4f} Msun')
for M1, R1 in ((1.0, 2.0), (1.07, 2.01), (1.2, 2.0)):
    m2 = 0.3
    for _ in range(200): m2 = (fM * (M1 + m2) ** 2) ** (1 / 3)
    a = 4.2084 * (M1 + m2) ** (1 / 3) * P ** (2 / 3)
    print(f'M1 {M1}: m2(i=90) {m2:.3f}; a {a:.1f} Rsun; R1/a {R1/a:.4f}')
    for lab, nu in (('A (companion in front, transit)', np.pi / 2 - w), ('B (primary in front, occultation)', 1.5 * np.pi - w)):
        r = a * (1 - e ** 2) / (1 + e * np.cos(nu)); v = 2 * np.pi * a / P * (1 + e * np.cos(nu)) / np.sqrt(1 - e ** 2)
        print(f'   {lab}: sep {r:.1f} Rsun; central T14 (R1 {R1} + R2 0.58) {2*(R1+0.58)/v*24:.2f} h; 1 R1 of impact = {np.degrees(np.arccos(R1/r)):.2f} deg incl')
# coarse two-sphere grid
def eclipse(b, k, front_primary, u1=0.45, u2=0.2, N=161):
    """fraction of light lost (relative to that star's own flux) for centre separation b (in R1), radius ratio k."""
    if front_primary:   # companion (radius k, uniform) behind primary (radius 1): fraction of companion covered
        if b >= 1 + k: return 0.0
        g = np.linspace(-k, k, N); X, Y = np.meshgrid(g, g); m = X ** 2 + Y ** 2 <= k * k
        return np.sum(m & ((X + b) ** 2 + Y ** 2 <= 1)) / m.sum()
    if b >= 1 + k: return 0.0
    g = np.linspace(-1, 1, 2 * N); X, Y = np.meshgrid(g, g); r2 = X ** 2 + Y ** 2; on = r2 <= 1
    mu = np.sqrt(np.clip(1 - r2, 0, 1)); I = (1 - u1 * (1 - mu) - u2 * (1 - mu) ** 2) * on
    return np.sum(I * ((X - b) ** 2 + Y ** 2 <= k * k)) / I.sum()
obs = dict(dA=0.0033, TA=3.9, dB=0.0125, TB=5.9)   # TESS-SPOC/TARS/QLP medians (afit.txt, ecl.txt)
print('observed: A depth ~0.20-0.48% (median ~0.30%), T14 ~3-4.5 h; B depth 1.0-1.45% (median ~1.2%), T14 5.5-6.1 h, flat 1.3-1.9 h')
M1, R1 = 1.07, 2.01; m2 = 0.3
for _ in range(200): m2 = (fM * (M1 + m2) ** 2) ** (1 / 3)
a = 4.2084 * (M1 + m2) ** (1 / 3) * P ** (2 / 3)
rA = (1 - e ** 2) / (1 + e * np.cos(np.pi / 2 - wbest)); rB = (1 - e ** 2) / (1 + e * np.cos(1.5 * np.pi - wbest))
vA = 2 * np.pi / P * (1 + e * np.cos(np.pi / 2 - wbest)) / np.sqrt(1 - e ** 2); vB = 2 * np.pi / P * (1 + e * np.cos(1.5 * np.pi - wbest)) / np.sqrt(1 - e ** 2)
best = []
for r1 in np.linspace(0.6, 1.4, 17) * R1 / a:
    for k in np.linspace(0.15, 0.45, 13):
        for cosi in np.linspace(0, 1.6 * r1 / rB, 41):
            bA, bB = rA * cosi / r1, rB * cosi / r1
            if bA >= 1 + k or bB >= 1 + k: continue
            fa = eclipse(bA, k, False)
            fb = eclipse(bB, k, True)
            if fb <= 0: continue
            T14A = 2 * r1 * np.sqrt(max((1 + k) ** 2 - bA ** 2, 0)) / vA * 24; T14B = 2 * r1 * np.sqrt(max((1 + k) ** 2 - bB ** 2, 0)) / vB * 24
            # companion light fraction L2/(L1+L2) chosen to match B depth: dB = l2 * fb ; then A depth = (1-l2) * fa
            l2 = obs['dB'] / fb
            if l2 >= 0.5: continue
            dA = (1 - l2) * fa
            chi = ((dA - obs['dA']) / 0.001) ** 2 + ((T14A - obs['TA']) / 0.6) ** 2 + ((T14B - obs['TB']) / 0.4) ** 2
            best.append((chi, r1, k, np.degrees(np.arccos(cosi)), bA, bB, l2, dA, T14A, T14B, fb))
best.sort()
print('best grid points (chi on dA, T14A, T14B; B depth matched exactly by the companion light fraction l2):')
for b in best[:8]: print('   chi2 %.2f r1 %.4f (R1 %.2f Rsun) k %.2f (R2 %.2f) i %.2f bA %.2f bB %.2f l2 %.3f fB(covered) %.2f -> dA %.3f%% T14A %.2f h T14B %.2f h' % (b[0], b[1], b[1] * a, b[2], b[2] * b[1] * a, b[3], b[4], b[5], b[6], b[10], b[7] * 100, b[8], b[9]))
# dilution
G = json.load(open('gaia.json')); g0 = float(G['src'][0]['phot_g_mean_mag'])
print('Neighbours G<16 within 90": needed eclipse depth on the neighbour = depth x 10^(0.4 dm)')
for r in G['nb'][1:]:
    g = float(r['phot_g_mean_mag'] or 99)
    if g < 16: print(f"   {r['source_id']} sep {float(r['sep']):5.1f}\" G {g:.2f}: B needs {1.25*10**(0.4*(g-g0)):.1f}%, A needs {0.33*10**(0.4*(g-g0)):.2f}%")
print('Next eclipses (B: observed ephemeris; A: observed A times on the B period):')
for t in (4400, 4500):
    k = np.ceil((t - T0B) / PB); s = np.sqrt(CB[0, 0] + k * k * CB[1, 1] + 2 * k * CB[0, 1]); tb = T0B + k * PB
    print(f'   B E{int(k)}: {tb:.4f} +- {s*1440:.1f} min;   A: {tb + ph*PB:.4f} +- ~{np.hypot(s, 5/1440)*1440:.0f} min')
