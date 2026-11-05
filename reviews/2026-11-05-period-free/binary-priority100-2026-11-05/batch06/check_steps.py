"""Quantify local raw steps, cadence gaps and QLP background at retained windows."""
import csv,json
from pathlib import Path
import numpy as np
from astropy.io import fits
B=Path(__file__).resolve().parent
rows=list(csv.DictReader((B/'queue.csv').open(newline='',encoding='utf-8')))
for r in rows:
 tic=r['tic'];d=json.loads((B/tic/'initial-numerics.json').read_text());o=[]
 for w in d['retained_flag_windows']:
  rec=next((x for x in d['file_receipts'] if x['sector']==w['sector']),None)
  if not rec:continue
  with fits.open(rec['path'],memmap=False) as h:
   a=h[1].data;t=np.asarray(a['TIME'],float);f=np.asarray(a['SAP_FLUX'],float);q=np.asarray(a['QUALITY'],int); names=h[1].columns.names
   b=np.asarray(a['SAP_BKG'],float) if 'SAP_BKG' in names else np.full(len(t),np.nan)
   x=np.asarray(a['SAP_X'],float) if 'SAP_X' in names else np.full(len(t),np.nan)
   y=np.asarray(a['SAP_Y'],float) if 'SAP_Y' in names else np.full(len(t),np.nan)
  valid=np.isfinite(t)&np.isfinite(f)&(f>0);t=t[valid];f=f[valid];q=q[valid];b=b[valid];x=x[valid];y=y[valid]
  c=w['time'];dur=w['duration'];dt=np.diff(t);near=(t[:-1]>c-max(2*dur,1))&(t[:-1]<c+max(2*dur,1));idx=np.flatnonzero(near);gaps=sorted([{'left':float(t[i]),'right':float(t[i+1]),'days':float(dt[i])} for i in idx],key=lambda z:-z['days'])[:4]
  windows={}
  for name,a0,a1 in [('pre',-1.3*dur,-.5*dur),('core',-.5*dur,.5*dur),('post',.5*dur,1.3*dur)]:
   m=(t>=c+a0)&(t<c+a1)&(q==0);windows[name]={'n':int(sum(m)),'flux_median':float(np.median(f[m])) if sum(m) else None,'bkg_median':float(np.nanmedian(b[m])) if sum(m) else None,'x_median':float(np.nanmedian(x[m])) if sum(m) else None,'y_median':float(np.nanmedian(y[m])) if sum(m) else None}
  o.append({**w,'gaps_nearby':gaps,'local_windows':windows})
 (B/tic/'step-context.json').write_text(json.dumps(o,indent=2)+'\n',encoding='utf-8')
 print(r['sample_id'],[(v['sector'],v['kind'],round(v['gaps_nearby'][0]['days'],2) if v['gaps_nearby'] else None) for v in o],flush=True)
