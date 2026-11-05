"""Actual cadence coverage of bounded repeating dip predictions; predictions are not fitted centers."""
from pathlib import Path
import json,math,hashlib
import numpy as np
from astropy.io import fits
B=Path(__file__).resolve().parent
cfg={'F022':('324424395',27.7684884,1676.85288,.6),'F023':('286094277',27.37165736,1747.3806,.15),'F028':('19385783',2.06594241,2229.57167,.08),'F030':('288649491',.54007319,2230.06185,.035)}
for sid,(tic,P,ep,h) in cfg.items():
    src=json.loads((B/tic/'lead-measurements.json').read_text(encoding='utf8'));rows=[]
    for r in src['source_receipts']:
        p=Path(r['path']);assert hashlib.sha256(p.read_bytes()).hexdigest()==r['sha256']
        with fits.open(p,memmap=False) as fitsfile:
            a=fitsfile[1].data;t=np.array(a['TIME'],float);f=np.array(a['SAP_FLUX'],float);q=np.array(a['QUALITY'],int)
        good=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0);t=t[good];f=f[good]
        if len(t)<30:continue
        dt=float(np.median(np.diff(t)))
        for n in range(math.ceil((t.min()-ep)/P),math.floor((t.max()-ep)/P)+1):
            pred=ep+n*P;x=t-pred;core=np.abs(x)<=h;left=(x>=-4*h)&(x<=-2*h);right=(x>=2*h)&(x<=4*h)
            tc=t[core];gap=float(max(np.diff(tc),default=float('nan')))
            full=bool(len(tc)>2 and tc.min()<=pred-h+dt and tc.max()>=pred+h-dt and gap<=max(.07,2.5*dt))
            side=bool(left.sum()>=3 and right.sum()>=3)
            depth=float((1-np.median(f[core])/np.median(f[left|right]))*1000) if full and side else None
            rows.append(dict(sector=int(r['sector']),cycle=n,predicted_btjd=float(pred),core_start_btjd=float(pred-h),core_end_btjd=float(pred+h),core_q0_positive=int(core.sum()),core_first_btjd=float(tc.min()) if len(tc) else None,core_last_btjd=float(tc.max()) if len(tc) else None,core_max_internal_gap_days=gap if np.isfinite(gap) else None,core_fully_covered=full,bilateral_baseline=side,core_median_depth_ppt=depth,source_sha256=r['sha256']))
    out=dict(sample_id=sid,tic=tic,trial_period_days=P,trial_epoch_btjd=ep,trial_core_halfwidth_days=h,source='hashed QLP raw SAP, finite positive, quality=0',prediction_caveat='Predicted windows are not measured eclipse centers. Depth is local median statistic, not a fitted depth. Baseline on 2-4 core halfwidths either side; events/gaps and opposite kinds may bias.',windows=rows,fully_covered=sum(x['core_fully_covered'] for x in rows),fully_covered_with_baseline=sum(x['core_fully_covered'] and x['bilateral_baseline'] for x in rows))
    (B/tic/'lead-coverage.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
    print(sid,len(rows),out['fully_covered'],out['fully_covered_with_baseline'],[(x['sector'],x['cycle'],round(x['core_median_depth_ppt'],2) if x['core_median_depth_ppt'] is not None else None) for x in rows if x['core_median_depth_ppt'] is not None][:30])
