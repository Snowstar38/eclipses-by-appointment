"""Mass function, m2, a, R1 from the LD fit's r1, central durations, dilution table, next eclipses. python physics.py -> physics.txt"""
import json, numpy as np
P, K, e, w = 33.671079, 27.489, 0.54987, np.radians(16.98)
fM = 1.0361e-7 * (1 - e ** 2) ** 1.5 * K ** 3 * P
print(f'f(M) = {fM:.4f} Msun (K {K} km/s, e {e}, P {P})')
for M1 in (1.15, 1.31, 1.45):
    m2 = 0.1
    for _ in range(100): m2 = (fM * (M1 + m2) ** 2) ** (1 / 3)
    a = 4.2084 * (M1 + m2) ** (1 / 3) * P ** (2 / 3)   # Rsun (G M P^2 / 4pi^2)
    print(f'M1 {M1}: m2(i=90) {m2:.3f} Msun, m2(i=87) {m2/np.sin(np.radians(87)):.3f}; a {a:.1f} Rsun; R1 from LD-fit r1 0.0293-0.0306 -> {0.0293*a:.2f}-{0.0306*a:.2f} Rsun (TIC 1.73)')
    R1, R2 = 1.73, 0.48
    for lab, nu in (('A', np.pi / 2 - w), ('B', 1.5 * np.pi - w)):
        r = a * (1 - e ** 2) / (1 + e * np.cos(nu)); v = 2 * np.pi * a / (P) * (1 + e * np.cos(nu) ) / np.sqrt(1 - e ** 2)   # transverse speed, Rsun/d
        print(f'   {lab}: separation {r:.1f} Rsun; central T14 (R1 {R1}+R2 {R2}) {2*(R1+R2)/v*24:.2f} h')
# dilution
G = json.load(open('gaia.json')); g0 = float(G['src'][0]['phot_g_mean_mag']); dep = 0.055
print('Neighbours G<15 within 90": needed fractional dip = depth x 10^(0.4 dm) (whole-star flux, before aperture losses)')
for r in G['nb'][1:]:
    g = float(r['phot_g_mean_mag'] or 99)
    if g < 15: print(f"   {r['source_id']} sep {float(r['sep']):5.1f}\" G {g:.2f}: needs {dep*10**(0.4*(g-g0))*100:.1f}%")
E = json.load(open('ephem.json')); T0, Pp, C = E['T0'], E['P'], np.array(E['cov'])
print('Next A eclipses (observed ephemeris, 1 sigma):')
for t in (4000, 4100, 4200, 4300, 4400):
    n = np.ceil((t - T0) / Pp); tt = T0 + n * Pp; s = np.sqrt(C[0, 0] + n * n * C[1, 1] + 2 * n * C[0, 1])
    print(f'   E {int(n)}: {tt:.4f} +- {s*1440:.1f} min')
print('Predicted B (A + 0.8222 P, Gaia phase sep +-0.0184 P = +-0.62 d; expected depth <~0.1% or none):')
for n in (75, 76, 77, 78):
    print(f'   after E{n}: {T0 + (n + 0.8222) * Pp:.2f} +- 0.62 d')
