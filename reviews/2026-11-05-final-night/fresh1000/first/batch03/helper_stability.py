import json
from pathlib import Path
import numpy as np
from astropy.io import fits
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
D=Path(r'[workspace]/Astra\made\final-night-2026-11-05\fresh1000\first\batch03\25073050'); E=json.loads((D/'lead-timing.json').read_text()); J=json.loads((D/'helper-localization.json').read_text()); N=json.loads((D/'helper-gaia-neighbors.json').read_text()); target=np.array(J['target_xy']); neighbor=np.array(N['neighbors_sorted'][0]['wcs_xy'])
with fits.open(D/'helper-tesscut.fits') as f:t=np.array(f[1].data['TIME'],float); q=np.array(f[1].data['QUALITY'],int); cube=np.array(f[1].data['FLUX'],float)
yy,xx=np.indices(cube.shape[1:]); sky=np.hypot(xx-target[0],yy-target[1])>2.8; cube=cube-np.nanmedian(cube[:,sky],axis=1)[:,None,None]; near=np.hypot(xx-target[0],yy-target[1])<3; outputs=[]; fig,axs=plt.subplots(1,3,figsize=(12,4))
for e,ax in zip(E,axs):
 c=e['center_btjd'];d=e['duration_d']; good=(q==0)&np.isfinite(t)
 for cf,s0,s1 in [(0.20,.75,1.5),(.25,.75,2),(.30,.85,1.7),(.20,1,2)]:
  core=good&(abs(t-c)<d*cf);side=good&(abs(t-c)>d*s0)&(abs(t-c)<d*s1)
  diff=np.nanmedian(cube[side],axis=0)-np.nanmedian(cube[core],axis=0); wt=np.maximum(diff,0)*near; xy=np.array([np.nansum(wt*xx)/np.nansum(wt),np.nansum(wt*yy)/np.nansum(wt)])
  outputs.append({'center':c,'kind':e['kind'],'core_fraction':cf,'side_durations':[s0,s1],'n_core':int(core.sum()),'n_side':int(side.sum()),'centroid':xy.tolist(),'target_distance_pixel':float(np.linalg.norm(xy-target)),'neighbor_distance_pixel':float(np.linalg.norm(xy-neighbor))})
  if cf==.25:
   ax.imshow(diff,origin='lower',cmap='coolwarm'); ax.plot(*target,'wx',ms=10,mew=2,label='target');ax.plot(*neighbor,'y+',ms=12,mew=2,label='neighbor');ax.plot(*xy,'go',ms=5,label='deficit');ax.set_title(f"{e['kind']} {c:.3f}");ax.legend(fontsize=7,loc='lower left')
fig.tight_layout();fig.savefig(D/'helper-centroid-stability.png',dpi=140)
(D/'helper-centroid-stability.json').write_text(json.dumps({'target_xy':target.tolist(),'neighbor_xy':neighbor.tolist(),'target_neighbor_separation_pixels':float(np.linalg.norm(target-neighbor)),'measurements':outputs,'caveat':'Per-cadence median outer-pixel background subtracted; positive difference centroid and window variations are descriptive, not calibrated astrometric uncertainties. Neighbor source position Gaia reference epoch, approximate WCS and unmodeled PRF.'},indent=2))
for o in outputs: print(o)

