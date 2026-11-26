"""How much third light do R623's eclipse depths allow?

Primary 338 ppt and secondary 99 ppt (medians of Earthshine's per-event depths,
timing/r623-events-earthshine.csv). For a radius ratio k = R2/R1 and impact parameter b,
L1 = depth1 / (fraction of star 1's limb-darkened flux hidden by star 2) and
L2 = depth2 / (fraction of star 2's flux hidden by star 1), in units of the total light;
the rest, 1 - L1 - L2, is third light. Quadratic limb darkening (0.45, 0.20) for the K dwarf
and (0.35, 0.30) for the M dwarf in the TESS band. Main-sequence radii for 0.64 and 0.41 Msun
give k of about 0.65; k up to 0.80 allows for an inflated M dwarf.
Run from the repository root: python3 reviews/duet-findings/timing/r623_third_light.py
"""
import csv, os
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ev = list(csv.DictReader(open(os.path.join(HERE, 'r623-events-earthshine.csv'))))
D1 = np.median([float(r['depth_ppt']) for r in ev if r['family'] == 'P']) / 1000
D2 = np.median([float(r['depth_ppt']) for r in ev if r['family'] == 'S']) / 1000


def hidden(k, b, u1, u2, n=600):
    x = np.linspace(-1, 1, n)
    X, Y = np.meshgrid(x, x)
    r2 = X ** 2 + Y ** 2
    mu = np.sqrt(np.clip(1 - r2, 0, 1))
    I = (1 - u1 * (1 - mu) - u2 * (1 - mu) ** 2) * (r2 < 1)
    return (I * (((X - b) ** 2 + Y ** 2) < k * k)).sum() / I.sum()


print(f"depths: primary {D1*1000:.0f} ppt, secondary {D2*1000:.0f} ppt")
best = {}
for k in np.arange(0.55, 0.801, 0.05):
    for b in np.arange(0, 0.61, 0.1):
        L1 = D1 / hidden(k, b, 0.45, 0.20)
        L2 = D2 / hidden(1 / k, b / k, 0.35, 0.30)
        L3 = 1 - L1 - L2
        if b == 0 or abs(b - 0.5) < 1e-9:
            print(f"k {k:.2f} b {b:.1f}: L1 {L1:.3f} L2 {L2:.3f} L3 {L3:+.3f}  (L3/L1 {max(L3, 0) / L1:.2f})")
        best[round(k, 2)] = max(best.get(round(k, 2), -1), L3 / L1)
print("largest third light relative to the primary, by k: "
      + ", ".join(f"{k:.2f}: {v:.2f}" for k, v in best.items()))
