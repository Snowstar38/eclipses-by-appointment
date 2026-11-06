import json,hashlib,numpy as np
from pathlib import Path
from astropy.io import fits
from astropy.wcs import WCS
import matplotlib;matplotlib.use('Agg')
import matplotlib.pyplot as plt
b=Path('[workspace]/Astra/made/final-night-2026-11-05/fresh18/batch01');pop=json.loads((b.parent.parent/'fresh-band-next400/population.json').read_text())['targets'];out=[]
for path in b.glob('*/helper*cut-s*.fits'):
 tic=path.parent.name;sec=int(path.stem.split('-s')[-1]);d=pop[tic]
 with fits.open(path) as h:a=h[1].data;t=np.asarray(a['TIME'],float);f=np.asarray(a['FLUX'],float);q=np.asarray(a['QUALITY'],int);xy=WCS(h[2].header).all_world2pix([[d['ra'],d['dec']]],0)[0]
 yy,xx=np.indices(f.shape[1:]);ap=(abs(xx-round(xy[0]))<=1)&(abs(yy-round(xy[1]))<=1);border=(xx==0)|(yy==0)|(xx==6)|(yy==6);bg=np.nanmedian(f[:,border],axis=1);flux=np.nansum(f[:,ap],axis=1)-bg*ap.sum();ok=(q==0)&np.isfinite(t)&np.isfinite(flux)&(flux>0);t=t[ok];flux=flux[ok];bg=bg[ok]
 np.savez(path.parent/f'lead-independent-s{sec}.npz',time=t,flux=flux,background=bg)
 fig,ax=plt.subplots(figsize=(13,3));ax.plot(t,flux/np.median(flux),'.',ms=1);ax.grid(alpha=.3);ax.set_title(f'TIC{tic} S{sec} independent 3x3 minus border background');fig.tight_layout();fig.savefig(path.parent/f'lead-independent-s{sec}.png',dpi=130);plt.close(fig)
 out.append(dict(tic=tic,sector=sec,target_xy=xy.tolist(),first=float(t.min()),last=float(t.max()),n=len(t),source_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),aperture_pixels=int(ap.sum()),method='3x3 aperture, cadence-specific median outer border subtraction; quality=0; same photons'))
(b/'lead-independent-receipts.json').write_text(json.dumps(out,indent=2))

