import json, numpy as np
from astropy.io import fits
from pathlib import Path
B=Path(__file__).parent;tic='241089793'
m=json.loads((B/tic/'measurements.json').read_text());p=m['historical_period_days'];t0=m['historical_epoch_btjd']
out=[]
for f in sorted((B.parent/'shared-qlp').glob(tic+'_s*.fits')):
 with fits.open(f) as h:
  a=h[1].data;t=np.array(a['TIME'],float);flux=np.array(a['SAP_FLUX'],float);q=np.array(a['QUALITY'],int)
 for cyc in range(int((np.nanmin(t)-t0)/p)-1,int((np.nanmax(t)-t0)/p)+2):
  c=t0+cyc*p;sel=np.isfinite(t)&np.isfinite(flux)&(flux>0)&(np.abs(t-c)<.35);clean=sel&(q==0)
  core=clean&(np.abs(t-c)<.045);side=clean&(np.abs(t-c)>.12)&(np.abs(t-c)<.32)
  if not np.any(sel):continue
  base=np.median(flux[side]) if np.any(side) else np.nan
  depth=(1-np.median(flux[core])/base)*1000 if np.any(core) else np.nan
  out.append(dict(sector=int(f.stem.split('_s')[1]),cycle=cyc,predicted_btjd=c,window_n=int(sel.sum()),quality_zero_n=int(clean.sum()),core_n=int(core.sum()),side_n=int(side.sum()),median_core_depth_ppt=float(depth) if np.isfinite(depth) else None,window_time_min=float(np.min(t[sel])),window_time_max=float(np.max(t[sel]))))
(B/'241089793-alias-coverage.json').write_text(json.dumps(out,indent=2))
for x in out:print(x)
