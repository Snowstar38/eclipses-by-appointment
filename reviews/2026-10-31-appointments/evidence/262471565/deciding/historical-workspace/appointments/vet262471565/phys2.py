"""Physics for TIC 262471565: f(M), m2(i=90), a, central durations at A and B, expected B depth for an M-dwarf companion,
b from T12/T14, e cos w from a candidate B phase. python phys2.py"""
import numpy as np
P, K, e, w = 29.385742, 15.80935, 0.0952, np.radians(92.12); R1 = 4.56; dep = 0.0045
fM = 1.0361e-7 * (1 - e ** 2) ** 1.5 * K ** 3 * P; print(f'f(M) = {fM:.5f} Msun')
for M1 in (1.0, 1.5, 2.0, 2.5):
    m2 = 0.1
    for _ in range(100): m2 = (fM * (M1 + m2) ** 2) ** (1 / 3)
    a = (M1 + m2) ** (1 / 3) * (P / 365.25) ** (2 / 3) * 215.03
    R2 = R1 * np.sqrt(dep / 1.1)  # LD-corrected k^2 ~ depth/1.1
    for lab, sgn in (('A (nu=90-w, near periastron)', +1), ('B (nu=270-w)', -1)):
        T = P / np.pi * np.arcsin((R1 + R2) / a) * np.sqrt(1 - e ** 2) / (1 + sgn * e * np.sin(w)) * 24
        print(f'M1 {M1}: m2(i=90) {m2:.3f} Msun  a {a:.1f} Rsun  R1/a {R1/a:.3f}  R2~{R2:.2f}  central T14 {lab}: {T:.1f} h')
    # impact-parameter scaling between conjunctions: r ~ (1-e^2)/(1+e sin(w)) at A, /(1-e sin w) at B
print(f'separation ratio r_B/r_A = {(1+e*np.sin(w))/(1-e*np.sin(w)):.3f} -> b_B = {(1+e*np.sin(w))/(1-e*np.sin(w)):.2f} b_A')
# B depth expectations
x = lambda T: 14388 / 0.8 / T
for T2 in (3200, 3350, 3500):
    sb = (np.exp(x(4891)) - 1) / (np.exp(x(T2)) - 1)
    print(f'T2 {T2} K: BB(0.8um) surface-brightness ratio {sb:.3f} -> B (full occultation) depth {dep/1.1*sb*1e6:.0f} ppm')
for MT2 in (8.8, 9.2, 9.6):
    print(f'M_T(companion) {MT2}: flux ratio vs giant (M_T {10.40-5*np.log10(100/1.9233):.2f}) {10**(-0.4*(MT2-(10.40-5*np.log10(100/1.9233))))*1e6:.0f} ppm')
for ph in (0.480, 0.4978):
    print(f'B-A phase {ph}: e cos w ~ pi/2 (ph-0.5) = {np.pi/2*(ph-0.5):+.4f}  (Gaia MC -0.0034 +- 0.0404)')
