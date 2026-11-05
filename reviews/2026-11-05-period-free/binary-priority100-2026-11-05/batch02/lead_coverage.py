"""Actual cadence coverage at selected predicted windows, never a rank-derived null."""
import csv,json
from pathlib import Path
import numpy as np
from astropy.io import fits
B=Path(__file__).resolve().parent
CHOICES={'T011':(3921.7114,52.1321502516,0.6), 'T014':(1832.6659,49.327372,0.10), 'T016':(1840.6365,51.813122944,0.12), 'T018':(3874.7706,56.17552444,0.4)}
for r in csv.DictReader((B/'queue.csv').open(newline='',encoding='utf-8')):
    if r['sample_id'] not in CHOICES:continue
    epoch,p,half=CHOICES[r['sample_id']];d=json.loads((B/r['tic']/'lead-numeric.json').read_text());out=[]
    for src in d['sources']:
        with fits.open(src['path'],memmap=False) as hd:
            h=hd[1].data;t=np.asarray(h['TIME'],float);f=np.asarray(h['SAP_FLUX'],float);q=np.asarray(h['QUALITY'],int)
        valid=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0);t=t[valid];f=f[valid];
        if not len(t):continue
        n0=int(np.floor((t.min()-epoch)/p))-1;n1=int(np.ceil((t.max()-epoch)/p))+1
        for n in range(n0,n1+1):
            pred=epoch+n*p
            if pred<t.min()-2*half or pred>t.max()+2*half:continue
            dt=t-pred;core=np.abs(dt)<=half;left=(dt>=-3*half)&(dt<=-1.5*half);right=(dt>=1.5*half)&(dt<=3*half)
            if not core.any() and not left.any() and not right.any():continue
            actual_core=t[core];gap=float(np.max(np.diff(actual_core))) if len(actual_core)>1 else None
            base=np.median(np.r_[f[left],f[right]]) if left.any() and right.any() else None
            med=np.median(f[core]) if core.any() else None
            out.append({'sector':src['sector'],'cycle':n,'pred_btjd':pred,'core_halfwidth_days':half,'core_quality0_n':int(sum(core)),'core_first_offset_days':float(dt[core].min()) if core.any() else None,'core_last_offset_days':float(dt[core].max()) if core.any() else None,'core_max_internal_gap_days':gap,'left_n':int(sum(left)),'right_n':int(sum(right)),'raw_core_deficit_ppt':float(1000*(1-med/base)) if base and med else None,'source_sha256':src['sha256']})
    (B/r['tic']/'lead-coverage.json').write_text(json.dumps({'sample_id':r['sample_id'],'tic':r['tic'],'conditional_epoch_btjd':epoch,'conditional_period_days':p,'windows':out,'caveat':'Sensitive null requires core endpoints, internal gaps and non-overlapping stable baselines; field variability can invalidate deficit.'},indent=2)+'\n')
    print(r['sample_id'],[(x['sector'],x['cycle'],x['core_quality0_n'],round(x['raw_core_deficit_ppt'] or 0,1)) for x in out])
