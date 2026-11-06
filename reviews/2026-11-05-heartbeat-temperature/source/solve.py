"""teff438089101/solve.py — joint (Teff, E(B-V)) fit for TIC 438089101 from
multi-band colors, then R from the Gaia DR3 parallax.

Why: TIC's Teff 11991 K has TeffFlag 'dered' with EBVflag 'schlegel'
(E(B-V) = 0.555) at galactic latitude b = -3.36 deg, where Schlegel is a
full-Galaxy column and an upper bound on the dust actually in front of a
star at 1.4 kpc. Opus 5.5's house-6 letter (2026-11-05) argues ~9000 K from
the tide amplitude, the delta Sct-like p modes and Gaia esphs 'A'.

Method: intrinsic colors vs Teff from the Pecaut & Mamajek (2013) dwarf
table (mamajek_colors.txt, version 2022.04.16, Gaia DR2 passbands);
extinction coefficients A_X/A_V from Wang & Chen 2019 (ApJ 877, 116):
G 0.789, BP 1.002, RP 0.589, J 0.243, H 0.131, Ks 0.078; R_V = 3.1.
Observed colors use different reddening slopes per E(B-V)
(J-Ks 0.51, BP-RP 1.28, G-Ks 2.20, V-Ks 2.86 mag per mag), which is what
breaks the Teff/E degeneracy.

Controls: (1) synthetic injection at a known (Teff, E) must be recovered;
(2) pinning E = 0.555 (TIC's Schlegel value) should land near TIC's 11991 K,
confirming the mechanism rather than a calibration offset.
"""
import numpy as np

# ---------- parse the Mamajek table ----------
COLS = None
rows = []
for line in open('mamajek_colors.txt'):
    if line.startswith('#SpT') and COLS is None:
        COLS = line[1:].split()
        continue
    if line.startswith('#') or COLS is None:
        continue
    parts = line.split()
    if len(parts) != len(COLS):
        continue
    rows.append(dict(zip(COLS, parts)))

def getf(r, k):
    v = r.get(k, '')
    try:
        return float(v)
    except ValueError:
        return np.nan

NEED = ['Teff', 'BCv', 'Mv', 'M_G', 'Bp-Rp', 'G-V', 'V-Ks', 'J-H', 'H-Ks']
tab = []
for r in rows:
    vals = {k: getf(r, k) for k in NEED}
    if any(np.isnan(v) for v in vals.values()):
        continue
    if not (5500 <= vals['Teff'] <= 20000):
        continue
    vals['SpT'] = r['SpT']
    tab.append(vals)
tab.sort(key=lambda d: d['Teff'])
T = np.array([d['Teff'] for d in tab])
print(f"table rows used: {len(tab)}, Teff {T[0]:.0f}..{T[-1]:.0f}")

def interp(key):
    y = np.array([d[key] for d in tab])
    return lambda t: np.interp(t, T, y)

c_bprp = interp('Bp-Rp')
c_gv   = interp('G-V')
c_vks  = interp('V-Ks')
c_jh   = interp('J-H')
c_hks  = interp('H-Ks')
i_bcv  = interp('BCv')
i_mv   = interp('Mv')
i_mg   = interp('M_G')

def intrinsic(t):
    """intrinsic colors: BP-RP, G-Ks, V-Ks, J-Ks"""
    vks = c_vks(t)
    return np.array([c_bprp(t), c_gv(t) + vks, vks, c_jh(t) + c_hks(t)])

# ---------- extinction ----------
RV = 3.1
AX = {'G': 0.789, 'BP': 1.002, 'RP': 0.589, 'V': 1.0,
      'J': 0.243, 'H': 0.131, 'Ks': 0.078}  # Wang & Chen 2019
# reddening slope d(color)/d(E(B-V)) for each fitted color
SLOPE = np.array([
    RV * (AX['BP'] - AX['RP']),   # BP-RP
    RV * (AX['G'] - AX['Ks']),    # G-Ks
    RV * (AX['V'] - AX['Ks']),    # V-Ks
    RV * (AX['J'] - AX['Ks']),    # J-Ks
])

# ---------- observed (tic.json / gaia.json receipts in ../vet438089101) ----------
G, BP, RP = 12.1067, 12.3504, 11.7431     # Gaia (G from DR3 source, BP/RP from TIC=DR2)
V, eV = 12.266, 0.031                      # Tycho-2-derived V (TIC VmagFlag tycho2v3)
J, H, Ks = 11.262, 11.153, 11.063          # 2MASS AAA
eJ = eH = eKs = 0.023
PLX, ePLX = 0.698672, 0.009672             # Gaia DR3 (mas)

OBS = np.array([BP - RP, G - Ks, V - Ks, J - H + (H - Ks)])
# errors: quadrature of band errors + 0.02 systematic floor (DR2-passband table
# vs DR3 photometry, dwarf table on a logg~3.9 star, calibration zero points)
SYS = 0.02
ERR = np.array([
    np.hypot(0.004, SYS),
    np.hypot(np.hypot(0.001, eKs), SYS),
    np.hypot(np.hypot(eV, eKs), SYS),
    np.hypot(np.hypot(eJ, eKs), SYS),
])
NAMES = ['BP-RP', 'G-Ks', 'V-Ks', 'J-Ks']
print('\nobserved colors:')
for n, o, e in zip(NAMES, OBS, ERR):
    print(f'  {n:6s} {o:+.3f} +- {e:.3f}   reddening slope {SLOPE[NAMES.index(n)]:.3f}/E(B-V)')

# ---------- grid fit ----------
tgrid = np.arange(6000, 16001, 25.0)
egrid = np.arange(0.0, 0.9001, 0.0025)
chi2 = np.empty((len(tgrid), len(egrid)))
intr = np.array([intrinsic(t) for t in tgrid])      # (nt, 4)
for j, e in enumerate(egrid):
    model = intr + SLOPE[None, :] * e
    chi2[:, j] = (((OBS[None, :] - model) / ERR[None, :]) ** 2).sum(axis=1)

def report(chi2, tag, mask_e=None):
    c = chi2.copy()
    if mask_e is not None:
        c[:, ~mask_e] = np.inf
    k = np.unravel_index(np.argmin(c), c.shape)
    tb, eb, cmin = tgrid[k[0]], egrid[k[1]], c[k]
    # 1-sigma marginal ranges (delta chi2 = 1 on the profile)
    prof_t = c.min(axis=1); prof_e = c.min(axis=0)
    tlo, thi = tgrid[prof_t <= cmin + 1][[0, -1]]
    elo, ehi = egrid[prof_e <= cmin + 1][[0, -1]]
    t2lo, t2hi = tgrid[prof_t <= cmin + 4][[0, -1]]
    print(f'\n[{tag}] best: Teff {tb:.0f} K, E(B-V) {eb:.3f}, chi2 {cmin:.2f} (4 colors, 2 params)')
    print(f'  Teff 1-sig [{tlo:.0f}, {thi:.0f}]  2-sig [{t2lo:.0f}, {t2hi:.0f}];  E(B-V) 1-sig [{elo:.3f}, {ehi:.3f}]')
    model = intrinsic(tb) + SLOPE * eb
    for n, o, m, e in zip(NAMES, OBS, model, ERR):
        print(f'    {n:6s} obs {o:+.3f}  model {m:+.3f}  pull {(o-m)/e:+.1f}')
    return tb, eb

tb, eb = report(chi2, 'free fit')

# pinned at TIC's Schlegel E(B-V)=0.555 — does TIC's 11991 come back?
report(chi2, 'E pinned to Schlegel 0.555', mask_e=np.abs(egrid - 0.555) < 0.002)

# ---------- control 1: synthetic injection ----------
for tinj, einj in [(9000.0, 0.40), (12000.0, 0.555), (7500.0, 0.25)]:
    obs_inj = intrinsic(tinj) + SLOPE * einj
    c = np.empty_like(chi2)
    for j, e in enumerate(egrid):
        model = intr + SLOPE[None, :] * e
        c[:, j] = (((obs_inj[None, :] - model) / ERR[None, :]) ** 2).sum(axis=1)
    k = np.unravel_index(np.argmin(c), c.shape)
    print(f'[control inject T={tinj:.0f} E={einj:.3f}] recovered T={tgrid[k[0]]:.0f} E={egrid[k[1]]:.3f} chi2min={c[k]:.4f}')

# ---------- radius vs Teff along the fit ----------
d_pc = 1000.0 / PLX
mu = 5 * np.log10(d_pc / 10.0)
print(f'\ndistance {d_pc:.0f} pc (DR3 plx), mu = {mu:.3f}')
print('Teff    E(fit BP-RP)  A_G    M_G    BC_G    L/Lsun   R/Rsun   [E needed for R=5.0]')
for t in [7000, 7500, 8000, 8500, 9000, 9500, 10000, 11000, 12000]:
    # E that matches BP-RP exactly at this Teff (the dominant constraint)
    e_t = (OBS[0] - c_bprp(t)) / SLOPE[0]
    ag = AX['G'] * RV * e_t
    mg = G - mu - ag
    bcg = (i_mv(t) + i_bcv(t)) - i_mg(t)       # BC_G = Mbol - M_G from table rows
    mbol = mg + bcg
    L = 10 ** (-0.4 * (mbol - 4.74))
    R = np.sqrt(L) * (5772.0 / t) ** 2
    # E(B-V) needed for R = 5.0 at this Teff
    L5 = 25.0 * (t / 5772.0) ** 4
    mbol5 = 4.74 - 2.5 * np.log10(L5)
    mg5 = mbol5 - bcg
    ag5 = G - mu - mg5
    e5 = ag5 / (AX['G'] * RV)
    print(f'{t:5.0f}   {e_t:.3f}        {ag:.3f}  {mg:+.3f}  {bcg:+.3f}  {L:7.1f}  {R:6.2f}   [{e5:.3f}]')

# at the joint best fit:
e_t = eb
ag = AX['G'] * RV * eb
mg = G - mu - ag
bcg = (i_mv(tb) + i_bcv(tb)) - i_mg(tb)
L = 10 ** (-0.4 * (mg + bcg - 4.74))
R = np.sqrt(L) * (5772.0 / tb) ** 2
# error on R: plx (0.0097/0.6987 = 1.4% -> 2.8% in L -> 1.4% in R), Teff 1-sig, E
print(f'\njoint best fit: Teff {tb:.0f}, E {eb:.3f} -> A_G {ag:.3f}, M_G {mg:+.3f}, '
      f'L {L:.1f} Lsun, R {R:.2f} Rsun')
