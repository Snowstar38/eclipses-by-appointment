"""Step 2: fold raw QLP SAP on Gaia's ephemeris (phase 0 = Gaia periastron).
Detrending is model-free: iterate {phase-binned template (100 bins) on all data} <-> {per-segment polynomial baseline
of the residual} so the baseline never sees the orbital shape. Segments = continuous runs split at gaps > 0.5 d;
degree = min(3, int(duration / 4 d)).  Writes s2_out.txt, detr.npz, s2_fold.png.
Also: per-sector hump/dip phase and peak-to-trough, Gaia A/B conjunction phases, phase smear, flagged-cadence count,
amplitude spectrum of the template-subtracted light curve (other variability)."""
import os, glob
import numpy as np
from lib import *

say = say_to(open(os.path.join(OUT, "s2_out.txt"), "w"))
G = gaia()
P = float(G["period"]); sP = float(G["period_error"]); tp = G["tp_btjd"]; stp = float(G["t_periastron_error"])
e = float(G["eccentricity"]); w = float(G["arg_periastron"])
say(f"Gaia: P {P:.6f} +- {sP:.6f}, Tp(BTJD) {tp:.4f} +- {stp:.4f}, e {e:.3f}, w {w:.1f}")
pA, pB = conj_phase(e, w, "A"), conj_phase(e, w, "B")
say(f"Gaia conjunction phases after periastron: A {pA:.4f}  B {pB:.4f}")

def segments(t, gap=0.5):
    br = np.where(np.diff(t) > gap)[0]
    return np.split(np.arange(len(t)), br + 1)

data = {}
for p in sorted(glob.glob(os.path.join(DL, "qlp_s*.fits"))):
    s = int(p[-8:-5])
    t, f, q, b = load_qlp(p)
    ta, fa, qa, ba = load_qlp(p, allq=True)
    data[s] = (t, f)
    say(f"s{s:03d}: {len(t)} q=0 cadences of {len(ta)} finite; t {t.min():.2f}-{t.max():.2f}; "
        f"cycles from Gaia Tp {((t.mean()-tp)/P):.0f}; smear n*sP = {((t.mean()-tp)/P)*sP:.3f} d = {((t.mean()-tp)/P)*sP/P:.3f} phase; "
        f"pt-pt rms {np.std(np.diff(f))/np.sqrt(2)*1e6:.0f} ppm; median bkg {np.median(b):.0f}")

T = np.concatenate([data[s][0] for s in data]); F = np.concatenate([data[s][1] for s in data])
SEC = np.concatenate([np.full(len(data[s][0]), s) for s in data])
seg_id = np.zeros(len(T), int); k = 0
for s in data:
    idx = np.where(SEC == s)[0]
    for sg in segments(T[idx]):
        seg_id[idx[sg]] = k; k += 1
say(f"{k} segments")
ph = np.mod((T - tp) / P + 0.5, 1) - 0.5          # -0.5..0.5, periastron at 0
nb = 100
edges = np.linspace(-0.5, 0.5, nb + 1)
base = np.ones_like(F)
for it in range(6):
    y = F / base
    ib = np.clip(np.digitize(ph, edges) - 1, 0, nb - 1)
    tmpl = np.array([np.median(y[ib == i]) if np.any(ib == i) else 1.0 for i in range(nb)])
    tmpl /= np.median(tmpl)
    model = np.interp(ph, 0.5 * (edges[1:] + edges[:-1]), tmpl, period=1.0)
    r = F / model
    for j in range(k):
        m = seg_id == j
        dur = T[m].max() - T[m].min(); deg = int(min(3, dur // 4))
        x = (T[m] - T[m].mean()) / max(dur, 1e-3)
        good = np.ones(m.sum(), bool)
        for _ in range(3):
            c = np.polyfit(x[good], r[m][good], deg)
            res = r[m] - np.polyval(c, x)
            sd = 1.4826 * np.median(np.abs(res[good] - np.median(res[good])))
            good = np.abs(res) < 5 * sd
        base[m] = np.polyval(c, x)
D = F / base - 1
np.savez(os.path.join(OUT, "detr.npz"), t=T, d=D, f=F, base=base, sec=SEC, seg=seg_id)

def shape(phx, y, nbin=60):
    xb, yb, eb, _ = binstat(phx, y, np.linspace(-0.5, 0.5, nbin + 1), minn=5)
    # smooth lightly (3-bin running mean, periodic)
    ys = (np.roll(yb, 1) + yb + np.roll(yb, -1)) / 3
    ih, idp = np.argmax(ys), np.argmin(ys)
    return xb, yb, eb, xb[ih], ys[ih], xb[idp], ys[idp]

say("\nPer-sector fold on Gaia ephemeris (60 bins, 3-bin smoothed; ppt relative to median out-of-pulse):")
say(" sec   hump phase  hump ppt   dip phase  dip ppt   pk-tr ppt   bin err ppm")
rows = {}
for s in list(data) + ["all"]:
    m = np.ones(len(T), bool) if s == "all" else SEC == s
    xb, yb, eb, xh, yh, xd, yd = shape(ph[m], D[m])
    rows[s] = (xb, yb, eb)
    say(f" {str(s):>4}   {xh:+.3f}     {yh*1e3:+.2f}     {xd:+.3f}    {yd*1e3:+.2f}    {(yh-yd)*1e3:.2f}       {np.median(eb)*1e6:.0f}")
# secondary hump (bump-dip-bump): local maxima in the all fold
xb, yb, eb = rows["all"]
ys = (np.roll(yb, 1) + yb + np.roll(yb, -1)) / 3
lm = [i for i in range(len(ys)) if ys[i] > ys[i - 1] and ys[i] >= ys[(i + 1) % len(ys)]]
say("all-fold local maxima (phase, ppt):", [(round(float(xb[i]), 3), round(float(ys[i] * 1e3), 2)) for i in lm])
lmin = [i for i in range(len(ys)) if ys[i] < ys[i - 1] and ys[i] <= ys[(i + 1) % len(ys)]]
say("all-fold local minima (phase, ppt):", [(round(float(xb[i]), 3), round(float(ys[i] * 1e3), 2)) for i in lmin])

# amplitude spectrum of template-subtracted residuals (other variability)
from astropy.timeseries import LombScargle
ib = np.clip(np.digitize(ph, edges) - 1, 0, nb - 1)
tm = np.array([np.mean(D[ib == i]) for i in range(nb)])
R = D - np.interp(ph, 0.5 * (edges[1:] + edges[:-1]), tm, period=1.0)
fr = np.linspace(0.02, 24, 200000)
for lab, m in (("all", np.ones(len(T), bool)), ("s62-90 (200s)", SEC >= 62)):
    pw = LombScargle(T[m], R[m], normalization="psd").power(fr)
    amp = np.sqrt(4 * pw / m.sum())
    top = np.argsort(amp)[::-1]
    picked = []
    for i in top:
        if all(abs(fr[i] - fr[j]) > 0.02 for j in picked): picked.append(i)
        if len(picked) == 8: break
    say(f"\nresidual amplitude spectrum ({lab}), median {np.median(amp)*1e6:.1f} ppm; top peaks:")
    for i in picked:
        say(f"   f {fr[i]:.4f} c/d  = {fr[i]*P:.3f} f_orb   amp {amp[i]*1e6:.0f} ppm")
    if lab == "all":
        np.savez(os.path.join(OUT, "s2_spec.npz"), f=fr, amp=amp)
# raw (undetrended-shape) spectrum: orbital harmonics
pw = LombScargle(T, D, normalization="psd").power(fr)
amp = np.sqrt(4 * pw / len(T))
say("\nraw detrended spectrum at orbital harmonics (ppm):", [(n, round(float(np.interp(n / P, fr, amp) * 1e6))) for n in range(1, 9)])

import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
fig, ax = plt.subplots(3, 3, figsize=(13, 10), sharex=True, sharey=True)
for a, s in zip(ax.flat, list(data) + ["all"]):
    xb, yb, eb = rows[s]
    m = np.ones(len(T), bool) if s == "all" else SEC == s
    if s != "all": a.plot(ph[m], D[m] * 1e3, ",", color="0.7")
    a.errorbar(xb, yb * 1e3, eb * 1e3, fmt="o", ms=3, color="k")
    for x, lab in ((0, "peri"), (pA if pA < 0.5 else pA - 1, "A"), (pB if pB < 0.5 else pB - 1, "B")):
        a.axvline(x, ls=":", color="r"); a.text(x, 6, lab, color="r")
    a.set_title(f"s{s}" if s != "all" else "all"); a.set_ylim(-12, 8)
fig.supxlabel("phase from Gaia periastron"); fig.supylabel("detrended SAP (ppt)")
fig.tight_layout(); fig.savefig(os.path.join(OUT, "s2_fold.png"), dpi=110)
