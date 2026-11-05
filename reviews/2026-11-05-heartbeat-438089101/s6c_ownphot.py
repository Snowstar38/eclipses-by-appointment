"""Step 6c: second pipelines. (1) My own TESScut 3x3-aperture photometry (own_phot.npz from s6b, 8 sectors): full
tide+beam fit with P free, and per-sector (S, Bm) at the frozen shape. (2) TGLC, GSFC-ELEANOR-LITE, T16 for s9/s10:
per-sector S, Bm at the frozen shape (QLP-fit ephemeris). The strong on-target p modes (13.609, 12.811, 13.646) and the
neighbour's 4.471 c/d are prewhitened per sector as extra linear columns. Writes s6c_out.txt."""
import os, json, glob
import numpy as np
from astropy.io import fits
from lib import *
from fitlib import *

say = say_to(open(os.path.join(OUT, "s6c_out.txt"), "w"))
G = gaia(); P0 = float(G["period"]); tp0 = G["tp_btjd"]; KG = float(G["semi_amplitude_primary"])
J = json.load(open(os.path.join(OUT, "s3_fit.json"))); best = J["fits"]["beam_Pfree"]; FAC = J["FAC"]
fr = [4.47108, 13.60915, 12.81149, 13.64614]
def sincols(B):
    cols = []
    for f in fr:
        for s in np.unique(B["sec"]):
            m = (B["sec"] == s).astype(float)
            cols += [m * np.sin(2 * np.pi * f * B["t"]), m * np.cos(2 * np.pi * f * B["t"])]
    return np.array(cols).T

o = np.load(os.path.join(OUT, "own_phot.npz"))
secs = sorted(int(k[1:]) for k in o.files if k.startswith("t"))
t = np.concatenate([o[f"t{s}"] for s in secs]); f = np.concatenate([o[f"f{s}"] for s in secs])
sec = np.concatenate([np.full(len(o[f"t{s}"]), s) for s in secs])
EXP = {9: 1800 / 86400, 10: 1800 / 86400, 36: 600 / 86400, 37: 600 / 86400}
B = bin_series(t, f, sec, 0.02, EXP)
x0 = np.array(best["x"])
for mode in ("tide", "beam"):
    M = Model(B, tp0, P0, mode=mode, pfree=True, extra=sincols(B))
    x2 = x0.copy(); x2[3] += np.pi
    r = M.fit([list(x0), list(x2)])
    s_ = M.summary(r.x)
    if s_.get("Bm", 0) < 0: s_["Bm"] = -s_["Bm"]; s_["w"] = (s_["w"] + 180) % 360
    say(f"OWN 3x3 photometry, {mode}: e {s_['e']:.4f} w {s_['w']:.2f} i {s_['i']:.1f} S {s_['S']:.3e} P {s_['P']:.6f} tp {s_['tp']:.4f} "
        f"chi2/dof {s_['chi2']/s_['dof']:.2f}" + (f" Bm {s_['Bm']:.2e} +- {s_['sBm']:.1e} (K1-eq {s_['Bm']*C_KMS/FAC:.0f} at 12000 K)" if mode == "beam" else ""))
    if mode == "beam": own_best = s_

def persec(B, lab, shape):
    e, w, inc, tp, P = shape
    rows = []
    for s in np.unique(B["sec"]):
        m = B["sec"] == s
        Bs = {k: v[m] for k, v in B.items()}
        tid, bm = shapes(Bs, tp, P, e, w, inc)
        Xb = design_baseline(Bs)
        X = np.column_stack([tid, bm, Xb, sincols(Bs)]); wt = 1 / Bs["err"]
        A = X * wt[:, None]; c, *_ = np.linalg.lstsq(A, Bs["y"] * wt, rcond=None)
        cov = np.linalg.pinv(A.T @ A); rr = Bs["y"] * wt - A @ c; rc = float(rr @ rr) / (len(rr) - X.shape[1])
        rows.append((s, c[0], np.sqrt(cov[0, 0] * max(rc, 1)), c[1], np.sqrt(cov[1, 1] * max(rc, 1))))
        say(f"  {lab} s{s:03d}: S {c[0]*1e3:.3f} +- {np.sqrt(cov[0,0]*max(rc,1))*1e3:.3f} ppt  Bm {c[1]*1e4:+.2f} +- {np.sqrt(cov[1,1]*max(rc,1))*1e4:.2f} e-4  redchi2 {rc:.2f}")
    rows = np.array(rows)
    for j, nm in ((1, "S"), (3, "Bm")):
        wv = 1 / rows[:, j + 1] ** 2; mu = np.sum(rows[:, j] * wv) / wv.sum()
        say(f"  {lab} {nm}: mean {mu:.3e} +- {1/np.sqrt(wv.sum()):.1e}, constancy chi2 {np.sum((rows[:, j]-mu)**2*wv):.1f}/{len(rows)-1}")
    return rows

shapeQ = (best["e"], np.radians(best["w"]), np.radians(best["i"]), best["tp"], best["P"])
say("\nPer-sector amplitudes, own photometry, shape frozen at the QLP beam_Pfree fit:")
persec(B, "own", shapeQ)

say("\nOther pipelines s9/s10 (shape frozen at QLP beam_Pfree):")
for tag, col, tcol in (("tglc", "cal_aper_flux", "time"), ("tglc", "cal_psf_flux", "time"), ("eleanor", "CORR_FLUX", "TIME"),
                       ("eleanor", "RAW_FLUX", "TIME"), ("t16", None, None)):
    T, F, S_ = [], [], []
    for s in (9, 10):
        p = os.path.join(DL, f"{tag}_s{s:03d}.fits")
        if not os.path.exists(p): continue
        with fits.open(p) as h:
            dd = h[1].data; names = [n.lower() for n in dd.columns.names]
            if col is None:
                # T16: pick the first flux-like column
                cand = [n for n in dd.columns.names if "FLUX" in n.upper() or "MAG" in n.upper()]
                c_ = cand[0] if cand else None; tc = [n for n in dd.columns.names if n.upper() in ("TIME", "BTJD", "TBJD")]
                if c_ is None or not tc: say(f"  {tag}: columns {dd.columns.names}"); continue
                cc, tt_ = c_, tc[0]
            else:
                cc = [n for n in dd.columns.names if n.lower() == col.lower()]; tt_ = [n for n in dd.columns.names if n.lower() == tcol.lower()]
                if not cc or not tt_: say(f"  {tag}: no {col}; columns {dd.columns.names}"); continue
                cc, tt_ = cc[0], tt_[0]
            tq = np.array(dd[tt_], float); fq = np.array(dd[cc], float)
            qn = [n for n in dd.columns.names if n.upper() in ("QUALITY", "TESS_FLAGS", "TGLC_FLAGS")]
            ok = np.isfinite(tq) & np.isfinite(fq)
            for qq in qn: ok &= (np.array(dd[qq]) == 0)
            if "MAG" in cc.upper(): fq = 10 ** (-0.4 * (fq - np.nanmedian(fq[ok])))
            ok &= fq > 0
            if ok.sum() < 100: say(f"  {tag} s{s} {cc}: only {ok.sum()} good points"); continue
            T.append(tq[ok]); F.append(fq[ok] / np.median(fq[ok])); S_.append(np.full(ok.sum(), s))
            lab = f"{tag}:{cc}"
    if not T: continue
    Bx = bin_series(np.concatenate(T), np.concatenate(F), np.concatenate(S_), 0.02, EXP)
    persec(Bx, lab, shapeQ)
