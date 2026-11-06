"""Actual q0 time coverage and local raw medians for ranked screening windows."""
from pathlib import Path
import csv,json,hashlib
import numpy as np
from astropy.io import fits
B=Path(__file__).resolve().parent;H=B.parent.parent/'binary-exploration-2026-11-04'/'bulk-results'
for row in csv.DictReader((B/'queue.csv').open(newline='',encoding='utf8')):
    tic=row['tic'];bulk=json.loads((H/f'{tic}.json').read_text()); results=[]
    for rec in bulk['files']:
        windows=sorted([w for w in rec['windows'] if w['kind']=='dip'],key=lambda w:w['contrast'],reverse=True)
        if not any(w['flag'] for w in windows):continue
        p=Path(rec['path']);assert hashlib.sha256(p.read_bytes()).hexdigest()==rec['sha256']
        with fits.open(p,memmap=False) as h:
            assert str(int(h[0].header['TICID']))==tic
            d=h[1].data;t=np.asarray(d['TIME'],float);f=np.asarray(d['SAP_FLUX'],float);q=np.asarray(d['QUALITY'],int)
        ok=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0);t=t[ok];f=f[ok];dt=float(np.median(np.diff(t)))
        for w in windows:
            if not w['flag']:continue
            c=float(w['time']);dur=float(w['duration']);half=dur/2
            region=np.abs(t-c)<half;left=(t>=c-1.5*dur)&(t<c-half);right=(t>c+half)&(t<=c+1.5*dur)
            times=t[region]; xx=t[(t>=c-1.5*dur)&(t<=c+1.5*dur)]
            n_expected=dur/dt
            v={'sector':rec['sector'],'screen_center_btjd':c,'screen_duration_days':dur,'contrast':w['contrast'],'n_core':int(sum(region)),'expected_core_cadences':round(n_expected,1),'core_coverage_fraction':round(float(sum(region)/n_expected),3),'first_core_offset_days':float(times[0]-c) if len(times) else None,'last_core_offset_days':float(times[-1]-c) if len(times) else None,'max_gap_core_days':float(max(np.diff(times))) if len(times)>1 else None,'max_gap_region_days':float(max(np.diff(xx))) if len(xx)>1 else None,'left_median_flux':float(np.median(f[left])) if sum(left) else None,'core_median_flux':float(np.median(f[region])) if sum(region) else None,'right_median_flux':float(np.median(f[right])) if sum(right) else None,'n_left':int(sum(left)),'n_right':int(sum(right)),'source_sha256':rec['sha256']}
            results.append(v)
    (B/tic/'window-audit.json').write_text(json.dumps({'tic':tic,'method':'raw SAP, quality=0 finite positive flux; screen centers not measured eclipse centers','windows':results},indent=2)+'\n')
    print(tic,len(results),flush=True)
