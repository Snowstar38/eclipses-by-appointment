"""Ephemeris, Gaia comparison, mass function, radii from ebfit3_q0_L0.json, next eclipses. python physics.py > physics.txt"""
import json, numpy as np
r = json.load(open('archives2.json'))['nss_full'][0]; eb = json.load(open('ebfit3_q0_L0.json')); E = json.load(open('ecl.json'))
Pg, sPg = float(r['period']), float(r['period_error']); K = float(r['semi_amplitude_primary']); eg = float(r['eccentricity']); wg = float(r['arg_periastron'])
B = {e['key']: e for e in E}
tB1, sB1 = B['TSPOC15']['t0'], max(B['TSPOC15']['et0'], abs(B['TSPOC15']['t0'] - B['QLP15']['t0'])); tB2, sB2 = B['QLP76']['t0'], B['QLP76']['et0']
PB = (tB2 - tB1) / 30; sPB = np.hypot(sB1, sB2) / 30
print(f'B-only ephemeris (2 events, 30 cycles): P {PB:.6f} +- {sPB:.6f} d; vs Gaia {Pg:.5f}+-{sPg:.5f}: {(PB-Pg)/sPg:+.2f} sigma; N=29/31 give {(tB2-tB1)/29:.3f}/{(tB2-tB1)/31:.3f} (excluded)')
tA = B['TSPOC16']['t0']; ph = ((tB1 - tA) / PB) % 1
print(f'A 1756 single event {tA:.5f}; phase of B after A {ph:.5f} (Gaia MC 0.2625 +- 0.0138)')
print(f"joint LD fit: P {eb['P']:.6f} +- {eb['err'][1]:.6f}, tA {eb['tP']:.5f}; e {eb['e']:.4f} w {eb['w']:.2f} (Gaia e {eg:.4f}+-0.0232, w {wg:.2f}+-3.58)")
print(f"  ecosw {eb['ecosw']:.4f}+-{eb['err'][2]:.4f} (Gaia -0.3816+-0.0235), esinw {eb['esinw']:.4f}+-{eb['err'][3]:.4f} (Gaia 0.0709+-0.0240)")
fM = 1.0361e-7 * K**3 * Pg * (1 - eg**2)**1.5
print(f'f(M) = {fM:.4f} Msun (K1 {K:.2f})')
for M1 in (1.2, 1.3, 1.4, 1.5, 1.6):
    m2 = 0.5
    for _ in range(100): m2 = (fM * (M1 + m2)**2)**(1/3)
    si = np.sin(np.radians(eb['inc'])); m2i = m2
    for _ in range(100): m2i = (fM * (M1 + m2i)**2)**(1/3) / si
    a = 215.03 * ((M1 + m2i) * (eb['P'] / 365.25)**2)**(1/3)
    print(f'  M1 {M1}: m2(i=90) {m2:.3f}, m2(i={eb["inc"]:.2f}) {m2i:.3f}; a {a:.1f} Rsun; R1 {eb["r1"]*a:.2f} R2 {eb["r2"]*a:.2f} Rsun')
e, w = eb['e'], np.radians(eb['w']); a1 = eb['r1']; a2 = eb['r2']; ci = eb['cosi']
for lab, nu in (('A (companion in front)', np.pi/2 - w), ('B (primary in front)', 1.5*np.pi - w)):
    rr = (1 - e**2) / (1 + e*np.cos(nu)); v = (1 + e*np.cos(nu)) / np.sqrt(1 - e**2)
    Tc = eb['P'] / np.pi * (a1 + a2) / v * 24
    print(f'  {lab}: separation {rr:.3f} a, central T14 {Tc:.2f} h, impact {rr*ci/a1:.3f} R1')
print(f"  surface-brightness ratio J {eb['J']:.3f}, k {eb['k']:.3f}, L2/L1(TESS) {eb['L2L1']:.3f}")
P, sP, T0 = eb['P'], max(eb['err'][1], sPB), eb['tP']; dph = 0.26535
print('next eclipses (BTJD), sigma from P error', f'{sP:.6f}:')
for n in range(47, 51):
    tAn = T0 + n*P; print(f'  A n={n}: {tAn:.4f} +- {n*sP*1440:.1f} min;  B: {tAn + dph*P:.4f} +- {n*sP*1440:.1f} min')
