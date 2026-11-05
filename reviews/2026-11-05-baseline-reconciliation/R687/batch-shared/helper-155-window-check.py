import numpy as np,json
from pathlib import Path
from astropy.io import fits
W=Path(__file__).resolve().parent; S=W.parent/'search256'; p=33.63348396287843
rows=[]
for s in [7,8,34,61,88]:
 f=(S/'followups'/f'155346713_s{s:03d}.fits') if s<10 else (S/'fresh-data'/f'155346713_s{s:03d}.fits')
 with fits.open(f) as h:
  d=h[1].data; t=np.array(d['TIME'],float); q=np.array(d['QUALITY']); y=np.array(d['SAP_FLUX'],float)
 good=np.isfinite(t)&np.isfinite(y)&(y>0)&(q==0); t=t[good]
 for kind,anchor,duration in [('A',3702.3295,1.03),('B',1502.49953,.23)]:
  for n in range(-100,101):
   c=anchor+n*p
   if t.min()-duration<=c<=t.max()+duration:
    near=t[abs(t-c)<duration/2]; inside=np.sort(near)
    gaps=np.diff(np.r_[c-duration/2,inside,c+duration/2]); rows.append(dict(sector=s,kind=kind,cycle=n,predicted_center=c,assumed_duration_days=duration,n_quality_zero=len(near),largest_gap_days=float(max(gaps)),first=float(t.min()),last=float(t.max())))
(W/'helper-155-window-check.json').write_text(json.dumps(rows,indent=2));print(json.dumps(rows,indent=2))
