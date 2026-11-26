"""Tertiary masses implied by Gaia's astrometric orbits (A73, R1003).

Gaia's Orbital solution measures the photocentre's semi-major axis a0 (mas). If the
eclipsing inner pair (mass M12) and a tertiary m3 orbit each other with relative semi-major
axis a (AU), then a^3 = (M12 + m3) P^2 and the photocentre moves on
    a0 = a * (m3/(M12 + m3) - beta),   beta = L3/(L12 + L3)  (G band).
beta = 0 (dark tertiary) gives the minimum m3; a main-sequence tertiary needs more.
Main-sequence G-band light is approximated as L ~ m^4 (m < ~1.5 Msun), so L12 = m1^4 + m2^4.
Thiele-Innes -> a0 from Fable's ESA TAP copy (nss.csv, 2026-11-25).
Usage: python3 tertiary_mass.py nss.csv
"""
import sys, csv, math
import numpy as np
from scipy.optimize import brentq

SYSTEMS = {  # source_id: name, inner masses (house assumptions)
    '2290881958791909248': ('A73', 1.2, 1.0),
    '5861580639046056832': ('R1003', 1.1, 0.9),
}

def a0_mas(A, B, F, G):
    u = (A*A + B*B + F*F + G*G) / 2; v = A*G - B*F
    return math.sqrt(u + math.sqrt(u*u - v*v))

def photocentre(m3, M12, L12, P_yr, lum=True):
    a = ((M12 + m3) * P_yr**2) ** (1/3)
    beta = (m3**4 / (L12 + m3**4)) if lum else 0.0
    return a * (m3 / (M12 + m3) - beta)

rows = {r['source_id']: r for r in csv.DictReader(open(sys.argv[1]))}
for sid, (name, m1, m2) in SYSTEMS.items():
    r = rows[sid]
    A, B, F, G = (float(r[k + '_thiele_innes']) for k in 'abfg')
    eA, eB, eF, eG = (float(r[k + '_thiele_innes_error']) for k in 'abfg')
    plx = float(r['parallax']); P = float(r['period']) / 365.25
    a0 = a0_mas(A, B, F, G); a0_AU = a0 / plx
    M12 = m1 + m2; L12 = m1**4 + m2**4
    # Monte Carlo over Thiele-Innes errors (uncorrelated; a rough error only)
    rng = np.random.default_rng(1)
    s = [a0_mas(*(rng.normal(x, e) for x, e in zip((A, B, F, G), (eA, eB, eF, eG)))) / plx for _ in range(4000)]
    lo, hi = np.percentile(s, [16, 84])
    print(f"{name}: P_out = {float(r['period']):.2f} d, e_out = {float(r['eccentricity']):.3f}, a0 = {a0:.3f} mas = {a0_AU:.4f} AU "
          f"(68%: {lo:.4f}-{hi:.4f}), parallax {plx:.3f} mas; inner pair {m1}+{m2} Msun")
    fm = a0_AU**3 / P**2
    print(f"   photocentric mass function a0^3/P^2 = {fm:.4f} Msun")
    for lum in (False, True):
        out = []
        for aa in (lo, a0_AU, hi):
            f = lambda m3: photocentre(m3, M12, L12, P, lum) - aa
            if lum:   # photocentre motion peaks and then falls as the tertiary gets bright
                grid = np.linspace(0.01, 1.5, 3000); pk = grid[np.argmax([photocentre(m, M12, L12, P, True) for m in grid])]
                hi_m = pk
            else:
                hi_m = 5.0
            try: out.append(brentq(f, 0.01, hi_m))
            except ValueError: out.append(float('nan'))
        print(f"   m3 ({'main-sequence tertiary, L~m^4' if lum else 'dark tertiary (minimum)'}): "
              f"{out[1]:.2f} Msun (68%: {out[0]:.2f}-{out[2]:.2f})")
    grid = np.linspace(0.01, 1.5, 3000); amax = max(photocentre(m, M12, L12, P, True) for m in grid)
    mpk = grid[np.argmax([photocentre(m, M12, L12, P, True) for m in grid])]
    print(f"   largest a0 a single main-sequence tertiary can give: {amax*plx:.3f} mas (at m3 = {mpk:.2f}); observed {a0:.3f}")
    # tertiary as an equal-mass pair of M dwarfs (total m3), or a white dwarf (dark)
    f2 = lambda m3: ((M12 + m3) * P**2) ** (1/3) * (m3/(M12 + m3) - 2*(m3/2)**4/(L12 + 2*(m3/2)**4)) - a0_AU
    g2 = np.linspace(0.05, 2.0, 2000); pk2 = g2[np.argmax([f2(m) for m in g2])]
    try: print(f"   if the tertiary is itself an equal-mass pair of dwarfs: m3 = {brentq(f2, 0.05, pk2):.2f} Msun in total")
    except ValueError: print(f"   an equal-mass pair of dwarfs can give at most {(f2(pk2)+a0_AU)*plx:.3f} mas")
    for m3 in (0.25, 0.35, 0.5, 1.0):
        print(f"   if m3 = {m3}: predicted a0 = {photocentre(m3, M12, L12, P, True)*plx:.3f} mas (dark: {photocentre(m3, M12, L12, P, False)*plx:.3f})")
