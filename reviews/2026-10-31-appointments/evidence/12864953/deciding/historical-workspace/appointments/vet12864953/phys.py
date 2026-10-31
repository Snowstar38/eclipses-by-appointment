"""Ephemeris (one A, one B event, s69; P cannot be measured from TESS alone), Gaia comparison with this star's covariance
(conj.json from conjmc.py), exact e cos w / e sin w consistency, mass function, m2, a, central durations, next eclipses.
python phys.py"""
import json, numpy as np
A, sA = 3204.1016, 1.5 / 1440      # mean of SPOC/TESS-SPOC/TARS/QLP (3204.10155-.10199); err ~ pipeline scatter
B, sB = 3196.0997, 2.5 / 1440      # mean of 4 pipelines (3196.09856-.10331)
r = json.load(open('archives2.json'))['nss_full'][0]
keys = ['period', 'center_of_mass_velocity', 'semi_amplitude_primary', 'eccentricity', 'arg_periastron', 't_periastron']
mu = np.array([float(r[k]) for k in keys]); sg = np.array([float(r[k + '_error']) for k in keys])
cv = [float(v) for v in r['corr_vec'].strip('()').split(',')]; C = np.eye(6); k = 0
for j in range(1, 6):
    for i in range(j): C[i, j] = C[j, i] = cv[k]; k += 1
S = np.random.default_rng(5).multivariate_normal(mu, C * np.outer(sg, sg), 400000); S = S[(S[:, 3] > 0) & (S[:, 3] < 0.95)]
P, e, w, Tp = S[:, 0], S[:, 3], np.radians(S[:, 4]), S[:, 5] + 389.0
def tc(nu0, near):
    nu = nu0 - w; E = 2 * np.arctan2(np.sqrt(1 - e) * np.sin(nu / 2), np.sqrt(1 + e) * np.cos(nu / 2))
    t = Tp + ((E - e * np.sin(E)) % (2 * np.pi)) / (2 * np.pi) * P
    return t + np.round((near - t) / P) * P
tA, tB = tc(np.pi / 2, A), tc(1.5 * np.pi, B)
for n, o, s, x in (('A', A, sA, tA), ('B', B, sB, tB)):
    print(f'{n}: observed {o:.4f}; Gaia MC {np.median(x):.3f} +- {np.std(x):.3f}; O-C {o-np.median(x):+.3f} d = {(o-np.median(x))/np.std(x):+.2f} sigma')
sep = ((tB - tA) / P) % 1; so = ((B - A) / mu[0]) % 1
print(f'B-A phase separation: observed {so:.5f} +- {np.hypot(sA,sB)/mu[0]:.5f}; Gaia {np.median(sep):.4f} +- {np.std(sep):.4f}; diff {(so-np.median(sep))/np.std(sep):+.2f} sigma')
print(f'A-B interval observed {A-B:.4f} d; Gaia {np.median((tA-tB)%P):.3f} +- {np.std((tA-tB)%P):.3f} d')
# exact: for which (e, w) is the separation the observed one? scan w at Gaia e, and e at Gaia w
def sepf(e_, w_):
    out = []
    for nu0 in (np.pi / 2, 1.5 * np.pi):
        nu = nu0 - w_; E = 2 * np.arctan2(np.sqrt(1 - e_) * np.sin(nu / 2), np.sqrt(1 + e_) * np.cos(nu / 2)); out.append((E - e_ * np.sin(E)) / (2 * np.pi))
    return (out[1] - out[0]) % 1
ww = np.radians(np.linspace(300, 380, 8001)); s_ = sepf(0.4668, ww); i = np.argmin(np.abs(s_ - so))
print(f'at Gaia e=0.4668 the observed separation needs w = {np.degrees(ww[i])%360:.2f} deg (Gaia 340.26 +- 2.00) -> e cos w {0.4668*np.cos(ww[i]):.4f}, e sin w {0.4668*np.sin(ww[i]):.4f}')
ee = np.linspace(0.3, 0.6, 3001); s_ = sepf(ee, np.radians(340.265)); i = np.argmin(np.abs(s_ - so))
print(f'at Gaia w=340.26 the observed separation needs e = {ee[i]:.4f} (Gaia 0.4668 +- 0.0125)')
print(f'MC: fraction of Gaia draws with separation <= observed: {np.mean(sep <= so):.2e}')
# mass function etc
K = mu[2]; Pg = mu[0]; eg = mu[3]; wg = np.radians(mu[4])
fM = 1.0361e-7 * (1 - eg ** 2) ** 1.5 * K ** 3 * Pg; print(f'f(M) = {fM:.4f} Msun')
for M1 in (0.95, 1.01, 1.1, 1.2):
    m = np.linspace(0.01, 1.5, 150001); m2 = m[np.argmin(np.abs(m ** 3 / (M1 + m) ** 2 - fM))]
    a = (7.496e-6 * (M1 + m2) * Pg ** 2) ** (1 / 3) * 215.03
    R1 = 1.669; R2 = 0.95 * m2 if m2 < 0.7 else m2
    rA = a * (1 - eg ** 2) / (1 + eg * np.sin(wg)); rB = a * (1 - eg ** 2) / (1 - eg * np.sin(wg))
    # central T14 ~ (R1+R2) * 2 / v_transverse ; v_t = 2 pi a / P * (1 + e cos nu)/sqrt(1-e^2), at A cos nu = sin w
    vA = 2 * np.pi * a / Pg * (1 + eg * np.sin(wg)) / np.sqrt(1 - eg ** 2); vB = 2 * np.pi * a / Pg * (1 - eg * np.sin(wg)) / np.sqrt(1 - eg ** 2)
    print(f' M1 {M1}: m2(i=90) {m2:.3f}; a {a:.1f} Rsun; sep at A {rA:.1f}, at B {rB:.1f} Rsun; central T14 A {2*(R1+R2)/vA*24:.2f} h, B {2*(R1+R2)/vB*24:.2f} h (R2~{R2:.2f}); grazing limit cos i < (R1+R2)/r: i > {np.degrees(np.arccos((R1+R2)/rA)):.2f} (A), {np.degrees(np.arccos((R1+R2)/rB)):.2f} (B)')
print('Next predicted eclipses (P = Gaia 31.62452 +- 0.00589, anchored on the s69 events):')
for n in range(1, 60):
    ta, tb = A + n * Pg, B + n * Pg
    if ta > 4320 and ta < 4520: print(f'  A n={n}: {ta:.3f} +- {np.hypot(sA, n*sg[0]):.3f}   B n={n}: {tb:.3f} +- {np.hypot(sB, n*sg[0]):.3f}')
