"""Actual cadence and raw-flux tests at P/2 interstitial windows for T014.

These conditional half-period windows are between five measured same-kind
eclipses, rather than folds or quality-row fractions. Only well-covered
windows with both external baselines can be used as nulls.
"""
import json
from pathlib import Path
import numpy as np
from astropy.io import fits
B=Path(__file__).resolve().parent;tic='313142904'
d=json.loads((B/tic/'lead-numeric.json').read_text());clock=json.loads((B/tic/'lead-timing.json').read_text())['kinds']['one_kind'];epoch=clock['epoch_btjd'];p=clock['period_days'];half=.10;out=[]
for src in d['sources']:
    with fits.open(src['path'],memmap=False) as hd:
        h=hd[1].data;t=np.asarray(h['TIME'],float);f=np.asarray(h['SAP_FLUX'],float);q=np.asarray(h['QUALITY'],int)
    m=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0);t=t[m];f=f[m]
    if len(t)<10:continue
    for n in range(int(np.floor((t.min()-epoch)/p))-1,int(np.ceil((t.max()-epoch)/p))+2):
        pred=epoch+(n+.5)*p
        if pred<t.min()-.5 or pred>t.max()+.5:continue
        dt=t-pred;core=abs(dt)<=half;left=(dt>=-.4)&(dt<=-.2);right=(dt>=.2)&(dt<=.4)
        if not core.any():continue
        x=t[core];baseline=np.median(np.r_[f[left],f[right]]) if left.any() and right.any() else None
        out.append({'sector':src['sector'],'half_cycle':n+.5,'pred_btjd':pred,'core_q0_n':int(sum(core)),'first_offset_days':float(dt[core].min()),'last_offset_days':float(dt[core].max()),'core_max_gap_days':float(np.max(np.diff(x))) if len(x)>1 else None,'left_n':int(sum(left)),'right_n':int(sum(right)),'core_deficit_ppt':float(1000*(1-np.median(f[core])/baseline)) if baseline else None,'source_sha256':src['sha256']})
(B/tic/'lead-half-alias.json').write_text(json.dumps({'tic':tic,'measured_period_days':p,'hypothesis':'P/2 would place a same-kind eclipse at half-integer cycles; target event ~0.2 d wide','windows':out},indent=2)+'\n')
print([(v['sector'],v['half_cycle'],v['core_q0_n'],round(v['core_deficit_ppt'] or 0,2)) for v in out])
