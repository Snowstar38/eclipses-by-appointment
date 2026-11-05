"""Step 3: Kumar tide and tide + Doppler beaming fitted to the light curve alone, on Gaia's frozen P and on a
light-curve-refit P. Then the per-sector gate: shape frozen at each ephemeris, (S, Bm) refit per sector and per
passage; print the slope of Bm against time FIRST, then constancy. Writes s3_out.txt, s3_fit.json."""
import os, json, sys
import numpy as np
from lib import *
from fitlib import *

say = say_to(open(os.path.join(OUT, "s3_out.txt"), "w"))
G = gaia(); P0 = float(G["period"]); sP = float(G["period_error"]); tp0 = G["tp_btjd"]
eG, seG, wG, swG, KG, sKG = (float(G[k]) for k in ("eccentricity", "eccentricity_error", "arg_periastron",
                                                     "arg_periastron_error", "semi_amplitude_primary", "semi_amplitude_primary_error"))
FAC = beaming_factor(12000.0)
d = np.load(os.path.join(OUT, "detr.npz"))
t, f, sec = d["t"], d["f"], d["sec"]
EXP = {9: 1800 / 86400, 10: 1800 / 86400, 36: 600 / 86400, 37: 600 / 86400}
B = bin_series(t, f, sec, 0.02, EXP)
say(f"{len(B['t'])} bins of 0.02 d from {len(t)} cadences; beaming factor {FAC:.3f} -> expected Bm {FAC*KG/C_KMS:.2e} at Gaia K1")

def canon(o):
    if o.get("Bm", 0) < 0:
        o["Bm"] = -o["Bm"]; o["w"] = (o["w"] + 180) % 360
    return o

res = {}
starts_np = [[dt, 0.27, np.radians(w0), np.radians(i0)] for dt in (-0.6, 0.0) for w0 in (60, 92, 130, 272) for i0 in (40, 65)]
for pfree in (False, True):
    for mode in ("tide", "beam"):
        M = Model(B, tp0, P0, mode=mode, pfree=pfree)
        st = [s[:1] + [-0.0007] + s[1:] for s in starts_np] if pfree else starts_np
        r = M.fit(st)
        o = canon(M.summary(r.x))
        o["x"] = list(r.x)
        tag = f"{mode}_{'Pfree' if pfree else 'Pgaia'}"
        res[tag] = o
        wcmp = (o["w"] - wG + 180) % 360 - 180
        wcmp180 = (o["w"] - wG + 90) % 180 - 90
        s = (f"{tag:12s}: e {o['e']:.4f} ({(o['e']-eG)/seG:+.2f} sig_G)  w {o['w']:.2f} (direct {wcmp:+.1f} = {wcmp/swG:+.2f} sig_G; "
             f"mod180 {wcmp180:+.1f})  i {o['i']:.1f}  S {o['S']:.3e}  P {o['P']:.6f} ({(o['P']-P0)/sP:+.2f} sig_G)  "
             f"tp {o['tp']:.4f} (dtp {o['tp']-tp0:+.3f})  chi2 {o['chi2']:.0f}/{o['dof']} = {o['chi2']/o['dof']:.2f}  BIC {o['bic']:.0f}")
        if mode == "beam":
            s += f"  Bm {o['Bm']:.3e} +- {o['sBm']:.1e} -> K1 {o['Bm']*C_KMS/FAC:.1f} +- {o['sBm']*C_KMS/FAC:.1f} km/s (Gaia {KG:.1f} +- {sKG:.1f})"
        say(s)
for pf in ("Pgaia", "Pfree"):
    say(f"Delta chi2 (tide - beam) on {pf}: {res['tide_'+pf]['chi2']-res['beam_'+pf]['chi2']:.1f}; dBIC {res['tide_'+pf]['bic']-res['beam_'+pf]['bic']:.1f}")

# ---------- per-sector / per-passage gate ----------
def amp_fit(Bsub, tp, P, e, w, inc, baseline="seg"):
    Ms = Model(Bsub, tp, P, mode="beam", baseline=baseline)
    tid, bm = shapes(Bsub, tp, P, e, w, inc)
    Xb = Ms.Xb if baseline == "seg" else design_linear_passage(Bsub, tp, P)
    X = np.column_stack([tid, bm, Xb]); wt = 1 / Bsub["err"]
    A = X * wt[:, None]; b = Bsub["y"] * wt
    c, *_ = np.linalg.lstsq(A, b, rcond=None); cov = np.linalg.pinv(A.T @ A)
    r = b - A @ c
    return c[0], np.sqrt(cov[0, 0]), c[1], np.sqrt(cov[1, 1]), float(r @ r) / max(1, len(r) - X.shape[1])

def sub(Bd, m):
    return {k: v[m] for k, v in Bd.items()}

def const_chi2(v, s):
    wv = 1 / s ** 2; mu = np.sum(v * wv) / np.sum(wv)
    return mu, np.sqrt(1 / np.sum(wv)), float(np.sum((v - mu) ** 2 * wv)), len(v) - 1

gate = {}
for pf in ("Pgaia", "Pfree"):
    o = res["beam_" + pf]
    e, w, inc, tp, P = o["e"], np.radians(o["w"]), np.radians(o["i"]), o["tp"], o["P"]
    for baseline in ("seg", "passage"):
        say(f"\n--- per-sector amplitudes, shape frozen at beam_{pf} (P {P:.6f}), baseline={baseline} ---")
        rows = []
        for s in np.unique(B["sec"]):
            m = B["sec"] == s
            S, sS, Bm, sBm, rc = amp_fit(sub(B, m), tp, P, e, w, inc, baseline)
            rows.append((s, B["t"][m].mean(), S, sS, Bm, sBm, rc))
        rows = np.array(rows)
        # slope of Bm vs time FIRST (errors inflated by sqrt(reduced chi2) of each sector fit)
        tt, Bv, sB = rows[:, 1], rows[:, 4], rows[:, 5] * np.sqrt(np.maximum(rows[:, 6], 1))
        A = np.column_stack([np.ones_like(tt), (tt - tt.mean()) / 1000]) / sB[:, None]
        c, *_ = np.linalg.lstsq(A, Bv / sB, rcond=None); cv = np.linalg.inv(A.T @ A)
        say(f"Bm-vs-time slope: {c[1]:+.2e} +- {np.sqrt(cv[1,1]):.1e} per 1000 d = {c[1]/np.sqrt(cv[1,1]):+.1f} sigma")
        for rr in rows:
            say(f"  s{int(rr[0]):03d}  t {rr[1]:.0f}  S {rr[2]*1e3:.3f} +- {rr[3]*1e3:.3f} ppt  Bm {rr[4]*1e4:+.2f} +- {rr[5]*1e4:.2f} e-4 "
                f"(K1-eq {rr[4]*C_KMS/FAC:+.0f} km/s)  redchi2 {rr[6]:.2f}")
        for lab, j in (("S", 2), ("Bm", 4)):
            mu, smu, chi, dof = const_chi2(rows[:, j], rows[:, j + 1] * np.sqrt(np.maximum(rows[:, 6], 1)))
            say(f"  {lab}: weighted mean {mu:.3e} +- {smu:.1e}; constancy chi2 {chi:.1f}/{dof}" +
                (f"  -> K1 {mu*C_KMS/FAC:.1f} +- {smu*C_KMS/FAC:.1f} km/s" if lab == "Bm" else ""))
        gate[f"{pf}_{baseline}_sector"] = rows.tolist()
        if baseline == "seg":
            # per passage (cycle from periastron; windows tp+-P/2), need >= 70% coverage
            cyc = np.round((B["t"] - tp) / P).astype(int)
            pr = []
            for cnum in np.unique(cyc):
                m = cyc == cnum
                if m.sum() < 0.7 * P / 0.02: continue
                Bs_ = sub(B, m); Bs_["seg"] = np.zeros(m.sum(), int)  # one linear+ baseline per passage
                S, sS, Bm, sBm, rc = amp_fit(Bs_, tp, P, e, w, inc, "passage")
                pr.append((cnum, B["t"][m].mean(), S, sS, Bm, sBm, rc))
            pr = np.array(pr)
            neg = int(np.sum(pr[:, 4] < 0))
            tt, Bv, sB = pr[:, 1], pr[:, 4], pr[:, 5]
            A = np.column_stack([np.ones_like(tt), (tt - tt.mean()) / 1000]) / sB[:, None]
            c, *_ = np.linalg.lstsq(A, Bv / sB, rcond=None); cv = np.linalg.inv(A.T @ A)
            sc_S = np.std(pr[:, 2]) / np.median(pr[:, 3]); sc_B = np.std(pr[:, 4]) / np.median(pr[:, 5])
            say(f"  per passage: {len(pr)} passages, Bm < 0 in {neg}; Bm slope {c[1]:+.2e} +- {np.sqrt(cv[1,1]):.1e}/1000 d "
                f"({c[1]/np.sqrt(cv[1,1]):+.1f} sig, formal); scatter/formal: S {sc_S:.1f}x, Bm {sc_B:.1f}x; "
                f"median S {np.median(pr[:,2])*1e3:.2f} ppt, median Bm {np.median(pr[:,4])*1e4:.2f}e-4, mean Bm {np.mean(pr[:,4])*1e4:.2f} +- {np.std(pr[:,4])/np.sqrt(len(pr))*1e4:.2f}e-4 "
                f"-> K1 {np.mean(pr[:,4])*C_KMS/FAC:.1f} +- {np.std(pr[:,4])/np.sqrt(len(pr))*C_KMS/FAC:.1f}")
            gate[f"{pf}_passage"] = pr.tolist()
json.dump({"fits": res, "gate": gate, "FAC": FAC}, open(os.path.join(OUT, "s3_fit.json"), "w"), indent=1, default=float)
