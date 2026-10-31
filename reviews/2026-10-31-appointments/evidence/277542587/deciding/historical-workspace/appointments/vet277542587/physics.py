"""Mass function, m2(i=90) for M1 options, a, central durations at A and B, neighbour dilution table. python -X utf8 physics.py"""
import json, numpy as np
r = json.load(open('archives2.json'))['nss_full'][0]; G = json.load(open('gaia.json'))
P = float(r['period']); K = float(r['semi_amplitude_primary']); e = float(r['eccentricity']); w = np.radians(float(r['arg_periastron']))
f = 1.0361e-7 * P * K ** 3 * (1 - e * e) ** 1.5
print(f'f(m) = {f:.4f} Msun  (P {P:.4f} d, K {K:.2f} km/s, e {e:.3f}, w {np.degrees(w):.1f})')
nuA, nuB = np.pi / 2 - w, 1.5 * np.pi - w
for M1, R1 in ((1.25, 2.82), (1.5, 2.82), (1.8, 2.82), (2.0, 2.82)):
    m2 = 0.1
    for _ in range(200): m2 = (f * (M1 + m2) ** 2) ** (1 / 3)
    a = (M1 + m2) ** (1 / 3) * (P / 365.25) ** (2 / 3) * 215.03
    R2 = m2 ** 0.8 if m2 < 1.2 else m2 ** 0.57 * 1.1
    out = []
    for lab, nu in (('A', nuA), ('B', nuB)):
        rr = a * (1 - e * e) / (1 + e * np.cos(nu)); vt = 2 * np.pi * a * 695700 / (P * 86400) * (1 + e * np.cos(nu)) / np.sqrt(1 - e * e)
        T = 2 * (R1 + R2) * 695700 / vt / 3600; out.append(f'{lab}: sep {rr:.1f} Rsun, T14(b=0) {T:.1f} h, b=1 at cos i {(R1+R2)/rr:.4f}')
    print(f'M1 {M1}: m2(i=90) {m2:.3f} Msun, a {a:.1f} Rsun, R2(MS) ~{R2:.2f};  ' + ';  '.join(out))
print('TIC: R 2.823 Rsun, M 1.25, Teff 6331, d 659 pc; Gaia plx 1.395 mas, RUWE 1.22, G 11.40, BP-RP 0.794')
print('Dilution: dip a neighbour would need = depth * 10^(0.4 dG)')
t = G['src'][0]; g0 = float(t['phot_g_mean_mag'])
for n in G['nb'][1:]:
    g = float(n['phot_g_mean_mag'] or 99)
    if g < 16 or float(n['sep']) < 10:
        x = 10 ** (0.4 * (g - g0)); print(f"  {n['source_id']} sep {float(n['sep']):5.1f}\" G {g:.2f}: needs B {0.1492*x*100:.0f}%  A {0.0776*x*100:.0f}%")
