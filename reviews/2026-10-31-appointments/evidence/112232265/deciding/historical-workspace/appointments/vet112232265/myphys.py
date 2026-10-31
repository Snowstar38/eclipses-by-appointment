"""Mass function, m2(i=90), a, separations and central durations at A/B, impact parameters given B's T14.
python myphys.py"""
import numpy as np
P, K, e, w = 28.40515, 36.5409, 0.44599, np.radians(211.2204)
f = 1.0361e-7 * K ** 3 * P * (1 - e ** 2) ** 1.5; print(f'f(m) = {f:.4f} Msun')
R1 = 2.58; T14B = 6.5 / 24
for M1 in (1.2, 1.4, 1.6):
    m2 = 0.1
    for _ in range(200): m2 = (f * (M1 + m2) ** 2) ** (1 / 3)
    R2 = 0.9 * m2 ** 0.8; a = ((M1 + m2) * (P / 365.25) ** 2) ** (1 / 3) * 215.03
    out = [f'M1 {M1} m2min {m2:.3f} (R2~{R2:.2f}) a {a:.1f} Rsun']
    for lab, nu in (('A', np.pi / 2 - w), ('B', 1.5 * np.pi - w)):
        r = a * (1 - e ** 2) / (1 + e * np.cos(nu)); v = 2 * np.pi * a * 696000 / (P * 86400) * (1 + e * np.cos(nu)) / np.sqrt(1 - e ** 2)
        Tc = 2 * (R1 + R2) * 696000 / v / 3600; out.append(f'{lab}: r {r:.1f} Rsun ({r/a:.3f}a) Tcentral {Tc:.1f} h'); 
        if lab == 'B': bB = np.sqrt(max(0, 1 - (T14B * 24 / Tc) ** 2)); cosi = bB * (R1 + R2) / r; rB = r
        else: rA = r
    out.append(f'b_B {bB:.2f} (R1+R2) -> i {np.degrees(np.arccos(cosi)):.2f} deg -> b_A {cosi*rA/(R1+R2):.2f} (R1+R2): A eclipse {"impossible" if cosi*rA>(R1+R2) else "possible"}')
    print('  '.join(out))
