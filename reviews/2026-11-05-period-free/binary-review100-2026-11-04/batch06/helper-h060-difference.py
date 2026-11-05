import numpy as np, json, hashlib
from pathlib import Path
from astropy.io import fits
from astropy.wcs import WCS
import matplotlib;matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent; p=B/'392924671/tesscut.fits'
with fits.open(p) as h:
 d=h[1].data;t=np.array(d['TIME']);q=np.array(d['QUALITY']);F=np.array(d['FLUX'],float);w=WCS(h[2].header)
xy=w.all_world2pix(206.88012644409343,4.845222190872993,0); ok=np.isfinite(t)&(q==0)
a=ok&(t>1933)&(t<1933.8);b=ok&(t>1934.1)&(t<1935.2)
A=np.nanmedian(F[a],axis=0);D=A-np.nanmedian(F[b],axis=0)
fig,axs=plt.subplots(1,2,figsize=(10,4))
for ax,z,name in zip(axs,[A,D],['pre-event','pre minus trough']):
 im=ax.imshow(z,origin='lower',cmap='RdBu_r' if name!='pre-event' else 'viridis'); ax.plot(*xy,'r+',ms=12);fig.colorbar(im,ax=ax);ax.set_title(name)
fig.tight_layout();fig.savefig(B/'helper-h060-difference.png',dpi=150)
y,x=np.indices(A.shape);mask=(abs(x-xy[0])<=2)&(abs(y-xy[1])<=2)
out={'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'target_xy':[float(z) for z in xy],'n_pre':int(a.sum()),'n_trough':int(b.sum()),'sum_difference_4x4':float(D[mask].sum()),'sum_pre_4x4':float(A[mask].sum()),'difference_pixels':D.tolist(),'caveat':'Difference compares two pre-gap intervals; no background or pointing model. Signed difference is diagnostic, not proof of localization.'}
(B/'helper-h060-difference.json').write_text(json.dumps(out,indent=2));print(out['n_pre'],out['n_trough'],out['target_xy'],out['sum_difference_4x4'],out['sum_pre_4x4'])

