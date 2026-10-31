"""Common-mode test: for every other star in the shared folder observed in the same sector and within 8 deg of the target,
dip = median(baseline) - median(window) in raw QLP SAP_FLUX (q==0); is the target's value unusual? python commonmode.py"""
import json, glob, numpy as np
from astropy.io import fits
D='[local path omitted]'; T=json.load(open(D+'targets.json'))
ra0,de0=4.33833807641,-17.68085326713
def sep(r,d): return np.degrees(np.arccos(np.clip(np.sin(np.radians(de0))*np.sin(np.radians(d))+np.cos(np.radians(de0))*np.cos(np.radians(d))*np.cos(np.radians(r-ra0)),-1,1)))
TESTS=[(69,(3196.02,3196.18),[(3195.5,3195.9),(3196.3,3196.7)],'s69 B 3196.10'),
       (69,(3204.03,3204.17),[(3203.5,3203.9),(3204.3,3204.7)],'s69 A 3204.10')]
for s,(a,b),base,lab in TESTS:
    vals=[]; tv=None
    for fn in glob.glob(D+f'*_s{s:03d}.fits'):
        tic=__import__('os').path.basename(fn).split('_')[0]
        if tic not in T: continue
        if sep(T[tic]['ra'],T[tic]['dec'])>8: continue
        try: d=fits.open(fn)[1].data
        except Exception: continue
        t=d['TIME']; f=d['SAP_FLUX']; q=d['QUALITY']; ok=np.isfinite(t)&np.isfinite(f)&(q==0)
        w=ok&(t>a)&(t<b); bb=ok&np.any([(t>x)&(t<y) for x,y in base],axis=0)
        if w.sum()<5 or bb.sum()<20: continue
        dip=(np.median(f[bb])-np.median(f[w]))/np.median(f[bb])
        if tic=='12864953': tv=dip
        else: vals.append(dip)
    v=np.array(vals)
    print(f'{lab}: {len(v)} neighbours-in-sky; their dip median {np.median(v)*100:+.3f}%  16-84% {np.percentile(v,16)*100:+.3f}..{np.percentile(v,84)*100:+.3f}%  frac >= 0.1%: {np.mean(v>=0.001):.2f}; target {tv*100 if tv is not None else float("nan"):+.3f}%  (target rank {np.mean(v<(tv or 0)):.2f})')
