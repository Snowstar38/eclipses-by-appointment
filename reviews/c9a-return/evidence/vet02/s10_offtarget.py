# From the s9 stacked images: (a) deficit vs out-of-eclipse flux at the brightest pixels more than 3 px from
# the target (bright stars beyond 90" at the cutout edges), (b) summed fractional depth of all pixels r>3 px
# (local common-mode check), (c) share of the total deficit inside r<=1.5 px vs share of the OOT flux.
import numpy as np, glob, re
for fn in sorted(glob.glob('s9_tesscut_*_s*.npz')):
    tic, sec = re.findall(r's9_tesscut_(\d+)_s(\d+)', fn)[0]
    z = np.load(fn)
    for k in ['pri', 'sec']:
        if f'{k}_dimg' not in z: continue
        d = z[f'{k}_dimg']; o = z[f'{k}_oimg']; cx, cy = z[f'{k}_ocen']
        Y, X = np.mgrid[0:d.shape[0], 0:d.shape[1]]; r = np.hypot(X - cx, Y - cy)
        far = r > 3
        idx = np.argsort(np.where(far, o, -np.inf).ravel())[::-1][:3]
        s = ', '.join(f'({i % d.shape[1]},{i // d.shape[1]}) OOT={o.ravel()[i]:.0f} deficit={d.ravel()[i]:+.2f} e/s ({1e3*d.ravel()[i]/o.ravel()[i]:+.1f} ppt)' for i in idx)
        inner = r <= 1.5
        print(f'TIC {tic} s{sec} [{k}]: brightest far pixels: {s}')
        print(f'      sum over r>3 px: deficit {d[far].sum():+.1f} e/s of OOT {o[far].sum():.0f} e/s -> {1e3*d[far].sum()/o[far].sum():+.2f} ppt;'
              f'  r<=1.5 px holds {100*d[inner].sum()/d.sum():.1f}% of the total deficit and {100*o[inner].sum()/o.sum():.1f}% of the OOT flux')
