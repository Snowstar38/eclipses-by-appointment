"""Candidate minima and actual cadence coverage, for manual review, not verdicts."""
import json
from pathlib import Path
import numpy as np
from astropy.io import fits
from scipy.ndimage import median_filter
from scipy.signal import find_peaks

B=Path(__file__).resolve().parent
for tic in ['313617927','246124257','198182954']:
    src=json.loads((B/tic/'raw-inspection.json').read_text()); out=[]
    for s in src['sectors']:
        if 'path' not in s: continue
        with fits.open(s['path'],memmap=False) as h:
            a=h[1].data; t=np.asarray(a['TIME'],float); f=np.asarray(a['SAP_FLUX'],float); q=np.asarray(a['QUALITY'],int)
        ok=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0);t=t[ok];f=f[ok]
        cadence=np.median(np.diff(t)); width=max(5,int(1.0/cadence)//2*2+1)
        trend=median_filter(f,size=width,mode='nearest'); resid=f/trend-1
        peaks,props=find_peaks(-resid,prominence=.004 if tic!='198182954' else .006,distance=max(1,int(.3/cadence)))
        chosen=[]
        for i,p in enumerate(peaks):
            if resid[p]>-.002:continue
            chosen.append({'btjd':round(float(t[p]),4),'residual_depth_ppt':round(float(-1000*resid[p]),2),
                           'prominence_ppt':round(float(1000*props['prominences'][i]),2)})
        out.append({'sector':s['sector'],'cadence_days':float(cadence),'minima':chosen})
    (B/tic/'event-check.json').write_text(json.dumps({'tic':tic,'method':'One-day running median detrend and scipy prominence candidate minima; diagnostic only. Must inspect SAP context; broad events and gaps bias minima.','sectors':out},indent=2)+'\n')
    print(tic,[(s['sector'],len(s['minima'])) for s in out],flush=True)
