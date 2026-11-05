"""Inspect raw SAP at actual Gaia-period repeats of each retained dip seed.

Coverage uses time bins, not the count of rows; median contrasts are descriptive.
"""
import csv, hashlib, json
from pathlib import Path
import numpy as np
from astropy.io import fits

B = Path(__file__).resolve().parent
rows = list(csv.DictReader((B/'queue.csv').open(newline='', encoding='utf-8')))
out = []
for row in rows:
    tic = row['tic']; P = float(row['gaia_period_days'])
    seed = float(row['best_window_btjd'])
    duration = float(row['best_window_duration_days'])
    half = max(duration/2, .18)
    records = []
    m = json.loads((B/tic/'lead-numeric.json').read_text())
    for source in m['sources']:
        path = Path(source['path'])
        assert hashlib.sha256(path.read_bytes()).hexdigest() == source['sha256']
        with fits.open(path, memmap=False) as h:
            d = h[1].data
            t = np.asarray(d['TIME'], float)
            f = np.asarray(d['SAP_FLUX'], float)
            q = np.asarray(d['QUALITY'], int)
        ok = np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0)
        t=t[ok]; f=f[ok]
        if len(t)<10: continue
        cadence = float(np.median(np.diff(t)))
        for n in range(int(np.floor((t.min()-seed)/P))-1, int(np.ceil((t.max()-seed)/P))+2):
            pred = seed+n*P
            if not (t.min()-2*half <= pred <= t.max()+2*half): continue
            core = np.abs(t-pred)<=half
            left=(t>=pred-3*half)&(t<pred-1.5*half)
            right=(t>pred+1.5*half)&(t<=pred+3*half)
            baseline=left|right
            bins=np.linspace(pred-half,pred+half,max(4,int(round(2*half/cadence))+1))
            covered=np.histogram(t[core],bins=bins)[0]>0
            rec=dict(sector=source['sector'],cycle=n,pred_btjd=float(pred),core_start_btjd=float(t[core].min()) if core.any() else None,core_end_btjd=float(t[core].max()) if core.any() else None,core_n=int(core.sum()),left_n=int(left.sum()),right_n=int(right.sum()),core_time_bin_coverage=float(covered.mean()),largest_core_gap_days=float(np.diff(t[core]).max()) if core.sum()>1 else None)
            if core.sum()>2 and baseline.sum()>6:
                rec['raw_core_minus_baseline_ppt']=float(1000*(np.median(f[core])/np.median(f[baseline])-1))
                rec['raw_baseline_median']=float(np.median(f[baseline]))
            records.append(rec)
    out.append(dict(sample_id=row['sample_id'],tic=tic,seed_is_screen_prediction_btjd=seed,gaia_period_days=P,core_half_width_days=half,records=records))
    print(row['sample_id'],[(a['sector'],a['cycle'],round(a['pred_btjd'],2),round(a['core_time_bin_coverage'],2),round(a.get('raw_core_minus_baseline_ppt',float('nan')),1)) for a in records if a['core_time_bin_coverage']>.6])
(B/'lead-fold-coverage.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
