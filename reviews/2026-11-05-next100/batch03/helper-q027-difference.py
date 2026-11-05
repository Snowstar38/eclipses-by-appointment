import zipfile,io,json,hashlib
from pathlib import Path
import numpy as np
from astropy.io import fits
from astropy.wcs import WCS
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent; fig,axs=plt.subplots(1,2,figsize=(10,5));out={}
for ax,s,t0 in zip(axs,[10,100],[1588.414,4075.502]):
 path=B/f'helper-q027-s{s}.zip';z=zipfile.ZipFile(path);h=fits.open(io.BytesIO(z.read(z.namelist()[0])));a=h[1].data;t=np.array(a['TIME']);f=np.array(a['FLUX']);q=np.array(a['QUALITY']);w=WCS(h[2].header);xy=w.all_world2pix([[176.9496890335,-53.0248128433]],0)[0];dt=abs(t-t0);on=(q==0)&(dt<.06);off=(q==0)&(dt>.12)&(dt<.35);d=np.nanmedian(f[off],axis=0)-np.nanmedian(f[on],axis=0);yy,xx=np.indices(d.shape);win=(xx-xy[0])**2+(yy-xy[1])**2<16;pos=np.clip(d,0,None)*win;cent=[float((pos*xx).sum()/pos.sum()),float((pos*yy).sum()/pos.sum())];peak=np.unravel_index(np.nanargmax(np.where(win,d,np.nan)),d.shape); ax.imshow(d,origin='lower',cmap='RdBu_r',vmin=-np.nanmax(abs(d[win])),vmax=np.nanmax(abs(d[win])));ax.scatter(*xy,marker='x',c='lime');ax.scatter(*cent,marker='+',c='yellow');ax.set_title(f'S{s}: target x, loss +');ax.set_xlim(2,12);ax.set_ylim(2,12);out[str(s)]={'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'on_cadences':int(on.sum()),'off_cadences':int(off.sum()),'target_xy':xy.tolist(),'positive_centroid_xy':cent,'peak_xy':[int(peak[1]),int(peak[0])]}
fig.tight_layout();fig.savefig(B/'helper-q027-difference.png',dpi=160);(B/'helper-q027-difference.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))

