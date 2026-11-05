"""Actual cadence coverage at Gaia screening predictions; never infer event centers."""
import csv,json,math
from pathlib import Path
import numpy as np
from astropy.io import fits
B=Path(__file__).resolve().parent
for r in csv.DictReader((B/'queue.csv').open(newline='',encoding='utf-8')):
 tic=r['tic'];o=B/tic;d=json.loads((o/'initial-numerics.json').read_text());P=float(r['gaia_period_days']);t0=float(r['best_window_btjd']);dur=max(.12,float(r['best_window_duration_days']));rows=[]
 for rec in d['file_receipts']:
  with fits.open(rec['path'],memmap=False) as h:
   a=h[1].data;t=np.asarray(a['TIME'],float);f=np.asarray(a['SAP_FLUX'],float);q=np.asarray(a['QUALITY'],int)
  v=np.isfinite(t)&np.isfinite(f)&(f>0);t=t[v];f=f[v];q=q[v]
  for kind,off in [('same',0),('opposite_half',.5)]:
   for n in range(math.ceil((t.min()-t0)/P-off),math.floor((t.max()-t0)/P-off)+1):
    c=t0+(n+off)*P;delta=t-c;core=abs(delta)<=dur/2;left=(delta>=-1.5*dur)&(delta<=-dur/2);right=(delta>=dur/2)&(delta<=1.5*dur);good=q==0;coreg=core&good;lg=left&good;rg=right&good
    if not np.any(core|left|right):continue
    rec0={'sector':rec['sector'],'kind':kind,'cycle':n,'predicted_btjd':c,'duration_days':dur,'core_quality0':int(sum(coreg)),'core_flagged':int(sum(core&~good)),'left_quality0':int(sum(lg)),'right_quality0':int(sum(rg)),'core_first_btjd':float(t[coreg].min()) if sum(coreg) else None,'core_last_btjd':float(t[coreg].max()) if sum(coreg) else None}
    if sum(coreg)>=3 and sum(lg)>=3 and sum(rg)>=3:
     baseline=(np.median(f[lg])+np.median(f[rg]))/2;rec0['core_median_deficit_ppt']=float(1000*(1-np.median(f[coreg])/baseline));rec0['status']='sampled_prediction_not_a_null'
    else:rec0['status']='incomplete_prediction'
    rows.append(rec0)
 (o/'predicted-windows.json').write_text(json.dumps({'tic':tic,'screen_period_days':P,'screen_anchor_btjd':t0,'note':'Gaia selection orbit and bulk flag anchor only; predicted windows are not measured events. These statistics are not clean nulls without raw baseline and gap review.','windows':rows},indent=2)+'\n',encoding='utf-8')
 print(r['sample_id'],len(rows),sum(x['status']=='sampled_prediction_not_a_null' for x in rows))
