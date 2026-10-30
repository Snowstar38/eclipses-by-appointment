r"""Pixel attribution from a TESScut FFI cutout, stacking every well-covered eclipse in the sector.
python -X utf8 diffstack.py <tic> <sector> <P> <T0> <T14_h> <depth> [label]
In-eclipse = |t - t_n| < 0.3 T14 (eclipse core); out = 0.75 T14 < |t - t_n| < 1.75 T14 on both sides of the same
event, so slow trends cancel. Per-cadence background = median of the 40% faintest pixels. Output: the
difference image D = out - in, its centroid against the target and against the out-of-eclipse light centroid,
the depth in apertures centred on the target, a least-squares fit D = a * I_out over the central 9x9 pixels
(an eclipse on the target makes D a scaled copy of the target's PSF), and, for every Gaia DR3 neighbour within
60", the eclipse depth it would need to produce the observed dip and the fractional loss at its own pixel.
Reads [local working path omitted; see provenance receipts] and data\gaia.json; writes diff_<label>.json/.png here."""
import json, os, sys
import numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from astropy.io import fits
from astropy.wcs import WCS
HERE = os.getcwd()   # run from the per-tic folder
tic, sec, P, T0 = sys.argv[1], int(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4])
D14, dep = float(sys.argv[5]) / 24, float(sys.argv[6])
lab = sys.argv[7] if len(sys.argv) > 7 else f's{sec:02d}'
cut = os.path.join(r'[local working path omitted; see provenance receipts]', 'vet' + tic, f'tesscut_s{sec:03d}.fits')
with fits.open(cut, memmap=False) as h:
    d = h[1].data; t = np.array(d['TIME'], float); F = np.array(d['FLUX'], float); q = np.array(d['QUALITY'], int)
    wcs = WCS(h[2].header)
G = json.load(open(os.path.join(HERE, 'gaia.json')))
src = G['src'][0]; Gt = float(src['phot_g_mean_mag'])
ok = np.isfinite(t) & np.all(np.isfinite(F.reshape(len(t), -1)), 1) & (q == 0)
t, F = t[ok], F[ok]
ny, nx = F.shape[1:]
flat = F.reshape(len(t), -1); bk = np.array([np.median(np.sort(r)[:int(0.4 * len(r))]) for r in flat])
F = F - bk[:, None, None]
tx, ty = [float(v) for v in wcs.all_world2pix(float(src['ra']), float(src['dec']), 0)]
ix, iy = int(round(tx)), int(round(ty))
cad = np.median(np.diff(t))
evs = []; Dsum = np.zeros((ny, nx)); Osum = np.zeros((ny, nx)); nev = 0
for n in range(int(np.ceil((t.min() - T0) / P)), int(np.floor((t.max() - T0) / P)) + 1):
    tp = T0 + n * P; dt = np.abs(t - tp)
    mi = dt < 0.3 * D14; mo = (dt > 0.75 * D14) & (dt < 1.75 * D14)
    pre = mo & (t < tp); post = mo & (t > tp)
    if mi.sum() * cad < 0.45 * D14 or pre.sum() * cad < 0.5 * D14 or post.sum() * cad < 0.5 * D14: continue
    Iin = np.median(F[mi], 0); Iout = 0.5 * (np.median(F[pre], 0) + np.median(F[post], 0)); Dn = Iout - Iin
    ap = (slice(iy - 1, iy + 2), slice(ix - 1, ix + 2))
    evs.append(dict(cycle=n, t=tp, n_in=int(mi.sum()), n_out=int(mo.sum()), depth_ap3=float(Dn[ap].sum() / Iout[ap].sum())))
    Dsum += Dn; Osum += Iout; nev += 1
if nev == 0: raise SystemExit('no well-covered eclipse in this cutout')
Dm, Om = Dsum / nev, Osum / nev
yy, xx = np.mgrid[:ny, :nx]


def cen(img, cx, cy, r=2):
    m = (np.abs(xx - cx) <= r) & (np.abs(yy - cy) <= r); v = np.clip(img, 0, None) * m
    return float((v * xx).sum() / v.sum()), float((v * yy).sum() / v.sum())


dx, dy = cen(Dm, ix, iy); ox, oy = cen(Om, ix, iy)
pk = np.unravel_index(np.argmax(Dm), Dm.shape)
FR = int(os.environ.get('DIFF_FITR', '4')); m9 = (np.abs(xx - ix) <= FR) & (np.abs(yy - iy) <= FR)
a = float((Dm[m9] * Om[m9]).sum() / (Om[m9] ** 2).sum()); resid = Dm[m9] - a * Om[m9]
frac_resid = float(np.sqrt((resid ** 2).sum() / (Dm[m9] ** 2).sum()))
res = dict(tic=tic, sector=sec, label=lab, n_events=nev, events=evs, target_px=[tx, ty], target_G=Gt,
           light_centroid=[ox, oy], deficit_centroid=[dx, dy],
           deficit_minus_target_px=[dx - tx, dy - ty], deficit_minus_light_px=[dx - ox, dy - oy],
           deficit_minus_light_arcsec=float(np.hypot(dx - ox, dy - oy) * 21.0), peak_deficit_px=[int(pk[1]), int(pk[0])],
           target_pixel=[ix, iy], psf_fit_scale=a, psf_fit_frac_resid=frac_resid)
for r in (0, 1, 2):
    sl = (slice(iy - r, iy + r + 1), slice(ix - r, ix + r + 1)); res[f'depth_ap{2*r+1}'] = float(Dm[sl].sum() / Om[sl].sum())
nbs = []
for r in G['nb'][1:]:
    sep = float(r['sep']); g = r['phot_g_mean_mag']
    if sep > float(os.environ.get('DIFF_RNB', '60')) or not g: continue
    g = float(g); fr = 10 ** (-0.4 * (g - Gt))
    need = dep * (1 + fr) / fr   # eclipse depth the neighbour itself would need, after dilution by the target
    px, py = [float(v) for v in wcs.all_world2pix(float(r['ra']), float(r['dec']), 0)]
    jx, jy = int(round(px)), int(round(py))
    loss = float(Dm[jy, jx] / Om[jy, jx]) if (0 <= jx < nx and 0 <= jy < ny) else None
    nbs.append(dict(source_id=r['source_id'], sep=sep, G=g, depth_needed=need, possible=bool(need <= 1.0),
                    px=[px, py], frac_loss_at_pixel=loss))
res['neighbours_60'] = nbs
res['n_neighbours_60'] = len(nbs); res['n_possible'] = int(sum(x['possible'] for x in nbs))
res['brightest_neighbour_60'] = min(nbs, key=lambda x: x['G']) if nbs else None
res['G_limit_for_depth'] = float(Gt - 2.5 * np.log10(dep))
json.dump(res, open(os.path.join(HERE, f'diff_{lab}.json'), 'w'), indent=1)
print(f"TIC {tic} s{sec}: {nev} eclipses stacked {[e['cycle'] for e in evs]}")
print(f"  target at ({tx:.2f},{ty:.2f}); light centroid ({ox:.2f},{oy:.2f}); deficit centroid ({dx:.2f},{dy:.2f})")
print(f"  deficit - target = ({dx-tx:+.2f},{dy-ty:+.2f}) px; deficit - light = ({dx-ox:+.2f},{dy-oy:+.2f}) px "
      f"= {res['deficit_minus_light_arcsec']:.1f} arcsec")
print(f"  peak deficit pixel {res['peak_deficit_px']} vs target pixel {[ix, iy]}")
print(f"  depth 1x1/3x3/5x5 on target: {res['depth_ap1']*1e3:.2f} / {res['depth_ap3']*1e3:.2f} / {res['depth_ap5']*1e3:.2f} ppt;"
      " per event 3x3: " + ', '.join(f"{e['depth_ap3']*1e3:.1f}" for e in evs))
print(f"  D = a*I_out over 9x9: a = {a*1e3:.2f} ppt, fractional residual {frac_resid:.3f}")
print(f"  neighbours within 60 arcsec: {len(nbs)}; G limit for a {dep*1e3:.1f}-ppt dip: {res['G_limit_for_depth']:.2f}; "
      f"able to make it: {res['n_possible']}")
for x in sorted(nbs, key=lambda x: x['G'])[:6]:
    lo = f"{x['frac_loss_at_pixel']*1e3:+.2f} ppt" if x['frac_loss_at_pixel'] is not None else 'off cutout'
    print(f"    G {x['G']:.2f} sep {x['sep']:.1f} needs depth {x['depth_needed']*100:.0f}%; loss at its pixel {lo}")
fig, ax = plt.subplots(1, 3, figsize=(16, 5.4))
frac = Dm / np.where(Om > 0.01 * Om.max(), Om, np.nan)
for k, (img, ttl) in enumerate(((Om, 'out of eclipse (e-/s)'), (Dm, 'out - in: flux lost (e-/s)'),
                                (frac * 1e3, 'fractional loss (ppt), pixels >1% of peak'))):
    A = ax[k]; im = A.imshow(img, origin='lower', cmap='viridis', interpolation='nearest'); plt.colorbar(im, ax=A, fraction=0.046)
    A.plot(tx, ty, '+', color='red', ms=16, mew=2.2, label=f'target G {Gt:.2f}')
    for x in nbs:
        if x['G'] < 17.5:
            A.plot(*x['px'], 'x', color='white', ms=7, mew=1.3)
            A.annotate(f"{x['G']:.1f}", x['px'], xytext=(3, 3), textcoords='offset points', color='white', fontsize=7)
    A.add_patch(plt.Circle((tx, ty), 60 / 21.0, fill=False, color='orange', ls='--', lw=1))
    A.set_xlim(-0.5, nx - 0.5); A.set_ylim(-0.5, ny - 0.5); A.set_title(ttl, fontsize=10)
ax[1].plot(dx, dy, 'o', mfc='none', mec='magenta', ms=14, mew=2, label='deficit centroid')
ax[1].plot(ox, oy, 's', mfc='none', mec='cyan', ms=10, mew=1.5, label='light centroid')
ax[1].legend(fontsize=7, loc='upper right'); ax[0].legend(fontsize=7, loc='upper right')
fig.suptitle(f"TIC {tic}, TESScut sector {sec}: {nev} eclipses stacked; Gaia DR3 G<17.5 within 60\" marked "
             f"(white x, G labelled; dashed circle = 60\"); deficit centroid {res['deficit_minus_light_arcsec']:.1f}\" "
             f"from the light centroid", fontsize=9)
plt.tight_layout(); plt.savefig(os.path.join(HERE, f'diff_{lab}.png'), dpi=80)

