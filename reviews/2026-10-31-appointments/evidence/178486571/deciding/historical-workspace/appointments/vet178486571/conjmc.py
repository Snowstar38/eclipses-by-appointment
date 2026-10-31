"""Gaia SB1 conjunctions with the FULL covariance (corr_vec, SB1 order: P, gamma, K1, e, w, Tp).
A: nu = 90 - w (primary behind = companion in front... for the RV primary: nu=90-w is when the primary is
   farthest from us, i.e. companion in front of primary); B: nu = 270 - w.
python -X utf8 conjmc.py <archives2.json> <t0> <t1>  -> prints per-conjunction median, sigma; conj.json"""
import json, sys, os, numpy as np
r = json.load(open(sys.argv[1]))['nss_full'][0]; t0, t1 = float(sys.argv[2]), float(sys.argv[3])
keys = ['period', 'center_of_mass_velocity', 'semi_amplitude_primary', 'eccentricity', 'arg_periastron', 't_periastron']
mu = np.array([float(r[k]) for k in keys]); sg = np.array([float(r[k + '_error']) for k in keys])
cv = [float(v) for v in r['corr_vec'].strip('()').split(',')]; n = 6; C = np.eye(n); k = 0
for j in range(1, n):
    for i in range(j): C[i, j] = C[j, i] = cv[k]; k += 1
rng = np.random.default_rng(7); S = rng.multivariate_normal(mu, C * np.outer(sg, sg), 200000)
S = S[(S[:, 3] >= 0) & (S[:, 3] < 0.95)]
P, e, w, Tp = S[:, 0], S[:, 3], np.radians(S[:, 4]), S[:, 5] + 389.0
def tc(nu0, P, e, w, Tp):
    nu = nu0 - w; E = 2 * np.arctan2(np.sqrt(1 - e) * np.sin(nu / 2), np.sqrt(1 + e) * np.cos(nu / 2))
    M = (E - e * np.sin(E)) % (2 * np.pi); return Tp + M / (2 * np.pi) * P
out = []
for lab, nu0 in (('A', np.pi / 2), ('B', 1.5 * np.pi)):
    x = tc(nu0, P, e, w, Tp); xn = tc(nu0, mu[0], mu[3], np.radians(mu[4]), mu[5] + 389.0)
    x = xn + ((x - xn + mu[0] / 2) % mu[0]) - mu[0] / 2
    for kk in range(int((t0 - xn) // mu[0]) - 1, int((t1 - xn) // mu[0]) + 2):
        y = x + kk * P; m = np.median(y)
        if t0 <= m <= t1: out.append((lab, kk, float(m), float(np.std(y)), float(np.percentile(y, 84) - np.percentile(y, 16)) / 2))
out.sort(key=lambda z: z[2])
for o in out: print(f"{o[0]} k={o[1]:4d}  {o[2]:.3f}  sd {o[3]:.3f}  (68% half {o[4]:.3f})")
pha = ((tc(1.5 * np.pi, *[np.array([v]) for v in (mu[0], mu[3], np.radians(mu[4]), mu[5] + 389)]) - tc(np.pi / 2, *[np.array([v]) for v in (mu[0], mu[3], np.radians(mu[4]), mu[5] + 389)])) / mu[0]) % 1
ph = ((tc(1.5 * np.pi, P, e, w, Tp) - tc(np.pi / 2, P, e, w, Tp)) / P) % 1
print(f"Gaia B-A phase separation {pha[0]:.4f}  MC {np.median(ph):.4f} +- {np.std(ph):.4f}")
print(f"Gaia e cos w = {np.median(e*np.cos(w)):.4f} +- {np.std(e*np.cos(w)):.4f};  e sin w = {np.median(e*np.sin(w)):.4f} +- {np.std(e*np.sin(w)):.4f}")
json.dump(out, open(os.path.join(os.path.dirname(os.path.abspath(sys.argv[1])), 'conj.json'), 'w'), indent=0)
