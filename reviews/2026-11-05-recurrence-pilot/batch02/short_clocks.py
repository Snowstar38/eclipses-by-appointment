"""Local waveform spacing diagnostics, not adopted eclipse periods."""
from pathlib import Path
import json,hashlib
import numpy as np
from astropy.io import fits
from scipy.signal import find_peaks,savgol_filter
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent;H=B.parent.parent/'binary-exploration-2026-11-04'/'bulk-results'
for tic,sector,prom,dist in [('365199313',50,.02,.15),('410449401',88,.001,.13),('366103941',85,.03,.30),('392025836',93,.003,.35)]:
    bulk=json.loads((H/f'{tic}.json').read_text());rec=next(r for r in bulk['files'] if r['sector']==sector);p=Path(rec['path']);assert hashlib.sha256(p.read_bytes()).hexdigest()==rec['sha256']
    with fits.open(p,memmap=False) as h:
        d=h[1].data;t=np.asarray(d['TIME'],float);f=np.asarray(d['SAP_FLUX'],float);q=np.asarray(d['QUALITY'],int)
    z=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0);t=t[z];f=f[z]/np.median(f[z]);dt=np.median(np.diff(t));
    sm=savgol_filter(f,5,2);idx,_=find_peaks(-sm,prominence=prom,distance=int(dist/dt))
    times=t[idx];delta=np.diff(times);delta=delta[(delta<1)&(delta>dist)]
    out={'tic':tic,'sector':sector,'source_sha256':rec['sha256'],'prominence_fraction':prom,'min_separation_days':dist,'minima_btjd':times.tolist(),'neighboring_minima_spacings_days':delta.tolist(),'median_spacing_days':float(np.median(delta)) if len(delta) else None,'interpretation':'waveform minima, not verified eclipses'}
    (B/tic/'short-clock.json').write_text(json.dumps(out,indent=2)+'\n')
    print(tic,sector,'n',len(times),'median',out['median_spacing_days'],flush=True)
