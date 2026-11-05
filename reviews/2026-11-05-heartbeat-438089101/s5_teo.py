"""Step 5: tidally excited oscillations. Residuals of the tide+beam model (light-curve ephemeris) per cadence.
Amplitude spectra (all data to 24 c/d; 200-s sectors s62-90 to 100 c/d); amplitude and S/N at every exact orbital
harmonic n f_orb; injection-recovery for the limit; the strongest non-harmonic peaks with per-sector amplitude/phase,
frequency in f_orb units with error. Writes s5_out.txt, s5_spec.npz."""
import os, json
import numpy as np
from astropy.timeseries import LombScargle
from lib import *
from fitlib import *

say = say_to(open(os.path.join(OUT, "s5_out.txt"), "w"))
G = gaia(); P0 = float(G["period"]); tp0 = G["tp_btjd"]
J = json.load(open(os.path.join(OUT, "s3_fit.json"))); best = J["fits"]["beam_Pfree"]
d = np.load(os.path.join(OUT, "detr.npz"))
EXP = {9: 1800 / 86400, 10: 1800 / 86400, 36: 600 / 86400, 37: 600 / 86400, 62: 200 / 86400, 63: 200 / 86400, 89: 200 / 86400, 90: 200 / 86400}
U = bin_series(d["t"], d["f"], d["sec"], 1e-6, EXP)
M = Model(U, tp0, P0, mode="beam", pfree=True)
r, coef, cov, X = M.solve(np.array(best["x"]), full=True)
res = U["y"] - X @ coef
t, sec = U["t"], U["sec"]
P = best["P"]; forb = 1 / P
say(f"{len(t)} cadences; residual rms {np.std(res)*1e6:.0f} ppm; f_orb {forb:.6f} c/d (P {P:.6f})")

def ampspec(tt, yy, fr):
    pw = LombScargle(tt, yy, fit_mean=True, center_data=True, normalization="psd").power(fr)
    return np.sqrt(4 * pw / len(tt))

def sinamp(tt, yy, fq):
    A = np.column_stack([np.sin(2 * np.pi * fq * tt), np.cos(2 * np.pi * fq * tt), np.ones_like(tt)])
    c, *_ = np.linalg.lstsq(A, yy, rcond=None)
    return np.hypot(c[0], c[1]), np.degrees(np.arctan2(c[1], c[0])) % 360

m2 = sec >= 62
fr_lo = np.arange(0.05, 24, 0.0002)
fr_hi = np.arange(0.05, 100, 0.0005)
A_all = ampspec(t, res, fr_lo)
A_200 = ampspec(t[m2], res[m2], fr_hi)
np.savez(os.path.join(OUT, "s5_spec.npz"), f_lo=fr_lo, A_all=A_all, f_hi=fr_hi, A_200=A_200, forb=forb)

def peaks(fr, A, k=12, sep=0.01):
    o = np.argsort(A)[::-1]; out = []
    for i in o:
        if all(abs(fr[i] - fr[j]) > sep for j in out): out.append(i)
        if len(out) == k: break
    return out

say("\nTop residual peaks, all sectors (0.05-24 c/d):")
for i in peaks(fr_lo, A_all):
    loc = (np.abs(fr_lo - fr_lo[i]) < 1) & (np.abs(fr_lo - fr_lo[i]) > 0.05)
    say(f"  f {fr_lo[i]:.4f} c/d = {fr_lo[i]/forb:.3f} f_orb  amp {A_all[i]*1e6:.0f} ppm  S/N {A_all[i]/np.median(A_all[loc]):.1f}")
say("Top residual peaks, s62-90 only (0.05-100 c/d):")
for i in peaks(fr_hi, A_200):
    loc = (np.abs(fr_hi - fr_hi[i]) < 1) & (np.abs(fr_hi - fr_hi[i]) > 0.05)
    say(f"  f {fr_hi[i]:.4f} c/d = {fr_hi[i]/forb:.3f} f_orb  amp {A_200[i]*1e6:.0f} ppm  S/N {A_200[i]/np.median(A_200[loc]):.1f}")

# --- prewhiten the strong non-harmonic peaks (iteratively, fixed global freq, global amp) to expose harmonics ---
rw = res.copy(); pw_list = []
for k in range(8):
    A = ampspec(t[m2], rw[m2], fr_hi)
    i = np.argmax(A); fq = fr_hi[i]
    # refine
    fine = np.linspace(fq - 0.001, fq + 0.001, 201)
    fq = fine[np.argmax(ampspec(t, rw, fine))]
    a, ph = sinamp(t, rw, fq)
    if a < 150e-6: break
    Am = np.column_stack([np.sin(2 * np.pi * fq * t), np.cos(2 * np.pi * fq * t)])
    c, *_ = np.linalg.lstsq(Am, rw, rcond=None); rw = rw - Am @ c
    pw_list.append((fq, a))
say("\nprewhitened (amp > 150 ppm): " + ", ".join(f"{fq:.5f} c/d ({fq/forb:.3f} f_orb, {a*1e6:.0f} ppm)" for fq, a in pw_list))

# --- per-sector amplitude and phase of the main non-harmonic peaks; frequency error from the coherent fit ---
for fq, a in pw_list[:4]:
    rows = []
    for s in np.unique(sec):
        mm = sec == s
        aa, pp = sinamp(t[mm], res[mm], fq)
        rows.append(f"s{s}:{aa*1e6:.0f}ppm/{pp:.0f}deg")
    # frequency error: least-squares nonlinear on all data (Montgomery & O'Donoghue 1999)
    T = t.max() - t.min(); sig = np.std(rw)
    sf = np.sqrt(6 / len(t)) * sig / (np.pi * T * a)
    say(f"  {fq:.5f} c/d: n = f/f_orb = {fq/forb:.4f} +- {sf/forb:.4f} (M&O sigma_f {sf:.1e}); per sector: " + " ".join(rows))

# --- exact harmonics ---
say("\nExact orbital harmonics on prewhitened residuals (all data, n <= 115 i.e. < 24 c/d):")
hs = []
for n in range(2, int(24 / forb)):
    fq = n * forb
    a, ph = sinamp(t, rw, fq)
    loc = (np.abs(fr_lo - fq) < 1) & (np.abs(fr_lo - fq) > 0.05)
    noise = np.median(ampspec(t, rw, fr_lo[loc][::10]))
    hs.append((n, a, a / noise, ph))
hs = np.array(hs)
o = np.argsort(hs[:, 2])[::-1][:8]
for j in o:
    n, a, sn, ph = hs[j]
    # coherence: phase in 2019 / 2021 / 2022 / 2024 groups
    grp = {"s9-10": (sec <= 10), "s36-37": (sec >= 36) & (sec <= 37), "s62-63": (sec >= 62) & (sec <= 63), "s89-90": sec >= 89}
    phs = " ".join(f"{g}:{sinamp(t[m], rw[m], n*forb)[0]*1e6:.0f}/{sinamp(t[m], rw[m], n*forb)[1]:.0f}" for g, m in grp.items())
    say(f"  n {int(n):3d}  f {n*forb:.4f}  amp {a*1e6:.1f} ppm  S/N {sn:.1f}  groups(ppm/deg) {phs}")
say(f"  median harmonic amplitude {np.median(hs[:,1])*1e6:.1f} ppm; median S/N {np.median(hs[:,2]):.2f}")

# --- injection-recovery at harmonics ---
rng = np.random.default_rng(9)
say("\nInjection at exact harmonics (into prewhitened residuals):")
for amp in (20e-6, 30e-6, 50e-6):
    sns = []
    for n in rng.choice(np.arange(5, 110), 8, replace=False):
        fq = n * forb
        y = rw + amp * np.sin(2 * np.pi * fq * t + rng.uniform(0, 2 * np.pi))
        a, ph = sinamp(t, y, fq)
        loc = (np.abs(fr_lo - fq) < 1) & (np.abs(fr_lo - fq) > 0.05)
        noise = np.median(ampspec(t, y, fr_lo[loc][::10]))
        sns.append(a / noise)
    say(f"  {amp*1e6:.0f} ppm -> recovered S/N {np.min(sns):.1f}-{np.max(sns):.1f} (median {np.median(sns):.1f})")
