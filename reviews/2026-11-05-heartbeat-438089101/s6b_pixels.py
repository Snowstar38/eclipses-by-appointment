"""Step 6b: pixel attribution on TESScut 21x21 cutouts, all nine sectors (incl. s35, which QLP lacks).
Per-pixel linear regression of the background-subtracted flux on: the heartbeat template H(t) (best tide+beam model on
the light-curve ephemeris, unit = fractional signal of the target), the tide and beaming shapes separately, sinusoid
pairs at the strong p modes (4.47108, 13.60915, 12.81149, 13.64614 c/d) and at the exact harmonics n = 69 and 74,
and per-segment cubic baselines. For each signal: coefficient map; a 2-D Gaussian (free centre, width, offset) fitted
to the map -> centre offset from the target (arcsec) and from the nearest bright neighbours; fractional amplitude in
1x1 / 3x3 / 5x5 apertures centred on the target. Signed amplitudes for sinusoids are projected on the phase of the
3x3 aperture sum. Also writes the 3x3-aperture light curve per sector (own photometry) to own_phot.npz.
Writes s6b_out.txt, s6b_maps.npz, s6b_maps_<sec>.png."""
import os, glob, json
import numpy as np
from astropy.io import fits
from astropy.wcs import WCS
from scipy.optimize import least_squares
from lib import *
from fitlib import segments

say = say_to(open(os.path.join(OUT, "s6b_out.txt"), "w"))
G = gaia(); J = json.load(open(os.path.join(OUT, "s3_fit.json"))); best = J["fits"]["beam_Pfree"]
P, tp, e, w, inc = best["P"], best["tp"], best["e"], np.radians(best["w"]), np.radians(best["i"])
S0, Bm0 = best["S"], best["Bm"]
NB = json.load(open(os.path.join(OUT, "neighbours.json")))
forb = 1 / P
FREQS = {"f4.471": 4.47108, "f13.609": 13.60915, "f12.811": 12.81149, "f13.646": 13.64614, "n69": 69 * forb, "n74": 74 * forb}
TC = os.path.join(DL, "tesscut")
allmaps = {}
own = {}
for sdir in sorted(glob.glob(os.path.join(TC, "s00*"))):
    if not os.path.isdir(sdir): continue
    sec = int(os.path.basename(sdir)[1:])
    fn = glob.glob(os.path.join(sdir, "*.fits"))[0]
    with fits.open(fn) as h:
        d = h[1].data; hdr2 = h[2].header
        t = np.array(d["TIME"], float); F = np.array(d["FLUX"], float); q = np.array(d["QUALITY"], int)
    wcs = WCS(hdr2)
    m = np.isfinite(t) & (q == 0) & np.all(np.isfinite(F.reshape(len(t), -1)), axis=1)
    say(f"\ns{sec:03d}: {len(t)} cadences in cutout, {m.sum()} usable (q==0, finite); quality values {np.unique(q)[:8]}")
    if np.nanmax(np.abs(np.nanmedian(F, axis=0)[8:13, 8:13])) < 1:
        say("   cutout is all zeros: the star is off the science pixels in this sector (why QLP has none) -> skipped")
        continue
    if m.sum() < 100:
        m = np.isfinite(t) & np.all(np.isfinite(F.reshape(len(t), -1)), axis=1) & (np.nansum(F.reshape(len(t), -1), axis=1) != 0)
        say(f"   too few q==0; with any quality: {m.sum()}")
        if m.sum() < 100: continue
    t, F = t[m], F[m]
    ny, nx = F.shape[1:]
    # background per cadence: median of the faintest 25% of pixels (crowded field: biased high, but common to all pixels)
    flat = F.reshape(len(t), -1)
    med_img = np.median(F, axis=0)
    faint = med_img.ravel() <= np.percentile(med_img, 25)
    bkg = np.median(flat[:, faint], axis=1)
    # reject the worst scattered-light cadences
    okb = bkg < np.percentile(bkg, 95)
    t, flat, bkg = t[okb], flat[okb], bkg[okb]
    order = np.argsort(t); t, flat, bkg = t[order], flat[order], bkg[order]
    keep = np.zeros(len(t), bool)
    for sg in segments(t):
        if len(sg) >= 20: keep[sg] = True
    t, flat, bkg = t[keep], flat[keep], bkg[keep]
    Y = flat - bkg[:, None]
    img = np.median(Y, axis=0).reshape(ny, nx)
    x0, y0 = wcs.world_to_pixel_values(RA, DEC)
    # regressors
    nu = true_anom(t, tp, P, e); R = (1 - e * e) / (1 + e * np.cos(nu))
    tid = (1 - 3 * np.sin(inc) ** 2 * np.sin(nu + w) ** 2) / R ** 3
    bm = -(np.cos(nu + w) + e * np.cos(w))
    H = S0 * tid + Bm0 * bm
    cols = [S0 * tid, Bm0 * bm]
    names = ["tide", "beam"]
    for k, fq in FREQS.items():
        cols += [np.sin(2 * np.pi * fq * t), np.cos(2 * np.pi * fq * t)]; names += [k + "_s", k + "_c"]
    nsig = len(cols)
    for sg in segments(t):
        dur = t[sg].max() - t[sg].min(); xx = np.zeros(len(t)); xx[sg] = (t[sg] - t[sg].mean()) / max(dur, 1e-3) * 2
        for dd in range(4):
            c = np.zeros(len(t)); c[sg] = xx[sg] ** dd; cols.append(c)
    X = np.column_stack(cols)
    C, *_ = np.linalg.lstsq(X, Y, rcond=None)           # (ncols, npix)
    resid = Y - X @ C
    sig = np.std(resid, axis=0)
    cov = np.linalg.pinv(X.T @ X)
    E = np.sqrt(np.outer(np.diag(cov)[:nsig], sig ** 2))  # coefficient errors per pixel
    maps = {"img": img}
    maps["hb"] = (C[0] + C[1]).reshape(ny, nx)           # unit-template amplitude (e-/s per unit of target fraction)
    maps["tide"] = C[0].reshape(ny, nx); maps["beam"] = C[1].reshape(ny, nx)
    maps["tide_err"] = E[0].reshape(ny, nx); maps["beam_err"] = E[1].reshape(ny, nx)
    ix, iy = int(round(float(x0))), int(round(float(y0)))
    def ap(arr, r):
        return arr[iy - r:iy + r + 1, ix - r:ix + r + 1].sum()
    for k in FREQS:
        js, jc = names.index(k + "_s"), names.index(k + "_c")
        a_s, a_c = C[js].reshape(ny, nx), C[jc].reshape(ny, nx)
        ph = np.arctan2(ap(a_c, 1), ap(a_s, 1))
        maps[k] = a_s * np.cos(ph) + a_c * np.sin(ph)      # signed amplitude along the aperture's phase
        maps[k + "_err"] = E[js].reshape(ny, nx)
    allmaps[sec] = maps
    # own photometry: 3x3 aperture, local background already removed
    lc = Y.reshape(len(t), ny, nx)[:, iy - 1:iy + 2, ix - 1:ix + 2].sum(axis=(1, 2))
    own[sec] = (t, lc / np.median(lc))
    say(f"\n=== s{sec:03d}: {len(t)} cadences; target at pixel ({float(x0):.2f}, {float(y0):.2f}); median bkg {np.median(bkg):.0f} e/s")
    # Gaussian fit to each signal map in a 7x7 box around the target
    yy, xx = np.mgrid[0:ny, 0:nx]
    box = (np.abs(xx - ix) <= 3) & (np.abs(yy - iy) <= 3)
    def gfit(mp, er):
        def rf(p):
            A, xc, yc, s, c0 = p
            mdl = A * np.exp(-((xx - xc) ** 2 + (yy - yc) ** 2) / (2 * s * s)) + c0
            return ((mp - mdl) / er)[box]
        p0 = [mp[iy, ix], ix, iy, 0.8, 0.0]
        r = least_squares(rf, p0, bounds=([-np.inf, ix - 3, iy - 3, 0.3, -np.inf], [np.inf, ix + 3, iy + 3, 3.0, np.inf]))
        Jm = r.jac; cv = np.linalg.pinv(Jm.T @ Jm) * max(1, 2 * r.cost / (box.sum() - 5))
        return r.x, np.sqrt(np.diag(cv))
    # image PSF reference: Gaussian fit to the median image itself
    pim, _ = gfit(img, np.sqrt(np.abs(img)) + 1)
    say(f"  median image Gaussian centre offset from target: {np.hypot(pim[1]-float(x0), pim[2]-float(y0))*21:.1f}\" (sigma {pim[3]:.2f} px)")
    for k in ["tide", "beam"] + list(FREQS):
        mp = maps[k]; er = maps[k + "_err"] if k + "_err" in maps else maps["tide_err"]
        frac = {r: ap(mp, r) / ap(img, r) for r in (0, 1, 2)}
        if k == "tide": frac = {r: v * S0 for r, v in frac.items()}
        if k == "beam": frac = {r: v * Bm0 for r, v in frac.items()}
        snr = ap(mp, 1) / np.sqrt((er[iy - 1:iy + 2, ix - 1:ix + 2] ** 2).sum())
        try:
            pg, eg = gfit(mp, er)
            off = np.hypot(pg[1] - float(x0), pg[2] - float(y0)) * 21; soff = np.hypot(eg[1], eg[2]) * 21
            # nearest bright neighbours to the fitted centre
            cen_w = wcs.pixel_to_world_values(pg[1], pg[2])
            dmin = sorted(((np.hypot((float(n["ra"]) - cen_w[0]) * np.cos(np.radians(DEC)), float(n["dec"]) - cen_w[1]) * 3600, n["g"], n["source_id"])
                           for n in NB if n["g"] < 17.5), key=lambda z: z[0])[:2]
            gs = f"Gaussian centre {off:.1f} +- {soff:.1f}\" from target (sigma {pg[3]:.2f} px); nearest G<17.5 to centre: " + \
                 ", ".join(f"G{g:.1f}@{dd:.1f}\"{' (TARGET)' if sid == GAIA_ID else ''}" for dd, g, sid in dmin)
        except Exception as ex:
            gs = f"gfit fail {ex}"
        unit = "" if k in ("tide", "beam") else " (amplitude)"
        say(f"  {k:8s}: frac 1x1 {frac[0]*1e3:+.3f} 3x3 {frac[1]*1e3:+.3f} 5x5 {frac[2]*1e3:+.3f} ppt{unit}; 3x3 S/N {snr:.1f}; {gs}")
np.savez(os.path.join(OUT, "own_phot.npz"), **{f"t{s}": v[0] for s, v in own.items()}, **{f"f{s}": v[1] for s, v in own.items()})
np.savez(os.path.join(OUT, "s6b_maps.npz"), **{f"s{s}_{k}": v for s, mp in allmaps.items() for k, v in mp.items()})

import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
for sec, mp in allmaps.items():
    keys = ["img", "tide", "beam", "f4.471", "f13.609", "n69", "n74"]
    fig, ax = plt.subplots(1, len(keys), figsize=(3 * len(keys), 3.2))
    for a, k in zip(ax, keys):
        v = mp[k]
        a.imshow(v, origin="lower", cmap="viridis" if k == "img" else "RdBu_r",
                 vmin=None if k == "img" else -np.nanmax(np.abs(v)), vmax=None if k == "img" else np.nanmax(np.abs(v)))
        a.plot(10, 10, "k+", ms=10); a.set_title(f"s{sec} {k}"); a.set_xticks([]); a.set_yticks([])
    fig.tight_layout(); fig.savefig(os.path.join(OUT, f"s6b_maps_{sec:03d}.png"), dpi=80); plt.close(fig)
