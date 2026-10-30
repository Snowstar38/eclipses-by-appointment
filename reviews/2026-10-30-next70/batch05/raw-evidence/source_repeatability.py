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
Ds=[]; evs = []; Dsum = np.zeros((ny, nx)); Osum = np.zeros((ny, nx)); nev = 0
for n in range(int(np.ceil((t.min() - T0) / P)), int(np.floor((t.max() - T0) / P)) + 1):
    tp = T0 + n * P; dt = np.abs(t - tp)
    mi = dt < 0.3 * D14; mo = (dt > 0.75 * D14) & (dt < 1.75 * D14)
    pre = mo & (t < tp); post = mo & (t > tp)
    if mi.sum() * cad < 0.45 * D14 or pre.sum() * cad < 0.5 * D14 or post.sum() * cad < 0.5 * D14: continue
    Iin = np.median(F[mi], 0); Iout = 0.5 * (np.median(F[pre], 0) + np.median(F[post], 0)); Dn = Iout - Iin
    ap = (slice(iy - 1, iy + 2), slice(ix - 1, ix + 2))
    evs.append(dict(cycle=n, t=tp, n_in=int(mi.sum()), n_out=int(mo.sum()), depth_ap3=float(Dn[ap].sum() / Iout[ap].sum())))
    Ds.append(Dn); Dsum += Dn; Osum += Iout; nev += 1
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

nb=json.load(open('diff_s97.json'))['brightest_neighbour_60']; nx0,ny0=nb['px']; measures=[]
for label,images in [('first_half',Ds[:len(Ds)//2]),('second_half',Ds[len(Ds)//2:])]+[(f'event_{i}',[x]) for i,x in enumerate(Ds)]:
 im=np.mean(images,axis=0);cx,cy=cen(im,ix,iy);measures.append(dict(label=label,n_events=len(images),centroid=[cx,cy],target_distance_arcsec=21*np.hypot(cx-tx,cy-ty),neighbour_distance_arcsec=21*np.hypot(cx-nx0,cy-ny0)))
from scipy.ndimage import shift
fits0={}
for label,pos in [('target',(tx,ty)),('neighbour',(nx0,ny0))]:
 template=shift(Om,(pos[1]-oy,pos[0]-ox),order=3);amp=np.sum(Dm[m9]*template[m9])/np.sum(template[m9]**2);fits0[label]=float(np.linalg.norm(Dm[m9]-amp*template[m9])/np.linalg.norm(Dm[m9]))
import hashlib
out=dict(tic=tic,sector=sec,input_cutout=cut,input_sha256=hashlib.sha256(open(cut,'rb').read()).hexdigest(),target_px=[tx,ty],neighbour=nb,measurements=measures,shifted_empirical_template_fractional_residual=fits0,note='Existing diffstack primitives; split-stack repeatability and shifted blended out-of-eclipse image diagnostic, not calibrated PRF likelihood; own-pixel mixed flux is not an exclusion.')
json.dump(out,open('source_repeatability.json','w'),indent=2);print(out)
