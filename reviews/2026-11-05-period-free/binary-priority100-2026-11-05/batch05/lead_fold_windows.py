"""Inspect actual raw-SAP coverage at the independent fold-screen predictions."""
import csv,json,math
from pathlib import Path
import numpy as np
from astropy.io import fits
B=Path(__file__).resolve().parent;R=B.parent
Q=list(csv.DictReader((B/'queue.csv').open(encoding='utf-8',newline='')))
for row in Q:
    tic=row['tic'];o=B/tic
    p=json.loads((R/'source-packets'/tic/'sources.json').read_text(encoding='utf-8'))['fold']['P']
    P=float(p['P']);t0=float(p['t0']);dur=float(p['dur']);num=json.loads((o/'lead-numeric.json').read_text(encoding='utf-8'))
    windows=[]
    for s in num['sources']:
        with fits.open(s['path'],memmap=False) as h:
            a=h[1].data;t=np.asarray(a['TIME'],float);f=np.asarray(a['SAP_FLUX'],float);q=np.asarray(a['QUALITY'],int)
        ok=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0);t=t[ok];f=f[ok]
        if len(t)<20:continue
        cadence=float(np.median(np.diff(t)))
        for n in range(math.ceil((t.min()-t0)/P),math.floor((t.max()-t0)/P)+1):
            pred=t0+n*P;half=max(dur/2,.05);outer=max(3*dur,.4)
            core=abs(t-pred)<half;side=(abs(t-pred)>max(dur,.15))&(abs(t-pred)<outer)
            tc=np.sort(t[core]);ts=np.sort(t[side]);nc=len(tc);ns=len(ts)
            if nc==0 and ns==0:continue
            deficit=float(1000*(1-np.median(f[core])/np.median(f[side]))) if nc>=2 and ns>=6 else None
            windows.append(dict(sector=s['sector'],cycle=n,pred_btjd=pred,core_n=nc,side_n=ns,core_first_btjd=float(tc.min()) if nc else None,core_last_btjd=float(tc.max()) if nc else None,core_max_gap_days=float(max(np.diff(tc))) if nc>1 else None,side_max_gap_days=float(max(np.diff(ts))) if ns>1 else None,cadence_days=cadence,raw_core_deficit_ppt=deficit,source_sha256=s['sha256']))
    (o/'lead-fold-windows.json').write_text(json.dumps(dict(screen_period_days=P,screen_epoch_btjd=t0,screen_duration_days=dur,windows=windows,method='Predicted windows are not measured events. Quality-zero raw SAP, core ±max(duration/2,0.05), side outside max(duration,0.15) to max(3duration,0.4). Report actual endpoints and internal gaps.'),indent=2)+'\n',encoding='utf-8')
    print(row['sample_id'],[(w['sector'],round(w['pred_btjd'],2),w['core_n'],w['side_n'],round(w['raw_core_deficit_ppt'],1) if w['raw_core_deficit_ppt'] is not None else None) for w in windows],flush=True)
