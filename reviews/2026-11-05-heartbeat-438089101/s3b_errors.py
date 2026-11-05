"""Step 3b: real errors and robustness for the tide+beam fit on the light-curve ephemeris (beam_Pfree from s3_fit.json).
 (1) bootstrap over orbital passages (200 resamples), (2) jackknife over sectors, (3) emcee over (dtp, dP, e, w, i)
 with bin errors inflated by sqrt(chi2/dof) and the linear terms profiled, (4) Bm fixed at Gaia's K1 (Teff range),
 (5) refit after prewhitening the residual pulsations (per-sector amplitude/phase at fixed global frequencies),
 (6) beaming factor vs Teff, (7) pure-tide fit errors (bootstrap) for the mod-180 comparison.
Writes s3b_out.txt, s3b.json, s3b_chain.npy."""
import os, json
import numpy as np
from lib import *
from fitlib import *

say = say_to(open(os.path.join(OUT, "s3b_out.txt"), "w"))
G = gaia(); P0 = float(G["period"]); sP = float(G["period_error"]); tp0 = G["tp_btjd"]
KG = float(G["semi_amplitude_primary"]); sKG = float(G["semi_amplitude_primary_error"])
J = json.load(open(os.path.join(OUT, "s3_fit.json")))
FAC = J["FAC"]
d = np.load(os.path.join(OUT, "detr.npz"))
t, f, sec = d["t"], d["f"], d["sec"]
EXP = {9: 1800 / 86400, 10: 1800 / 86400, 36: 600 / 86400, 37: 600 / 86400}
B = bin_series(t, f, sec, 0.02, EXP)
best = J["fits"]["beam_Pfree"]; xb = np.array(best["x"])
say(f"start: beam_Pfree e {best['e']:.4f} w {best['w']:.2f} i {best['i']:.1f} P {best['P']:.6f} Bm {best['Bm']:.3e} chi2/dof {best['chi2']/best['dof']:.3f}")

def sub(m):
    return {k: v[m] for k, v in B.items()}

def fit_one(Bd, x0, mode="beam", extra=None):
    M = Model(Bd, tp0, P0, mode=mode, pfree=True, extra=extra)
    # x0 may be on the mirrored branch; try both
    x1 = np.array(x0); x2 = x1.copy(); x2[3] += np.pi
    r = M.fit([list(x1), list(x2)])
    o = M.summary(r.x)
    if o.get("Bm", 0) < 0: o["Bm"] = -o["Bm"]; o["w"] = (o["w"] + 180) % 360
    o["x"] = r.x
    return o

def wrap(w, ref):   # bring w near ref
    return ref + (w - ref + 180) % 360 - 180

keys = ["e", "w", "i", "S", "Bm", "P", "tp"]
# ---- (2) jackknife over sectors ----
jk = []
for s in np.unique(B["sec"]):
    o = fit_one(sub(B["sec"] != s), xb)
    jk.append([o[k] for k in keys]); jk[-1][1] = wrap(jk[-1][1], best["w"])
    say(f"jackknife -s{s:03d}: e {o['e']:.4f} w {jk[-1][1]:.2f} i {o['i']:.1f} S {o['S']:.3e} Bm {o['Bm']:.2e} (K1 {o['Bm']*C_KMS/FAC:.0f}) P {o['P']:.6f}")
jk = np.array(jk); n = len(jk)
sjk = np.sqrt((n - 1) / n * np.sum((jk - jk.mean(0)) ** 2, axis=0))
say("jackknife sigma: " + ", ".join(f"{k} {v:.4g}" for k, v in zip(keys, sjk)))

# ---- each sector alone ----
for s in np.unique(B["sec"]):
    try:
        o = fit_one(sub(B["sec"] == s), xb)
        say(f"sector s{s:03d} alone: e {o['e']:.3f} w {wrap(o['w'], best['w']):.1f} i {o['i']:.1f} S {o['S']:.2e} Bm {o['Bm']:.2e} (K1 {o['Bm']*C_KMS/FAC:.0f})")
    except Exception as ex:
        say("sector alone fail", s, ex)

# ---- (1) bootstrap over passages ----
rng = np.random.default_rng(3)
cyc = np.round((B["t"] - best["tp"]) / best["P"]).astype(int)
ucyc = np.unique(cyc); idx_by = {c: np.where(cyc == c)[0] for c in ucyc}
bs = []
for it in range(200):
    pick = rng.choice(ucyc, len(ucyc))
    ii = np.concatenate([idx_by[c] for c in pick]); ii.sort()
    Bd = {k: v[ii] for k, v in B.items()}
    try:
        o = fit_one(Bd, xb)
        bs.append([o[k] for k in keys]); bs[-1][1] = wrap(bs[-1][1], best["w"])
    except Exception:
        pass
bs = np.array(bs)
sbs = bs.std(0)
say(f"bootstrap over {len(ucyc)} passages, {len(bs)} resamples: " + ", ".join(f"{k} {v:.4g}" for k, v in zip(keys, sbs)))
say("bootstrap 16/50/84: " + "; ".join(f"{k} {np.percentile(bs[:,j],16):.4g}/{np.percentile(bs[:,j],50):.4g}/{np.percentile(bs[:,j],84):.4g}" for j, k in enumerate(keys)))

# ---- (3) emcee ----
import emcee
M = Model(B, tp0, P0, mode="beam", pfree=True)
infl = best["chi2"] / best["dof"]
def lnp(p):
    dtp, dP, e, w, inc = p
    if not (-1.5 < dtp < 1.5 and -0.01 < dP < 0.01 and 0 <= e < 0.8 and 0 < inc < np.pi / 2): return -np.inf
    r = M.solve(p)
    return -0.5 * float(r @ r) / infl
nw, nd = 24, 5
p0 = xb + 1e-4 * rng.standard_normal((nw, nd)) * np.array([1, 0.01, 0.1, 1, 1])
samp = emcee.EnsembleSampler(nw, nd, lnp)
samp.run_mcmc(p0, 1500, progress=False)
ch = samp.get_chain(discard=500, flat=True)
np.save(os.path.join(OUT, "s3b_chain.npy"), ch)
e_c = ch[:, 2]; w_c = np.degrees(ch[:, 3]) % 360; i_c = np.degrees(ch[:, 4]); P_c = P0 + ch[:, 1]; tp_c = tp0 + ch[:, 0]
w_c = wrap(w_c, best["w"])
say(f"emcee (errors x sqrt({infl:.2f})): acceptance {np.mean(samp.acceptance_fraction):.2f}; "
    f"e {np.median(e_c):.4f} +- {np.std(e_c):.4f}; w {np.median(w_c):.2f} +- {np.std(w_c):.2f}; i {np.median(i_c):.1f} +- {np.std(i_c):.1f}; "
    f"P {np.median(P_c):.6f} +- {np.std(P_c):.6f}; tp {np.median(tp_c):.4f} +- {np.std(tp_c):.4f}")
r, coef, cov, X = M.solve(xb, full=True)
say(f"linear terms at best (cov x infl): S {coef[0]:.3e} +- {np.sqrt(cov[0,0]*infl):.1e}; Bm {coef[1]:.3e} +- {np.sqrt(cov[1,1]*infl):.1e}")

# ---- (4) Bm fixed at Gaia's K1: refit everything else ----
fac_T = {T: beaming_factor(T) for T in (6500, 7500, 9000, 10000, 12000, 14000)}
say("beaming factor vs Teff (blackbody, 600-1000 nm photon-weighted): " + ", ".join(f"{T} K {v:.2f}" for T, v in fac_T.items()))
say(f"K1-equivalent of best Bm {best['Bm']:.3e} vs Teff: " + ", ".join(f"{T} K {best['Bm']*C_KMS/v:.0f}" for T, v in fac_T.items()) + " km/s")
for T in (7500, 12000):
    Bfix = fac_T[T] * KG / C_KMS
    Bd = dict(B); Bd = {k: v.copy() for k, v in B.items()}
    # subtract fixed beaming inside the model by modifying y each step is non-linear in shape -> do it via a wrapper
    class MF(Model):
        def solve(self, p, full=False):
            tp, P, e, w, inc = self.unpack(p)
            tid, bm = shapes(self.B, tp, P, e, w, inc)
            X = np.column_stack([tid, self.Xb]); A = X * self.w8[:, None]
            b = (self.B["y"] - Bfix * bm) * self.w8
            c, *_ = np.linalg.lstsq(A, b, rcond=None); rr = b - A @ c
            if full: return rr, c, np.linalg.pinv(A.T @ A), X
            return np.append(rr, 1e3 if c[0] < 0 else 0.0)
    Mf = MF(B, tp0, P0, mode="tide", pfree=True)
    x2 = xb.copy(); x2[3] += np.pi
    rf = Mf.fit([list(xb), list(x2)]); rr, c, _, _ = Mf.solve(rf.x, full=True)
    tp, P, e, w, inc = Mf.unpack(rf.x)
    say(f"Bm FIXED at Gaia K1 x factor({T} K) = {Bfix:.2e}: e {e:.4f} w {np.degrees(w)%360:.2f} i {np.degrees(inc):.1f} chi2 {rr@rr:.0f} "
        f"(free-Bm best {best['chi2']:.0f}; delta {rr@rr-best['chi2']:+.0f})")

# ---- (5) prewhiten residual pulsations, refit ----
r, coef, cov, X = M.solve(xb, full=True)
model_bins = X @ coef
resid_bins = B["y"] - model_bins
from astropy.timeseries import LombScargle
fr = np.linspace(0.3, 24, 120000)
freqs = []
res = resid_bins.copy()
for k in range(6):
    pw = LombScargle(B["t"], res).power(fr)
    fk = fr[np.argmax(pw)]
    freqs.append(fk)
    cols = []
    for fq in freqs:
        for s in np.unique(B["sec"]):
            m = (B["sec"] == s).astype(float)
            cols += [m * np.sin(2 * np.pi * fq * B["t"]), m * np.cos(2 * np.pi * fq * B["t"])]
    Xs = np.array(cols).T
    cc, *_ = np.linalg.lstsq(Xs / B["err"][:, None], resid_bins / B["err"], rcond=None)
    res = resid_bins - Xs @ cc
say("prewhitening frequencies (from 0.02-d bins): " + ", ".join(f"{fq:.4f}" for fq in freqs))
o = fit_one(B, xb, extra=Xs)
say(f"after prewhitening: e {o['e']:.4f} w {wrap(o['w'], best['w']):.2f} i {o['i']:.1f} S {o['S']:.3e} Bm {o['Bm']:.3e} (K1 {o['Bm']*C_KMS/FAC:.1f}) "
    f"P {o['P']:.6f} chi2/dof {o['chi2']/o['dof']:.3f}")

# ---- (7) pure tide bootstrap for mod-180 errors ----
bt = []
xt = np.array(J["fits"]["tide_Pfree"]["x"])
for it in range(100):
    pick = rng.choice(ucyc, len(ucyc))
    ii = np.concatenate([idx_by[c] for c in pick]); ii.sort()
    Bd = {k: v[ii] for k, v in B.items()}
    o = fit_one(Bd, xt, mode="tide")
    bt.append([o["e"], wrap(o["w"] % 180, J["fits"]["tide_Pfree"]["w"] % 180), o["i"]])
bt = np.array(bt)
say(f"pure tide bootstrap (100): e sd {bt[:,0].std():.4f}, w(mod180) sd {bt[:,1].std():.2f}, i sd {bt[:,2].std():.1f}")
json.dump({"jk_sigma": dict(zip(keys, sjk.tolist())), "bs_sigma": dict(zip(keys, sbs.tolist())),
           "emcee": {"e": [float(np.median(e_c)), float(np.std(e_c))], "w": [float(np.median(w_c)), float(np.std(w_c))],
                     "i": [float(np.median(i_c)), float(np.std(i_c))], "P": [float(np.median(P_c)), float(np.std(P_c))],
                     "tp": [float(np.median(tp_c)), float(np.std(tp_c))]},
           "tide_bs": {"e": float(bt[:, 0].std()), "w": float(bt[:, 1].std()), "i": float(bt[:, 2].std())},
           "freqs": freqs, "fac_T": fac_T}, open(os.path.join(OUT, "s3b.json"), "w"), indent=1)
