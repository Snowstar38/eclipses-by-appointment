import numpy as np, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt,json
from pathlib import Path
from astropy.io import fits
W=Path(__file__).resolve().parent; S=W.parent/'search256'/'fresh-data'; P=41.804020454205606; anchor=3380.391
fig,ax=plt.subplots(7,1,figsize=(12,15)); out=[]
for a,s in zip(ax,[15,55,56,75,76,82,83]):
 f=W/f'helper-167197264_s{s:03d}.fits' if s<76 else S/f'167197264_s{s:03d}.fits'
 with fits.open(f) as h:
  d=h[1].data; t=np.array(d['TIME'],float); y=np.array(d['SAP_FLUX'],float); q=np.array(d['QUALITY'])
 m=np.isfinite(t)&np.isfinite(y)&(y>0)&(q==0); t=t[m];y=y[m]; y=y/np.median(y);a.plot(t,y,'.',ms=1)
 for n in range(-100,100):
  c=anchor+n*P
  if t.min()-1<c<t.max()+1:
   a.axvline(c,c='r'); sub=np.abs(t-c)<.75; out.append(dict(sector=s,cycle=n,predicted_center=c,n=int(sub.sum()),min=float(y[sub].min()) if sub.any() else None,maximum_gap=float(max(np.diff(np.r_[c-.75,np.sort(t[sub]),c+.75])))))
 a.set_title(f's{s}');a.grid();
fig.tight_layout();fig.savefig(W/'helper-167-all.png',dpi=150); (W/'helper-167-windows.json').write_text(json.dumps(out,indent=2)); print(json.dumps(out,indent=2))
