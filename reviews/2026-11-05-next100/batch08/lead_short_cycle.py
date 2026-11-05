import json
from pathlib import Path
import numpy as np
from astropy.io import fits
from scipy.signal import find_peaks,savgol_filter
B=Path(__file__).resolve().parent
spec=[('270523058',82,.025,.45,.6412),('295351347',99,.004,.4,.6923)]
for tic,sec,prom,distance,p0 in spec:
 s=next(x for x in json.loads((B/tic/'lead-context.json').read_text())['sectors'] if x['sector']==sec)
 with fits.open(s['source_path'],memmap=False) as h:
  a=h[1].data;t=np.asarray(a['TIME'],float);f=np.asarray(a['SAP_FLUX'],float);q=np.asarray(a['QUALITY'],int)
 g=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0);t=t[g];f=f[g]/np.median(f[g])
 cad=np.median(np.diff(t));grid=np.arange(t.min(),t.max(),cad);y=np.interp(grid,t,f);sm=savgol_filter(y,31,3)
 pk,_=find_peaks(-sm,prominence=prom,distance=int(distance/cad));tm=np.array([grid[i] for i in pk if np.min(abs(t-grid[i]))<2*cad]);
 if tic=='295351347':tm=tm[tm>4063.5]
 n=np.rint((tm-tm[0])/p0).astype(int);co=np.polyfit(n,tm,1);res=tm-np.polyval(co,n)
 out=dict(tic=tic,sector=sec,minima_times_btjd=tm.tolist(),integer_cycles=n.tolist(),linear_period_days=float(co[0]),epoch_btjd=float(co[1]),rms_residual_days=float(np.std(res)),max_abs_residual_days=float(np.max(abs(res))),source_sha256=s['source_sha256'],note='Within-sector recurrence; broader orbital aliases and source identity remain to check.')
 (B/tic/'lead-short-cycle.json').write_text(json.dumps(out,indent=2)+'\n')
 print(tic,len(tm),co,np.std(res),np.max(abs(res)))
