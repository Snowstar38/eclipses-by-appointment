import numpy as np,json,hashlib
from astropy.io import fits
from astropy.wcs import WCS
import matplotlib;matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path
B=Path(__file__).resolve().parent
out=[]
for sec,guess in [(106,4247.2),(108,4299.3)]:
 p=B/f'lead-extra-s{sec}.fits'
 with fits.open(p) as h:
  a=h[1].data;t=np.array(a['TIME']);q=np.array(a['QUALITY']);f=np.array(a['FLUX']); w=WCS(h[2].header); xy=w.all_world2pix([[74.7622014277498,-28.8916285368164]],0)[0]
 ok=(q==0)&np.isfinite(t); z=np.nansum(f[:,1:4,1:4],axis=(1,2)); sel=ok&(abs(t-guess)<.6); ix=np.flatnonzero(sel)[np.argmin(z[sel])]; c=t[ix]; inn=ok&(abs(t-c)<.045); baseline=ok&(abs(t-c)>.18)&(abs(t-c)<.40)
 diff=np.nanmedian(f[baseline],axis=0)-np.nanmedian(f[inn],axis=0); med=np.nanmedian(f[baseline],axis=0)
 fig,ax=plt.subplots(1,2,figsize=(9,4)); im=ax[0].imshow(med,origin='lower');fig.colorbar(im,ax=ax[0]); im=ax[1].imshow(diff,origin='lower');fig.colorbar(im,ax=ax[1]);
 for a in ax:a.plot(*xy,'rx',ms=12,mew=2);a.set_xticks(range(5));a.set_yticks(range(5));a.grid(alpha=.3)
 ax[0].set_title('baseline flux, target x');ax[1].set_title('baseline minus event, target x');fig.suptitle(f'S{sec} BTJD {c:.6f}');fig.tight_layout();fig.savefig(B/f'helper-diff-s{sec}.png',dpi=150);plt.close(fig)
 d=np.maximum(diff,0);cx=(d*np.arange(5)[None,:]).sum()/d.sum();cy=(d*np.arange(5)[:,None]).sum()/d.sum()
 r=dict(sector=sec,center_btjd=float(c),n_in=int(inn.sum()),n_baseline=int(baseline.sum()),target_xy=xy.tolist(),positive_diff_centroid=[float(cx),float(cy)],diff=diff.tolist(),baseline=med.tolist(),sha256=hashlib.sha256(p.read_bytes()).hexdigest());out.append(r)
print(json.dumps(out,indent=2));(B/'helper-pixel-768070.json').write_text(json.dumps(out,indent=2))
