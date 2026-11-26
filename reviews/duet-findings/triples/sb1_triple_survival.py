"""Which tertiaries can a Gaia DR3 SB1 orbit survive? (companion to sb1_gamma_drift.py)

Chance that Gaia publishes the inner pair's SB1 (F2 < 3) for a circular, coplanar, edge-on
outer orbit at random phase, with the sample's median N_RV (22) and per-epoch error
(3.7 km/s) and the same noise factor, for an inner pair of 2.0 Msun (two 1 Msun stars).
Also the light-travel semi-amplitude, so the grid can be read against what TESS timing sees.
Run from the repository root: python3 reviews/duet-findings/triples/sb1_triple_survival.py
"""
import contextlib, io, math, os, sys
import numpy as np
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
with contextlib.redirect_stdout(io.StringIO()):
    import sb1_gamma_drift as S
S.rng = np.random.default_rng(7)
G = 2.959122e-4          # au^3 Msun^-1 d^-2
AU_KMS = 1731.456837     # au/d in km/s
M12, N, SIG = 2.0, 22, 3.7
proto = dict(rv_n_good_obs_primary=str(N), period='5.0', eccentricity='0', t_periastron='0', arg_periastron='0',
             semi_amplitude_primary='40', semi_amplitude_primary_error=f"{SIG / math.sqrt(N / 2):.4f}")
infl = S.inflation(proto)
P3s = [365, 730, 1461, 2922, 5844]
m3s = [0.1, 0.25, 0.5, 1.0]
print(f"inner pair {M12} Msun, N_RV {N}, {SIG} km/s per epoch (noise x{infl:.2f}); entries: chance published, "
      f"[gamma semi-amplitude km/s, light-travel semi-amplitude min]")
print("m3 \\ P3 (yr) " + "".join(f"{p / 365.25:>17.0f}" for p in P3s))
for m3 in m3s:
    line = f"{m3:5.2f} Msun   "
    for P3 in P3s:
        a = (G * (M12 + m3) * (P3 / (2 * math.pi)) ** 2) ** (1 / 3)
        a12 = a * m3 / (M12 + m3)
        K = 2 * math.pi * a12 / P3 * AU_KMS
        ltt = a12 * 499.005 / 60
        pub = []
        for k in range(400):
            ph = S.rng.uniform(0, 2 * math.pi)
            v = lambda t, K=K, P3=P3, ph=ph: K * np.cos(2 * math.pi * t / P3 + ph)
            s, _, _ = S.sim(proto, v, 1, infl)
            pub.append(s[0] < 3)
        line += f"  {np.mean(pub):4.0%} [{K:4.1f},{ltt:4.1f}]"
    print(line)
