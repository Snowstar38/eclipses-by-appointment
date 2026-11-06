"""Rescale the referee's equilibrium-tide expectation (s4_out.txt rows) to the
revised stellar parameters. The referee's row at (M1 3.2, m2 0.69, a 18.8 Rsun,
R1 3.25) gives undiluted S 7.85e-4 with alpha_ell 1.06; S scales as
(m2/M1) * (R1/a)**3 with i, e, omega fixed, so S_new = S_ref * (q/q_ref) *
(R1/R1_ref)**3 * (a_ref/a)**3. m2 from Gaia's f(m) = 0.014367 at i = 60.7 deg;
a from Kepler at P = 4.800079 d."""
import numpy as np
from scipy.optimize import brentq

FM = 0.014366966        # Msun, Gaia SB1
INC = np.radians(60.7)  # referee's fit
P_D = 4.800079
S_REF, Q_REF, R_REF, A_REF = 7.85e-4, 0.69 / 3.2, 3.25, 18.8
CONTRATIO = 0.369332135
S_FIT = 2.53e-3

def m2_of(m1):
    f = lambda m2: m2**3 * np.sin(INC)**3 / (m1 + m2)**2 - FM
    return brentq(f, 0.01, 5.0)

def a_rsun(mtot):
    # a^3 = G Mtot P^2 / (4 pi^2); in units: a/AU = (Mtot/Msun)^(1/3) (P/yr)^(2/3)
    a_au = mtot**(1/3) * (P_D / 365.25)**(2/3)
    return a_au * 215.032

print(f'referee row check: q {Q_REF:.4f}, a {a_rsun(3.2 + 0.69):.2f} (printed 18.8)')
print(f'fitted S {S_FIT:.3e}; dilution factor 1/(1+contratio) = {1/(1+CONTRATIO):.3f}\n')
print(' M1    m2     q      a(Rsun)  R1    S_undil   S_diluted  fitted/expected')
for m1, r1 in [(3.2, 3.25),            # TIC (the referee's row, as control)
               (2.0, 3.65), (1.9, 3.65), (2.2, 3.65),  # revised Teff ~7000 K
               (2.0, 3.40),            # if Teff 8500-9000 end of range
               (2.0, 5.0)]:
    m2 = m2_of(m1)
    q = m2 / m1
    a = a_rsun(m1 + m2)
    s_u = S_REF * (q / Q_REF) * (r1 / R_REF)**3 * (A_REF / a)**3
    s_d = s_u / (1 + CONTRATIO)
    print(f'{m1:4.1f}  {m2:.3f}  {q:.3f}  {a:7.2f}  {r1:4.2f}  {s_u:.3e}  {s_d:.3e}   {S_FIT/s_d:5.2f}x')

# R1 needed for exact match at M1 = 2.0
m2 = m2_of(2.0); q = m2/2.0; a = a_rsun(2.0+m2)
r_need = R_REF * ((S_FIT * (1+CONTRATIO) / S_REF) * (Q_REF/q) * (a/A_REF)**-3)**0  # placeholder
r_need = (S_FIT * (1+CONTRATIO) / (S_REF * (q/Q_REF) * (A_REF/a)**3))**(1/3) * R_REF
print(f'\nR1 for exact match at M1 2.0: {r_need:.2f} Rsun '
      f'(vs 3.65 from the color fit; was 5.3 at TIC M1 3.2)')
