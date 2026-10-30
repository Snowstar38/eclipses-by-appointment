# Physics sanity, duration-ratio e sin(omega), primary/secondary period difference, independent nominal check
# of the Gaia conjunction times, and ephemerides + next three primaries in UTC (barycentric light-time removed
# for a geocentric observer). Inputs: s6_period.out values (pasted), gaia_nss_tap.csv, s11 depths.
import numpy as np, pandas as pd
from scipy.optimize import brentq, least_squares
from astropy.time import Time
from astropy.coordinates import SkyCoord, EarthLocation
import astropy.units as u
G = pd.read_csv('gaia_nss_tap.csv').set_index('source_id')
ST = {'470235665': dict(gid=2287291537931000064, ra=345.74771690923, dec=81.69976438579, M1=(0.93, 1.3), R1tic=2.2972, Teff=5353,
        Ppri=(10.326183, 0.000002), T0pri=(1795.74233, 0.00018), Psec=(10.326173, 0.000002), T0sec=(1801.14120, 0.00023),
        dA=0.1224, dB=0.0809, T14A=6.45, T14B=9.01, T23A=2.46, T23B=2.79),   # SPOC SAP means (s11); QLP ~4% deeper
      '379251709': dict(gid=519027491846682624, ra=29.75443908755, dec=67.54616264314, M1=(0.91, 1.3), R1tic=1.88078, Teff=5279,
        Ppri=(12.323912, 0.000007), T0pri=(1961.25375, 0.00060), Psec=None, T0sec=None,
        dA=0.0363, dB=0.0025, T14A=4.22, T14B=4.50, T23A=0.94, T23B=None)}
def mfun(P, K, e): return 1.0361e-7 * K ** 3 * P * (1 - e ** 2) ** 1.5
def planck_ratio(T2, T1, lam=0.8e-6):
    c = 1.4388e-2 / lam; return (np.exp(c / T1) - 1) / (np.exp(c / T2) - 1)
def conj_time(Tp, P, e, w, nu_deg):
    nu = np.radians(nu_deg); E = 2 * np.arctan2(np.sqrt(1 - e) * np.sin(nu / 2), np.sqrt(1 + e) * np.cos(nu / 2))
    M = (E - e * np.sin(E)) % (2 * np.pi); return Tp + P * M / (2 * np.pi)
now = Time.now(); now_btjd = now.tdb.jd - 2457000
print(f'now = {now.utc.iso} UTC = BTJD {now_btjd:.3f} (TDB, no light-time)')
for tic, s in ST.items():
    g = G.loc[s['gid']]; P, K, e, w = g.period, g.semi_amplitude_primary, g.eccentricity, g.arg_periastron
    Tp = g.t_periastron + 389.0
    print('=' * 10, 'TIC', tic)
    fm = mfun(P, K, e); print(f'mass function f(m) = {fm:.4f} Msun (P={P:.4f} d, K1={K:.2f} km/s, e={e:.3f})')
    for M1 in s['M1']:
        m2 = brentq(lambda m: m ** 3 / (M1 + m) ** 2 - fm, 0.01, 5)
        a = 4.2084 * (M1 + m2) ** (1 / 3) * s['Ppri'][0] ** (2 / 3)
        print(f'   M1={M1:.2f}: m2(i=90)={m2:.3f} Msun, a={a:.2f} Rsun')
    # --- nominal Gaia conjunctions (no MC) propagated both ways: independent of s8 ---
    tA = conj_time(Tp, P, e, w, 90 - w); tB = conj_time(Tp, P, e, w, 270 - w)
    T0, Pt = s['T0pri'][0], s['Ppri'][0]
    n = np.round((tA - T0) / Pt); back = T0 + n * Pt
    print(f'nominal Gaia conj A = BTJD {tA:.3f}, conj B = {tB:.3f} (B-A phase {((tB-tA)/P)%1:.4f}); TESS primary ephemeris at that epoch: {back:.3f} -> primary - A = {back-tA:+.3f} d, primary - B = {(back-tB+P/2)%P-P/2:+.3f} d')
    # --- duration ratio: e sin w lower bound (equal impact parameters) ---
    rat = s['T14B'] / s['T14A']; print(f'T14(B)/T14(A) = {rat:.3f} -> e sin w >= {(rat-1)/(rat+1):+.3f} (equal-b approximation); Gaia e sin w = {e*np.sin(np.radians(w)):+.3f}')
    if s['Psec']:
        dP = s['Psec'][0] - s['Ppri'][0]; edP = np.hypot(s['Psec'][1], s['Ppri'][1])
        print(f'P_sec - P_pri = {dP*1e6:+.1f} +- {edP*1e6:.1f} x1e-6 d ({dP/edP:+.1f} sigma); over 178 cycles the secondary drifts {178*dP*1440:+.1f} min relative to the primary')
    # --- geometry from the light curve (sphere-sphere, no limb darkening; rough) ---
    esw = e * np.sin(np.radians(w)); sq = np.sqrt(1 - e ** 2)
    hr = s['Ppri'][0] / np.pi * 24
    if tic == '470235665':
        l2 = s['dB']; k = np.sqrt(s['dA'] / (1 - l2))  # A annular transit (flat bottom), B total occultation
        def resid(p):
            ra, bA = p; bB = bA * (1 + esw) / (1 - esw)
            T14A = hr * ra * np.sqrt(max((1 + k) ** 2 - bA ** 2, 0)) * sq / (1 + esw)
            T14B = hr * ra * np.sqrt(max((1 + k) ** 2 - bB ** 2, 0)) * sq / (1 - esw)
            return [T14A - s['T14A'], T14B - s['T14B']]
        sol = least_squares(resid, [0.08, 0.3], bounds=([0.01, 0], [0.5, 1.2])); ra, bA = sol.x; bB = bA * (1 + esw) / (1 - esw)
        T23A = hr * ra * np.sqrt(max((1 - k) ** 2 - bA ** 2, 0)) * sq / (1 + esw); T23B = hr * ra * np.sqrt(max((1 - k) ** 2 - bB ** 2, 0)) * sq / (1 - esw)
        J = l2 / (k ** 2 * (1 - l2)); T2 = brentq(lambda T: planck_ratio(T, s['Teff']) - J, 2000, 9000)
        print(f'LC geometry (k from depths assuming annular A + total B, Gaia e,w): k=R2/R1={k:.3f}, companion light l2={l2:.3f}, R1/a={ra:.4f}, b_A={bA:.2f}, b_B={bB:.2f}')
        print(f'   predicted T23: A {T23A:.2f} h, B {T23B:.2f} h (trapezoid fits: {s["T23A"]}, {s["T23B"]} h; LD makes trapezoid T23 a poor proxy)')
        print(f'   surface-brightness ratio J={J:.2f} -> T2 ~ {T2:.0f} K (T1={s["Teff"]} K, 0.8 um blackbody)')
        for M1 in s['M1']:
            m2 = brentq(lambda m: m ** 3 / (M1 + m) ** 2 - fm, 0.01, 5); a = 4.2084 * (M1 + m2) ** (1 / 3) * s['Ppri'][0] ** (2 / 3)
            print(f'   M1={M1:.2f}: R1={ra*a:.2f} Rsun (TIC {s["R1tic"]}), R2={k*ra*a:.2f} Rsun, m2={m2:.2f} Msun, i={np.degrees(np.arccos(bA*ra*(1+esw)/(1-e**2))):.1f} deg')
    else:
        for M1 in s['M1']:
            m2 = brentq(lambda m: m ** 3 / (M1 + m) ** 2 - fm, 0.01, 5); a = 4.2084 * (M1 + m2) ** (1 / 3) * s['Ppri'][0] ** (2 / 3)
            R2ms = m2 ** 0.9  # rough M-dwarf mass-radius
            k = R2ms / s['R1tic']; ra = s['R1tic'] / a
            # impact parameter that reproduces T14 for this k
            f = lambda b: hr * ra * np.sqrt(max((1 + k) ** 2 - b ** 2, 0)) * sq / (1 + esw) - s['T14A']
            try: b = brentq(f, 0, 1 + k - 1e-6)
            except ValueError: b = np.nan
            print(f'   M1={M1:.2f}: m2={m2:.2f} Msun, R2~{R2ms:.2f} Rsun, k={k:.3f} (k^2={1e3*k**2:.1f} ppt vs depth {1e3*s["dA"]:.1f} ppt), T14 needs b={b:.2f} (grazing if b>1-k={1-k:.2f})')
        # non-grazing reading of the trapezoid shape: T23/T14 fixes b for a given k; T14 then fixes R1/a
        for k in [0.18, 0.20, 0.22]:
            r2 = (s['T23A'] / s['T14A']) ** 2; b = np.sqrt(((1 - k) ** 2 - r2 * (1 + k) ** 2) / (1 - r2))
            ra = s['T14A'] / (hr * np.sqrt((1 + k) ** 2 - b ** 2) * sq / (1 + esw))
            print(f'   non-grazing (T23/T14={s["T23A"]/s["T14A"]:.2f}), k={k:.2f}: b={b:.2f}, R1/a={ra:.4f} -> R1={ra*23.78:.2f}-{ra*26.51:.2f} Rsun (TIC {s["R1tic"]}), R2={k*ra*23.78:.2f}-{k*ra*26.51:.2f} Rsun')
        for T2 in [3200, 3500]:
            J = planck_ratio(T2, s['Teff']); print(f'   companion {T2} K: J={J:.3f}; full-occultation depth ~ k^2 J for k=0.20: {1e3*0.04*J:.1f} ppt, k=0.22: {1e3*0.0484*J:.1f} ppt (measured secondary ~2.5 ppt)')
    # --- ephemerides and next three primaries ---
    T0, eT0 = s['T0pri']; Pp, eP = s['Ppri']
    print(f'EPHEMERIS primary: T0 = BTJD {T0:.5f} +- {eT0:.5f} = BJD_TDB {T0+2457000:.5f}; P = {Pp:.6f} +- {eP:.6f} d')
    if s['Psec']: print(f'EPHEMERIS secondary: T0 = BTJD {s["T0sec"][0]:.5f} +- {s["T0sec"][1]:.5f}; P = {s["Psec"][0]:.6f} +- {s["Psec"][1]:.6f} d')
    c = SkyCoord(s['ra'], s['dec'], unit='deg'); geo = EarthLocation.from_geocentric(0, 0, 0, unit=u.m)
    n0 = int(np.ceil((now_btjd - T0) / Pp))
    for kind, (TT0, PP) in [('primary', (T0, Pp))] + ([('secondary', (s['T0sec'][0], s['Psec'][0]))] if s['Psec'] else []):
        n0 = int(np.ceil((now_btjd - TT0) / PP))
        for n in range(n0, n0 + 3):
            tb = TT0 + n * PP; err = np.hypot(eT0, n * eP) * 1440
            tt = Time(tb + 2457000, format='jd', scale='tdb')
            tg = tt
            for _ in range(3):
                ltt = tg.light_travel_time(c, kind='barycentric', location=geo); tg = tt - ltt
            print(f'   next {kind} E{n}: BTJD {tb:.4f} (BJD_TDB {tb+2457000:.4f}) +- {err:.1f} min -> geocentric UTC {tg.utc.iso[:16]} (light-time {ltt.to(u.min).value:+.1f} min removed)')
