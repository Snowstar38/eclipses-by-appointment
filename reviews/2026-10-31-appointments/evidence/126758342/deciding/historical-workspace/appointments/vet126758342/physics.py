"""Physics: mass function, m2, a, separations/velocities at each conjunction, impact parameter at B from the observed
T14, and whether the A conjunction must miss. MC over Gaia (e, w) with the per-star covariance; P fixed to the eclipse P.
Uniform-disc overlap for the occulted fraction. python physics.py"""
import json, numpy as np
r = json.load(open('arch2.json'))['nss_full'][0]
keys = ['period', 'center_of_mass_velocity', 'semi_amplitude_primary', 'eccentricity', 'arg_periastron', 't_periastron']
mu = np.array([float(r[k]) for k in keys]); sg = np.array([float(r[k + '_error']) for k in keys])
cv = [float(v) for v in r['corr_vec'].strip('()').split(',')]; C = np.eye(6); k = 0
for j in range(1, 6):
    for i in range(j): C[i, j] = C[j, i] = cv[k]; k += 1
Pe = 22.86993; T14B = 6.1 / 24; dep = 0.021
G = 2.959122e-4  # AU^3 / Msun / d^2
def fm(P, K, e): return 1.0361e-7 * K ** 3 * P * (1 - e * e) ** 1.5
def m2_of(f, M1, sini=1.0):
    m = 0.5
    for _ in range(60): m = (f * (M1 + m) ** 2) ** (1 / 3) / sini
    return m
def r_ms(m): return m ** 0.9 if m < 1 else m ** 0.8
def teff_ms(m): return 5772 * m ** 0.55 if m > 0.45 else 3500
def sb(T, Tref=7142, lam=0.8):  # Planck ratio at 0.8 um
    return (np.exp(14388 / (lam * Tref)) - 1) / (np.exp(14388 / (lam * T)) - 1)
def overlap(d, R, r_):  # area of disc r_ covered by disc R at separation d
    d = np.asarray(d, float); r_ = np.broadcast_to(r_, d.shape).astype(float); out = np.zeros_like(d)
    full = d <= R - r_; out[full] = np.pi * r_[full] ** 2
    p = (d > R - r_) & (d < R + r_); dd = d[p]; r_all = r_; r_ = r_[p]
    a1 = r_ ** 2 * np.arccos((dd ** 2 + r_ ** 2 - R ** 2) / (2 * dd * r_)); a2 = R ** 2 * np.arccos((dd ** 2 + R ** 2 - r_ ** 2) / (2 * dd * R))
    a3 = 0.5 * np.sqrt((-dd + r_ + R) * (dd + r_ - R) * (dd - r_ + R) * (dd + r_ + R)); out[p] = a1 + a2 - a3
    return out / (np.pi * r_all ** 2)
print(f"Gaia nominal: P {mu[0]:.4f} K1 {mu[2]:.2f} e {mu[3]:.3f} w {mu[4]:.1f}; e sin w {mu[3]*np.sin(np.radians(mu[4])):+.3f}  e cos w {mu[3]*np.cos(np.radians(mu[4])):+.3f}")
f0 = fm(Pe, mu[2], mu[3]); print(f"f(M) = {f0:.4f} Msun (nominal; K1 err {sg[2]:.1f} km/s)")
R1 = 2.188
for M1 in (1.4, 1.59, 1.8):
    m2 = m2_of(f0, M1); R2 = r_ms(m2); T2 = teff_ms(m2); L2 = (R2 / R1) ** 2 * sb(T2)
    a = (G * (M1 + m2) * Pe ** 2 / (4 * np.pi ** 2)) ** (1 / 3) * 215.03
    print(f"M1 {M1}: m2(i=90) {m2:.3f} Msun (MS R2 {R2:.2f} Rsun, Teff ~{T2:.0f} K) a {a:.1f} Rsun; companion TESS light fraction ~{L2/(1+L2)*100:.1f}%")
# MC
rng = np.random.default_rng(3); S = rng.multivariate_normal(mu, C * np.outer(sg, sg), 400000)
S = S[(S[:, 3] >= 0) & (S[:, 3] < 0.95) & (S[:, 2] > 0)]
K, e, w = S[:, 2], S[:, 3], np.radians(S[:, 4]); M1 = rng.uniform(1.4, 1.8, len(e))
f = fm(Pe, K, e); m2 = np.array([m2_of(x, y) for x, y in zip(f[:40000], M1[:40000])]); n = len(m2)
K, e, w, M1, f = K[:n], e[:n], w[:n], M1[:n], f[:n]
R2 = np.where(m2 < 1, m2 ** 0.9, m2 ** 0.8); T2 = 5772 * m2 ** 0.55; L2f = (R2 / R1) ** 2 * sb(T2); L2f = L2f / (1 + L2f)
a = (G * (M1 + m2) * Pe ** 2 / (4 * np.pi ** 2)) ** (1 / 3) * 215.03
esw = e * np.sin(w)
rB = a * (1 - e * e) / (1 - esw); rA = a * (1 - e * e) / (1 + esw)   # B: nu = 270 - w (primary in front); A: nu = 90 - w
vB = 2 * np.pi * a / Pe / np.sqrt(1 - e * e) * (1 - esw); vA = 2 * np.pi * a / Pe / np.sqrt(1 - e * e) * (1 + esw)
TcB = 2 * (R1 + R2) / vB; TcA = 2 * (R1 + R2) / vA
x = T14B / TcB; okB = x < 1
bB = (R1 + R2) * np.sqrt(np.clip(1 - x ** 2, 0, 1)); cosi = bB / rB; bA = rA * cosi
missA = bA > (R1 + R2)
occ = overlap(bB, R1, R2); depB = occ * L2f
print(f"MC ({n} draws, M1 U(1.4,1.8), MS companion): m2 median {np.median(m2):.2f} [{np.percentile(m2,16):.2f},{np.percentile(m2,84):.2f}]; companion light {np.median(L2f)*100:.1f}% [{np.percentile(L2f,16)*100:.1f},{np.percentile(L2f,84)*100:.1f}]")
print(f"  e sin w {np.median(esw):+.3f} +- {np.std(esw):.3f}; rA/rB median {np.median(rA/rB):.2f}")
print(f"  central T14 at B {np.median(TcB)*24:.1f} h [{np.percentile(TcB,16)*24:.1f},{np.percentile(TcB,84)*24:.1f}]; at A {np.median(TcA)*24:.1f} h")
print(f"  draws with central T14_B > observed 6.1 h (B eclipse possible at this duration): {okB.mean()*100:.0f}%")
s = okB
print(f"  among those: i median {np.degrees(np.arccos(np.median(cosi[s]))):.2f} deg; b_B/(R1+R2) {np.median(bB[s]/(R1+R2)[s]):.2f}; B partial (b_B > R1-R2) {np.mean(bB[s] > (R1-R2)[s])*100:.0f}%; "
      f"A misses (b_A > R1+R2) {np.mean(missA[s])*100:.0f}%")
s2 = s & missA
print(f"  among those with A missing: predicted B depth (uniform discs, companion occulted) median {np.median(depB[s2])*100:.2f}% [{np.percentile(depB[s2],16)*100:.2f},{np.percentile(depB[s2],84)*100:.2f}] vs observed ~2.0-2.2%;"
      f" e sin w {np.median(esw[s2]):+.3f} [{np.percentile(esw[s2],16):+.3f},{np.percentile(esw[s2],84):+.3f}]")
s3 = s & ~missA
print(f"  draws where A would eclipse: the A event (companion transits the A star, k^2 ~ {np.median((R2/R1)**2)*100:.0f}%) would be ~{np.median(overlap(bA[s3], R1, R2[s3]) * (R2[s3]/R1)**2)*100 if s3.sum() else 0:.1f}% deep (median) - excluded by the <=0.35-0.46% upper limit")
print(f"  e sin w bound from 'A misses': A misses requires e sin w < {np.percentile(esw[s2], 95):+.3f} (95th pct of passing draws)")
