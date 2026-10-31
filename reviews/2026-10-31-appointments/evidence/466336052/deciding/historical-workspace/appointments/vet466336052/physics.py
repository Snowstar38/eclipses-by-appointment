"""Ephemeris from the two A events, Gaia comparison, mass function, m2, a, central durations, next eclipses. python physics.py"""
import numpy as np
A = [(2818.48299, 0.7), (3557.68457, 1.0)]   # pipeline means (QLP, TESS-SPOC, TARS) from ecl.txt; err min = max(formal, scatter)
dT = A[1][0] - A[0][0]; sdT = np.hypot(A[0][1], A[1][1]) / 1440
gP, gsP = 32.146500864092275, 0.0462197
for N in (22, 23, 24):
    P = dT / N; print(f'N={N}: P {P:.6f} +- {sdT/N:.6f}  vs Gaia {(P-gP)/gsP:+.2f} sigma')
P = dT / 23; sP = sdT / 23; T0 = A[0][0]; sT0 = A[0][1] / 1440
K, e, se, w = 14.550694462883524, 0.233008, 0.0482, np.radians(313.64)
fM = 1.0361e-7 * (1 - e * e) ** 1.5 * K ** 3 * P; print(f'f(M) = {fM:.5f} Msun')
for M1 in (1.0, 1.1, 1.2, 1.35):
    m = np.linspace(0.01, 1.5, 150001); m2 = m[np.argmin(np.abs(m ** 3 / (M1 + m) ** 2 - fM))]
    a = 4.2084 * (M1 + m2) ** (1 / 3) * P ** (2 / 3)
    vA = (1 + e * np.cos(np.pi / 2 - w)) / np.sqrt(1 - e * e); vB = (1 + e * np.cos(1.5 * np.pi - w)) / np.sqrt(1 - e * e)
    rA = (1 - e * e) / (1 + e * np.sin(w)); rB = (1 - e * e) / (1 - e * np.sin(w))
    R1, R2 = 1.44, 0.196 * 1.44
    TcA = P / np.pi * (R1 + R2) / a / vA * 24; TcB = P / np.pi * (R1 + R2) / a / vB * 24
    print(f'M1 {M1}: m2(i=90) {m2:.3f} Msun, a {a:.1f} Rsun ({a/215.03:.3f} AU); sep at A {rA*a:.1f}, at B {rB*a:.1f} Rsun; '
          f'central T14 (R1 1.44, k 0.196) A {TcA:.2f} h, B {TcB:.2f} h; v_t factor A {vA:.3f} B {vB:.3f}')
print(f'ephemeris A: T0 {T0:.5f} +- {sT0*1440:.1f} min, P {P:.6f} +- {sP:.6f}')
print('next A eclipses (BTJD):')
for n in range(48, 53):
    print(f'  A E{n}: {T0+n*P:.4f} +- {np.hypot(sT0, n*sP)*1440:.1f} min')
print('next B windows: sep 0.601+-0.034 (Gaia, conditioned) and restricted by bnull.py to 0.562-0.628 (B depth>=0.2% excluded elsewhere):')
for n in range(48, 53):
    tA = T0 + n * P
    print(f'  B before A E{n}: {tA+(0.6012-1)*P:.2f} +- {0.0335*P:.2f} d; allowed {tA+(0.562-1)*P:.2f} .. {tA+(0.628-1)*P:.2f}')
