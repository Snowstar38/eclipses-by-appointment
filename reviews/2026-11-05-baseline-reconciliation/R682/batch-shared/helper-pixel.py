import json,csv,glob
from pathlib import Path
import numpy as np
from astropy.io import fits
from astropy.wcs import WCS
import matplotlib;matplotlib.use('Agg')
import matplotlib.pyplot as plt
p=Path(__file__).parent
for q in csv.DictReader((p/'queue.csv').open()):
 tic=q['tic']; paths=list((p/tic/'pixels').glob('tesscut*.fits')); assert len(paths)==1
 with fits.open(paths[0],memmap=False) as h:
  w=WCS(h[2].header); sec=int(h[2].header['SECTOR']); d=h[1].data; t=np.asarray(d['TIME']); flux=np.asarray(d['FLUX']); qual=np.asarray(d['QUALITY']); good=np.isfinite(t)&(qual==0)
  ev=max([e for e in json.loads((p/tic/'measurements.json').read_text())['events'] if e.get('timing_usable') and e['sector']==sec],key=lambda e:e['depth_ppt']); c=ev['mid_btjd']; width=ev['duration_hours']/24; ix=good&(abs(t-c)<width*.20); ox=good&(abs(t-c)>width*.7)&(abs(t-c)<width*1.5); D=np.nanmedian(flux[ox],axis=0)-np.nanmedian(flux[ix],axis=0); stars=json.loads((p/tic/'pixels/gaia-stars.json').read_text()); target=next(s for s in stars if str(s['source_id'])==q['gaia_dr3_source_id']); fig,ax=plt.subplots(figsize=(7,6)); im=ax.imshow(D,origin='lower',cmap='inferno'); fig.colorbar(im,ax=ax,label='out minus in e-/s');
  for s in stars:
   if s['phot_g_mean_mag'] is None or s['phot_g_mean_mag']-target['phot_g_mean_mag']>4.5: continue
   x,y=w.all_world2pix(s['ra'],s['dec'],0); ident=str(s['source_id']); ax.plot(x,y,'o',ms=8,mfc='none',mec='cyan' if ident==q['gaia_dr3_source_id'] else 'lime'); ax.annotate('T' if ident==q['gaia_dr3_source_id'] else ident[-5:],(x,y),color='white',fontsize=7)
  ax.set(xlim=(-.5,D.shape[1]-.5),ylim=(-.5,D.shape[0]-.5),title=f'{tic} sector {sec} {ev["kind"]}: {ix.sum()} in, {ox.sum()} out'); fig.tight_layout(); fig.savefig(p/f'helper-pixel-{tic}.png',dpi=140);plt.close(fig)
