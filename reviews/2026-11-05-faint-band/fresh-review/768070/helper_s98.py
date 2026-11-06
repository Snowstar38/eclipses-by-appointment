from astropy.io import fits
from astropy.wcs import WCS
import numpy as np,json,matplotlib;matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path
B=Path(__file__).resolve().parent;p=B/'lead-extra-s98.fits'
with fits.open(p) as h:
 a=h[1].data;t=np.array(a['TIME']);q=np.array(a['QUALITY']);f=np.array(a['FLUX']);w=WCS(h[2].header);xy=w.all_world2pix([[74.7622014277498,-28.8916285368164]],0)[0]
ok=(q==0)&np.isfinite(t);inn=ok&(t>4038.49)&(t<4038.59);base=ok&(t>4038.1)&(t<4038.35); diff=np.median(f[base],axis=0)-np.median(f[inn],axis=0);med=np.median(f[base],axis=0)
fig,ax=plt.subplots(1,2,figsize=(9,4))
for a,data in zip(ax,[med,diff]):
 im=a.imshow(data,origin='lower');fig.colorbar(im,ax=a);a.plot(*xy,'rx',ms=12);a.set_xticks(range(5));a.set_yticks(range(5));a.grid(alpha=.3)
ax[0].set_title('S98 baseline');ax[1].set_title('baseline minus low interval');fig.tight_layout();fig.savefig(B/'helper-diff-s98.png',dpi=150)
local=t[ok&(t>4038.2)&(t<4039.0)];g=np.diff(local);i=np.argmax(g)
r=dict(target_xy=xy.tolist(),peak_xy=list(map(int,np.unravel_index(np.argmax(diff),diff.shape)[::-1])),difference=diff.tolist(),n_in=int(inn.sum()),n_base=int(base.sum()),maxgap_days=float(g[i]),gap_endpoints_btjd=[float(local[i]),float(local[i+1])],timing_note='Partial low event reaches gap, post-gap baseline lower; not a complete eclipse without further modeling.')
(B/'helper-s98.json').write_text(json.dumps(r,indent=2));print(json.dumps(r,indent=2))
