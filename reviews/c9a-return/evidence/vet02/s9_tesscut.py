# TESScut 11x11 cube for one (tic, sector): own aperture photometry, per-event depths, stacked difference
# image (median in-eclipse minus median local out-of-eclipse, per event, averaged), deficit centroid
# (Gaussian fit to the deficit vs to the out-of-eclipse image), per-pixel fractional depth at the target and
# at every G<18 neighbour within 90", and the dilution arithmetic. The cube is deleted at the end.
# usage: python3 -I s9_tesscut.py <tic> <sector>
import sys, os, glob, shutil, json, warnings
import numpy as np
warnings.filterwarnings('ignore')
from astropy.io import fits
from astropy.wcs import WCS
from astropy.coordinates import SkyCoord
import astropy.units as u
from scipy.optimize import curve_fit
tic, sec = sys.argv[1], int(sys.argv[2])
VET = '[local path omitted]'
D = f'/tmp/claude-0/-home-user-eclipses-paper-review/55c92ff4-798a-544f-be03-9888c6804905/scratchpad/data/vet02/{tic}/tesscut_s{sec}'
os.makedirs(D, exist_ok=True)
# ephemerides from s6 (eclipse mid-times only); shapes = median T14/T23 from events_<tic>.csv
EPH = {'470235665': dict(T0=1795.74251, P=10.326180, kinds={'pri': (0.0, 6.44, 2.45), 'sec': (0.52275, 9.00, 2.80)}),
       '379251709': dict(T0=1961.25375, P=12.323912, kinds={'pri': (0.0, 4.15, 1.00), 'sec': (0.4960, 4.2, 0.9)})}
RA = {'470235665': (345.74771690923, 81.69976438579), '379251709': (29.75443908755, 67.54616264314)}  # Gaia DR3
e = EPH[tic]
out = open(f'{VET}/s9_tesscut_{tic}_s{sec}.txt', 'w')
def pr(*a):
    s = ' '.join(str(x) for x in a); print(s, flush=True); out.write(s + '\n')
# ---------- download (skip if present) ----------
f = glob.glob(f'{D}/**/*.fits', recursive=True)
if not f:
    from astroquery.mast import Tesscut
    c = SkyCoord(*RA[tic], unit='deg')
    m = Tesscut.download_cutouts(coordinates=c, size=11, sector=sec, path=D)
    f = glob.glob(f'{D}/**/*.fits', recursive=True)
fn = f[0]; pr('cube', os.path.basename(fn), 'size %.1f MB' % (os.path.getsize(fn) / 1e6))
h = fits.open(fn)
hd0 = h[0].header; d = h[1].data; w = WCS(h[2].header)
pr(f'TIC {tic} sector {sec} camera {hd0.get("CAMERA")} ccd {hd0.get("CCD")}')
t = d['TIME']; F = d['FLUX'].astype(float); q = d['QUALITY']
bk = d['FLUX_BKG'].astype(float) if 'FLUX_BKG' in d.names else None
good = (q == 0) & np.isfinite(t) & np.all(np.isfinite(F.reshape(len(t), -1)), axis=1)
t = t[good]; F = F[good]; bk = bk[good] if bk is not None else None
h.close()
cad = np.median(np.diff(t)); pr(f'frames q==0: {len(t)} cadence {cad*1440:.1f} min span {t.min():.2f}-{t.max():.2f}; FLUX_BKG column present: {bk is not None}')
# extra local background: per-frame median of the faintest 25% of pixels (removes residual sky)
ny, nx = F.shape[1:]
med_img0 = np.median(F, 0)
faint = med_img0 <= np.percentile(med_img0, 25)
sky = np.median(F[:, faint], axis=1)
F = F - sky[:, None, None]
# target and neighbours in pixel coords
x0, y0 = w.world_to_pixel(SkyCoord(*RA[tic], unit='deg'))
x0 = float(x0); y0 = float(y0)
pr(f'target pixel (x,y)=({x0:.2f},{y0:.2f}); residual sky median {np.median(sky):.1f} e/s/pix')
nb = [l.strip().split(',') for l in open('[local path omitted]') if l.startswith(tic + ',')]
stars = []
for r in nb:
    xs, ys = w.world_to_pixel(SkyCoord(float(r[2]), float(r[3]), unit='deg'))
    stars.append(dict(sid=r[1], G=float(r[4]), sep=float(r[9]), x=float(xs), y=float(ys)))
# ---------- eclipse windows ----------
ev = []
for kind, (ph, T14h, T23h) in e['kinds'].items():
    T14 = T14h / 24
    n0 = int(np.floor((t.min() - e['T0']) / e['P'])) - 1; n1 = int(np.ceil((t.max() - e['T0']) / e['P'])) + 1
    for n in range(n0, n1 + 1):
        tc = e['T0'] + (n + ph) * e['P']
        inn = np.abs(t - tc) < 0.3 * T14
        oot = (np.abs(t - tc) > 0.65 * T14) & (np.abs(t - tc) < 0.65 * T14 + 0.5)
        pre = ((t < tc) & oot).sum(); post = ((t > tc) & oot).sum()
        if inn.sum() * cad < 0.45 * 0.6 * T14 or pre * cad < 0.1 or post * cad < 0.1: 
            if np.abs(t - tc).min() < T14: pr(f'  {kind} E{n} tc={tc:.3f}: incomplete coverage, not used')
            continue
        ev.append(dict(kind=kind, n=n, tc=tc, inn=inn, oot=oot, T14=T14, T23=T23h / 24))
pr('usable events:', ', '.join(f'{v["kind"]} E{v["n"]} {v["tc"]:.3f}' for v in ev))
# ---------- per-event difference images ----------
def gauss2d(xy, A, xc, yc, s, c):
    X, Y = xy; return (A * np.exp(-((X - xc) ** 2 + (Y - yc) ** 2) / (2 * s ** 2)) + c).ravel()
Y, X = np.mgrid[0:ny, 0:nx]
def gfit(img, xg, yg):
    p0 = [img.max(), xg, yg, 0.8, 0]
    p, c = curve_fit(gauss2d, (X, Y), img.ravel(), p0=p0, bounds=([0, -2, -2, 0.3, -np.inf], [np.inf, nx + 1, ny + 1, 3, np.inf]), maxfev=20000)
    return p
res = {}
for kind in ['pri', 'sec']:
    E = [v for v in ev if v['kind'] == kind]
    if not E: continue
    diffs = []; oots = []; cents = []
    for v in E:
        oimg = np.median(F[v['oot']], 0); iimg = np.median(F[v['inn']], 0)
        dimg = oimg - iimg  # deficit (positive where flux is lost)
        diffs.append(dimg); oots.append(oimg)
        try:
            p = gfit(dimg, x0, y0); cents.append((p[1], p[2]))
        except Exception: pass
    dimg = np.mean(diffs, 0); oimg = np.mean(oots, 0)
    frac = dimg / np.where(oimg > 0, oimg, np.nan)
    pd_ = gfit(dimg, x0, y0); po = gfit(oimg, x0, y0)
    cents = np.array(cents)
    ecx = np.std(cents[:, 0], ddof=1) / np.sqrt(len(cents)) if len(cents) > 1 else np.nan
    ecy = np.std(cents[:, 1], ddof=1) / np.sqrt(len(cents)) if len(cents) > 1 else np.nan
    off_t = np.hypot(pd_[1] - x0, pd_[2] - y0) * 21.0
    off_o = np.hypot(pd_[1] - po[1], pd_[2] - po[2]) * 21.0
    pk = np.unravel_index(np.nanargmax(dimg), dimg.shape)
    pr(f'[{kind}] N_events={len(E)}  deficit Gaussian centre (x,y)=({pd_[1]:.3f},{pd_[2]:.3f}) sigma={pd_[3]:.2f}px; per-event scatter -> err of mean ({ecx:.3f},{ecy:.3f}) px')
    pr(f'      out-of-eclipse image centre (x,y)=({po[1]:.3f},{po[2]:.3f}) sigma={po[3]:.2f}px')
    pr(f'      offset deficit - target(WCS) = {off_t:.2f}" ; deficit - OOT centroid = {off_o:.2f}" (err ~{21*np.hypot(ecx,ecy):.2f}"); peak deficit pixel (x,y)=({pk[1]},{pk[0]})')
    tx, ty = int(round(x0)), int(round(y0))
    brt = oimg > 0.05 * oimg.max(); fb = np.where(brt, frac, np.nan); kmx = np.unravel_index(np.nanargmax(fb), fb.shape)
    pr(f'      fractional depth at target pixel ({tx},{ty}) = {1e3*frac[ty,tx]:.1f} ppt; max over pixels with OOT flux >5% of peak ({brt.sum()} px) = {1e3*np.nanmax(fb):.1f} ppt at (x,y)=({kmx[1]},{kmx[0]})')
    for s in stars:
        if s['sep'] < 1: continue
        ix, iy = int(round(s['x'])), int(round(s['y']))
        if 0 <= ix < nx and 0 <= iy < ny:
            ddist = np.hypot(s['x'] - pd_[1], s['y'] - pd_[2]) * 21
            pr(f'      neighbour G={s["G"]:.2f} sep={s["sep"]:.1f}" pix=({s["x"]:.2f},{s["y"]:.2f}) frac depth at its pixel = {1e3*frac[iy,ix]:.1f} ppt; distance from deficit centre {ddist:.1f}"')
        else:
            pr(f'      neighbour G={s["G"]:.2f} sep={s["sep"]:.1f}" outside cutout')
    res[kind] = dict(dimg=dimg, oimg=oimg, frac=frac, cen=pd_[1:3], ocen=po[1:3], sig=po[3])
# ---------- aperture photometry ----------
r = np.hypot(X - x0, Y - y0); ap = r <= 1.5
lc = F[:, ap].sum(1); lc = lc / np.median(lc)
pr(f'aperture: r<=1.5 px around target, {ap.sum()} pixels')
# dilution arithmetic with a Gaussian PRF of the width fitted to the OOT image
sig = res['pri']['sig'] if 'pri' in res else 0.8
def frac_in_ap(xs, ys, s=sig):
    # integrate a 2D Gaussian over the aperture pixels on a 10x10 sub-grid per pixel
    sub = (np.arange(10) + 0.5) / 10 - 0.5; tot = 0
    for (iy, ix) in zip(*np.where(ap)):
        gx = ix + sub[None, :]; gy = iy + sub[:, None]
        tot += np.sum(np.exp(-((gx - xs) ** 2 + (gy - ys) ** 2) / (2 * s ** 2))) / 100
    return tot / (2 * np.pi * s ** 2)
fl = []
for s in stars:
    fl.append(10 ** (-0.4 * (s['G'] - stars[0]['G'])) * frac_in_ap(s['x'], s['y']))
fl = np.array(fl); share = fl / fl.sum()
# ---------- per-event aperture depths (trapezoid, shape fixed, quadratic baseline) ----------
def trap(tt, tc, dd, T14, T23):
    x = np.abs(tt - tc); y = np.zeros_like(tt); y[x <= T23 / 2] = dd
    i = (x > T23 / 2) & (x < T14 / 2); y[i] = dd * (T14 / 2 - x[i]) / ((T14 - T23) / 2); return y
ns = 7 if cad > 0.004 else 1; offs = (np.arange(ns) - (ns - 1) / 2) / ns * cad
deps = {}
pr('per-event aperture depths (ppt), shape fixed, tc free, quadratic baseline over +-(0.5*T14+0.4 d):')
for v in ev:
    W = np.abs(t - v['tc']) < 0.5 * v['T14'] + 0.4
    tw = t[W]; fw = lc[W]
    def mdl(tt, tc, dd, c0, c1, c2):
        tr = trap((tt[:, None] + offs[None, :]).ravel(), tc, dd, v['T14'], v['T23']).reshape(len(tt), ns).mean(1)
        dt = tt - v['tc']; return (c0 + c1 * dt + c2 * dt ** 2) * (1 - tr)
    try:
        p, c = curve_fit(mdl, tw, fw, p0=[v['tc'], 0.1 if tic == '470235665' else 0.03, 1, 0, 0], maxfev=20000)
        rs = fw - mdl(tw, *p); s_ = np.std(rs)
        p2, c2 = curve_fit(mdl, tw, fw, p0=p, sigma=np.full(len(tw), s_), absolute_sigma=True, maxfev=20000)
        pr(f'  {v["kind"]} E{v["n"]} tc={p[0]:.5f}+-{np.sqrt(c2[0,0]):.5f} (pred {v["tc"]:.5f}, O-C {1440*(p[0]-v["tc"]):+.1f} min) depth={1e3*p[1]:.2f}+-{1e3*np.sqrt(c2[1,1]):.2f} rms={1e3*s_:.2f}')
        deps.setdefault(v['kind'], []).append((p[1], np.sqrt(c2[1, 1])))
    except Exception as ex:
        pr('  fit fail', v['kind'], v['n'], ex)
pr('dilution arithmetic (aperture r<=1.5 px, Gaussian PRF sigma=%.2f px, fluxes from Gaia G):' % sig)
for kind, L in deps.items():
    dm = np.mean([x[0] for x in L])
    pr(f'  [{kind}] mean aperture depth {1e3*dm:.2f} ppt; target share of aperture flux {share[0]:.4f}')
    ft = frac_in_ap(stars[0]['x'], stars[0]['y'])
    pr(f'     (target fraction of its own flux inside aperture, Gaussian PRF: {ft:.3f}; worst case below puts 100% of the neighbour flux in the aperture)')
    for s, sh in zip(stars[1:], share[1:]):
        need = dm / sh if sh > 0 else np.inf
        fn_ = 10 ** (-0.4 * (s['G'] - stars[0]['G'])); shw = fn_ / (ft + fn_); needw = dm / shw
        pr(f'     G={s["G"]:.2f} sep={s["sep"]:5.1f}": PRF share={sh:.2e} -> required {min(100*need,1e5):.0f}%; worst-case share={shw:.3f} -> required {100*needw:.0f}% {"EXCLUDED" if needw > 1 else "NOT excluded"}')
np.savez_compressed(f'{VET}/s9_tesscut_{tic}_s{sec}.npz', t=t, lc=lc, ap=ap, **{f'{k}_{kk}': vv for k, rr in res.items() for kk, vv in rr.items()})
# small PNG: OOT image, deficit image, fractional depth (primary)
import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
kk = 'pri' if 'pri' in res else list(res)[0]
fig, axs = plt.subplots(1, 3, figsize=(10, 3.4))
for a, img, ttl in zip(axs, [res[kk]['oimg'], res[kk]['dimg'], 1e3 * res[kk]['frac']], ['out of eclipse (e/s)', f'{kk} deficit (OOT - in)', 'fractional depth (ppt)']):
    im = a.imshow(img, origin='lower', cmap='viridis'); plt.colorbar(im, ax=a, fraction=0.046)
    a.plot(x0, y0, 'r+', ms=12, mew=2)
    for s in stars[1:]:
        if -0.5 < s['x'] < nx - 0.5 and -0.5 < s['y'] < ny - 0.5: a.plot(s['x'], s['y'], 'wx', ms=6)
    a.plot(*res[kk]['cen'], 'mo', mfc='none', ms=10)
    a.set_title(ttl, fontsize=9)
fig.suptitle(f'TIC {tic} s{sec}: + target, x Gaia G<18 neighbours, o deficit centre', fontsize=9)
fig.tight_layout(); fig.savefig(f'{VET}/s9_tesscut_{tic}_s{sec}.png', dpi=90)
out.close()
shutil.rmtree(D)  # delete the cube
print('cube deleted')
