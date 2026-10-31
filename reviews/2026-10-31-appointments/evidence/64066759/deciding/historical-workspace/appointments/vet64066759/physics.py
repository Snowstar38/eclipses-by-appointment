"""Physics MC for TIC 64066759: f(M), m2, a, separation and transverse speed at A (nu=90-w, companion in front) and
B (nu=270-w); cos i from the observed A T14 (straight chord); whether B can eclipse; uniform-disc + linear-LD depth of A.
Gaia (P,K,e,w) drawn with this star's corr_vec; P replaced by the eclipse P. R1 ~ U(1.7,2.3) (L from G, plx: R~1.9),
M1 ~ U(0.9,1.3); R2 from MS m2. python physics.py -> physics.txt"""
import json, numpy as np
r = json.load(open('archives2.json'))['nss_full'][0]
keys = ['period', 'center_of_mass_velocity', 'semi_amplitude_primary', 'eccentricity', 'arg_periastron', 't_periastron']
mu = np.array([float(r[k]) for k in keys]); sg = np.array([float(r[k + '_error']) for k in keys])
cv = [float(v) for v in r['corr_vec'].strip('()').split(',')]; C = np.eye(6); k = 0
for j in range(1, 6):
    for i in range(j): C[i, j] = C[j, i] = cv[k]; k += 1
rng = np.random.default_rng(3); N = 200000
S = rng.multivariate_normal(mu, C * np.outer(sg, sg), N); K, e, w = S[:, 2], S[:, 3], np.radians(S[:, 4])
P = 40.93771; T14A = 4.19 / 24; depA = 0.0227
M1 = rng.uniform(0.9, 1.3, N); R1 = rng.uniform(1.7, 2.3, N)
f = 1.0361e-7 * K ** 3 * P * (1 - e * e) ** 1.5
m2 = np.full(N, 0.5)
for _ in range(50): m2 = (f * (M1 + m2) ** 2) ** (1 / 3)
m2 = m2 * 1.003   # i ~ 85 deg
R2 = np.where(m2 < 1, m2 ** 0.9, m2 ** 0.8)
aAU = ((M1 + m2) * (P / 365.25) ** 2) ** (1 / 3); a = aAU * 215.03
rA = a * (1 - e * e) / (1 + e * np.sin(w)); rB = a * (1 - e * e) / (1 - e * np.sin(w))
v0 = 2 * np.pi * a * 696000 / (P * 86400) / np.sqrt(1 - e * e)   # km/s; transverse speed at conj = v0 (1 +- e sin w)
vA = v0 * (1 + e * np.sin(w)); vB = v0 * (1 - e * np.sin(w))
TcA = 2 * (R1 + R2) * 696000 / vA / 3600; TcB = 2 * (R1 + R2) * 696000 / vB / 3600
ok = TcA > 4.19
bA = np.sqrt(np.clip((R1 + R2) ** 2 - (T14A * 24 * 3600 * vA / 696000 / 2) ** 2, 0, None))
cosi = bA / rA; bB = rB * cosi; Becl = bB < (R1 + R2)
# A depth: area of companion disc overlapping primary at b=bA, uniform disc, linear LD u=0.6 at the overlap mu
def ov(R, r_, d):
    d = np.clip(d, 1e-9, None); x = np.clip((d * d + r_ * r_ - R * R) / (2 * d * r_), -1, 1); y = np.clip((d * d + R * R - r_ * r_) / (2 * d * R), -1, 1)
    A = r_ * r_ * np.arccos(x) + R * R * np.arccos(y) - 0.5 * np.sqrt(np.clip((-d + r_ + R) * (d + r_ - R) * (d - r_ + R) * (d + r_ + R), 0, None))
    return np.where(d >= R + r_, 0, np.where(d <= abs(R - r_), np.pi * np.minimum(R, r_) ** 2, A))
A = ov(R1, R2, bA); u = 0.6; rho = np.clip((bA + R1) / 2 / R1, 0, 1); muL = np.sqrt(1 - np.minimum(rho, 0.999) ** 2)
L2frac = (R2 / R1) ** 2 * ((np.where(m2 < 0.45, 3500, 5772 * m2 ** 0.55)) / 5313) ** 3.0   # crude TESS-band ratio
depmod = A / (np.pi * R1 ** 2) * (1 - u * (1 - muL)) / (1 - u / 3) / (1 + L2frac)
q = lambda x: f'{np.median(x[ok]):.3f} [{np.percentile(x[ok],16):.3f}, {np.percentile(x[ok],84):.3f}]'
print(f'f(M) {np.median(f):.4f} +- {np.std(f):.4f} Msun')
for m in (0.9, 1.1, 1.3):
    mm = 0.5
    for _ in range(50): mm = (np.median(f) * (m + mm) ** 2) ** (1 / 3)
    print(f'  M1 {m}: m2(i=90) {mm:.3f} Msun')
print('a [Rsun]', q(a), ' rA', q(rA), ' rB', q(rB), '  rB/rA', q(rB / rA))
print('R2', q(R2), ' central T14 A [h]', q(TcA), ' central T14 B [h]', q(TcB))
print(f'fraction of draws where observed A T14 (4.19 h) < central: {ok.mean():.3f}')
print('b_A/(R1+R2)', q(bA / (R1 + R2)), ' i [deg]', q(np.degrees(np.arccos(cosi))))
print('b_B/(R1+R2)', q(bB / (R1 + R2)), f'  P(B eclipses at all) = {Becl[ok].mean():.4f}')
print('predicted A depth (grazing transit of companion, LD)', q(depmod), ' observed 2.2-2.35%; L2/L1 TESS', q(L2frac))
need = (R1 + R2) / rB
print('B eclipses only if cos i <', q(need), ' i.e. b_A/(R1+R2) <', q(rA / rB))
# depth vs assumed R1 (wider range), and vs R2 scaling
for lo, hi in ((1.3, 1.5), (1.5, 1.7), (1.7, 1.9), (1.9, 2.1), (2.1, 2.3)):
    R1b = rng.uniform(lo, hi, N); bAb = np.sqrt(np.clip((R1b + R2) ** 2 - (T14A * 24 * 3600 * vA / 696000 / 2) ** 2, 0, None))
    Ab = ov(R1b, R2, bAb); rhob = np.clip((bAb + R1b) / 2 / R1b, 0, 0.999); mub = np.sqrt(1 - rhob ** 2)
    L2b = (R2 / R1b) ** 2 * ((np.where(m2 < 0.45, 3500, 5772 * m2 ** 0.55)) / 5313) ** 3.0
    db = Ab / (np.pi * R1b ** 2) * (1 - u * (1 - mub)) / (1 - u / 3) / (1 + L2b); okb = (bAb > 0)
    print(f'R1 {lo}-{hi}: A depth {np.median(db[okb])*100:.2f}% [{np.percentile(db[okb],16)*100:.2f}, {np.percentile(db[okb],84)*100:.2f}]  b_A/(R1+R2) {np.median((bAb/(R1b+R2))[okb]):.3f}  P(B) {(rB*bAb/rA < R1b+R2)[okb].mean():.4f}')
