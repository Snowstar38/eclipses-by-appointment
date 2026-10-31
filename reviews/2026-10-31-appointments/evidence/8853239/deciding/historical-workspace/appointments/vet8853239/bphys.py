"""B-window box scan (QLP q0 and TESS-SPOC SAP, local quadratic baseline over +-1 d excluding box) + empirical false-alarm
rate at all other s48 times; then physics (f(M), m2, a, central durations, e sin w from Gaia vs observed).
python bphys.py -> bphys.txt"""
import json, numpy as np
from astropy.io import fits
D = '[local path omitted]'
def load(fn):
    d = fits.open(fn)[1].data; t = np.array(d['TIME'], float); f = np.array(d['SAP_FLUX'], float); q = np.array(d['QUALITY'])
    ok = np.isfinite(t) & np.isfinite(f) & (q == 0); t, f = t[ok], f[ok]; return t, f / np.median(f)
L = {'QLP': load(D + '8853239_s048.fits'), 'TSPOC': load(D + 'vet8853239/hlsp_tess-spoc_tess_phot_0000000008853239-s0048_tess_v1_lc.fits')}
def box(t, f, x, dur):
    inn = np.abs(t - x) < dur / 2; base = (np.abs(t - x) < dur / 2 + 0.8) & ~inn
    if inn.sum() < 0.6 * dur / (10 / 1440) or base.sum() < 40: return None
    c = np.polyfit(t[base] - x, f[base], 2); r = f - np.polyval(c, t - x)
    sd = np.std(r[base]); return -np.mean(r[inn]), sd / np.sqrt(inn.sum())
for dur in (7 / 24, 9.5 / 24):
    for k, (t, f) in L.items():
        A = [(x, *box(t, f, x, dur)) for x in np.arange(t.min() + 0.5, t.max() - 0.5, 0.02) if box(t, f, x, dur) and abs(x - 2629.07) > 0.6]
        A = np.array(A); inw = np.abs(A[:, 0] - 2616.33) < 3.0
        i = np.argmax(A[inw, 1]); bx = A[inw][i]
        fa = np.mean(A[~inw, 1] >= bx[1])
        print(f"{k} dur {dur*24:.1f} h: B window 2613.3-2619.3 coverage {inw.sum()*0.02:.1f} d of 6.0; max box {bx[1]*100:.3f}+-{bx[2]*100:.3f}% at {bx[0]:.2f}; "
              f"fraction of out-of-window times with a deeper box {fa:.2f}; 3-sigma UL at 2616.33 +- 1: max over window of (d+3s) = {np.max(A[inw,1]+3*A[inw,2])*100:.3f}%")
        j = np.argmin(np.abs(A[:, 0] - 2616.1)); print(f"   box at 2616.10: {A[j,1]*100:.3f} +- {A[j,2]*100:.3f}%")
# physics
r = json.load(open('arch2.json'))['nss_full'][0]
P = float(r['period']); e = float(r['eccentricity']); w = np.radians(float(r['arg_periastron'])); K = float(r['semi_amplitude_primary'])
fM = 1.0361e-7 * (1 - e**2)**1.5 * K**3 * P
print(f"\nP {P:.4f} e {e:.3f} w {np.degrees(w):.1f} K1 {K:.2f} -> f(M) {fM:.4f} Msun")
G = 6.674e-11; Ms = 1.989e30; Rs = 6.957e8
for M1 in (0.95, 1.01, 1.10):
    m2 = 0.05
    for _ in range(100): m2 = (fM * (M1 + m2)**2)**(1 / 3)
    a = (G * (M1 + m2) * Ms * (P * 86400)**2 / (4 * np.pi**2))**(1 / 3) / Rs
    print(f"M1 {M1}: m2(i=90) {m2:.3f} Msun, a {a:.1f} Rsun")
M1, R1 = 1.01, 1.576; m2 = 0.05
for _ in range(100): m2 = (fM * (M1 + m2)**2)**(1 / 3)
a = (G * (M1 + m2) * Ms * (P * 86400)**2 / (4 * np.pi**2))**(1 / 3) / Rs
k = np.sqrt(0.0600)  # flat-bottom depth -> k if total/central transit of a dark body (lower bound on R2/R1)
for lab, nu in (('A', np.pi / 2 - w), ('B', 1.5 * np.pi - w)):
    rr = a * (1 - e**2) / (1 + e * np.cos(nu)); vt = 2 * np.pi * a / P * (1 + e * np.cos(nu)) / np.sqrt(1 - e**2)  # Rsun/day transverse speed
    T14 = 2 * R1 * (1 + k) / vt * 24; T23 = 2 * R1 * (1 - k) / vt * 24
    print(f"{lab}: separation {rr:.1f} Rsun; central T14 {T14:.2f} h, T23 {T23:.2f} h (R1 {R1}, k {k:.3f})")
# observed A: T14 6.95, T12 1.45 -> b from trapezoid (Seager & Mallen-Ornelas) with k
T14o, T12o = 6.95, 1.45; T23o = T14o - 2 * T12o
b2 = ((1 - k)**2 - (T23o / T14o)**2 * (1 + k)**2) / (1 - (T23o / T14o)**2)
print(f"A observed T14 {T14o} h, T23 {T23o:.2f} h -> k(from depth) {k:.3f}, b^2 {b2:.3f}")
vA = 2 * np.pi * a / P * (1 + e * np.cos(np.pi / 2 - w)) / np.sqrt(1 - e**2)
R1_needed = T14o / 24 * vA / (2 * (1 + k) * np.sqrt(max(0, 1 - b2 / (1 + k)**2)) ) if b2 < (1+k)**2 else np.nan
print(f"R1 implied by A duration at that b: {R1_needed:.2f} Rsun (TIC 1.576)")
print(f"Gaia e sin w {e*np.sin(w):+.3f}, e cos w {e*np.cos(w):+.3f}; predicted T14_B/T14_A = {(1+e*np.cos(np.pi/2-w))/(1+e*np.cos(1.5*np.pi-w)):.3f}")
